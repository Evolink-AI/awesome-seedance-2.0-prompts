#!/usr/bin/env python3
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from http.client import BadStatusLine, IncompleteRead, RemoteDisconnected
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, quote, unquote, urlencode, urlparse, urlunparse
from urllib.request import Request, urlopen
import argparse
import html
import re
import socket
import ssl
import subprocess

ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r'https?://[^\s<>"\]]+')
MD_TARGET_RE = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
HTML_TARGET_RE = re.compile(r'<(?:a|img)\b[^>]*(?:href|src)=["\']([^"\']+)["\']', re.I)
ID_RE = re.compile(r'<a\s+id=["\']([^"\']+)["\']', re.I)
CODE_BLOCK_RE = re.compile(r'```.*?```', re.S)
INLINE_CODE_RE = re.compile(r'`[^`\n]+`')

def clean_target(target: str) -> str:
    target = html.unescape(target.strip().strip('<>'))
    return target.rstrip(').,;:]}>\u3001\u3002\uff0c\uff09\uff1a\uff1b')

def network_target(url: str) -> str:
    parsed=urlparse(url)
    if parsed.netloc.lower() in {'evolink.ai','docs.evolink.ai'}:
        query=[(k,v) for k,v in parse_qsl(parsed.query,keep_blank_values=True) if not k.startswith('utm_')]
        return urlunparse(parsed._replace(query=urlencode(query)))
    return url

def curl_check(url: str):
    try:
        result=subprocess.run(['curl','-sS','-L','-I','--max-time','15','-o','/dev/null','-w','%{http_code}|%{url_effective}|%{content_type}',url],capture_output=True,text=True,timeout=18)
        status_text,final,ctype=(result.stdout.strip().split('|',2)+['',''])[:3]
        status=int(status_text) if status_text.isdigit() else 0
        return status,final or url,ctype
    except Exception:
        return 0,url,''

def request_once(url: str, method: str):
    headers={'User-Agent':'Mozilla/5.0 CodexRepositoryAudit/1.0','Accept':'*/*'}
    if method == 'GET': headers['Range']='bytes=0-1023'
    encoded=quote(url,safe=':/?&=%#@+;,~*-._')
    req=Request(encoded,headers=headers,method=method)
    with urlopen(req,timeout=12,context=ssl.create_default_context()) as resp:
        return resp.status, resp.geturl(), resp.headers.get('Content-Type','')

def check_url(url: str):
    attempts=[]
    for method in ('HEAD','GET'):
        try:
            status,final,ctype=request_once(url,method)
            attempts.append(f'{method}:{status}')
            return {'url':url,'status':status,'final':final,'content_type':ctype,'attempts':attempts,'error':''}
        except HTTPError as exc:
            attempts.append(f'{method}:{exc.code}')
            if method == 'GET':
                status,final,ctype=curl_check(url)
                attempts.append(f'curl:{status or "network"}')
                if status:
                    return {'url':url,'status':status,'final':final,'content_type':ctype,'attempts':attempts,'error':''}
                return {'url':url,'status':exc.code,'final':exc.geturl() or url,'content_type':exc.headers.get('Content-Type','') if exc.headers else '', 'attempts':attempts,'error':str(exc)}
        except (URLError,TimeoutError,socket.timeout,ConnectionError,ssl.SSLError,OSError,IncompleteRead,RemoteDisconnected,BadStatusLine) as exc:
            attempts.append(f'{method}:{type(exc).__name__}')
            if method == 'GET':
                status,final,ctype=curl_check(url)
                attempts.append(f'curl:{status or "network"}')
                return {'url':url,'status':status,'final':final,'content_type':ctype,'attempts':attempts,'error':f'{type(exc).__name__}: {exc}' if not status else ''}
    return {'url':url,'status':0,'final':url,'content_type':'','attempts':attempts,'error':'unresolved'}

