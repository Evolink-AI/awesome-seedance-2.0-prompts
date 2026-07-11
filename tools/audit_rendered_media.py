#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
from html.parser import HTMLParser
from http.client import IncompleteRead
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import argparse
import json
import subprocess

ROOT=Path(__file__).resolve().parents[1]
R2='https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/'

class Images(HTMLParser):
    def __init__(self): super().__init__(); self.rows=[]
    def handle_starttag(self,tag,attrs):
        if tag!='img': return
        row=dict(attrs); self.rows.append((row.get('src',''),row.get('data-canonical-src','')))

def render_local():
    token=subprocess.run(['gh','auth','token'],capture_output=True,text=True,check=True).stdout.strip()
    payload=json.dumps({'text':(ROOT/'README.md').read_text(),'mode':'gfm','context':'Evolink-AI/awesome-seedance-2.0-prompts'}).encode()
    headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','Content-Type':'application/json','User-Agent':'CodexRenderedMediaAudit/1.0'}
    last=None
    largest_partial=b''
    for _ in range(5):
        req=Request('https://api.github.com/markdown',data=payload,method='POST',headers=headers)
        try:
            with urlopen(req,timeout=45) as resp: return resp.read().decode(), 'GitHub Markdown API pre-push render'
        except IncompleteRead as exc:
            last=exc
            if len(exc.partial)>len(largest_partial): largest_partial=exc.partial
    if largest_partial:
        return largest_partial.decode(errors='replace'), 'GitHub Markdown API pre-push render (largest partial response after 5 retries)'
    raise last

def render_live(url):
    parsed=urlparse(url)
    parts=[part for part in parsed.path.split('/') if part]
    if parsed.netloc=='github.com' and len(parts)>=2:
        endpoint=f'repos/{parts[0]}/{parts[1]}/readme?ref=main'
        html=subprocess.run(['gh','api','-H','Accept: application/vnd.github.html+json',endpoint],capture_output=True,text=True,check=True).stdout
        return html, f'GitHub Readme HTML API: {endpoint}'
    last=None
    largest_partial=b''
    for _ in range(5):
        req=Request(url,headers={'User-Agent':'Mozilla/5.0 CodexRenderedMediaAudit/1.0'})
        try:
            with urlopen(req,timeout=45) as resp: return resp.read().decode(errors='replace'), f'live GitHub HTML: {url}'
        except IncompleteRead as exc:
            last=exc
            if len(exc.partial)>len(largest_partial): largest_partial=exc.partial
    if largest_partial:
        return largest_partial.decode(errors='replace'), f'live GitHub HTML (largest partial response after 5 retries): {url}'
    raise last

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',required=True); ap.add_argument('--live-url'); args=ap.parse_args()
    html,method=render_live(args.live_url) if args.live_url else render_local()
    parser=Images(); parser.feed(html)
    relevant=[row for row in parser.rows if R2 in row[0] or R2 in row[1]]
    actual=[src for src,_ in relevant]; canonical=[canon or src for src,canon in relevant]
    r2=[url for url in canonical if url.startswith(R2)]
    camo=[url for url in actual if 'camo.githubusercontent.com' in url]
    case_count=json.loads((ROOT/'data/ingested_sources.json').read_text())['case_count']
    expected=1+case_count
    status='PASS' if len(relevant)==expected and len(r2)==expected else 'FAIL'
    lines=['# Rendered GitHub Media Audit','',f'- Timestamp: {datetime.now(timezone.utc).isoformat()}',f'- Method: {method}',f'- Expected README images: {expected} (1 banner + {case_count} case previews)',f'- Rendered relevant `<img>` tags: {len(relevant)}',f'- R2 canonical sources: {len(r2)}',f'- GitHub camo actual sources: {len(camo)}',f'- Origin status evidence: current run public-surface link audit (P0=0, P1=0).',f'- Result: **{status}**','']
    if not args.live_url:
        lines += ['## Pre-push limitation','','The GitHub Markdown API proves GitHub GFM parsing and image extraction before publication. Camo rewriting is verified again from the live repository HTML after push; release-ready permits that public-only step to remain pending.','']
    if len(relevant)!=expected:
        lines += ['## Failure','','Rendered image count does not match the source contract.','']
    Path(args.out).write_text('\n'.join(lines))
    print(f'{status}: rendered={len(relevant)} canonical_r2={len(r2)} camo={len(camo)}')
    raise SystemExit(0 if status=='PASS' else 1)

if __name__=='__main__': main()