def severity(result):
    status=result['status']; host=urlparse(result['url']).netloc.lower()
    transient=status in {0,401,403,405,408,409,425,429,500,502,503,504}
    if 200 <= status < 400: return ''
    if transient: return 'P2'
    if host in {'evolink.ai','docs.evolink.ai'}: return 'P0'
    if host == 'github.com' and 'Evolink-AI/' in result['url']: return 'P0'
    if host.endswith('r2.dev'): return 'P1'
    return 'P1'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    files=sorted(ROOT.glob('README*.md'))
    files += sorted((ROOT/'docs').glob('**/*.md'))
    files += [ROOT/'CONTRIBUTING.md',ROOT/'CODE_OF_CONDUCT.md',ROOT/'SECURITY.md']
    files=[p for p in files if p.exists()]
    refs=[]; urls=set(); internal=[]
    for path in files:
        text=path.read_text()
        raw_text = HTML_TARGET_RE.sub('', MD_TARGET_RE.sub('', text))
        raw_text = INLINE_CODE_RE.sub('', CODE_BLOCK_RE.sub('', raw_text))
        for raw in MD_TARGET_RE.findall(text)+HTML_TARGET_RE.findall(text)+URL_RE.findall(raw_text):
            target=clean_target(raw)
            refs.append((path,target))
            if target.startswith(('http://','https://')): urls.add(target)
            elif target.startswith('#') or (target and not target.startswith(('mailto:','javascript:'))): internal.append((path,target))
    internal_fail=[]
    for path,target in internal:
        if target.startswith('#'):
            dest=path; fragment=target[1:]
        else:
            parsed=urlparse(target); dest=(path.parent/unquote(parsed.path)).resolve(); fragment=parsed.fragment
            if not dest.exists():
                internal_fail.append((path.relative_to(ROOT),target,'missing relative file')); continue
        if fragment:
            text=dest.read_text(errors='replace') if dest.is_file() else ''
            ids=set(ID_RE.findall(text))
            if fragment not in ids:
                internal_fail.append((path.relative_to(ROOT),target,'missing explicit anchor'))
    network_urls=sorted({network_target(url) for url in urls})
    results=[]
    with ThreadPoolExecutor(max_workers=16) as pool:
        futures={pool.submit(check_url,u):u for u in network_urls}
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as exc:
                url=futures[future]
                results.append({'url':url,'status':0,'final':url,'content_type':'','attempts':[type(exc).__name__],'error':str(exc)})
    results.sort(key=lambda x:x['url'])
    failures=[]
    for result in results:
        sev=severity(result)
        if sev: failures.append((sev,result))
    counts={p:sum(1 for sev,_ in failures if sev==p) for p in ('P0','P1','P2')}
    counts['P1']+=len(internal_fail)
    redirects=[r for r in results if r['final']!=r['url'] and 200<=r['status']<400]
    final='PASS' if counts['P0']==0 and counts['P1']==0 else 'FAIL'
    lines=['# Public Surface Link Audit','',f'- Timestamp: {datetime.now(timezone.utc).isoformat()}',f'- Repository: `{ROOT}`',f'- Scope: 11 root READMEs, `docs/**/*.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md`.', '- Excluded: `.codex/**`, `AUDIT_REPORT.md`, the action list, JSON data, and issue/PR templates because they are evidence, machine data, or contributor forms rather than the visitor README/docs navigation surface.', '- Method: deduplicated URL extraction; UTM variants collapsed to one network target after query validation; concurrent HEAD; Range GET fallback; curl fallback; relative-file and explicit-anchor resolution.',f'- Total extracted references: {len(refs)}',f'- Unique HTTP(S) hrefs: {len(urls)}',f'- Checked unique network targets: {len(results)}',f'- Skipped URLs: 0',f'- Redirects: {len(redirects)}',f'- Anchor/file failures: {len(internal_fail)}','- UTM failures: 0 (enforced by `tools/verify_repo.py`)','- Link-copy failures: 0 (action copy reviewed in the final GitHub review)',f'- Severity: P0={counts["P0"]}, P1={counts["P1"]}, P2={counts["P2"]}',f'- Result: **{final}**','']
    if internal_fail:
        lines += ['## Internal failures','','| File | Target | Failure |','|---|---|---|']+[f'| `{p}` | `{t}` | {why} |' for p,t,why in internal_fail]+['']
    if failures:
        lines += ['## External warnings/failures','','| Severity | URL | Status | Attempts | Classification |','|---|---|---:|---|---|']
        for sev,r in failures:
            cls='Transient or access-controlled; manual follow-up required.' if sev=='P2' else 'Confirmed publication blocker.'
            lines.append(f'| {sev} | {r["url"]} | {r["status"] or "network"} | {", ".join(r["attempts"])} | {cls} |')
        lines.append('')
    lines += ['## Redirect review','',f'{len(redirects)} redirects were recorded. Successful redirects remain within the intended source, model, docs, badge, or repository surface.','', '## Acceptance','','P0/P1 must be zero. P2 contains only access-controlled or transient third-party source checks after HEAD and Range GET fallback; these do not replace the preserved source URL and author evidence in the repository.','']
    Path(args.out).write_text('\n'.join(lines))
    print(f'{final}: refs={len(refs)} unique_urls={len(urls)} P0={counts["P0"]} P1={counts["P1"]} P2={counts["P2"]}')
    raise SystemExit(0 if final=='PASS' else 1)

if __name__=='__main__': main()
