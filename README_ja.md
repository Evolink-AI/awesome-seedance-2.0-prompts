<div align="center">

<a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=banner&utm_campaign=awesome-seedance-2.0-prompts&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/banner/seedance-2-prompts-banner-893ce3ae.png" width="900" alt="EvoLinkのSeedance 2プロンプトバナー"></a>

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![ブラウザで Seedance 2.0 を試す](https://img.shields.io/badge/Try_in-Browser-black)](https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=badge&utm_campaign=awesome-seedance-2.0-prompts&utm_content=model_try)
[![プロンプト-166件](https://img.shields.io/badge/%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88-166%E4%BB%B6-111111)](README.md)

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-Default_Source-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-Ver-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-Ver-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-表示-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-보기-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-Ansehen-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-Voir-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-Görüntüle-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-查看-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-查看-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-Смотреть-577590)](README_ru.md)

</div>

<a id="introduction"></a>
## 🍌 はじめに

Awesome Seedance 2.0 Prompts リポジトリへようこそ！🤗

**このリポジトリには、出典を明記した Seedance 2.0 のユニークな動画生成プロンプト 166 件を収録しています。**

公開されたクリエイター投稿からプロンプトを厳選し、再利用可能な資料として保存しています。

[EvoLink で Seedance 2.0 プロンプトの概要を見る](https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=readme&utm_campaign=awesome-seedance-2.0-prompts&utm_content=landing_overview)

> [!NOTE]
> プロンプトブロックは全言語で同一に保ち、表示されるケース名とインターフェースラベルは言語ごとに確認済みの翻訳を使用します。

<a id="quick-start"></a>
## 🚀 クイックスタート

[ブラウザで Seedance 2.0 を試す](https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedance-2.0-prompts&utm_content=browser_try) には、EvoLink のプロンプト画面を使ってください。

API を使う場合は [EvoLink API キー](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-seedance-2.0-prompts&utm_content=api_key) を取得し、タスクを作成して結果をポーリングしてください。

```bash
export EVOLINK_API_KEY="your_key_here"

curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-text-to-video",
    "prompt": "A one-shot cinematic chase through a neon market, handheld camera, fast parallax, dramatic lighting, natural motion blur",
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9"
  }'
```

Endpoint: `POST https://api.evolink.ai/v1/videos/generations`

Create 呼び出しが `id` を返したら、結果の準備ができるまで `GET https://api.evolink.ai/v1/tasks/{task_id}` で状態を確認します。

```bash
export TASK_ID="task_id_from_create_response"

curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/${TASK_ID}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

補助リソース: [API サンプル](https://github.com/Evolink-AI/Seedance-2.0-Gateway-Service)、[OpenClaw skill](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)、[EvoLink API ドキュメント](https://docs.evolink.ai/en/api-manual/video-series/seedance2.0/seedance-2.0-overview?utm_source=github&utm_medium=docs&utm_campaign=awesome-seedance-2.0-prompts&utm_content=first_run)。
<a id="statistics"></a>
## 📊 統計

8 カテゴリ、176 件のユニークなケースを 11 個の README で同期しています。

<a id="how-to-use"></a>
## 🧭 このリポジトリの使い方

カテゴリを選び、出典付きケースを開き、プロンプトをコピーして必要な被写体やメディア参照だけを置き換えてください。

<a id="menu"></a>
## 📑 メニュー

- [はじめに](#introduction)
- [クイックスタート](#quick-start)
- [統計](#statistics)
- [このリポジトリの使い方](#how-to-use)
- [メニュー](#menu)
- [⚔️ アクション / ファンタジー](#action-fantasy) (36)
  - [ケース 1: ストリートラップ MV パフォーマンス (投稿者 @songguoxiansen)](#action-fantasy-case-1)
  - [ケース 2: 黒猫の砂漠武術対決 (投稿者 @nopinduoduo)](#action-fantasy-case-2)
  - [ケース 3: 実写版・呼吸法対決 (投稿者 @johnAGI168)](#action-fantasy-case-3)
  - [ケース 4: 20 カットの高速アニメシーケンス (投稿者 @tebasaki3D)](#action-fantasy-case-4)
  - [ケース 5: 油まみれの整備士が修理する様子 (投稿者 @sebatheepan)](#action-fantasy-case-5)
  - [ケース 6: 侍の復讐短編映画 (投稿者 @sailorv321)](#action-fantasy-case-6)
  - [ケース 7: スタイライズされた 3D バトルアニメーション (投稿者 @johnAGI168)](#action-fantasy-case-7)
  - [ケース 8: テンポの速いコメディパロディ短編 (投稿者 @drjoetw)](#action-fantasy-case-8)
  - [ケース 9: 巨大忍者の特撮バトル (投稿者 @EarthGigantea)](#action-fantasy-case-9)
  - [ケース 10: 日本アニメの会話シーケンス (投稿者 @_3912657840)](#action-fantasy-case-10)
  - [ケース 11: 15 秒のオリジナル元素バトル短編 (投稿者 @ZikinArt)](#action-fantasy-case-11)
  - [ケース 12: ファベルジェ風ファンタジーエッグのアニメーション (投稿者 @ShamiWeb3)](#action-fantasy-case-12)
  - [ケース 13: オリジナル元素バトル短編 (投稿者 @David_eficaz)](#action-fantasy-case-13)
  - [ケース 14: 映画的な SF ファンタジー対決 (投稿者 @CharaspowerAI)](#action-fantasy-case-14)
  - [ケース 15: 15 秒連続ワンカット・アクション (投稿者 @Artedeingenio)](#action-fantasy-case-15)
  - [ケース 16: 崖上で対峙する孤高の侍 (投稿者 @Alin_Reaper05)](#action-fantasy-case-16)
  - [ケース 17: ならず者ドラゴンの空中急降下 (投稿者 @sebatheepan)](#action-fantasy-case-17)
  - [ケース 18: 無重力下のメカ争奪戦 (投稿者 @Dheepanratnam)](#action-fantasy-case-18)
  - [ケース 19: ドラゴンに乗る少女の超高速飛行アクション (投稿者 @naoyuki_okada)](#action-fantasy-case-19)
  - [ケース 20: 15 秒のオリジナル砂漠武術短編 (投稿者 @NimEshed)](#action-fantasy-case-20)
  - [ケース 21: 峡谷への空爆シーケンス (投稿者 @Mr_TuanDoan)](#action-fantasy-case-21)
  - [ケース 22: 15 秒の超写実的な戦争大作 (投稿者 @john87445528)](#action-fantasy-case-22)
  - [ケース 23: オフィスのコーヒーブレイクが大惨事に (投稿者 @Dheepanratnam)](#action-fantasy-case-23)
  - [ケース 24: 15 秒連続ワンカット・アクション (投稿者 @Artedeingenio)](#action-fantasy-case-24)
  - [ケース 25: ブラックスワン対ボクサー (投稿者 @KanaWorks_AI)](#action-fantasy-case-25)
  - [ケース 26: 地面を割って飛び立つスーパーマン (投稿者 @techprophett)](#action-fantasy-case-26)
  - [ケース 27: 雲洞の剣影 (投稿者 @Adam38363368936)](#action-fantasy-case-27)
  - [ケース 28: 神々の都 — 東洋幻想のワンカット飛行 (投稿者 @john87445528)](#action-fantasy-case-28)
  - [ケース 29: 壮大なファンタジーバトル — 映画的な 10 秒シーケンス (投稿者 @a_shimanski)](#action-fantasy-case-29)
  - [ケース 30: ダークファンタジー変身 — 東洋風 (投稿者 @johnAGI168)](#action-fantasy-case-30)
  - [ケース 31: ワニを燃料ラインへ誘導する川の罠 (投稿者 @rahulnanda86)](#action-fantasy-case-31)
  - [ケース 32: 電撃が走る地下闘技場の決闘 (投稿者 @CharaspowerAI)](#action-fantasy-case-32)
  - [ケース 33: 滑走路で飛行機に引きずられるワニ (投稿者 @rahulnanda86)](#action-fantasy-case-33)
  - [ケース 34: 稲妻ストライカーのアニメゴール (投稿者 @CharaspowerAI)](#action-fantasy-case-34)
  - [ケース 35: 野花咲く谷を飛ぶグリフィン (投稿者 @Mayz1169)](#action-fantasy-case-35)
  - [ケース 36: モンゴル騎兵のパルティアンショット (投稿者 @Ankit_patel211)](#action-fantasy-case-36)
- [🎞️ シネマティック・リアリズム](#cinematic-realism) (6)
  - [ケース 1: 現代日本のドキュメンタリーシーケンス (投稿者 @kuranoayashi)](#cinematic-realism-case-1)
  - [ケース 2: 影を追うロングボードのダウンヒル (投稿者 @Dheepanratnam)](#cinematic-realism-case-2)
  - [ケース 3: 隕石で覚醒する戦乙女 (投稿者 @ChrisTheNerv)](#cinematic-realism-case-3)
  - [ケース 4: 霧のカプセル島ドラマ (投稿者 @umesh_ai)](#cinematic-realism-case-4)
  - [ケース 5: 嵐の断崖に現れる侍 (投稿者 @umesh_ai)](#cinematic-realism-case-5)
  - [ケース 6: VHSプール大飛び込み審査員 (投稿者 @Ankit_patel211)](#cinematic-realism-case-6)
- [🥽 POV / FPV](#pov-fpv) (20)
  - [ケース 1: 胸部カメラによる迷彩チェイス (投稿者 @genel_ai)](#pov-fpv-case-1)
  - [ケース 2: 上海サイバーパンク都市のショーリール (投稿者 @Adam38363368936)](#pov-fpv-case-2)
  - [ケース 3: 呪われた侍の一貫性アクションプロンプト (投稿者 @Just_sharon7)](#pov-fpv-case-3)
  - [ケース 4: Y2K プールパーティーのビデオカメラ・モンタージュ (投稿者 @johnAGI168)](#pov-fpv-case-4)
  - [ケース 5: テスラカード視点の都市バースト (投稿者 @xingsthatmatter)](#pov-fpv-case-5)
  - [ケース 6: アニメ MV の極端なクローズアップ (投稿者 @drjoetw)](#pov-fpv-case-6)
  - [ケース 7: 高速でシームレスな 16 ショット (投稿者 @aisavvy1)](#pov-fpv-case-7)
  - [ケース 8: 中世ファンタジー都市への降下 (投稿者 @LudovicCreator)](#pov-fpv-case-8)
  - [ケース 9: ソーダのグラスに落ちる氷を一人称で見る (投稿者 @LudovicCreator)](#pov-fpv-case-9)
  - [ケース 10: 自然な粒子感を持つ荒々しい手持ち 35 mm フィルム (投稿者 @AngelNwoha)](#pov-fpv-case-10)
  - [ケース 11: 10 秒のフォトリアルな映画的 POV 映像 (投稿者 @umitsuru_fire)](#pov-fpv-case-11)
  - [ケース 12: 終末後の超未来メガシティが嵐の中で目覚める (投稿者 @johnAGI168)](#pov-fpv-case-12)
  - [ケース 13: スタイル：超写実的な工業タイムラプス (投稿者 @craftian_keskin)](#pov-fpv-case-13)
  - [ケース 14: 怪物襲撃で変身する女子高生 (投稿者 @Yuupapa_free)](#pov-fpv-case-14)
  - [ケース 15: 東京 POV ジェットコースター (投稿者 @TechTalkNAVI)](#pov-fpv-case-15)
  - [ケース 16: 映画的な北京文化広告 — 8K 一人称視点 (投稿者 @crayon1267)](#pov-fpv-case-16)
  - [ケース 17: 極限マクロ FPV — 妖精の翼を追うショット (投稿者 @EHuanglu)](#pov-fpv-case-17)
  - [ケース 18: 火山洞窟への重力ダイブ (投稿者 @LudovicCreator)](#pov-fpv-case-18)
  - [ケース 19: 超音速で駆け抜ける砂漠峡谷 POV (投稿者 @LudovicCreator)](#pov-fpv-case-19)
  - [ケース 20: フランス花火 FPV フライオーバー (投稿者 @LudovicCreator)](#pov-fpv-case-20)
- [🏷️ コマーシャル / 商品](#commercial-product) (26)
  - [ケース 1: 香水 CM 風アニメ三人組ダンスステージ (投稿者 @ShadeLurk)](#commercial-product-case-1)
  - [ケース 2: ダークファンタジー教会の決闘 (投稿者 @ZaraIrahh)](#commercial-product-case-2)
  - [ケース 3: ダークファンタジー神殿ホールの決闘 (投稿者 @MiraMusic_AI)](#commercial-product-case-3)
  - [ケース 4: 日本のお菓子 CM のオチ (投稿者 @aigeboku)](#commercial-product-case-4)
  - [ケース 5: Seedance 2 向け映画的武術シーケンス (投稿者 @CharaspowerAI)](#commercial-product-case-5)
  - [ケース 6: 日本の教室でささやく恋 (投稿者 @JiahaoYang_art)](#commercial-product-case-6)
  - [ケース 7: LaFerrari CM ストーリーボード (投稿者 @Adam38363368936)](#commercial-product-case-7)
  - [ケース 8: 熱血アニメの最終決闘 (投稿者 @gkxspace)](#commercial-product-case-8)
  - [ケース 9: 磁器クチュールの天空鏡面ランウェイ (投稿者 @johnAGI168)](#commercial-product-case-9)
  - [ケース 10: 現代の農村クリエイターによる収穫広告 (投稿者 @johnAGI168)](#commercial-product-case-10)
  - [ケース 11: ネオン街のストリートレース (投稿者 @CharaspowerAI)](#commercial-product-case-11)
  - [ケース 12: スーパーモデルと高級スポーツカー (投稿者 @johnAGI168)](#commercial-product-case-12)
  - [ケース 13: 研究所を破壊したアンドロイド少女の逃走 (投稿者 @aiehon_aya)](#commercial-product-case-13)
  - [ケース 14: ネオン廃墟都市のゲームトレーラー (投稿者 @adrianaia_)](#commercial-product-case-14)
  - [ケース 15: オリジナル・ダークファンタジーアクション短編 (投稿者 @Rufus87078959)](#commercial-product-case-15)
  - [ケース 16: 00:00–00:04 ショット 1：追跡撮影 (投稿者 @IamEmily2050)](#commercial-product-case-16)
  - [ケース 17: 列車屋根上の戦術格闘 (投稿者 @ImperfectEngel)](#commercial-product-case-17)
  - [ケース 18: マンハッタン取引フロアの狂騒 (投稿者 @johnAGI168)](#commercial-product-case-18)
  - [ケース 19: ポリツィオッテスコ風の水曜日 (投稿者 @ChrisGwinnLA)](#commercial-product-case-19)
  - [ケース 20: 折りたたみスマートフォンのファッション広告 (投稿者 @Adam38363368936)](#commercial-product-case-20)
  - [ケース 21: 旅の相棒になるスーツケースのモンタージュ (投稿者 @ChaseAIx)](#commercial-product-case-21)
  - [ケース 22: 真上からのファッションルックブック — 衣装替え (投稿者 @johnAGI168)](#commercial-product-case-22)
  - [ケース 23: 高級ライフスタイル CM — Vlog 自撮り風 (投稿者 @johnAGI168)](#commercial-product-case-23)
  - [ケース 24: ビート同期の防水スニーカー映像 (投稿者 @madpencil_)](#commercial-product-case-24)
  - [ケース 25: マンゴスチン美容液のプロダクトリビール (投稿者 @ritesh_ai)](#commercial-product-case-25)
  - [ケース 26: ムンバイのスーツケースタクシーお披露目 (投稿者 @rahulnanda86)](#commercial-product-case-26)
- [🖼️ 参照画像ベース](#reference-driven) (21)
  - [ケース 1: 骸骨ピアニストのミニチュアジオラマ演奏 (投稿者 @tea_story_hoshi)](#reference-driven-case-1)
  - [ケース 2: 嵐の船上の王女対クラーケン (投稿者 @applete77191758)](#reference-driven-case-2)
  - [ケース 3: メイド剣舞：メイ対ココ (投稿者 @MiraMusic_AI)](#reference-driven-case-3)
  - [ケース 4: 終末の屋上でピアノに別れを告げる (投稿者 @liyue_ai)](#reference-driven-case-4)
  - [ケース 5: 映画的 8 mm 魚眼、FPV レースドローン、超流動モーション (投稿者 @itsPixieVerse)](#reference-driven-case-5)
  - [ケース 6: 参照画像駆動のカンフースタント (投稿者 @YaReYaRu30Life)](#reference-driven-case-6)
  - [ケース 7: レイトレーシング、Unreal Engine レンダリング、豪雨の町 (投稿者 @Gwsubsa)](#reference-driven-case-7)
  - [ケース 8: 月面コンビニの夜勤 (投稿者 @zasuko_michiksa)](#reference-driven-case-8)
  - [ケース 9: 屋上で覚醒し F-14 へ変形 (投稿者 @john87445528)](#reference-driven-case-9)
  - [ケース 10: 装甲組み立てからの街頭反撃 (投稿者 @egeberkina)](#reference-driven-case-10)
  - [ケース 11: 画像 1 のキャラクターを実写人物化 (投稿者 @Adam38363368936)](#reference-driven-case-11)
  - [ケース 12: ホッキョクグマのマッチカット剣闘テンプレート (投稿者 @aimikoda)](#reference-driven-case-12)
  - [ケース 13: 7 枚の画像によるシームレス変形 (投稿者 @YaReYaRu30Life)](#reference-driven-case-13)
  - [ケース 14: Stridex スニーカー CM (投稿者 @ShamsAmin56)](#reference-driven-case-14)
  - [ケース 15: 歌う猫を使った画像駆動プロンプト (投稿者 @pan_soramame_da)](#reference-driven-case-15)
  - [ケース 16: キャラクター参照アニメプロンプト (投稿者 @Reiria123)](#reference-driven-case-16)
  - [ケース 17: アニメ動物を実写化 (投稿者 @MustafyOf)](#reference-driven-case-17)
  - [ケース 18: 固定ストーリーボードの参照階層 (投稿者 @startracker)](#reference-driven-case-18)
  - [ケース 19: VOLTIA 吸電モンタージュ (投稿者 @itsPixieVerse)](#reference-driven-case-19)
  - [ケース 20: クレオパトラの宮殿告白 (投稿者 @kinovi_ai)](#reference-driven-case-20)
  - [ケース 21: 街灯の下の雨の再会 (投稿者 @umesh_ai)](#reference-driven-case-21)
- [🌀 シュール / VFX](#surreal-vfx) (14)
  - [ケース 1: 無重力の刀剣戦 (投稿者 @MiraMusic_AI)](#surreal-vfx-case-1)
  - [ケース 2: 雲を泳ぐクジラのシュールな叙事詩 (投稿者 @chaosdotjpg)](#surreal-vfx-case-2)
  - [ケース 3: 深海ダイバーが海洋生物へ変貌 (投稿者 @AIARTGALLARY)](#surreal-vfx-case-3)
  - [ケース 4: 異次元メガシティの裂け目崩壊 (投稿者 @LudovicCreator)](#surreal-vfx-case-4)
  - [ケース 5: 雨の地下路地での融合 (投稿者 @Dheepanratnam)](#surreal-vfx-case-5)
  - [ケース 6: 量子現実の破砕による街路の裂け目 (投稿者 @Dheepanratnam)](#surreal-vfx-case-6)
  - [ケース 7: 目が突然開く (投稿者 @roco_kn_roco)](#surreal-vfx-case-7)
  - [ケース 8: 浮遊する溶岩川の上空で激突 (投稿者 @LudovicCreator)](#surreal-vfx-case-8)
  - [ケース 9: クリエイティブディレクターの次元歩行 (投稿者 @lukasersil)](#surreal-vfx-case-9)
  - [ケース 10: 深淵の存在を刻む祭壇碑文 — ダークファンタジー (投稿者 @Adam38363368936)](#surreal-vfx-case-10)
  - [ケース 11: 浮遊 UI カラーホイールによる場面変換 (投稿者 @johnAGI168)](#surreal-vfx-case-11)
  - [ケース 12: 炎の女帝の変身シーケンス (投稿者 @LudovicCreator)](#surreal-vfx-case-12)
  - [ケース 13: 砂の巨人への砂漠変身 (投稿者 @LudovicCreator)](#surreal-vfx-case-13)
  - [ケース 14: 逃走車のごみ収集車変形 (投稿者 @LavrionX)](#surreal-vfx-case-14)
- [📐 テンプレートと構造化形式](#templates-structured) (17)
  - [ケース 1: 超大型空母の壊滅的沈没 (投稿者 @johnAGI168)](#templates-structured-case-1)
  - [ケース 2: 記憶の断片を再構築 (投稿者 @TechTalkNAVI)](#templates-structured-case-2)
  - [ケース 3: 設計図から現実へ — 平屋住宅の変形 (投稿者 @craftian_keskin)](#templates-structured-case-3)
  - [ケース 4: 武術オートクチュールの仕立て屋 (投稿者 @Adam38363368936)](#templates-structured-case-4)
  - [ケース 5: ビート同期の衣装切り替えテンプレート (投稿者 @aimikoda)](#templates-structured-case-5)
  - [ケース 6: 踊る超高層ビル街テンプレート (投稿者 @TechTalkNAVI)](#templates-structured-case-6)
  - [ケース 7: 星明かりの影／星くずのシルエット (投稿者 @TechTalkNAVI)](#templates-structured-case-7)
  - [ケース 8: 絵画風パルクール POV テンプレート (投稿者 @0xbisc)](#templates-structured-case-8)
  - [ケース 9: 360 度 POV 下り階段ラン・テンプレート (投稿者 @aimikoda)](#templates-structured-case-9)
  - [ケース 10: 食べ物とキャラクターの動きテンプレート (投稿者 @Just_sharon7)](#templates-structured-case-10)
  - [ケース 11: 不可能カメラのキッチンダッシュ (投稿者 @Dheepanratnam)](#templates-structured-case-11)
  - [ケース 12: 時間停止 POV バースト (投稿者 @CharaspowerAI)](#templates-structured-case-12)
  - [ケース 13: 宇宙飛行士の初船外活動テンプレート (投稿者 @BrennanErbz)](#templates-structured-case-13)
  - [ケース 14: ゴールデンレトリバーの日常テンプレート (投稿者 @0xbisc)](#templates-structured-case-14)
  - [ケース 15: スタイライズ 3D 理髪店変身シーケンス (投稿者 @ShamiWeb3)](#templates-structured-case-15)
  - [ケース 16: 印象派のボートをこぐ手テンプレート (投稿者 @0xbisc)](#templates-structured-case-16)
  - [ケース 17: 女戦士 — 構造化された被写体プロンプト (投稿者 @noman23761)](#templates-structured-case-17)
- [🎬 一般シネマティック](#general-cinematic) (36)
  - [ケース 1: ハイヒールとビートが同期するファッション接写 (投稿者 @TingFengAIAI)](#general-cinematic-case-1)
  - [ケース 2: 子ども部屋でミニスケートボード脱出 (投稿者 @anson7956)](#general-cinematic-case-2)
  - [ケース 3: ラッカー・パークのおばあちゃん対決 (投稿者 @techhalla)](#general-cinematic-case-3)
  - [ケース 4: 消防士による赤ちゃん救出 (投稿者 @AITalesNBH)](#general-cinematic-case-4)
  - [ケース 5: 古代衣装への変身ショー (投稿者 @johnAGI168)](#general-cinematic-case-5)
  - [ケース 6: 夜の銀座、未来のサイバーパンク (投稿者 @ChiakiAkagi)](#general-cinematic-case-6)
  - [ケース 7: 跳ねる者の物語 (投稿者 @starks_arq)](#general-cinematic-case-7)
  - [ケース 8: 渋谷スクランブル交差点の中央に立つ怪しい男 (投稿者 @roco_kn_roco)](#general-cinematic-case-8)
  - [ケース 9: 漁船の群衆を捉えるスマホ映像 (投稿者 @maxescu)](#general-cinematic-case-9)
  - [ケース 10: デジタルトンネルを高速落下する少女 (投稿者 @_3912657840)](#general-cinematic-case-10)
  - [ケース 11: スカイツリー・レールガン発射 (投稿者 @TechTalkNAVI)](#general-cinematic-case-11)
  - [ケース 12: ハリウッド映画の予告編 (投稿者 @SSSS_CRYPTOMAN)](#general-cinematic-case-12)
  - [ケース 13: 映画的な縦型 9:16 シーケンス (投稿者 @Mayz1169)](#general-cinematic-case-13)
  - [ケース 14: 沿岸都市のそばで巨大氷河壁がフィヨルドへ崩落 (投稿者 @LudovicCreator)](#general-cinematic-case-14)
  - [ケース 15: 月明かりのピアノ追跡劇とネズミ (投稿者 @Dheepanratnam)](#general-cinematic-case-15)
  - [ケース 16: 15 秒連続ワンカットのカートゥーン (投稿者 @Artedeingenio)](#general-cinematic-case-16)
  - [ケース 17: 夕暮れのスチームパンク飛行船戦 (投稿者 @Alin_Reaper05)](#general-cinematic-case-17)
  - [ケース 18: ビーチサンダルのジェット翼を追うショット (投稿者 @maxescu)](#general-cinematic-case-18)
  - [ケース 19: 深山にある古寺の外観 (投稿者 @cdexsta)](#general-cinematic-case-19)
  - [ケース 20: 自由の女神と日の出のストーリーボード (投稿者 @MrDasOnX)](#general-cinematic-case-20)
  - [ケース 21: 劇的照明で描く歴史場面 (投稿者 @AskVenice)](#general-cinematic-case-21)
  - [ケース 22: ロケットサーフィンの連続追跡撮影 (投稿者 @maxescu)](#general-cinematic-case-22)
  - [ケース 23: スタンドアップコメディ独白テンプレート (投稿者 @Adam38363368936)](#general-cinematic-case-23)
  - [ケース 24: 誕生日の裏切りを描くレストランドラマ (投稿者 @Lighterkissan33)](#general-cinematic-case-24)
  - [ケース 25: 古代パルクールの衣装替え (投稿者 @Adam38363368936)](#general-cinematic-case-25)
  - [ケース 26: エンジン内部 — ピストンの機械ディテール (投稿者 @YaReYaRu30Life)](#general-cinematic-case-26)
  - [ケース 27: 90 年代日本恋愛シミュレーション — セル画風 (投稿者 @kinopioai_ai)](#general-cinematic-case-27)
  - [ケース 28: 映画演出技法 — マルチショット・プロンプト (投稿者 @noman23761)](#general-cinematic-case-28)
  - [ケース 29: 東アジア女性のポートレート — 自然な笑顔 (投稿者 @noman23761)](#general-cinematic-case-29)
  - [ケース 30: 終末後のサバイバル — 映画的セットアップ (投稿者 @noman23761)](#general-cinematic-case-30)
  - [ケース 31: ピクサー風の森の空き地 — 3D アニメーション (投稿者 @SPEEDAI07)](#general-cinematic-case-31)
  - [ケース 32: 布団の中でおやつを盗む子猫 (投稿者 @lynneatyoumind)](#general-cinematic-case-32)
  - [ケース 33: Seedance 2.0 T2V 自然発話テスト (投稿者 @tanabe_fragm)](#general-cinematic-case-33)
  - [ケース 34: 紙人形ホラーアニメーション (投稿者 @TomaAIbijo)](#general-cinematic-case-34)
  - [ケース 35: 赤い砂漠を走るバイクの追跡ショット (投稿者 @LudovicCreator)](#general-cinematic-case-35)
  - [ケース 36: ポンペイ災害の DV 映像 (投稿者 @venturetwins)](#general-cinematic-case-36)
<a id="action-fantasy"></a>
## ⚔️ アクション / ファンタジー

<a id="action-fantasy-case-1"></a>
<!-- Case 1: Street Rap MV Performance (by @songguoxiansen) -->
### ケース 1: [ストリートラップ MV パフォーマンス](https://x.com/songguoxiansen/status/2033175478765289598) (投稿者 [@songguoxiansen](https://x.com/songguoxiansen))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-1"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/021.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
16:9 horizontal screen, street rap MV style, neon purple and blue cool tones, explosive cool and fierce atmosphere. 0-3 seconds: Medium shot push-in, city street night scene with flashing neon lights, an 80-year-old silver-haired woman stands in front of a graffiti wall, short silver-white hair styled in a neat slick-back, distinct square face contour, sword-like eyebrows slanting towards the temples, eyes sharp like electricity, wrinkles at the corners of her eyes like badges of time, a confident smile on the corner of her mouth, wearing a black leather jacket over a white printed T-shirt (large black letters "YOLO" on the chest) + black cargo pants + white high-top sneakers, a thick gold chain necklace around her neck, silver bracelet on her wrist, holding up a microphone with both hands, strong drum beats of the BGM start, the old woman's eyes sharpen, and her lips open to start Rap. 3-7 seconds: Medium shot + close-up switch, the old woman starts rapping, with an extremely strong sense of rhythm, her silver hair flying with her head-nodding movements, one hand holding the microphone, the other hand making gestures to match the rhythm—index finger pointing at the camera, palm cutting the rhythm up and down, making hip-hop gestures, movements are smooth and flowing, eyes sharp and looking directly at the camera, wrinkles vividly jumping with her expression, lips opening and closing rapidly to spit out lyrics: [Rap Lyrics] "Eighty-year-old legs, can jump better than you! Silver hair flowing, this is my pride! Don't call me old, my Flow is better than yours, when you were playing rap, I was listening to disco!" (Fast speed, strong rhythm, fierce attitude) Quick cuts: facial close-ups, hand movements, full-body swaying, side silhouettes, synchronized with the BGM beat. 7-11 seconds: Dance segment, the camera pulls back to show the full body, the old woman starts dancing—first the classic hip-hop bounce, then a neat street dance freeze, followed by a body wave transmitting from the shoulders to the toes, and then a quick footwork workout, movements are clean and sharp, silver hair flies under the neon lights, the leather jacket flutters in the air, she continues to Rap while dancing: [Rap Lyrics] "Legs and feet are nimble, speed is not slow, my lyrics are carved in time! You play with phones, I play with beats, eighty years of life, written into this verse!" (Faster rhythm, stronger tone) Low-angle upward shot + 360-degree surrounding shot, capturing the old woman's cool and fierce dance moves. 11-15 seconds: Climax ending, the old woman makes a cool turn, her silver hair arcs in the air, she faces the camera and makes a "shush" gesture with her finger, then her lips move closer to the microphone, singing the last line in a low, magnetic voice: [Reality Lyrics] "Time never defeats a beauty, I just changed the way I experience youth..." (Slow rhythm, deep emotion, lingering finish) The camera slowly pushes in for a close-up of the old woman's eyes, the wrinkles at the corners of her eyes are all stories, her gaze is still sharp yet with a hint of kindness, the BGM abruptly stops at the climax, the frame freezes on the old woman's cool yet slightly gentle smile, vignetting + neon purple light halo.
```

<a id="action-fantasy-case-2"></a>
<!-- Case 2: Black Cat Desert Martial-Arts Duel (by @nopinduoduo) -->
### ケース 2: [黒猫の砂漠武術対決](https://x.com/nopinduoduo/status/2039915824216261101) (投稿者 [@nopinduoduo](https://x.com/nopinduoduo))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-2"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/031.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second Original Desert Martial Arts Short Film: A black cat warrior in light armor stands alone in a desert where yellow sand is flying all over the sky, facing the pursuers. The shots combine slow motion and fast editing; under backlight, the yellow sand rolls like ink mist. The character's movements are elegant yet ferocious, with tattered but flowing robes. Holding a short weapon, he shuttles and counterattacks at high speed. The overall tone is cold, lonely and oppressive, with high-end colors and obvious shallow depth of field, just like a high-quality oriental martial arts movie.
```

<a id="action-fantasy-case-3"></a>
<!-- Case 3: Live-Action Breathing Technique Duel (by @johnAGI168) -->
### ケース 3: [実写版・呼吸法対決](https://x.com/johnAGI168/status/2021610292979876208) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-3"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/035.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Live-Action Anime Adaptation · Breathing Technique Decisive Battle (15 seconds · Super Burning Special Effects Version)
【Core Focus】: Water Breathing (Blue Water Dragon) VS Thunder Breathing (Golden Lightning), live-action extreme speed duel.

【Style】: Hollywood live-action anime adaptation film quality, dark samurai style, 4K ultra-clear, extreme fast cuts, explosive particle light effects, no gore.
【Duration】: 15 seconds
【Scene】: Misty forest under the moonlight, muddy ground, falling leaves.

[00:00-00:05] Shot 1: Water Melody Prelude · Starting Stance (Sense of charging)
Visuals: A young samurai wearing a green and black checkered haori (jacket), lowering his center of gravity under the moonlight, gripping his sword with both hands.
Action: He takes a deep breath, and the surrounding air instantly solidifies. As he draws his sword, a giant blue water dragon, condensed from high-pressure water flow, appears out of thin air, rotating rapidly around his body and blade, emitting the roar of flowing water.
Special Effects Details: The water flow has a realistic sense of splashing, illuminating the dark forest.

[00:05-00:10] Shot 2: Thunder Flash · Charge (Sense of extreme speed)
Visuals: The opponent, a blonde swordsman wearing a yellow triangular patterned haori, is crouched extremely low, adopting the posture of Iaijutsu (sword drawing technique).
Action: The ground suddenly explodes, and he instantly transforms into a dazzling golden lightning afterimage, refracting and charging through the forest in a "Z" shape at a speed undetectable by the naked eye.
Special Effects Details: Golden electric arcs and scorched fallen leaves remain in the places he passes.

[00:10-00:15] Shot 3: Water and Thunder Collision · Final Sound (Ultimate move clash)
Visuals: Extreme speed collision. The young samurai swings the giant blue water dragon down to meet the attack, and the blonde swordsman, transformed into lightning, crashes into him head-on.
Action: The two swords violently collide in the center of the frame.
Special Effects Spectacle: The blue water dragon and the golden lightning instantly explode, forming a massive water-thunder energy storm that spreads outwards. The surrounding large trees are snapped in half by the energy wave, and mud and light obscure the camera. The scene ends in an extremely dazzling blue, yellow, and white light.
```

<a id="action-fantasy-case-4"></a>
<!-- Case 4: 20-Cut High-Speed Anime Sequence (by @tebasaki3D) -->
### ケース 4: [20 カットの高速アニメシーケンス](https://x.com/tebasaki3D/status/2039903531415552048) (投稿者 [@tebasaki3D](https://x.com/tebasaki3D))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/039.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Anime high-speed cut test — 20 hard cuts in 10 seconds (0.5 seconds per cut, no fade-in/fade-out, no transitions).
[0.0 seconds to 0.5 seconds]: Cut 1 — Close-up. Anime Girl A: Long crimson hair, vivid green eyes. Winks at the camera.
```

<a id="action-fantasy-case-5"></a>
<!-- Case 5: Watch a grease-stained mechanic fix (by @sebatheepan) -->
### ケース 5: [油まみれの整備士が修理する様子](https://x.com/sebatheepan/status/2040079840754205010) (投稿者 [@sebatheepan](https://x.com/sebatheepan))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-5"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/041.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Watch a grease-stained mechanic fix 
a violently rattling junker like it’s a martial arts fight. 

Wrenches flying, spark plugs thrown like knives, hood slammed with a thunderous boom. 

From rusty disaster to purring monster in seconds.
```

<a id="action-fantasy-case-6"></a>
<!-- Case 6: Samurai Revenge Short Film (by @sailorv321) -->
### ケース 6: [侍の復讐短編映画](https://x.com/sailorv321/status/2040127822908596305) (投稿者 [@sailorv321](https://x.com/sailorv321))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-6"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/042.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A short film about a samurai who loses his life on a burning battlefield and wakes up as a baby in another world.
The first half is a fierce battle on a battlefield covered in mud and flames. The young samurai challenges his final duel, seems to win for a moment, but is ultimately cut down and falls. His vision tilts low, and his consciousness fades as he is enveloped in fire and smoke.
```

<a id="action-fantasy-case-7"></a>
<!-- Case 7: Stylized 3D Battle Animation (by @johnAGI168) -->
### ケース 7: [スタイライズされた 3D バトルアニメーション](https://x.com/johnAGI168/status/2039924160567058725) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-7"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/047.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Stylized 3D animation with exaggerated proportions, sharp kung-fu-soccer choreography, and controlled rhythmic energy. CHARACTERS - Football master: an impeccably focused martial-arts soccer prodigy in a fitted training top, wrapped wrists, tapered athletic pants, and classic football boots. Piercing gaze. Every movement follows a precise rhythm: pause -> burst -> lock. Theatrical, hypnotic, absolute master of the field. - Opponent goalkeeper: tense, exhausted, intimidated, standing before the goal line under immense pressure. ENVIRONMENT Futuristic night football stadium with glowing floodlights, wet grass, drifting mist, roaring crowd silhouettes, dramatic contrast. MOOD Aggressive precision. Football master = total control. Goalkeeper = anxious, overwhelmed. TIMELINE 0:00-0:02 (Close-up) The ball rests at the player's feet. He taps it lightly once, then rolls his ankle and snaps into a low martial stance, one hand extended, one foot pinning the ball, energy coiling before release. 0:02-0:05 (Action sequence) He flicks the ball high into the air. Launching upward, he strikes it in mid-air with a flurry of kung-fu kicks and spinning leg strikes, each impact perfectly controlled. The ball accelerates, glowing with spiraling energy trails like a dragon sphere. 0:05-0:08 (Tracking shot) He lands and sprints forward with impossible precision footwork, dribbling through multiple defenders in braided arcs, body feints, sweeping turns, and explosive step-overs. The camera tracks low and fast as the glowing ball never leaves his control. 0:08-0:11 He plants his foot, twists his waist, and unleashes a violent, rhythmic power shot. The kick lands with a percussive burst, grass and mist exploding outward, the ball becoming a blazing comet with frosted vapor and shockwave ripples. 0:11-0:13 The goalkeeper dives desperately as the ball curves through the air in a smoking arc, slicing through the frame with dragon-fire energy, then smashes into the top corner of the net. 0:13-0:15 FINAL REVEAL The net whips violently. Smoke and light dissipate. The glowing ball settles in the goal. The goalkeeper lies stunned. The football master stands in silence, turns away calmly, and flicks his wrist as the crowd erupts. Epic, ultra-detailed, cinematic, premium animation, powerful lighting, heroic finish.
```

<a id="action-fantasy-case-8"></a>
<!-- Case 8: Fast-Paced Comedic Parody Short (by @drjoetw) -->
### ケース 8: [テンポの速いコメディパロディ短編](https://x.com/drjoetw/status/2039905967597613558) (投稿者 [@drjoetw](https://x.com/drjoetw))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-8"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/050.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A fast-paced comedic parody Seedance 2 short set in an ancient imperial study. An orange cat dressed as Qin Shi Huang in Han-style golden dragon robes sits behind a large desk. Gray mice in minister outfits line up, each stepping forward with scrolls. The cat barely looks and scribbles messy, meaningless brush strokes, moving faster and faster.

Dialogue (overlapping): Mice: “Your Majesty, urgent matter!” “National crisis!” Cat: “Approved. Next. Whatever.”

Suddenly, the cat slams the desk and shouts, “ENOUGH!!” He stands up and kicks the mice one by one, sending them flying like rockets. Final shot: he smugly adjusts his robe and strides out, saying, “This empire runs perfectly.”

Camera: fast cuts, whip pans, strong motion blur, 0.6–1.2s pacing, ending in slow motion. Tone: absurd, exaggerated, high-energy comedy.
```

<a id="action-fantasy-case-9"></a>
<!-- Case 9: Giant Ninja Tokusatsu Battle (by @EarthGigantea) -->
### ケース 9: [巨大忍者の特撮バトル](https://x.com/EarthGigantea/status/2044026356984623194) (投稿者 [@EarthGigantea](https://x.com/EarthGigantea))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-9"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/OPGJe_kwdEgXZcfi.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A high-energy giant ninja battle in 1980s Japanese Tokusatsu style. The fight features two humanoid ninjas battling in a miniature city.

Characters:
- Blue Ninja (Replacing Hero): A male ninja with blue skin, short blue hair, and a single horn on his forehead. He has piercing red eyes and wears a sleek, dark blue shinobi outfit. He is agile and uses swift martial arts.
- Red Ninja (Replacing Enemy): A male ninja with red skin, medium-length gray hair, and two gray horns. He has red eyes and wears a dark red scarf that flutters in the wind. He is heavily built and wears red-themed shinobi armor.

Action:
The Blue Ninja performs a rapid series of karate strikes and a high-speed backflip to dodge a heavy punch from the Red Ninja. The Red Ninja counters with aggressive, powerful strikes. The camera uses a low-angle perspective to make them look like 50-meter-tall giants fighting among miniature buildings and power lines.

Visual Style:
1980s film aesthetic, 35mm film grain, vibrant retro colors. The movement has the weight and physics of suit-actors performing on a miniature set. Dramatic pyrotechnic sparks fly on impact. Clear blue sky with soft, old-school studio lighting. Close-up on the Blue Ninja's face at the end, showing his red eyes and single horn.
```

<a id="action-fantasy-case-10"></a>
<!-- Case 10: Japanese Anime Dialogue Sequence (by @_3912657840) -->
### ケース 10: [日本アニメの会話シーケンス](https://x.com/_3912657840/status/2040018529441730815) (投稿者 [@_3912657840](https://x.com/_3912657840))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-10"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/056.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Japanese anime. Dialogue in Japanese. Flowing clouds. A girl walks, jumps cutely, and hits a red switch. At the moment of the explosion, it briefly becomes black and white high contrast, then flame-colored high contrast. The tower in the background explodes violently, creating a flame backlight high contrast. The girl says, "Haa~!?" Surprised by the explosion.
```

<a id="action-fantasy-case-11"></a>
<!-- Case 11: 15-Second Original Elemental Battle Short Film (by @ZikinArt) -->
### ケース 11: [15 秒のオリジナル元素バトル短編](https://web.archive.org/web/*/https://x.com/ZikinArt/status/2040006818953322644) (投稿者 [@ZikinArt](https://x.com/ZikinArt))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-11"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/058.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second Original Elemental Battle Short Film: On an ice-covered volcanic mountain range, a warrior in lava obsidian armor collides head-on with an opponent who controls cold crystal power. Under their feet are snow-covered cracked lava; in the air, there are simultaneous flame roars, ice crystal shatters, steam eruptions and storm howls. The camera quickly switches between close-ups of armor textures, ice crystals, ground cracks and the ultimate collision moment, and finally ends with a steam explosion engulfing the screen, featuring a strong "fire vs. ice" visual conflict.
```

<a id="action-fantasy-case-12"></a>
<!-- Case 12: Faberge Fantasy Egg Animation (by @ShamiWeb3) -->
### ケース 12: [ファベルジェ風ファンタジーエッグのアニメーション](https://x.com/ShamiWeb3/status/2040096061835059412) (投稿者 [@ShamiWeb3](https://x.com/ShamiWeb3))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-12"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/064.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Highly detailed cinematic 4K animated video, precious enchanted Faberge-style Easter eggs floating in a dreamy ethereal space, ornate golden filigree and glowing runes on creamy porcelain and jewel-toned shells, semi-transparent eggs revealing intricate animated miniature fantasy
```

<a id="action-fantasy-case-13"></a>
<!-- Case 13: Original Elemental Battle Short Film (by @David_eficaz) -->
### ケース 13: [オリジナル元素バトル短編](https://x.com/David_eficaz/status/2039966320414937236) (投稿者 [@David_eficaz](https://x.com/David_eficaz))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-13"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/074.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Original 15-second short film about an elemental battle: In a volcanic mountain range covered in ice, a warrior in volcanic obsidian armor clashes head-on with an opponent who controls the power of cold crystal. Cracked, snow-covered lava stretches beneath their feet; in the air, flames roar, ice crystals shatter, steam erupts, and storms howl. The camera rapidly alternates close-ups of the armor textures, ice crystals, cracks in the ground, and the culminating moment of the clash, finally ending with an explosion of steam that floods the screen, creating a strong visual conflict between fire and ice.
```

<a id="action-fantasy-case-14"></a>
<!-- Case 14: Cinematic Sci-Fi Fantasy Duel (by @CharaspowerAI) -->
### ケース 14: [映画的な SF ファンタジー対決](https://x.com/CharaspowerAI/status/2040013966986957144) (投稿者 [@CharaspowerAI](https://x.com/CharaspowerAI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-14"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/076.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
ultra cinematic sci-fi fantasy duel in daylight, a warrior wielding a glowing energy blade stands facing a massive terrifying creature, calm and focused, ready for an intense high-speed confrontation

Dynamic cinematic system, mix of tracking shots + fast orbit moves + whip pans, seamless transitions masked by blade motion, impacts, and energy bursts, fluid continuous sequence with alternating real-time and slow motion highlights

(0-3s) wide establishing shot, warrior standing still, energy blade ignites with bright glow, creature approaching aggressively, tension builds
(3-6s) creature lunges forward, warrior reacts instantly with precise sidestep, fast blade strike, fluid defensive movement
(6-9s) high-speed combat exchange, warrior chaining fast strikes and evasions, blade leaving light trails, creature attacking with powerful sweeping motions, camera orbiting rapidly
(9-12s) slow motion highlight, warrior leaps and spins mid-air, energy blade slicing through space, creature reacting to impact, debris and dust suspended
(12-15s) final clash, creature charges, warrior channels force-like energy push combined with forward strike, massive impact sending shockwave across environment

Open landscape under bright daylight, minimal clutter, ground reacting to impacts, dust and debris enhancing motion and scale
Ultra realistic, high-end cinematic action, precise choreography, glowing energy blade effects, strong contrast lighting, fluid motion, intense speed, epic scale, no distortion, no stretching
```

<a id="action-fantasy-case-15"></a>
<!-- Case 15: 15-second continuous single-shot action sequence (by @Artedeingenio) -->
### ケース 15: [15 秒連続ワンカット・アクション](https://x.com/Artedeingenio/status/2039997977897435190) (投稿者 [@Artedeingenio](https://x.com/Artedeingenio))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-15"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/078.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second continuous single-shot action sequence.
No cuts. No scene transitions.

Dark cinematic fantasy realism, dense forest shadows, fog layers, dynamic camera, strong motion weight, grounded creature physics

Scene Structure

Dense forest → cliff edge → open valley

0–3s —
```

<a id="action-fantasy-case-16"></a>
<!-- Case 16: Lone Samurai Cliffside Standoff (by @Alin_Reaper05) -->
### ケース 16: [崖上で対峙する孤高の侍](https://x.com/Alin_Reaper05/status/2040042931172655384) (投稿者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-16"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/079.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A lone samurai stands on a cliff overlooking cherry blossom mountains at sunset, wind blowing petals around him, he slowly draws his katana for the last time, single tear on his face, slow cinematic crane shot rising above him as sun sets, emotional widescreen, ultra-realistic, like Ghost of Tsushima + The Last Samurai, warm golden tones, heartbreaking moment
```

<a id="action-fantasy-case-17"></a>
<!-- Case 17: Aerial Rogue Dragon Dive (by @sebatheepan) -->
### ケース 17: [ならず者ドラゴンの空中急降下](https://x.com/sebatheepan/status/2039723026124575231) (投稿者 [@sebatheepan](https://x.com/sebatheepan))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-17"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/085.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A daring aerial rogue diving on a bio-mechanical glider through a chaotic floating-island bazaar, weaving effortlessly through airborne merchants, dodging passing airships, flocking griffins, and tethered trading posts. He plummets past crumbling stone arches, busy rope bridges, and cascading waterfalls, barrel-rolling through narrow gaps with precision and style. Cinematic tracking shots follow his descent, enhanced by dynamic motion blur and ethereal dappled sunlight reflecting off crystal formations and mist. The sky-city pulses with an energetic fantasy vibe—flapping wings, shouting vendors, and nonstop vertical motion. Ultra-realistic detail with an epic high-fantasy action aesthetic, capturing speed, agility, and fearless momentum through the clouds.
```

<a id="action-fantasy-case-18"></a>
<!-- Case 18: Zero-G Mech Scramble Sequence (by @Dheepanratnam) -->
### ケース 18: [無重力下のメカ争奪戦](https://x.com/Dheepanratnam/status/2044338893764383111) (投稿者 [@Dheepanratnam](https://x.com/Dheepanratnam))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-18"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/ofW5CfXPYCWpNX7M.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
ENVIRONMENT: Cramped zero-G berth, flickering red emergency strobes, rusted airlock, cramped cockpit, stark black void of space with laser fire.
MOOD: Adrenaline shock, desperate scramble, high-G physical strain, exhausted deflation.
MUSIC: Aggressive industrial synth-metal.
COLOR LOGIC: Gritty Cyber-Industrial Look.
STYLE: Ultra-Realistic.
LOGIC RULE: Keep logical consistency in wardrobe, props, locations, and action continuity across all shots.
SHOT 1: ECU, 85mm push-in / Flashing red warning light reflecting in a dilated pupil as the eye snaps open. / SFX: klaxon blare, heavy inhale.
SHOT 2: WS, 35mm handheld jolt / Rhythmic cut into the pilot kicking off the metal bulkhead, floating violently across the zero-G berth, thermal undergarments clinging to sweat. / SFX: metal clang, fabric rip, fast breath.
SHOT 3: MCU, 50mm slide / Cut on action into a magnetic boot locking onto a steel deck plate, sparks kicking up from the impact. / SFX: heavy mechanical clack, spark hiss.
SHOT 4: Insert shot, 85mm rack focus / Match cut into pressure gloves snapping onto wrist seals, twisting violently to lock, green indicator light flaring. / SFX: pneumatic hiss, plastic click.
SHOT 5: Interior locker view, 24mm wide / Object pass into the camera inside the gear locker looking out as the heavy helmet is ripped from the rack, red strobe light illuminating a panicked grimace. / SFX: metal rattle, heavy scrape.
SHOT 6: Insert shot, 50mm handheld / Rhythmic cut into the helmet slamming over the head, latches snapping shut beneath the chin. / SFX: heavy thud, air pressurization whine.
SHOT 7: MCU, centered 50mm push-in / Match cut into a violent thrust forward, hand slamming a yellow airlock release button. / SFX: solid smack, pneumatic release.
SHOT 8: Bird's-eye insert, 35mm overhead / Cut on action into heavy thruster pack igniting, blue flame violently scorching the deck. / SFX: thruster roar, metal groan.
SHOT 9: MS, 35mm pivot / Camera wipe into a chaotic trajectory through the airlock, thermal suit completely covered by the scratched pressure suit, tearing through floating debris. / SFX: wind rush, debris clatter.
SHOT 10: Insert shot, 50mm overhead / Match cut into a thick throttle lever being yanked entirely backward in one aggressive pull. / SFX: mechanical clank, heavy friction.
SHOT 11: WS, 24mm parallax / Whip pan transition into the massive rusted mech tearing out of the hangar bay into the black void of space, thrusters leaving a hard white trail. / SFX: vacuum silence, low bass rumble.
SHOT 12: MS to CU, 35mm glide into 85mm push-in / Sound bridge into the cockpit interior as the pilot grips the dual joysticks, body vibrating with G-force, eyes darting across radar pings, dodging a blinding green laser blast that chars the hull outside the glass. / SFX: radar ping, hull creak, heavy breathing, laser sizzle.
SHOT 13: Insert to MCU, 50mm snap zoom / Smash cut to the primary weapon trigger as a thumb crushes the red button, recoil shaking the frame violently. / SFX: cannon boom, metallic recoil.
SHOT 14: OTS, 35mm handheld / Rhythmic cut into targeting reticles locking, warning screens flashing yellow, sweat violently flinging from the pilot's brow as the cockpit violently rolls. / SFX: warning buzzer, violent thruster hiss.
SHOT 15: WS, 50mm pull-out / L-cut with a match from the targeting screen close to the berth re-entry as the pressure suit drops, helmet rolls across the deck, and the pilot floats backward in thermal wear, collapsing into the netting in the opening frame shape. / SFX: airlock hiss, heavy thud, deep exhale, room tone.
```

<a id="action-fantasy-case-19"></a>
<!-- Case 19: A super high-speed flight action scene of a girl riding a dragon (by @naoyuki_okada) -->
### ケース 19: [ドラゴンに乗る少女の超高速飛行アクション](https://x.com/naoyuki_okada/status/2039573038392614995) (投稿者 [@naoyuki_okada](https://x.com/naoyuki_okada))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-19"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/086.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A super high-speed flight action scene of a girl riding a dragon. High number of frames, 24FPS Japanese full-color anime.
Two dragons, one blue and one red, are flying high above the clouds. They are flying faster than 100 km/h, cutting through the wind and passing between the clouds. A sense of freedom, liberation from anything that might interfere, and speed.
```

<a id="action-fantasy-case-20"></a>
<!-- Case 20: 15-Second Original Desert Martial Arts Short Film (by @NimEshed) -->
### ケース 20: [15 秒のオリジナル砂漠武術短編](https://x.com/NimEshed/status/2039816152222949829) (投稿者 [@NimEshed](https://x.com/NimEshed))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-20"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/091.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second Original Desert Martial Arts Short Film: A black cat warrior in light armor stands alone in a desert where yellow sand is flying all over the sky, facing the pursuers. The shots combine slow motion and fast editing; under backlight, the yellow sand rolls like ink mist. The character’s movements are elegant yet ferocious, with tattered but flowing robes. Holding a short weapon, he shuttles and counterattacks at high speed. The overall tone is cold, lonely and oppressive, with high-end colors and obvious shallow depth of field, just like a high-quality oriental martial arts movie.
```

<a id="action-fantasy-case-21"></a>
<!-- Case 21: Canyon Airstrike Sequence (by @Mr_TuanDoan) -->
### ケース 21: [峡谷への空爆シーケンス](https://x.com/Mr_TuanDoan/status/2044750468849729604) (投稿者 [@Mr_TuanDoan](https://x.com/Mr_TuanDoan))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-21"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/RpLzRvgpJopkYzwc.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
ultra-realistic military strike sequence, shot on ARRI Alexa 65, natural lighting, high contrast, subtle film grain, grounded physics, no CGI feel, intense sound design (NO MUSIC — only raw SFX)

LOCATION: vast desert canyon with rocky ridges, abandoned structures, heat haze, harsh midday sunlight, dust in the atmosphere

SHOT 01 (0-2s) ultra long lens aerial shot — fighter jet already at extreme speed slicing across canyon camera: compressed perspective, heavy heat distortion, slight handheld shake jet crosses frame in milliseconds SFX: distant jet roar building fast

SHOT 02 (2-4s) cockpit interior — tight, shaky handheld realism pilot locked in, oxygen mask, visor reflecting terrain rushing below HUD elements faintly visible (subtle, realistic) camera vibrates with jet turbulence SFX: engine scream, radio static, breathing through mask

SHOT 03 (4-6s) targeting POV — ground rushing fast beneath crosshair locks onto structures below camera: digital zoom feel but realistic optics, slight lag and jitter SFX: targeting beep... wind shear

SHOT 04 (6-8s) under-wing close-up — bomb release mechanism mechanical clamps open — bomb drops cleanly camera: attached rigid cam, no cinematic movement SFX: metallic clunk + air tearing as bomb falls

SHOT 05 (8-11s) bomb falling — tracking shot from above and slightly behind no slow motion, pure gravity acceleration air distortion, subtle spin stabilization fins working ground rushing up fast SFX: air screaming louder

SHOT 06 (11-13s) impact — massive grounded explosion shockwave kicks dust outward realistically, debris heavy and weighty no overdone fireball — dense dust and rock flying camera: distant long lens, shakes from pressure wave SFX: delayed boom, ground rumble

SHOT 07 (13-15s) wide aerial — jet exits frame at insane speed, heat haze trailing smoke column rising from canyon camera: slow pull-back, scale emphasized SFX: jet fades... wind + distant crackling debris
```

<a id="action-fantasy-case-22"></a>
<!-- Case 22: A 15-second hyper-realistic epic war blockbuster (by @john87445528) -->
### ケース 22: [15 秒の超写実的な戦争大作](https://x.com/john87445528/status/2039348028574744685) (投稿者 [@john87445528](https://x.com/john87445528))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-22"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/110.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A 15-second hyper-realistic epic war blockbuster. Style: rugged realism, 35mm handheld film aesthetic, natural grain, subtle shake. Xiang Yu, the Hegemon-King of Western Chu, wearing the armor from Image 2, riding the horse from Image 1, holding a 13-foot 7-inch Overlord Spear, in a famous scene of slaughter on an ancient battlefield, leading a small number of soldiers against thousands of enemy troops in a display of lonely bravery. Scene 1: One-shot, low-angle ground-level slow follow of the horse's hooves, panning up to a close-up of Xiang Yu's face, showing bloodstains, resolute eyes, and a roaring expression as he shouts: “Zhai Xiaoniao,” give me back my money; Scene 2: Low-angle follow shot of Xiang Yu charging on horseback, leading the way; Generate only fighting sound effects and environmental sounds, no background music.
```

<a id="action-fantasy-case-23"></a>
<!-- Case 23: Office Coffee Break Gone Wrong (by @Dheepanratnam) -->
### ケース 23: [オフィスのコーヒーブレイクが大惨事に](https://x.com/Dheepanratnam/status/2039387346706001941) (投稿者 [@Dheepanratnam](https://x.com/Dheepanratnam))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-23"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/117.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Office Coffee Break Gone WrongShot 1: Tired office worker in a button-up shirt sips coffee at his desk in a modern open-plan office. Calm medium shot, fluorescent lights, papers everywhere.Shot 2: He spills a drop — the coffee suddenly animates into a hyper-caffeinated coffee monster with espresso eyes and foam tentacles.Shot 3: Low-angle shot: The monster rampages across desks, flinging staplers and keyboards in realistic arcs while the worker dodges in panic.Shot 4: Fast-paced tracking shot through the office as coworkers scream and dive under tables, papers flying like confetti with accurate physics.Shot 5: Climax: Worker grabs a fire extinguisher and blasts the monster, turning it back into harmless foam. He sits exhausted, now covered in foam, as everyone claps slowly
```

<a id="action-fantasy-case-24"></a>
<!-- Case 24: 15-second continuous single-shot action sequence (by @Artedeingenio) -->
### ケース 24: [15 秒連続ワンカット・アクション](https://x.com/Artedeingenio/status/2039333445403287777) (投稿者 [@Artedeingenio](https://x.com/Artedeingenio))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-24"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/119.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second continuous single-shot action sequence.
No cuts. No scene transitions.

Cinematic fantasy realism, large-scale creature animation, fire simulation, smoke, embers, dramatic lighting, atmospheric depth, dynamic camera tracking

Weighty creature movement, believable scale,
```

<a id="action-fantasy-case-25"></a>
<!-- Case 25: Black Swan vs Boxer (by @KanaWorks_AI) -->
### ケース 25: [ブラックスワン対ボクサー](https://x.com/KanaWorks_AI/status/2045098229847716305) (投稿者 [@KanaWorks_AI](https://x.com/KanaWorks_AI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-25"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/iILeAyierBn5imMB.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Japanese anime style with the exhilarating feel of a competitive fighting game. Set in a boxing ring, 15 seconds, 30fps, no subtitles. High-contrast cinematic lighting, volumetric light, atmospheric particles and smoke, with a strong audience presence. The overall pacing is clean and sharp, with decisive and powerful camera movement, no dragging. High dynamic range with realistic physical feedback.
[Entrance 0–5s]
Low-angle fast tracking shot with a steady push-in. A tall blonde, blue-eyed ballet dancer descends dramatically from above in a “Black Swan” form—more flamboyant and oppressive in presence. As she spins and lands, her movement carries clear aggression; the impact is heavier, sharper, with precise yet tension-filled body control. Feathers scatter through the air like black blades.
Lighting shifts to a cold, high-contrast tone, with sharp highlights outlining her silhouette, creating a dangerous atmosphere. The crowd erupts in cheers mixed with gasps.
Cut—
A towering boxer stands at the center of the ring (red shorts, red gloves, beast-style mouthguard), radiating pressure. Like a gorilla, he pounds his chest, laughing arrogantly with disdain and provocation.
[Fight 5–15s]
Extreme close-up of the boxing bell as it rings sharply. Hard cut back to the ring.
The boxer throws a heavy punch—the Black Swan dodges with an extreme backbend, then immediately unleashes a counterattack:
A rapid upward high kick, followed by consecutive spinning kicks and slicing leg techniques. Her movements are sharper, more aggressive, with accelerated pacing and continuous, relentless attacks. Her motion is both elegant and feral.
The boxer is completely overwhelmed, forced into a defensive state, retreating step by step as his movements grow disordered.
Final move—after a high-speed spin, the Black Swan delivers a powerful horizontal whip kick (with strong kinetic force and air-tearing impact), launching the boxer high into the air before crashing heavily to the ground.
K.O.
The crowd erupts in thunderous cheers. The Black Swan slowly settles her stance, standing at the center of the spotlight. She gracefully bows like a noble black swan.
```

<a id="action-fantasy-case-26"></a>
<!-- Case 26: Ground Crack Superman Launch (by @techprophett) -->
### ケース 26: [地面を割って飛び立つスーパーマン](https://x.com/techprophett/status/2045091209417249026) (投稿者 [@techprophett](https://x.com/techprophett))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-26"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/JnftRXbRJtRUNj2a.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[SCENE SETUP] An open rugged landscape. Rocky ground, overcast sky, wide and cinematic.

[CHARACTER INTRO] The character descends slowly from above, landing firmly on the ground. The impact of his landing sends a small natural shudder through the dirt and loose rocks around his feet.

[THE CROUCH] He slowly crouches down, pressing one fist firmly into the earth. Still. Composed. Eyes forward.

[ENERGY BUILD] The ground around his fist begins cracking and splintering outward. Dirt, small rocks and dust vibrate and tremble. The air around him distorts slightly. Everything shakes — loose stones, dust lifting naturally off the ground around him.

[THE TAKEOFF] He launches violently straight up, leaving a crater where he knelt. Dirt and rocks scatter naturally from the force. He cuts through the low hanging clouds and disappears into the open sky above.

[STYLE] Cinematic. Photoreal. 4K. Natural lighting. Grounded and raw. No energy beams, no glowing effects. Gravity and weight drive everything.
```

<a id="action-fantasy-case-27"></a>
<!-- Case 27: Cloud Cave Sword Shadow (by @Adam38363368936) -->
### ケース 27: [雲洞の剣影](https://x.com/Adam38363368936/status/2039865857179013318) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-27"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/081.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[Cloud Cave Sword Shadow · Heavenly Gate Bloody Battle]
— One-shot sequence at Tianmen Mountain, Zhangjiajie
Core Style: Tsui Hark's new style Wuxia blockbuster, one-shot sequence, high frame rate, 4K ultra-clear.

Tone: Tsui Hark's bright tone, “Cold Jade Blue-Black + Amber Flowing Light.” High contrast, mountain mist acts as a soft light filter, sharpening character outlines, DaVinci industrial-grade color grading.

Scene: Tianmen Mountain, Zhangjiajie (Wacky terrain of Western Hunan. Tianmen Cave opens, swallowing clouds and mist; 999 steps of the Heavenly Ladder hang vertically on the cliff, like a path to heaven; stone forests and pillars cluster like sharp swords, plank roads are faintly visible amidst surging clouds, birds do not cross).

Camera Movement Trajectory:
Low-angle upward shot (emphasizing the natural danger) → Rapid push toward the cave entrance → 180° horizontal pan (showing intense fight on the plank road) → Dive down → Slowly pull back to center → Backlit close-up.

Shot Script:
0-4 seconds [Opening Stance · Heavenly Gate Cloud Surge]:

Movement: Extreme low-angle upward shot, the camera rapidly swoops up and over the Heavenly Ladder from the bottom.

Visuals: Character face reference @[Image 1] Wuxia swordsman attire (white clothes like snow, low-pressed bamboo hat, holding a long sword) stands alone in the center of the 999 steps.

Action: Strong winds whip up the surrounding clouds and mist. [Image 1] holds the sword hilt with the right hand, and the left hand forms a sword-finger gesture across the bridge of the nose. The camera pulls back to show the Tianmen Cave behind him, resembling a giant eye of the heavens.

4-8 seconds [Fierce Battle · Suspended Ladder Interception]:

Movement: 180° orbiting pan.

Visuals: More than ten assassins in tight suits swing down from both sides, clinging to the cliff like monkeys.

Action: [Image 1] touches the steps with his toes, his body spinning upside down. (Tsui Hark-style slow-motion dynamics) The sword remains sheathed, using the sheath as a stick to point, parry, and strike. The air current shakes the rainwater on the steps into mist. The camera rapidly orbits, capturing afterimages and the sparks of metal impact.

8-11 seconds [Breaking the Formation · Traversing the Stone Forest]:

Movement: The camera follows the character diving, passing through a stone archway into the cliffside plank road.

Visuals: Assassins set up a steel wire trap.

Action: [Image 1]'s long sword finally unsheathes (the blade reflects amber sunlight), executing a sweeping strike. The sword energy transforms into a blue-black arc of light, cutting the steel wires. The snapping wires rebound and shatter cliff rocks. He dodges and weaves on the narrow plank road, his figure intersecting with the stone pillars, blending virtual and real.

11-15 seconds [Closing Stance · Mist Dissipates on the Lonely Peak]:

Movement: The camera slowly pulls out from the cave entrance, widening the view to reveal the abyss.

Visuals: Paper talismans (or dead leaves) flutter in the wind. [Image 1] stands at the edge of the Tianmen Cave, with a sea of clouds below his feet.

Action: He performs a sword flourish and sheathes the sword, placing it on his back. Sunlight streams through the Tianmen Cave, creating a massive Tyndall effect.

Freeze Frame: The camera pushes in for an extreme close-up. A drop of blood drips from the edge of the bamboo hat, tracing his jawline. His eyes are sharp as lightning, with the vast landscape in the background.
```

<a id="action-fantasy-case-28"></a>
<!-- Case 28: City of Gods — One-Take Oriental Fantasy Flight (by @john87445528) -->
### ケース 28: [神々の都 — 東洋幻想のワンカット飛行](https://x.com/john87445528/status/2041000256930763046) (投稿者 [@john87445528](https://x.com/john87445528))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-28"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041000256930763046.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
神佛之城·宗师登台】
镜头以一镜到底的方式，在巨型东方奇幻神都中俯仰、翻滚、旋转、飞驰。
【起始帧 - 图1场景】：镜头从天空俯冲而下，掠过悬浮的巨大苍白月球，快速接近两尊耸立云端的巨型佛像立掌雕塑（高度超过百米），穿过佛像指缝间缭绕的薄雾与红色灯笼串。镜头急速下降，俯瞰脚下青绿色运河纵横的东方奇幻水上都城，密集的木质古建筑、吊脚楼、石桥、灯火通明的船坞在雾气中若隐若现。
镜头穿过佛像掌心的雕花装饰，沿着盘绕佛像基座的螺旋木质栈道急速下坠，闪避悬挂的红灯笼、飘扬的经幡、朝拜的僧侣与香火烟雾。镜头俯冲掠过运河水面，激起水花，穿过一艘悬挂红灯的乌篷船顶，滑入水下。
水下镜头轻盈穿过透明的玻璃观景廊道，看到两侧深邃的水底古城废墟、沉没的石柱与浮游的锦鲤。镜头向上突破水面，冲出中心祭祀广场的喷泉，水珠四溅。
镜头在半空翻转，横扫过广场上整齐列队的数百名黑衣武者（如图2所示），他们双手抱拳、静默肃立，形成人墙。镜头穿过武者之间的缝隙，贴地滑行，掠过刻有云雷纹的巨型石质祭坛台阶。
【过渡段】：镜头沿着台阶螺旋上升，闪避两侧燃烧的巨型青铜香炉、摇曳的火光与飘散的香烟。镜头急速旋转360度，展现背景中两尊巨佛雕像、悬浮的苍白月球、雾气弥漫的天际线。
【结束帧 - 图2场景】：镜头最终稳定在祭坛顶端平台，正对着一位身穿白色长袍、腰束米色腰带、肩披黑色机械护甲的中年东方武者（参考图3角色）。他双手自然垂于身侧，手持两柄交叉的银色机械长刀，面带淡然微笑，站在台阶尽头的中心位置。
镜头缓缓后拉，展现他身后两尊巨型佛像立掌雕塑、下方密密麻麻的黑衣武者方阵、以及远处雾气中的水上古城全景。天空苍白月球巨大悬挂，薄雾缭绕，氛围庄严肃穆、史诗感十足。
￼
无剪辑、不可思议的镜头运动、无缝衔接，充满东方神秘、史诗宏大、极具电影感。8K高清画质，高品质影像素材。
```

<a id="action-fantasy-case-29"></a>
<!-- Case 29: Epic Fantasy Battle — Cinematic 10-Second Sequence (by @a_shimanski) -->
### ケース 29: [壮大なファンタジーバトル — 映画的な 10 秒シーケンス](https://x.com/a_shimanski/status/2041431226507051027) (投稿者 [@a_shimanski](https://x.com/a_shimanski))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-29"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041431226507051027.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
I just generated this with a single prompt
Prompt👇
Cinematic 10-second epic fantasy battle sequence in the style of Lord of the Rings, opening with a sweeping aerial crane shot pulling back over a massive ruined battlefield where thousands of armored Norse warriors charge through ash and smoke toward three colossal stone giants crackling with blue lightning, then cutting to a low ground-level tracking shot racing between the boots of sprinting soldiers as a giant's massive stone foot slams into the earth sending warriors flying in slow motion through dust and embers, then cutting to a medium dutch angle shot of a purple-robed female mage and a male sorcerer unleashing violet and blue arc lightning into the giants faces lit dramatically from below, then a whip pan over-the-shoulder shot from the giant's perspective as his enormous clawed hand sweeps across the battlefield scattering warriors like leaves with fire exploding to the right, finally ending on an extreme slow-motion close-up of a blood-soaked Norse warrior's determined face raising his sword and charging directly at the camera before the frame freezes in a blinding white lightning flash and smashes to black, desaturated steel blue and volcanic orange color grade, photorealistic, 8K, cinematic motion blur, epic orchestral atmosphere
```

<a id="action-fantasy-case-30"></a>
<!-- Case 30: Dark Fantasy Transformation — Eastern Style (by @johnAGI168) -->
### ケース 30: [ダークファンタジー変身 — 東洋風](https://x.com/johnAGI168/status/2041146946681721113) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-30"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041146946681721113.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
也可以生成同款视频📺

Seedance 2.0 prompt 👇

【风格】暗黑东方奇幻变身（Dark Fantasy Transformation），电影质感，8K超清，真实摄影（Photorealistic），达芬奇高级调色 【时长】12秒 【场景】明亮现代居家走廊（镜头1）→ 昏暗客厅·深色丝绒沙发（镜头2-3） 【角色】年轻亚洲女性，黑色长发，
图片1
[00:00-00:01] 镜头1：粒子化解体（Particle Dissolve） 中景，明亮居家走廊。女性居中站立直视镜头，身穿深蓝色短袖与黑色短裤。 一道耀眼红色魔法光环从脚底升起，由下至上急速包裹全身（Red Magic Ring FX）。光环扫过之处，身体瞬间碎裂为极速旋转的红色光辉粒子（Particle Burst），整个人化作一团高速旋转的红色粒子球体。 [00:01-00:04] 镜头2：九尾狐凝形（Fox Materialization） 红色粒子球体从走廊门口飞速穿梭进入昏暗客厅（Particle Travel），拖出一条红色光尾轨迹。 粒子撞上深色丝绒沙发表面，炸开后迅速向内收缩聚拢，光影汇聚凝实，幻化为一只巨大的暗黑色九尾狐趴卧于沙发之上。 狐狸周身燃烧红紫相间的魔法火焰（Realistic Fire Simulation），火焰贴着毛发翻涌。体表金色发光符文缓慢流转明灭。九条蓬松巨尾自然散开，尾尖带红色微光。镜头缓推至狐狸面部，琥珀色瞳孔在暗光中发亮。 [00:04-00:12] 镜头3：狐灵化人（Slow Dolly In） 九尾狐全身泛起金色光芒，化作漫天金色火光粒子向上消散（Golden Dissolve FX）。金光散尽，沙发上丝滑显现侧卧的女性身影。 双丸子头发型，身穿紫红色抹胸紧身裙，外搭黑色薄纱披肩。赤足，白皙肤色，深红唇妆，眼神冷艳凌厉直视镜头。 冷色侧光（Cold Side Lighting），一侧明一侧暗。镜头从中景极缓推进至面部特写（Ultra Slow Dolly In），最终定格于双眼，瞳孔中隐约映出一丝残留的红色火光。
```

<a id="action-fantasy-case-31"></a>
<!-- Case 31: Crocodile Fuel-Line River Trap (by @rahulnanda86) -->
### ケース 31: [ワニを燃料ラインへ誘導する川の罠](https://x.com/rahulnanda86/status/2075816671080747410) (投稿者 [@rahulnanda86](https://x.com/rahulnanda86))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-31"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075816671080747410.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
An army river crossing point in bright daylight, a shallow river with a drainage gate built upstream. A jeep is stuck in the water, and a mega crocodile, huge as a truck, has grabbed onto its front bumper, refusing to let go. Nearby, the depot sergeant stands at the drainage gate controls — the same gate he checks and adjusts every single day. A second team waits downriver near a deep pool. Sound: rushing water, groaning metal, croc hissing, shouting, radio voices.

Shot 1 (0–3s) — THE HOOK: Low shot at the water line. The mega crocodile has its jaws locked around the jeep's front bumper, pulling hard, the whole jeep rocking in the current. The driver grips the wheel and shouts into his radio: "IT'S GOT THE BUMPER! IT WON'T LET GO!"

Shot 2 (3–6s): At the drainage gate, the sergeant grabs the control wheel, checking the gauge fast — the same gauge he reads every morning. He calls on the radio: "Opening the gate now! Get ready downriver!"

Shot 3 (6–9s): The sergeant throws the gate open. A sudden surge of water rushes down the river, hitting the crocodile hard from the side and rolling its whole body away from the jeep, tumbling it downstream toward the deep pool where the second team waits.

Shot 4 (9–13s) — BIG SLOW-MOTION MOMENT: The surge carries the crocodile into the pool. Bullet time — its huge body rolls and twists through the rushing water in slow motion, claws and tail thrashing, water spraying high into the air as it's swept further from the jeep.

Shot 5 (13–15s): Time snaps back. The crocodile crashes into the deep pool, caught by the waiting team downstream. The jeep sits safe in the shallow water, the driver breathing hard, looking back at the current still rushing past.
```

<a id="action-fantasy-case-32"></a>
<!-- Case 32: Electric Underground Arena Duel (by @CharaspowerAI) -->
### ケース 32: [電撃が走る地下闘技場の決闘](https://x.com/CharaspowerAI/status/2075596085926514810) (投稿者 [@CharaspowerAI](https://x.com/CharaspowerAI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-32"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075596085926514810.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A battle-crazed martial artist with golden eyes, torn sleeveless robe and crackling lightning aura surrounding his fists, rendered in ultra-premium Japanese anime rendering, MAPPA-inspired action choreography, sharp cel shading, dynamic motion smears, impact frame animation
- Enters an underground arena where a monstrous champion waits among roaring spectators;
- The arena explodes into chaos as both fighters exchange devastating punches, every impact generating visible shockwaves that crack the floor and launch debris into the air;
- The martial artist unleashes a final lightning-infused uppercut that sends the giant opponent crashing through the arena ceiling, ending with sunlight pouring into the destroyed arena as the crowd erupts
Brutal anime combat, tournament arc energy, insane sakuga payoff.
```

<a id="action-fantasy-case-33"></a>
<!-- Case 33: Crocodile Runway Plane Drag (by @rahulnanda86) -->
### ケース 33: [滑走路で飛行機に引きずられるワニ](https://x.com/rahulnanda86/status/2075816060360753484) (投稿者 [@rahulnanda86](https://x.com/rahulnanda86))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-33"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075816060360753484.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
An army airstrip in bright daylight, a long concrete runway with a side taxiway lined with parked fuel bowsers. A supply plane is taxiing fast, trying to line up for takeoff. A mega crocodile, huge as a truck, has clamped onto the plane's wheel strut and will not let go, dragging alongside as the plane rolls. Ground crew stand back near the fuel bowsers — nobody can risk a shot this close to the aircraft. Sound: roaring engines, groaning metal, croc hissing, shouting, radio voices.

Shot 1 (0–3s) — THE HOOK: Low shot at wheel height. The mega crocodile has its jaws locked around the plane's wheel strut, its huge body dragging along the runway as the plane picks up speed. The pilot fights the controls and shouts into his radio: "IT WON'T LET GO OF THE WHEEL! I CAN'T LIFT OFF LIKE THIS!"

Shot 2 (3–6s): On the ground, the crew chief watches from a safe distance near the fuel bowsers, radio in hand. He calls up to the cockpit: "Turn onto the side strip! Use the bowsers!" The pilot's eyes flick to the parked fuel trucks lined up ahead.

Shot 3 (6–9s): The pilot throws the plane into a hard turn off the main runway onto the side taxiway. The crocodile, still clamped to the strut, is dragged sideways along with the turning plane, sliding across the concrete straight toward the row of parked fuel bowsers.

Shot 4 (9–13s) — BIG SLOW-MOTION MOMENT: The crocodile slams into the nearest fuel bowser. Bullet time — the impact crumples the tanker's side in slow motion, metal folding inward, fuel spraying out around the crocodile's body just before it ignites.

Shot 5 (13–15s): Time snaps back. The fuel bowser explodes in one huge fireball, throwing the crocodile clear as fire rolls across the side taxiway. The plane straightens out and speeds down the main runway, lifting off safely into the sky. Cut.
```

<a id="action-fantasy-case-34"></a>
<!-- Case 34: Lightning Striker Anime Goal (by @CharaspowerAI) -->
### ケース 34: [稲妻ストライカーのアニメゴール](https://x.com/CharaspowerAI/status/2075583075044475292) (投稿者 [@CharaspowerAI](https://x.com/CharaspowerAI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-34"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075583075044475292.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
.

I love this kind of concept where you mix
football, hype, energy, and a super stylish anime render.

PROMPT
A French superstar striker inspired by Kylian Mbappé, explosive speed, sharp golden eyes, blue France jersey covered in grass stains, rendered in ultra-premium Japanese sports anime rendering, Anime-inspired sakuga, sharp manga linework, high-contrast cel shading, hand-drawn speed lines, explosive impact frames, dynamic motion smears, glowing aura VFX, Captain Tsubasa-level spectacle
- 0–3s: receives the ball near midfield against Morocco while two Moroccan midfielders press instantly;
- 3–8s: accelerates like a blue lightning bolt, feints past the first Moroccan defender, nutmegs the second, cuts inside past the Moroccan fullback and slips between two Moroccan center-backs, camera whipping around every touch;
- 8–12s: reaches the edge of the box as the Moroccan goalkeeper rushes out and a final defender slides across the shooting lane;
- 12–15s: clearly plants his left foot beside the ball, swings his right leg and strikes with the laces of his boot, a devastating blue comet shot blasting into the top corner while the Moroccan goalkeeper cannot react, ending with the French striker frozen in a heroic anime pose as teammates rush toward him.
```

<a id="action-fantasy-case-35"></a>
<!-- Case 35: Wildflower Griffin Valley Flight (by @Mayz1169) -->
### ケース 35: [野花咲く谷を飛ぶグリフィン](https://x.com/Mayz1169/status/2076561795813355832) (投稿者 [@Mayz1169](https://x.com/Mayz1169))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-35"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2076561795813355832.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[0-4s] The white-haired girl warrior riding her feathered white griffin beast launches off a cliff edge into open golden morning sky, powerful wingbeats, joyful expression, gaining altitude smoothly. [4-9s] They soar low and fast over golden rolling hills and wildflower fields, wind streaming through her hair and the griffin's feathers, banking gently as they glide through soft white clouds, natural relaxed posture, no dramatic pose. [9-13s] They swoop down along a forested mountain ridge and skim just above a sparkling river bend, the griffin glancing playfully at its rider, smooth continuous fast flight. [13-15s] They glide onward into warm golden sunset light over the valley, frame holds steady.
```

<a id="action-fantasy-case-36"></a>
<!-- Case 36: Mongol Cavalry Parthian Shot (by @Ankit_patel211) -->
### ケース 36: [モンゴル騎兵のパルティアンショット](https://x.com/Ankit_patel211/status/2076945741898272939) (投稿者 [@Ankit_patel211](https://x.com/Ankit_patel211))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=action-fantasy-case-36"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2076945741898272939.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

モデルのバリアント: Seedance 2 Mini

**プロンプト:**

```
Endless golden grassland, low sun, wind rippling the grass like water. A Mongol woman rides a compact steppe pony at a controlled canter, bow drawn. She's harassing a Jin cavalry patrol — feigned retreat, turning in the saddle for the Parthian shot, arrow after arrow finding gaps in lamellar armor. The horsemanship is the star: no hands on reins, controlling the horse with legs and weight, the pony reading her body. When one pursuer closes, she drops the bow to a saddle loop, draws a curved saber, and executes a single passing cut. The pursuit becomes a wide sweeping shot — dozens of riders spread across the plain, dust trails behind each one.
```

<a id="cinematic-realism"></a>

<a id="cinematic-realism"></a>
## 🎞️ シネマティック・リアリズム

<a id="cinematic-realism-case-1"></a>
<!-- Case 1: Modern Japan Documentary Sequence (by @kuranoayashi) -->
### ケース 1: [現代日本のドキュメンタリーシーケンス](https://x.com/kuranoayashi/status/2040055299835650266) (投稿者 [@kuranoayashi](https://x.com/kuranoayashi))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=cinematic-realism-case-1"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/045.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Modern Japan. A 15-second live-action documentary-style video set during a high-rise building fire in Tokyo Bay. 
No BGM. No subtitles. Only environmental sounds, radio, wind, fire, and people's voices from the scene.
---
```

<a id="cinematic-realism-case-2"></a>
<!-- Case 2: Shadow-Tracking Longboard Descent (by @Dheepanratnam) -->
### ケース 2: [影を追うロングボードのダウンヒル](https://x.com/Dheepanratnam/status/2039982273076810119) (投稿者 [@Dheepanratnam](https://x.com/Dheepanratnam))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=cinematic-realism-case-2"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/073.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[0-5s] Dynamic low-angle tracking shot pacing a female downhill longboarder in a deep aerodynamic tuck speeding down a steep mountain pass. Blinding, intense directional sunlight hits her profile, generating stark, elongated, pitch-black shadows onto the sheer, rough-hewn ancient stone cliff walls to her right. The atmosphere is adrenaline-fueled with high-contrast, dramatic lighting. 

[5-10s] The camera smoothly tilts up and racks focus entirely to the cliff face, filling the frame with her razor-sharp shadow mimicking her fluid slalom carves across the weathered, pitted limestone architecture, creating a mesmerizing optical illusion of a dark silhouette dancing along the ancient masonry. 

[10-15s] A rapid whip-pan and macro snap-zoom abruptly shifts the camera down to street level for an ultra-realistic extreme close-up of the longboard's vibrant polyurethane wheels executing a heavy sideways drift. Thick, volumetric white friction smoke billows from the wheels as they violently grind against the highly textured, sun-baked granular black asphalt, highlighting raw kinetic energy and photorealistic surface materiality.
```

<a id="cinematic-realism-case-3"></a>
<!-- Case 3: Meteor Awakening War Heroine (by @ChrisTheNerv) -->
### ケース 3: [隕石で覚醒する戦乙女](https://x.com/ChrisTheNerv/status/2040043939109953944) (投稿者 [@ChrisTheNerv](https://x.com/ChrisTheNerv))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=cinematic-realism-case-3"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/075.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
100% real-life shooting texture, Hollywood IMAX blockbuster quality, natural light and shadow, cold documentary style, natural light on a cloudy day, handheld one-shot throughout, breathing shake, random focus shift, 16:9 widescreen.
【Scene Environment】
A destroyed city street extending into the distance. On both sides are ruined concrete buildings, exposed rebar, shattered windows, and some buildings are still burning, with orange flames and black smoke rising. Abandoned cars are scattered on the cracked asphalt road, several of which are burning. The sky is gloomy gray, with smoke and dust suspended in the air. Multiple meteorites streak across the sky with long trails of fire and dense smoke. In the background, terrified civilians scatter among the ruins, some falling, others dragging the injured.
【Main Character】
Chinese beauty, deep red hair tied in a loose, messy bun, with a few strands hanging by her face. Fair skin, sharp features, defined jawline, natural makeup, detailed eye makeup. Attire: Black long leather trench coat over a black vest, black denim mini skirt, black flat combat boots, no belt, wearing black futuristic gauntlets on both hands. Expression is tense and restrained, slightly painful, with slightly furrowed brows—eyes filled with despair and strong will.
【15-Second One-Shot · Awakening Strike Version】
0-2 seconds · Awakening
Low-angle shot, framing her upper body and face, looking up at her standing alone in the center of the destroyed street. The wind blows her black leather trench coat. She opens her lips and screams in Japanese: "Kakusei shiro!" She suddenly opens her right hand, and the black futuristic gauntlet crackles. Purple crystal-textured electric arcs burst from her arm and gauntlet. Air compresses inward, and space warps and distorts. The shockwave emits a low sonic boom. Purple rune lines appear and circulate around her body.
2-5 seconds · Eruption
The camera begins to orbit around her. Dark gold cracks burst from her chest, and thick golden liquid oozes out like blood. She screams in pain. Purple mist and fine electric arcs shoot outward. All her clothing tears open and explodes from the inside, burning into ash—leaving nothing. Organic armor fragments shoot outward, then retract unnaturally to reattach to her body. Purple patterns symmetrically spread across her face. A crack opens on her cheek, revealing pulsating purple light underneath. Simultaneously, multiple mechanical arm-like appendages violently burst from her back—dark metallic texture, blade-shaped, spreading outward like devil's wings. Sparks, blue electric arcs, and golden energy particles explode from the eruption point. The camera captures the complete unfolding from behind—her silhouette outlined against the gray sky, mechanical appendages spread like a fan. The eruption sound is like tearing metal mixed with arc discharge.
5-8 seconds · Growth
Organic matter seeps from her body, the surface shimmering with iridescent light. White armor plates collide and fuse, leaving burn marks. The armor extends downward, completely engulfing and replacing her flat combat boots, forming white and dark purple interwoven armored boots, locking into place with tiny sparks. She grits her teeth and lets out a painful roar. The core in her chest flickers like embers. Purple-black metal spreads over her face, forming an uneven mask, the left eye covered before the right. Compound eyes begin to form, irregularly flashing with liquid light medium. The camera continues to orbit around her.
8-12 seconds · Completion
The camera continues to slowly orbit her. The mask completely seals. Horn-like structures grow upward from the top of her head, burning with purple-gold flames. One compound eye glows steadily, the other flickers with unstable current. The armor is interwoven with white and dark purple, uneven and covered in battle damage, with glowing purple cracks oozing light fluid. Mechanical appendages sway slightly behind her. Each armor plate emits a crisp metallic click when locked, followed by distinct mechanical reset sounds. She slowly lowers her head to examine her hands—the knuckles of the white and dark purple interwoven armored gauntlets seep purple light. She slowly raises her head to look straight ahead, and the compound eyes suddenly glow fully.
12-15 seconds · Supersonic Charge
The camera rapidly retreats. She pushes off the ground with her feet, and the asphalt instantly explodes into a deep crater. A violent purple energy explosion spreads outward from the takeoff point, sending gravel and asphalt fragments flying into the air. She shoots into the air at supersonic speed, charging directly towards the camera—a conical sonic boom cloud forms behind her, the mechanical appendages are flattened backward by the airflow, and the image generates strong dynamic blur. Her figure grows larger and closer, filling the entire frame. A purple energy trail drags behind her. In the final frame, her armored faceplate almost hits the lens, the compound eyes glow scarlet red, and the screen suddenly cuts to black.
【Ambient Sound】
Low sonic boom during awakening, tearing metal and arc discharge sounds, painful screams, crisp metallic clicks, heavy metal sounds of mechanical appendages unfolding, crackling sounds of burning in the background and distant explosions, the final supersonic charge accompanied by the sound of the takeoff explosion, sonic boom impact, and rapidly approaching wind pressure. Everything falls silent the moment the screen cuts to black.
【Physical Texture Enhancement】
Real light and shadow, visible skin texture on the face before transformation, visible real wear and tear on the leather trench coat before transformation. Mechanical appendages possess physical weight and inertia—they sway slightly after unfolding, not rigidly fixed. The armor plates are interwoven with white and dark purple, with visible scratches, welding marks, and uneven edges—not clean and smooth. All movements are steady and powerful, full of pain but resolute—she awakens while enduring. Occasional slight camera shake, pure handheld follow-shot feel.
【Sound Design】
Layered progression from the scream activation to the explosive mechanical eruption, escalating to the takeoff point explosion and the sonic boom of the supersonic charge, finally cutting abruptly to silence. The entire sequence exudes absolute power. Generate sound effects only, no music.
```

<a id="cinematic-realism-case-4"></a>
<!-- Case 4: Misty Capsule Island Drama (by @umesh_ai) -->
### ケース 4: [霧のカプセル島ドラマ](https://x.com/umesh_ai/status/2075847160353181852) (投稿者 [@umesh_ai](https://x.com/umesh_ai))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=cinematic-realism-case-4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075847160353181852.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Use the uploaded image as the exact visual reference for the environment: a dreamy yellow capsule house on a tiny lush island, mossy green terrain, rocky edges, still reflective water, misty forest backdrop, warm glowing interior, and a peaceful cinematic atmosphere. Create a 15 second slow-paced cinematic short with two subjects: a young woman and a young man in simple elegant neutral-toned clothing. Focus on ambience, silence, and emotional subtlety.

Scene 1, beginning: Wide misty establishing shot from across the water at dawn. The tiny island home glows softly. Slow push in as both subjects stand outside near the water’s edge, quietly taking in the view. The woman softly says, “It feels hidden from the world.”

Scene 2: Low angle glide across the reflective water, then tilt up to reveal the grass-covered roof, trees, and the capsule architecture. The man looks worried and says, “Maybe not hidden enough.”

Scene 3, conflict: Interior side shot through the glass wall. They sit across from each other in the two chairs, warm light around them, tension quiet but visible. A distant rumble, light wind in the trees, gentle ripples in the water. The woman whispers, “Do we stay?” He pauses.

Scene 4: Slow orbit outside the house, circling from the rocky shore to the panoramic glass, savouring the full landscape. The man steps closer to the glass, watching the mist clear.

Scene 5, climax: Close intimate shot. He turns to her and says, “We stay. Together.” She smiles with relief.

Scene 6, resolution: Final wide pullback from above and across the lake. Both subjects now stand side by side inside the glowing capsule home, calm and reunited, framed by the serene island, soft fog, still water, and quiet forest. The mood ends peaceful, intimate, and healing.
```

<a id="cinematic-realism-case-5"></a>
<!-- Case 5: Storm Cliff Samurai Reveal (by @umesh_ai) -->
### ケース 5: [嵐の断崖に現れる侍](https://x.com/umesh_ai/status/2076604605937688791) (投稿者 [@umesh_ai](https://x.com/umesh_ai))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=cinematic-realism-case-5"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2076604605937688791.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
From a low angle, the camera rockets up past razor-edged cliffs, riding the wind to a breathtaking height, then tilts down to reveal a violent ocean smashing itself into stone. At the very edge, a lone samurai warrior stands perfectly still, silhouetted against spray and thunder, looking down into the chaos.
```

<a id="cinematic-realism-case-6"></a>
<!-- Case 6: VHS Pool Cannonball Judge (by @Ankit_patel211) -->
### ケース 6: [VHSプール大飛び込み審査員](https://x.com/Ankit_patel211/status/2077121431339725240) (投稿者 [@Ankit_patel211](https://x.com/Ankit_patel211))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=cinematic-realism-case-6"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2077121431339725240.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

モデルのバリアント: Seedance 2 Mini

**プロンプト:**

```
This is real 1990s home video footage shot on a VHS camcorder at a crowded public swimming pool. The video has the typical faded colors, analog grain, soft image quality, slight tracking distortion, and subtle tape noise characteristic of consumer VHS recordings from that era.
The camera is handheld and very shaky, filming from a distance across the pool. In the background, a woman wearing a colorful floral one-piece swimsuit stands nervously at the top of the diving board. A large crowd around the pool begins cheering rhythmically with loud "eh-eh-eh" chants, encouraging her to jump.
After several seconds she finally runs forward and performs a surprisingly perfect cannonball. She hits the water with tremendous force, creating an enormous splash that reaches several meters into the air and completely drenches nearby spectators.
For a brief moment everything becomes silent. Then an elderly man wearing sandals, white tube socks, sunglasses, and a sun visor slowly walks into frame carrying a homemade cardboard sign with a large handwritten "10.0." Without saying anything he raises it high above his head exactly like an Olympic diving judge.
The entire crowd immediately erupts into loud cheering, applause, laughter, whistles, and celebration. Several strangers begin chanting her name while children clap excitedly. The woman climbs out of the pool laughing as spectators congratulate her like she has just won an international championship. People gather around asking to take photos with her while the elderly judge proudly continues displaying the scorecard.
The camera movement remains extremely handheld and shaky throughout, with natural motion blur, imperfect zooming, accidental reframing, and several unplanned cuts as the person filming struggles to follow the celebration.
Natural sound only. Crowd chanting, loud applause, laughter, splashing water, echoing pool ambience, and authentic VHS microphone audio. No background music or narration.
The result must feel like authentic raw 1990s home video footage capturing a completely ordinary pool jump that somehow turned into an Olympic-level celebration.
```


<a id="pov-fpv"></a>
## 🥽 POV / FPV

<a id="pov-fpv-case-1"></a>
<!-- Case 1: Chest-Mounted Camouflage Chase Sequence (by @genel_ai) -->
### ケース 1: [胸部カメラによる迷彩チェイス](https://x.com/genel_ai/status/2039538309790404797) (投稿者 [@genel_ai](https://x.com/genel_ai))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-1"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/004.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A hyper-realistic, 8K resolution, adrenaline-fueled single-take POV action sequence. The camera is chest-mounted on a man wearing camouflage joggers and worn-out black-and-white sneakers. He stands on the dizzying edge of a rusted skyscraper, 1000 feet above a crystalline turquoise ocean. No clouds, no haze—just a sheer, terrifying vertical drop into the deep blue.
[The Initial Freefall]
The sequence begins with a sudden, heart-stopping leap into a 20-meter vertical freefall. The camera points directly at his feet as the sea surface rushes toward the lens. A deafening, high-pitched whistling 'Hyuo' wind screams past the microphone. Just before the impact, he catches a lower rusted horizontal bar with both hands—white wristband visible—and swings his body forward to land on a tiny vertical pole.
[The Rhythmic Jumps & The Near-Death Slip]
He immediately begins a rhythmic series of high-speed jumps:
Jump 1: A clean, agile spring to a second vertical pole 2 meters away.
Jump 2: A rapid leap to a thin, rusted horizontal pipe.
Jump 3 (The Slip): As he jumps toward the third vertical pole, his right sneaker completely misses the mark and slides off the rusted metal. The camera tilts violently over the edge, staring straight down at the 1000-foot abyss. He lets out a sharp, panicked gasp. For a terrifying second, his body leans into the void, but he desperately claws at the pole with his fingers, his boots scrambling against the side until he manages to hook his leg and haul himself back up.
Jump 4: Still trembling, he forces a frantic, heavy-breathing leap to the next bar to keep the momentum.
Jump 5: A final, explosive long-distance jump to a swaying metal platform. He lands with a heavy, jarring metallic 'Clang', his body hunching low, gripping the vibrating metal for dear life.
[The Ending]
The camera remains in a low, fetal position on the final bar, shaking from the adrenaline. No dialogue. The audio is a visceral layer of the aggressive 'Hyuo' wind, his intense, ragg
```

<a id="pov-fpv-case-2"></a>
<!-- Case 2: Shanghai Cyberpunk City Sizzle Reel (by @Adam38363368936) -->
### ケース 2: [上海サイバーパンク都市のショーリール](https://x.com/Adam38363368936/status/2039498800801398911) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-2"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/005.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
You can try this:

A 15-second Hollywood-level Shanghai city fast-cut video. Style: a fusion of cyberpunk and modern Haipai aesthetics, cinematic teal-and-orange color grading, 8K ultra-HD.
Shot sequence:
1. The Lujiazui skyline trio cuts through dawn clouds and mist in a dramatic helicopter dive shot.
2. The camera rapidly pushes toward the Bund's historic buildings, revealing detailed stone textures.
3. An FPV craft races through neon-lit night streets and sweeps past the Oriental Pearl Tower.
4. Timelapse of the spiral approach bridge of Nanpu Bridge, with golden car-light trails converging into rings.
5. An aerial shot glides smoothly past the Wukang Building beneath plane-tree shadows.
6. Macro close-up: a steaming basket of Nanxiang soup dumplings is lifted by chopsticks, the broth trembling inside.
7. High-speed montage flashback: Shikumen alleyways, the maglev train, Yuyuan traditional architecture, and the modern skyline flash by rapidly.
Requirements: extremely dynamic camera movement, FPV aerial motion, macro cinematography, and silky transitions.
Mood: energetic, futuristic, premium, fast-paced. Combine wide city views with fine details to emphasize the city's pulse and a commercial-advertising texture. 4K, realistic style, smooth motion.
```

<a id="pov-fpv-case-3"></a>
<!-- Case 3: Cursed Samurai Consistency Action Prompt (by @Just_sharon7) -->
### ケース 3: [呪われた侍の一貫性アクションプロンプト](https://x.com/Just_sharon7/status/2040685931858907646) (投稿者 [@Just_sharon7](https://x.com/Just_sharon7))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-3"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/006.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Strictly follow the reference character’s face, hairstyle, outfit silhouette, and body proportions. Do not change identity or facial structure. Fixed appearance: glowing dark eyes, torn black samurai kimono, traditional katana, black cursed smoke slowly leaking from the body, flowing shadow energy aura, calm but cruel expression, supernatural high-speed movement, consistent identity and physical appearance throughout the entire scene. Strictly follow the reference character’s face, hairstyle, outfit silhouette, and body proportions. Do not change identity or facial structure. Fixed appearance: glowing dark eyes, torn black samurai kimono, traditional katana, black cursed smoke slowly leaking from the body, flowing shadow energy aura, calm but cruel expression, supernatural high-speed movement, consistent identity and physical appearance throughout the entire scene. Hyper-realistic cinematic action, Unreal Engine quality, fast-paced 12s sequence. Cursed lone samurai (strict consistency: female Japanese, long tied black hair, pale skin, glowing dark eyes, torn black kimono armor, katana, black cursed smoke, shadow aura, calm ruthless expression). Environment: abandoned temple shrine at night, broken torii gates, shattered statues, debris, moonlight + dim lanterns, dust and wind, dozens of enemies, dark gritty tone. Camera: aggressive tracking, whip pans, blade POV, high-speed motion, no slow motion. Action: 0–3s: Samurai stands surrounded → instant iaijutsu draw → dark energy slash cuts multiple enemies. 3–6s: High-speed dashes, shadow afterimages, rapid slashes, enemies fall, debris flying. 6–9s: Close combat, parries, teleport-like strikes, circular slashes clearing groups. 9–12s: Final spinning slash → massive dark wave → enemies freeze then collapse → silence, smoke fading.
```

<a id="pov-fpv-case-4"></a>
<!-- Case 4: Y2K Pool Party Camcorder Montage (by @johnAGI168) -->
### ケース 4: [Y2K プールパーティーのビデオカメラ・モンタージュ](https://x.com/johnAGI168/status/2040628800422322359) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/010.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[Style] Millennium retro pool party (Y2K Pool Party), MiniDV camcorder texture, overexposed warm yellow highlights, film grain, VHS interference lines, fast beat-synced editing.
[Duration] 15 seconds.
[Scene] A 2000s American backyard pool party under blazing sun, with glaring light reflections on the water, folding lounge chairs, a silver CD player, rainbow inflatable floats, and a plastic whale.
[Characters] A group of Y2K-styled girls: low-rise bikinis, belly chains, colorful plastic sunglasses, butterfly clips, and glossy glitter lips.
[00:00-00:01.5] Shot 1: explosive water emergence (Close-up / Pullback)
A DV startup blue screen flashes with a red REC dot. Extreme face close-up: a girl wearing colorful plastic sunglasses bursts up from underwater, flipping wet hair into an arc of water in slow motion. Water droplets splash onto the lens. She laughs straight into the DV camera as the sunlight blows out to pure white.
[00:01.5-00:03] Shot 2: poolside parade (Low Angle / Right Pan)
A low waist-height right pan tracks three girls in sheer cover-ups walking across wet tiles holding canned drinks. One of them takes a selfie with a flip phone. Thick platform flip-flops slap against the ground.
[00:03-00:04.5] Shot 3: push into the pool (Dutch Angle)
Dutch-angle medium shot. One girl shoves her friend into the pool from behind. A soda can flies out, the body crashes into the water, spray explodes everywhere, and the girl who pushed her bends over laughing.
[00:04.5-00:06] Shot 4: FPV dive (FPV Drone Dive)
An FPV shot dives from above, skimming over the water. The girls lie sunbathing on floats. Someone raises a disposable camera and flashes directly into the lens.
[00:06-00:07] Shot 5: ice into the cup (Macro / Still)
Macro static shot. Ice cubes drop into a plastic cup, orange liquid splashes upward, and the hand holding the cup wears colorful rubber bracelets. Sunlight passes through the liquid and casts caustic light patterns.
[00:07-00:08.5] Shot 6: dance follow shot (Tracking / Backward Follow)
The camera tracks backward while locking onto the face. A girl with wet hair stuck to her cheeks and butterfly clips dances through the crowd in a woven bikini. Her hoop earrings swing as she smiles straight at the lens.
[00:08.5-00:10] Shot 7: diving silhouette (Worm's Eye / Push-in)
A worm's-eye push-in captures a girl launching from the diving board as a silhouette. The sun bursts into lens flare, and water droplets turn into points of light in the air.
[00:10-00:11.5] Shot 8: cheers (Close-up / Left Pan)
Fast left pan. Two girls clink red plastic cups together, liquid splashing out in golden arcs while they squint and laugh.
[00:11.5-00:13] Shot 9: DJ over-shoulder (OTS / Pull-in)
Push in from behind the DJ's shoulder. In the foreground, fingers press the silver CD player's button. In the background, the girls splash water wildly in rhythm, and the backlit spray becomes a curtain of golden rain.
[00:13-00:15] Shot 10: golden wide freeze frame (Extreme Wide / Crane Rise)
A rapid crane rise opens the entire pool party in golden-hour warm light, full of people and inflatable toys, with the water shimmering like broken gold. Overlay a DV timestamp reading "08/15/2000 PM 5:47" and freeze the frame with a flickering VHS pause effect.
```

<a id="pov-fpv-case-5"></a>
<!-- Case 5: Tesla Card POV City Burst (by @xingsthatmatter) -->
### ケース 5: [テスラカード視点の都市バースト](https://x.com/xingsthatmatter/status/2040190310043812035) (投稿者 [@xingsthatmatter](https://x.com/xingsthatmatter))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-5"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/038.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Cinematic CG ad quality, ultra-realistic, first-person POV, high-speed one-take camera movement, strong visual impact.

The camera bursts out from inside image1, the Tesla card, as the card spins forward at high speed. The camera stays tight to its edge, tracking it through city
```

<a id="pov-fpv-case-6"></a>
<!-- Case 6: Anime MV Extreme Close-Up Sequence (by @drjoetw) -->
### ケース 6: [アニメ MV の極端なクローズアップ](https://x.com/drjoetw/status/2040036596897222773) (投稿者 [@drjoetw](https://x.com/drjoetw))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-6"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/049.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A highly dramatic, fast-cut anime MV with exaggerated cinematic tension and comedic payoff. 1930s Tokyo rice paddies, muddy textures, stormy sky. Extreme sense of falling urgency using rapid cuts, POV distortion, speed ramps, spinning camera, impact zooms. Dramatic orchestral music escalating non-stop, then sudden comedic release at the end. No dialogue, no voice-over. Each shot 0.6–1.2s.

0–0.8s (HOOK)
Extreme close-up: muddy water surface. Ripple expands → reflection shows a white tiger falling from the sky at insane speed.

0.8–1.6s
SMASH CUT → tiger tumbling mid-air, body spinning violently, wind tearing fur.

1.6–2.4s
POV tiger → ground rushing upward extremely fast. Rice paddies distort with speed.

2.4–3.2s
Cut → orange cat in muddy farmer clothes, calmly planting rice. Slow, peaceful motion.

3.2–4.0s
Back to tiger → extreme close-up eyes, panic rising. Sunglasses slightly slipping.

4.0–4.8s
Rapid micro-cuts: sky spin → ground zoom → cat step → sky spin → distance collapsing fast.

4.8–5.6s
Top-down shot → tiger perfectly aligned to crash into orange cat.

5.6–6.4s
Tiger yanks parachute → explosive deploy → instant violent spinning chaos.

6.4–7.2s
Camera rotates 360° with tiger. Horizon flips. Ground now dangerously close.

7.2–8.0s
Parachute unstable → cords under extreme tension. Tiger loses control completely.

8.0–8.8s
Tiger panic peaks → aggressively twists cords into a tight yarn-ball knot.

8.8–9.6s
Parachute collapses → freefall speed doubles. Sound compresses into heartbeat rhythm.

9.6–10.4s
Ultra-fast dive shot → motion blur streaks. Orange cat grows rapidly in frame.

10.4–11.2s
Cut → cat finally senses something. Slight head turn.

11.2–12.0s (IMPACT BUILD)
Extreme close-up: tiger face in silent scream → smash zoom toward ground.

12.0–12.8s (IMPACT)
Massive muddy explosion. Water and mud burst upward in slow motion.

12.8–13.6s
Mud rain falls. Silence. Shapes slowly appear through the splash.

13.6–14.2s (REVEAL)
White tiger sitting on top of the orange cat’s back, slightly dazed but intact.

14.2–15.0s (COMEDIC PAYOFF)
Close-up: orange cat’s face, completely covered in mud, eyes half-open, extremely annoyed.
White tiger casually adjusts sunglasses while sitting on him.
Freeze frame → dramatic music abruptly cuts.
```

<a id="pov-fpv-case-7"></a>
<!-- Case 7: Fast Seamless 16-Shot Sequence (by @aisavvy1) -->
### ケース 7: [高速でシームレスな 16 ショット](https://x.com/aisavvy1/status/2040054688054382972) (投稿者 [@aisavvy1](https://x.com/aisavvy1))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-7"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/052.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Create a fast, seamless 16:9 flying POV sequence with five linked shots.
Shot 1: Start inside a dark ancient stone corridor with a wooden door at the far end. Fly straight toward it at high speed. As the camera reaches the door, it begins to swing open, revealing a gap of bright blue ocean behind it. End mid-opening.
Shot 2: Continue through the opening door into the ocean. Fly forward through fish, bubbles, light rays, and underwater plants. A giant fish approaches and opens its mouth directly in front of the camera. End inside its mouth.
Shot 3: The darkness inside the fish’s mouth becomes the dark interior of a large stainless steel kitchen hood or service opening. Fly forward into a busy high-end restaurant kitchen with chefs, flames, steam, pans, and plated dishes. Fly low over the counter. End with the glowing opening of a large industrial oven filling the frame.
Shot 4: Continue into the glowing oven as it transforms into a volcanic lava tunnel with molten light and black rock. Fly through the tunnel. End with a bright circular stone opening filling the frame.
Shot 5: Continue through the circular opening into a Mediterranean cliffside village above the sea. Fly fast between terraces, rooftops, arches, and sunlit walls toward the ocean. End with a wide sea-facing reveal.
Fast, smooth, continuous movement. No flying device, shadow, or reflection. Cinematic.
```

<a id="pov-fpv-case-8"></a>
<!-- Case 8: Medieval Fantasy City Descent (by @LudovicCreator) -->
### ケース 8: [中世ファンタジー都市への降下](https://x.com/LudovicCreator/status/2039983776206344231) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-8"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/069.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
**Environment:**

A massive medieval-fantasy city under siege at dusk. Stone towers, cathedral spires, and narrow streets stretch toward the horizon while fire spreads through rooftops and smoke rises into the orange evening sky. Wind currents swirl between the tall buildings.

**Action:**

15.0s sequence from the first-person perspective of a colossal dragon in flight. The viewer sees the edges of scaled wings occasionally entering frame as the dragon glides between towers. Heat shimmer ripples from its throat with every breath.

At the 2-second mark the dragon dives sharply between two cathedral spires.

Stone gargoyles and stained-glass windows rush past at extreme speed.

The dragon unleashes a stream of fire across a city wall below, igniting entire streets.

Velocity Ramp choreography: the moment the dragon pulls up from the dive slows dramatically — embers, sparks, and falling debris suspended in mid-air — before snapping back as the dragon bursts through a collapsing tower.

**Camera:**

Fast aerial predator POV weaving through the skyline, banking sharply between towers and rooftops.

**Style & Constraints:**

Photorealistic fire simulation, volumetric smoke, cinematic sunset lighting, realistic wing turbulence and debris physics, 8K resolution.
```

<a id="pov-fpv-case-9"></a>
<!-- Case 9: First-person POV of an ice cube dropped into a glass of soda (by @LudovicCreator) -->
### ケース 9: [ソーダのグラスに落ちる氷を一人称で見る](https://x.com/LudovicCreator/status/2039623813080416486) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-9"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/093.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
First-person POV of an ice cube dropped into a glass of soda.

The cube crashes into a bubbling ocean of carbonated liquid.

Gigantic bubbles rise like balloons around the cube.

A lemon slice floats overhead like a glowing sun.

The ice cube slowly melts as the drink level lowers.

Finally the cube slides toward a straw vortex and disappears.

Macro drink environment POV, carbonation bubble storms, melting ice transformation, cinematic macro realism, 4K.
```

<a id="pov-fpv-case-10"></a>
<!-- Case 10: Gritty, raw handheld 35mm film aesthetic with natural film grain (by @AngelNwoha) -->
### ケース 10: [自然な粒子感を持つ荒々しい手持ち 35 mm フィルム](https://x.com/AngelNwoha/status/2039792884841591009) (投稿者 [@AngelNwoha](https://x.com/AngelNwoha))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-10"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/102.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Gritty, raw handheld 35mm film aesthetic with natural film grain. Bright early-morning sunlight streaming through windows, creating sharp indoor shadows. Controlled handheld tracking shot (3rd person POV, over-the-shoulder), stabilized cinematic motion with subtle natural shake.
```

<a id="pov-fpv-case-11"></a>
<!-- Case 11: 10-second photorealistic cinematic POV video (by @umitsuru_fire) -->
### ケース 11: [10 秒のフォトリアルな映画的 POV 映像](https://x.com/umitsuru_fire/status/2039295650039554051) (投稿者 [@umitsuru_fire](https://x.com/umitsuru_fire))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-11"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/105.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
10-second photorealistic cinematic POV video. A Japanese woman in her early 20s with a black short bob hairstyle, straight hair, natural refined makeup, and a white blouse sits inside a Ferris wheel gondola at night near the top. Outside the window is a beautiful city nightscape
```

<a id="pov-fpv-case-12"></a>
<!-- Case 12: A super futuristic megacity after the apocalypse awakens in a storm (by @johnAGI168) -->
### ケース 12: [終末後の超未来メガシティが嵐の中で目覚める](https://x.com/johnAGI168/status/2039380975801471305) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-12"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/108.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A super futuristic megacity after the apocalypse awakens in a storm. Dark clouds press down on the city. Giant battleships slowly descend from the sky, piercing through thunderclouds. The city's high-rise buildings are interwoven with neon lights and fire. Countless drones and armored vehicles shuttle rapidly through the streets. A distant energy tower erupts with dazzling blue electric arcs. The camera dives from high altitude into the city canyon, then rapidly pushes through falling debris and flames, finally settling on the back of a lonely hero wearing a black trench coat, standing on the edge of a skyscraper overlooking the entire burning city. Cinematic lighting, IMAX epic feel, ultra-high detail, stunning composition, strong volumetric light, realistic explosion smoke and dust, epic disaster movie atmosphere, extreme realism, top Hollywood visual effects.
```

<a id="pov-fpv-case-13"></a>
<!-- Case 13: Style: Ultra-realistic industrial timelapse (by @craftian_keskin) -->
### ケース 13: [スタイル：超写実的な工業タイムラプス](https://x.com/craftian_keskin/status/2039415621960499603) (投稿者 [@craftian_keskin](https://x.com/craftian_keskin))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-13"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/111.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Style: Ultra-realistic industrial timelapse
Pacing: Extremely fast (hyperlapse feel)
Camera: Mostly fixed with slight cinematic motion (slider/drone feel)
Lighting: Bright factory lights, metallic reflections
Audio: Captivating cinematic electronic/industrial music (no dialogue)

[00:00–00:03] — Bare Frame

Shot 1 (wide, static)

Empty car chassis suspended on assembly line
Conveyor begins moving

Workers enter frame rapidly (timelapse speed)
Tools flashing, sparks briefly

[00:03–00:06] — Structure Builds

Shot 2 (slight side angle)

Doors, internal components appear quickly
Technicians blur in motion

Robotic arms assisting (fast, precise movements)
Parts snapping into place rapidly

[00:06–00:09] — Complexity Grows

Shot 3 (closer view)

Wiring, dashboard, engine components installed

Hands moving at hyper speed
Panels closing, interior forming

[00:09–00:12] — Exterior Completion

Shot 4 (dynamic angle)

Body panels attach
Wheels snap into place

Car begins to look complete
Motion blur emphasizes speed

[00:12–00:15] — Final Form

Shot 5 (hero shot)

Fully assembled car rolls forward

Lights flick on
Clean, finished vehicle

End moment:

Camera holds briefly as car exits frame
```

<a id="pov-fpv-case-14"></a>
<!-- Case 14: Monster Attack Schoolgirl Transformation (by @Yuupapa_free) -->
### ケース 14: [怪物襲撃で変身する女子高生](https://x.com/Yuupapa_free/status/2039329682492121547) (投稿者 [@Yuupapa_free](https://x.com/Yuupapa_free))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-14"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/113.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
cinematic, heavy action blockbuster film, Japanese city center, collapsed main street at dusk. A giant monster is knocking down buildings, dust, sparks, rubble, and black smoke are flying, and a Japanese high school girl in a uniform is desperately running towards the camera. Cut 1 (0.0s-2.5s): low angle tracking shot following the high school girl from the front as she retreats. Her hair and skirt are violently fluttering, the ground shakes from the monster's footsteps behind her, cars overturn, and window glass shatters. Her face shows determination amidst fear. Cut 2 (2.5s-3.7s): close-up of her feet. With every step she runs, black metal frames and pink glowing lines deploy onto her legs, rapidly equipping from her thighs to her shins and boots. Sparks and fine energy particles, mechanical transformation. Cut 3 (3.7s-4.8s): close-up of her hands. As she swings her arms, armor forms around her forearms, wrists, and fingertips, with pink light strips running through the gaps in the black armor. Cut 4 (4.8s-6.0s): close-up of her abdomen and chest. Abdominal inner wear, chest armor, and shoulder units lock sequentially, and the central core pulses pink with her breathing. Rack focus shows the detail of the armor. Cut 5 (6.0s-7.0s): close-up of her head. As her hair flies, a helmet deploys from the sides and back, enveloping her face line, and finally the visor closes while glowing. eyes visible through translucent visor. whip pan completes the transformation. Cut 6 (7.0s-8.8s): wide shot. After running a few steps at high speed, the transformed girl skids to a halt, scattering sparks and fragments, twists her body, and faces the monster. She thrusts one hand forward, and a pink spherical energy vortex converges on the device on the back of her hand, drawing in surrounding rubble. Cut 7 (8.8s-10.5s): over-the-shoulder shot capturing the monster, and she silently fires an energy blast all at once. A thick pink shockwave runs straight through, piercing the monster's chest. Cut 8 (10.5s-12.0s): super large explosion. The monster is blown to smithereens, fragments and smoke fly into the sky, and the giant body collapses. The final shot is a hero shot, the high school girl in a black and pink powered suit standing with the explosion behind her. dramatic backlight, debris, heat haze, high contrast, realistic destruction, dynamic motion blur, no BGM, no dialogue
```

<a id="pov-fpv-case-15"></a>
<!-- Case 15: Tokyo POV Rollercoaster (by @TechTalkNAVI) -->
### ケース 15: [東京 POV ジェットコースター](https://x.com/TechTalkNAVI/status/2039941029265355123) (投稿者 [@TechTalkNAVI](https://x.com/TechTalkNAVI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-15"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/061.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
{
 "location": "Tokyo Cityscape (Night)",
 "duration": "10s",
 "prompt": "A cinematic POV shot riding an invisible rollercoaster through Tokyo at night. A glowing neon rail 'creates itself' milliseconds before the camera hits it, weaving through the steel structures of Tokyo Tower and nearby buildings. As the camera passes, each building it touches instantly transforms into a stack of glowing cubes that rotate and re-assemble. The shot ends with the camera diving straight down into a sea of neon lights, which turns into a giant QR code or a logo just before the screen goes black.",
 "vfx_focus": [
 "Procedural rail generation",
 "Dynamic environment transformation (Geometry nodes style)",
 "Extremely high-speed camera motion with light streaks"
 ]
}
```

<a id="pov-fpv-case-16"></a>
<!-- Case 16: Cinematic Beijing Cultural Ad — 8K First-Person (by @crayon1267) -->
### ケース 16: [映画的な北京文化広告 — 8K 一人称視点](https://x.com/crayon1267/status/2040826411783762286) (投稿者 [@crayon1267](https://x.com/crayon1267))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-16"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2040826411783762286.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
电影级国风城市文化创意广告，超写实 8K，第一人称舒缓追随镜头，丝滑慢节奏运镜，北京古都氛围浓厚，治愈人文感，强代入感，建筑与自然细节清晰真实。整片时长 15 秒内，整体节奏放缓，镜头停留更从容，核心主体为一朵带晨露的白色蒲公英，镜头始终轻柔追随绒球。全程无背景音乐，仅保留环境拟音 + 极简地点旁白。 【0-4s】晨雾中的北京胡同，蒲公英被清风托起，镜头轻柔掠过瓦顶、院门与晨练残影。旁白：胡同 【4-8s】蒲公英缓缓飘行，掠过故宫角楼、天坛祈年殿。旁白：故宫、天坛 【8-12s】蒲公英继续轻飘，掠过颐和园十七孔桥、八达岭长城。旁白：颐和园、长城 【12-15s】蒲公英轻落什刹海湖面，镜头缓缓拉出城市全景。旁白（提前 1 秒出现）：风过北京，万物有灵。画面定格治愈收尾，不拖尾。 音效设计 全程无背景音乐，仅保留微风声、环境自然音、蒲公英飘飞轻响，旁白清晰干净，无多余嘈杂音效。
```

<a id="pov-fpv-case-17"></a>
<!-- Case 17: Extreme Macro FPV — Fairy Wing Tracking Shot (by @EHuanglu) -->
### ケース 17: [極限マクロ FPV — 妖精の翼を追うショット](https://x.com/EHuanglu/status/2041132328655954201) (投稿者 [@EHuanglu](https://x.com/EHuanglu))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-17"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041132328655954201.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
extreme macro FPV tracking shot, camera tightly attached to the fairy's back, synchronized with wing flapping frequency
```

<a id="pov-fpv-case-18"></a>
<!-- Case 18: Volcanic Cave Gravity Dive (by @LudovicCreator) -->
### ケース 18: [火山洞窟への重力ダイブ](https://x.com/LudovicCreator/status/2075641309654622486) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-18"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075641309654622486.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
First-person camera perspective only, no drone, no aircraft, no propellers, no visible vehicle. The camera launches through a volcanic cave, skimming above lava rivers, weaving between magma geysers, then diving into a gravity vortex at the crater’s core. Final reveal: the volcano opens into outer space, with molten rocks becoming newborn planets around a burning star. Continuous one-take, aggressive POV motion, Hollywood VFX, volumetric smoke, glowing particles, epic cinematic scale.
```

<a id="pov-fpv-case-19"></a>
<!-- Case 19: Supersonic Desert Canyon POV (by @LudovicCreator) -->
### ケース 19: [超音速で駆け抜ける砂漠峡谷 POV](https://x.com/LudovicCreator/status/2076607661244665980) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-19"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2076607661244665980.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Pure first-person camera perspective, no visible drone, no cockpit, no aircraft visible. The camera flies at supersonic speed through an enormous desert canyon, hugging the terrain only inches above the rocks. Sonic booms echo through the cliffs while dust erupts behind every turn. The camera slices through impossibly narrow rock arches, skims over waterfalls, enters a dark canyon tunnel, then bursts back into daylight as multiple supersonic shockwaves ripple across the landscape. The final climb rockets vertically through thick clouds into the upper atmosphere with the Earth stretching across the horizon. Continuous one-take, authentic high-speed inertia, aggressive banking, cinematic motion blur, atmospheric distortion, volumetric dust, blockbuster Hollywood VFX, hyper-realistic.
```

<a id="pov-fpv-case-20"></a>
<!-- Case 20: France Fireworks FPV Flyover (by @LudovicCreator) -->
### ケース 20: [フランス花火 FPV フライオーバー](https://x.com/LudovicCreator/status/2077090789356609683) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=pov-fpv-case-20"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2077090789356609683.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Immersive first-person flying camera perspective, no visible drone or flying device. The entire sequence takes place at night beneath a deep blue sky. The camera races above the illuminated lavender fields of Provence while fireworks burst continuously in blue, white, and red across the horizon. It weaves through glowing medieval villages, vineyards, French châteaux, the cliffs of Normandy, and Mont-Saint-Michel reflected in the dark tide, with fireworks erupting above every location. The camera then follows the Seine into Paris at extreme speed, skimming beneath historic bridges, banking around the Arc de Triomphe, and climbing beside the fully illuminated Eiffel Tower as enormous synchronized fireworks fill the sky and reflect across the river. At the finale, the camera pulls back above Paris while the fireworks create a vast tricolor glow. A gigantic French flag unfurls naturally from the top of the Eiffel Tower, waving majestically above the city as the final fireworks burst behind it. No text, no words, no letters. Continuous POV shot, no cuts, aggressive banking, cinematic motion blur, realistic night lighting, volumetric smoke, detailed fireworks, ultra-realistic travel cinematography, spectacular blockbuster VFX, IMAX quality.
```

<a id="commercial-product"></a>
## 🏷️ コマーシャル / 商品

<a id="commercial-product-case-1"></a>
<!-- Case 1: Perfume-Style Anime Trio Dance Stage (by @ShadeLurk) -->
### ケース 1: [香水 CM 風アニメ三人組ダンスステージ](https://x.com/ShadeLurk/status/2040671186984796632) (投稿者 [@ShadeLurk](https://x.com/ShadeLurk))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-1"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/007.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
PR [Topview]
#TopviewAI #Seedance2
Dance

prompt:
Three anime girls perform Perfume-style formation dance on an illuminated stage. Each girl performs different assigned choreography, but all movements are locked to the exact same beat with mechanical precision. The camera cuts rapidly between full shots and medium shots every 0.7-1.0 seconds, occasionally switching to side angles and overhead angles. The structure follows a call-and-response pattern between the three dancers. The choreography ranges from sharp upright arm work to low crouching floor sweeps. Blue-white spotlights carve through purple haze. LED panels pulse with blue-to-purple gradients. Triangular formation.
```

<a id="commercial-product-case-2"></a>
<!-- Case 2: Dark Fantasy Church Duel (by @ZaraIrahh) -->
### ケース 2: [ダークファンタジー教会の決闘](https://x.com/ZaraIrahh/status/2040667542390190245) (投稿者 [@ZaraIrahh](https://x.com/ZaraIrahh))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-2"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/008.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Original Dark Fantasy Action Short Film: Inside a dilapidated church, a white-clad warrior and a black-armored opponent launch their final battle amid an atmosphere like a chorus. Stained glass shatters, moonlight penetrates the smoke and dust, and benches are overturned. The camera switches between high-angle overhead shots and low-angle upward shots, focusing on showing the sense of space of the religious building, the sense of oppression of the characters, and the temperament of a fateful decisive battle, just like the climax segment of an original fantasy animated film. A strong hook in the first 2 seconds, stable main body, coherent actions, movie-level composition, real light and shadow, epic sense, strong emotion, high-definition details, suitable for social media communication, avoiding copyrighted characters, avoiding brand logos, and completely original design.
```

<a id="commercial-product-case-3"></a>
<!-- Case 3: Dark Fantasy Shrine Hall Duel (by @MiraMusic_AI) -->
### ケース 3: [ダークファンタジー神殿ホールの決闘](https://x.com/MiraMusic_AI/status/2040595365096034700) (投稿者 [@MiraMusic_AI](https://x.com/MiraMusic_AI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-3"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/012.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Original Japanese-Style Dark Fantasy Action Short Film:
Inside a dilapidated shrine hall, a white-robed warrior and a black-armored samurai engage in their final battle amid an atmosphere reminiscent of ritual chanting. Wooden beams creak, paper screens tear apart, and fragments scatter as moonlight filters through drifting dust and smoke. Tatami mats are disrupted and scattered across the floor.
The camera alternates between high-angle overhead shots and low-angle upward perspectives, emphasizing the spatial depth of traditional Japanese architecture, the oppressive tension surrounding the characters, and the solemn intensity of a fateful duel—evoking the climactic moment of an original Japanese fantasy animated film.
A strong hook within the first 2 seconds, followed by a stable and cohesive progression. Fluid, continuous action with cinematic composition, realistic lighting and shadow, an epic atmosphere, intense emotional weight, and high-definition detail. Designed for social media engagement. Avoids copyrighted characters and brand logos, ensuring a completely original creation.
```

<a id="commercial-product-case-4"></a>
<!-- Case 4: Japanese Snack Commercial Punchline (by @aigeboku) -->
### ケース 4: [日本のお菓子 CM のオチ](https://x.com/aigeboku/status/2040562471027782017) (投稿者 [@aigeboku](https://x.com/aigeboku))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/014.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Here it is.

A 15-second Japanese snack commercial.
Shot 1 (3s): A man walks through a shopping street. As he passes, two housewives whisper, "It's out."
Shot 2 (3s): The man turns around, slightly concerned by the two women, and an old man holding a newspaper says, "Is it out?"
Shot 3 (3s): Slightly flustered, the man looks at his smartphone, and a YouTube influencer says, "It's out!"
Shot 4 (3s): The man rushes into a Japanese convenience store. The clerk says, "It's out!" while holding the new snack package used in Shot 5.
Shot 5 (3s): Close-up of the new snack package. Narration: "It's out! New release!"
```

<a id="commercial-product-case-5"></a>
<!-- Case 5: Cinematic Martial Art Sequence for Seedance 2 (by @CharaspowerAI) -->
### ケース 5: [Seedance 2 向け映画的武術シーケンス](https://x.com/CharaspowerAI/status/2040376349504815467) (投稿者 [@CharaspowerAI](https://x.com/CharaspowerAI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-5"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/017.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Cinematic Martial Art Sequence for Seedance 2
PROMPT
cinematic martial arts confrontation in broad daylight, a blind shaolin monk wearing a dark, stylized combat outfit inspired by legendary fighters stands calm and centered, eyes closed, surrounded by multiple hostile creatures emerging from a traditional Japanese landscape
Ultra cinematic choreography coverage, mix of slow dolly-ins + orbit moves + whip pans, transitions masked by body motion and impacts, alternating real-time and slow motion, continuous fluid sequence
(0-2s) wide establishing shot, monk standing still in center, wind moving fabric, creatures circling, tension builds
(2-4s) slow push-in close-up on monk’s face, eyes closed, subtle head tilt sensing movement
(4-6s) sudden attack from first creature, monk reacts instantly, precise sidestep + redirection, fluid motion
(6-8s) chained combat sequence, monk engages multiple opponents, spinning strikes, controlled movements, each impact sending creatures flying backward with stylized motion
(8-10s) slow motion highlight: mid-air dodge + counter sequence, cloth movement and body rotation emphasized, creatures suspended briefly before being thrown away
(10-12s) final burst of speed, monk flows through remaining opponents in one continuous movement, camera orbiting rapidly, enemies collapsing or being thrown aside
Traditional Japanese environment, open landscape with temples, wooden structures, distant mountains, clear daylight, subtle wind movement, dust and debris reacting to motion
Ultra realistic, high-end martial arts film choreography, precise body mechanics, cinematic slow motion, strong contrast lighting, volumetric atmosphere, fluid transitions, intense but controlled physical interaction, no distortion, no stretching
```

<a id="commercial-product-case-6"></a>
<!-- Case 6: Japanese Classroom Whisper Romance (by @JiahaoYang_art) -->
### ケース 6: [日本の教室でささやく恋](https://x.com/JiahaoYang_art/status/2033119940216344616) (投稿者 [@JiahaoYang_art](https://x.com/JiahaoYang_art))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-6"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/022.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second cinematic Japanese drama pure love ambiguous short film, ultra-realistic quality, warm golden sunlight in an empty classroom in the afternoon, spilling through the blinds onto the side-by-side desks, fine dust motes slowly floating in the light beams, old wooden desks, extremely natural subtle movements, breathing, and eye tension, characters maintain consistent faces, clothing, and hairstyles throughout without deformation, drift, or artifacts, real slight chest rise and fall synchronized with breathing, shallow depth of field, creamy blurred background, warm film grain, 8K sharp, Japanese youth restrained heart-fluttering suffocating atmosphere.
0-4 seconds: Extremely slow push-in shot from a medium shot of the desktop to a close-up of the two people's side profiles sitting side-by-side. A pure girl in a summer school uniform is focused on writing notes with her head down, long black hair and stray hairs by her ears are gently lifted by a slight breeze, long eyelashes cast subtle shadows, skin is naturally pink and tender, a slight, unintentional upturn of the corner of her mouth in concentration, light and even breathing.
4-9 seconds: Switch to a close-up of the boy. His school uniform collar is slightly loose, he props his elbow on the desk and secretly turns his head to gaze at her, his eyes filled with gentle, restrained affection and tenderness, pupils slightly dilated, his Adam's apple gently rolls. Suddenly noticing her pen pause, he quickly and flusteredly turns his head to pretend to look at his own notes, his earlobes quickly turn slightly red, his fingertips tremble slightly as he grips the pen, occasionally glancing at her from under his bangs, his breathing is slightly disordered, and his lips are tightly pressed in an effort to remain calm.
9-15 seconds: Extreme close-up of both faces in the same frame, slow-motion eyes suddenly meet: the girl slowly turns her head, first showing a dazed surprise, then quickly and shyly lowers her head for 0.3 seconds, gently biting her lower lip, her cheeks and earlobes instantly bloom with cherry blossom pink, her moist eyelashes timidly look up to meet his gaze again, while softly and shyly whispering, "...What are you looking at?"; the boy freezes completely, his pupils dilate, and he is stunned for 0.4 seconds, then flusteredly and quietly stutters in response, "N-nothing...". The girl whispers even quieter, biting her lip and peeking at him again, continuing to whisper, "...Liar.". The boy pauses, then gently sighs and whispers, "...Just looking at you.", the corner of his mouth slowly curls up into a shy, gentle, crooked smile, fine lines appear at the corners of his eyes, and his breathing noticeably deepens. An invisible current seems to pull the ambiguous tension between their faces, sharing each other's breathing temperature, the background completely melts into layers of creamy, dreamy light spots, warm halos, and fine air particles.
Lip synchronization is natural and precise, emotional micro-tremors and breathing are synchronized, dialogue is low-energy whispering with a shy tone, natural short pauses between 200-400 milliseconds, the mouth only moves slightly when speaking, without exaggeration or robotic feel, perfect natural lip-sync and emotional authenticity.
Overall Sound Effects: Distant summer cicada chirping faintly, the soft scratching sound of the pen touching the paper, the almost inaudible low-frequency pulse of their heartbeats, finally fading into a very light, airy piano. The dialogue is completely naturally integrated into the scene as whispers, the girl's voice is soft and shy, the boy transitions from flustered stuttering to gentle.
Character identity is maintained throughout, real subtle head tilts, eye movements, and breathing synchronization, no text, watermarks, or subtitles, pure Japanese style youth secret crush heart-fluttering suspense.
```

<a id="commercial-product-case-7"></a>
<!-- Case 7: LaFerrari Commercial Storyboard (by @Adam38363368936) -->
### ケース 7: [LaFerrari CM ストーリーボード](https://x.com/Adam38363368936/status/2039932977287979053) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-7"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/030.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Supercar commercial cinematography storyboard

Shot 1 (1.5s): Opening frame on the supercar from the front, showcasing its signature aggressive face.

Shot 2 (1s): Close shot. The virtual camera slowly orbits around the emblem without spinning in a full circle, emphasizing the Ferrari prancing-horse logo.

Shot 3 (1.5s): Close shot, angled view of the LaFerrari's distinctive butterfly door from the side of the car, with a slow orbiting move that emphasizes the body lines.

Shot 4 (1s): Camera moves to the rear for a close shot, then slowly pulls backward using a Hitchcock dolly-zoom effect for visual impact.

Shot 5 (1s): Close shot of the car's side mirror with a slow orbiting move.

Shot 6 (1s): Camera slowly pushes forward using a low-angle advancing move. The car remains still, showing strong perspective, shifting light and shadow, professional automotive cinematography, deep background, cinematic composition, stable visual center, and high-definition live-action quality.

Shot 7 (1s): Lateral track move. The camera sweeps parallel across the LaFerrari body. The car stays completely still as the frame glides smoothly. Side lighting traces the waistline, includes wheel close-ups, delicate reflections, a premium feel, cinematic movement, and clean composition.

Shot 8 (1s): Top-down angle. The camera slowly descends. Static supercar, perfect body proportions, top-light texture, clean ground reflections, aerial-feel movement, the car remains still, symmetrical composition, luxurious texture, 8K ultra-realistic, advertising-grade image.

Shot 9 (1s): Slow push-in close-up from the full car toward the headlights / wheel / waistline. The car remains still. Macro detail, shifting light and shadow, cinematic shallow depth of field, premium texture, sharp detail, commercial photography.

Notes:

No transitions are needed between shots.

No people should appear in the frame.

Highest image quality: 8K.
```

<a id="commercial-product-case-8"></a>
<!-- Case 8: Hot-Blooded Anime Final Duel (by @gkxspace) -->
### ケース 8: [熱血アニメの最終決闘](https://x.com/gkxspace/status/2039894982434111716) (投稿者 [@gkxspace](https://x.com/gkxspace))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-8"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/032.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Tested it:

Original Hot-Blooded Duel Anime Short Film: Two top warriors launch their final duel against the backdrop of aerial ruins and thunderstorms. The camera emphasizes extreme speed, intense energy collisions and a sense of oppression from the characters. When moves are released, the surrounding buildings, clouds and debris are simultaneously affected by the force. The actions are like the top-level battle animation of TV anime, with theater-level color grading and lens language, focusing on highlighting the "highly intense, exciting, and blockbuster-like" vibe. A strong hook in the first 2 seconds, with a stable main body, coherent actions, movie-level composition and light and shadow, real texture, epic sense, strong emotion, high-definition details, suitable for social media communication. Completely original characters, worldview, costumes, weapons and moves, no copyright risks, and no use of well-known IPs, celebrity faces, brand logos or existing elements.
```

<a id="commercial-product-case-9"></a>
<!-- Case 9: Porcelain Couture Sky Mirror Runway (by @johnAGI168) -->
### ケース 9: [磁器クチュールの天空鏡面ランウェイ](https://x.com/johnAGI168/status/2025849650654122348) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-9"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/033.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[Style] Hollywood Haute Couture Fantasy blockbuster, 8K ultra-clear, Photorealistic, High-fashion Editorial Style, Unreal Engine 5 fluid rendering, visual illusion. [Duration] 15 seconds. [Scene] An endless, real-life Salar de Uyuni (Sky Mirror) salt flat. The sky is filled with oppressive dark clouds, and the ground perfectly reflects everything like a mirror, with the overall picture presenting a minimalist, cool tone. [00:00-00:05] Shot 1: Haute Couture Entrance and Porcelain Skin. Camera position: Extremely low-angle upward shot, ultra-telephoto lens zoom-in. Action: An Asian female model with a highly recognizable, high-fashion face walks coolly on the water surface. Effect: She is wearing not fabric, but a long dress made of flowing, real Liquid Blue-and-White Porcelain. As she walks, the skirt makes a crisp collision sound like real ceramic, with a flowing luster on the surface. The traditional blue-and-white patterns move across the white porcelain-textured skirt as if alive. [00:05-00:10] Shot 2: Physical Shattering and Ink-wash Descent. Camera position: Extreme close-up of the face, focus rapidly pulls back. Action: The model suddenly stops, stares coldly at the camera, and snaps her fingers crisply. Effect: The moment the fingers snap, her blue-and-white porcelain dress does not fall, but instantly explodes into thousands of extremely photorealistic Ink-wash Swallows. These swallows carry real water droplets and ink marks, dragging black fluid afterimages in the air, spinning frantically around her. [00:10-00:15] Shot 3: Dimensional Dissolution and Abyss Reflection. Camera position: High-altitude overhead shot, camera rapidly rotates and descends. Action: The swarm of ink-wash swallows plunges into the mirrored lake water beneath the model's feet. Effect: The surface tension of the originally solid salt lake instantly disappears. The entire extremely realistic world begins to violently bleed and dissolve like concentrated ink dropped into clear water. The real dark clouds and the model's figure transform entirely into an extremely grand 3D Fluid Ink Vortex, completely swallowing the camera into a black and white interwoven abyss.
```

<a id="commercial-product-case-10"></a>
<!-- Case 10: Modern Rural Creator Harvest Ad (by @johnAGI168) -->
### ケース 10: [現代の農村クリエイターによる収穫広告](https://x.com/johnAGI168/status/2021818021354848258) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-10"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/034.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[Style]
Modern Rural Aesthetics, Cinematic Commercial quality, shot with Sony A7S3/cinema camera, 4K/8K ultra-clear, Extreme Macro, natural transparent lighting, healing ASMR, no historical costume drama feel.

[Scene]
A well-maintained modern farmhouse open kitchen, background is a lush vegetable garden, bright sunshine.

[Character]
Modern Rural Creator, black long hair casually tied up with a wooden hairpin, wearing a dark blue comfortable linen outfit, clear makeup, focused and peaceful eyes.

[Shot Details]
[00:00-00:05] Shot 1: Morning Harvest (The Freshness)
Visuals: High-definition close-up. Morning sunlight hits the plants with side backlighting.
Action: The Creator's bare hands (long, clean fingers) pick a bright red tomato with glistening dew drops from the vine.
Details: Extremely sharp focus, clearly showing the fuzz on the tomato surface and the trajectory of sliding water droplets. Background is blurred high-quality green.

[00:05-00:10] Shot 2: Extreme Craftsmanship (The Craft)
Visuals: Indoor stove area, full of life but spotless.
Action: The Creator is cutting vegetables, movements are skilled and precise (non-performance nature).
Details: Macro lens captures the moment the knife blade slices through the ingredients, juice splattering. Then switches to the orange flame flickering in the earthen stove, light and shadow are warm and real.

[00:10-00:15] Shot 3: Tranquil Time (The Moment)
Visuals: Full shot/Medium shot.
Action: A delicate home-cooked dish is placed on the wooden long table in the yard. The Creator sits down quietly, gently tidies a stray hair, and picks up a bite of food.
Atmosphere: Steam slowly rises against the backlight, the scene is so quiet you can almost hear the wind, showcasing the ultimate sense of relaxation modern people yearn for.
```

<a id="commercial-product-case-11"></a>
<!-- Case 11: Neon Street Racing Sequence (by @CharaspowerAI) -->
### ケース 11: [ネオン街のストリートレース](https://x.com/CharaspowerAI/status/2039651574297792688) (投稿者 [@CharaspowerAI](https://x.com/CharaspowerAI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-11"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/036.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
cinematic street racing sequence at night, a focused driver inside a high-performance car grips the steering wheel, intense eye focus, city lights reflecting on windshield, tension building before sudden acceleration

camera: rapid multi-angle system with seamless transitions, interior close-up → over-the-shoulder → exterior tracking → low ground shots, ultra dynamic camera movement, whip pans + speed ramp transitions + motion blur masking cuts, continuous flow illusion

(0-2s) interior close-up on driver, hand tightens on gear shift, subtle breathing, dashboard lights glowing
(2-4s) over-the-shoulder shot, road ahead stretching into neon-lit city, engine vibration building
(4-6s) extreme close-up on finger pressing NOS button, instant ignition reaction
(6-8s) explosive acceleration, camera snaps to exterior side tracking shot, car launches forward with violent speed surge
(8-10s) ultra low ground shot near asphalt, wheels spinning at extreme velocity, environment streaking past
(10-12s) high-speed chase through tight streets, sharp turns, camera whip pans between angles, reflections and light trails enhancing speed

Dense urban night environment, wet asphalt reflecting neon lights, tunnel passages, street lights streaking, high-speed city atmosphere
Ultra realistic, fast and furious inspired energy, photorealistic lighting, intense motion blur, high contrast neon reflections, cinematic depth of field, extreme sense of speed, fluid transitions, no distortion, no stretching
```

<a id="commercial-product-case-12"></a>
<!-- Case 12: Supermodel and Luxury Sports Cars (by @johnAGI168) -->
### ケース 12: [スーパーモデルと高級スポーツカー](https://x.com/johnAGI168/status/2039984306085327298) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-12"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/046.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Generate a visual blockbuster featuring an Asian supermodel and luxury sports cars with top-tier commercial quality, requiring director-level storyboard arrangement and a fast-paced, high-end rhythm. 0-2 seconds: [Macro to Micro] The opening uses an extreme push-in shot, instantly cutting from the sharp headlights of the sports car with delayed afterimages to a close-up of the pupils of the top Asian supermodel, showcasing the ultimate Oriental charm. 2-5 seconds: [LOCKED-ON SHOT] The camera locks onto the model's profile, tracking her with a lateral pan (Tracking Shot) as she walks confidently and elegantly. The model wears a high-fashion silk evening gown, her hair slightly moving in the wind, against a background of a blurred neon urban viaduct. 5-8 seconds: [360-degree Orbit Shot] The model stands at the center intersection of three sports cars, and the camera quickly orbits around her at a low angle. Use slow motion (slow-motion processing) to capture her cold, stunning glance back, with eyes possessing strong aggression and high-end appeal. 8-10 seconds: [Low-angle Hero Shot] The camera quickly pulls back from a ground perspective to a full view. The model stands proudly in the center of the luxury car cluster. The composition presents perfect symmetrical aesthetics, with light focusing on the face, displaying queen-like dominance. Visual Style: Extreme cinematic realism, 2.35:1 widescreen. The overall color tone leans towards cool Teal & Orange, with natural film grain and soft highlights. The character's skin texture is delicate and natural, possessing the makeup and styling quality of a top luxury magazine. Sound Design: Heavy bass electronic ambient music. Sound effects must sync with the camera cuts (Swish sound effects), and the visual rhythm should breathe with the music beats. Control Instructions: Lock the facial features and high-end makeup of the Asian model, ensuring character consistency across various shots; action transitions must be smooth without stuttering; light and shadow should produce real-time physical reflections as the model moves.
```

<a id="commercial-product-case-13"></a>
<!-- Case 13: Android Girl Lab Destruction Chase (by @aiehon_aya) -->
### ケース 13: [研究所を破壊したアンドロイド少女の逃走](https://x.com/aiehon_aya/status/2040187587889905861) (投稿者 [@aiehon_aya](https://x.com/aiehon_aya))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-13"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/054.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
An android girl malfunctions and proceeds to destroy an evil research lab one after another. The evil boss, a doctor with a bad face, chases the girl, shouting, "Waaah! Stop it! Please stop it!!" but the girl doesn't stop and continues to destroy things while laughing. In the end, there is a big explosion, and the lab is destroyed without a trace. The girl yawns and says, "Job complete," and falls asleep right there. The doctor kneels down, utterly dejected.
```

<a id="commercial-product-case-14"></a>
<!-- Case 14: Neon Ruined City Game Trailer (by @adrianaia_) -->
### ケース 14: [ネオン廃墟都市のゲームトレーラー](https://x.com/adrianaia_/status/2039972811067031657) (投稿者 [@adrianaia_](https://x.com/adrianaia_))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-14"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/055.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Positive Prompt: Original action game concept trailer. The protagonist travels through a neon ruined city, where the debris by the road emits faulty advertising lights, and mechanical guards fall from the faults of high-rise buildings. After dodging with a slide, the protagonist pulls out a folding energy blade. The camera is like an AAA game debut trailer, with third-person follow, rapid switching between close-up and ultra-wide shots, strong rhythm and distinct scene layers. It finally stops at the silhouette of the boss's appearance, creating a strong feeling of "wanting to play this game". Negative Restrictions: No Cyberpunk 2077 logos, no well-known game UI, no existing game character outlines. A strong hook in the first 2 seconds, stable main body, coherent actions, movie-level composition, real light and shadow, epic sense, strong emotion, high-definition details, suitable for social media communication, avoiding copyrighted characters, avoiding brand logos, and completely original design.
```

<a id="commercial-product-case-15"></a>
<!-- Case 15: Original Dark Fantasy Action Short Film (by @Rufus87078959) -->
### ケース 15: [オリジナル・ダークファンタジーアクション短編](https://x.com/Rufus87078959/status/2039949879607197828) (投稿者 [@Rufus87078959](https://x.com/Rufus87078959))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-15"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/066.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Original Dark Fantasy Action Short Film: Inside a dilapidated church, a white-clad warrior and a black-armored opponent launch their final battle amid an atmosphere like a chorus. Stained glass shatters, moonlight penetrates the smoke and dust, and benches are overturned. The camera switches between high-angle overhead shots and low-angle upward shots, focusing on showing the sense of space of the religious building, the sense of oppression of the characters, and the temperament of a fateful decisive battle, just like the climax segment of an original fantasy animated film. A strong hook in the first 2 seconds, stable main body, coherent actions, movie-level composition, real light and shadow, epic sense, strong emotion, high-definition details, suitable for social media communication, avoiding copyrighted characters, avoiding brand logos, and completely original design.
```

<a id="commercial-product-case-16"></a>
<!-- Case 16: 00:00-00:04 Shot 1: Follow shot (by @IamEmily2050) -->
### ケース 16: [00:00–00:04 ショット 1：追跡撮影](https://web.archive.org/web/*/https://x.com/IamEmily2050/status/2040213294443847933) (投稿者 [@IamEmily2050](https://x.com/IamEmily2050))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-16"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/070.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[00:00-00:04] Shot 1: Follow shot. In a smoky underground rave club, a female cyborg with an exposed red mechanical spine walks through the crowd. She suddenly turns around, her delicate white porcelain face beginning to convulse violently. [00:04-00:10] Shot 2: Close-up to mid-shot. The cyborg's porcelain face doesn't just split; it is violently shattered from the inside like an eggshell. A massive amount of thick, black viscous fluid erupts outward as an alien head with rusted metallic fangs and multiple mandibles forces its way out of her neck. Simultaneously, her red mechanical spine violently tears through her back, mutating into a giant, multi-jointed metallic scorpion tail dripping with corrosive acid. [00:10-00:15] Shot 3: Wide shot. The club's lighting turns a sickly fluorescent green. The alien tail violently impales the dance floor, suspending the cyborg's ruined body in mid-air as it emits an ear-piercing, non-human shriek. The surrounding crowd is paralyzed with absolute terror, pinned against the walls by webs of black organic matter. Extreme biomechanical horror, terrifying VFX mixing flesh and metal.
```

<a id="commercial-product-case-17"></a>
<!-- Case 17: Train-Top Tactical Fight Sequence (by @ImperfectEngel) -->
### ケース 17: [列車屋根上の戦術格闘](https://web.archive.org/web/*/https://x.com/ImperfectEngel/status/2039796558238286329) (投稿者 [@ImperfectEngel](https://web.archive.org/web/*/https://x.com/ImperfectEngel))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-17"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/095.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
"Dramatic low-angle tracking shot speeding along rain-slicked train tracks through a narrow mountain gorge. Dark rocky cliff walls rise on both sides, with overhead bridges and power lines crossing above. Moody overcast sky. The camera rushes forward at high speed. Two women — one with pink hair in all-black tactical gear, the other in a white bodysuit — fight on top of the moving train, exchanging martial arts blows as sparks fly. Dynamic action choreography, dark teal-grey color grade, cinematic speed and motion blur, sci-fi action film aesthetic."
```

<a id="commercial-product-case-18"></a>
<!-- Case 18: Manhattan Trading Floor Frenzy (by @johnAGI168) -->
### ケース 18: [マンハッタン取引フロアの狂騒](https://x.com/johnAGI168/status/2039277115690877430) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-18"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/109.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Hollywood movie-level commercial blockbuster quality, handheld photography, slight camera shake, fast-paced montage editing, the scene is full of energy and oppression, no subtitles appear.
The open-plan office hall of a luxurious securities company in Manhattan, USA, in the 1990s. Hundreds of young male brokers in suits densely fill the entire space. American flags hang around, ribbons fall in the air, and the entire hall is plunged into a religious ritual-like collective frenzy.
00:00-00:04 Wide-frame panoramic push-in shot: A powerful middle-aged male protagonist in a suit stands on top of a desk, arms spread, cheering loudly, shouting: "I am not leaving! We are not leaving!" Hundreds of employees below him respond wildly, waving their arms, pounding desks, hugging each other, the hall roaring and shaking. Handheld camera powerfully pushes towards the crowd, creating an overwhelming sense of presence.
00:04-00:09 Quick cut switch: Close-up of the protagonist above the chest, slightly sweaty, eyes burning, lips forcefully shouting: "They want to take it all away from you — ARE YOU GONNA LET THEM?!" The dialogue cue switches to close-ups of employees—young faces contorted in extreme excitement. Some are crying, some are tearing off their ties, some are jumping on tables and howling in response: "NO!!!"
00:09-00:15 The protagonist single-handedly pounds his chest, raising his other fist high, saying the last sentence in a low, forceful voice: "This is who we are." The camera suddenly pulls back from the close-up to a panoramic view—the hundreds of people in the hall erupt in the highest climax of shouting at the same moment. Ribbons pour down, the camera slightly tilts up to capture the protagonist's silhouette standing against the light at the top of the crowd, freezing in that high-energy moment where heroism and madness coexist.
```

<a id="commercial-product-case-19"></a>
<!-- Case 19: (Poliziottesco Wednesday) (by @ChrisGwinnLA) -->
### ケース 19: [ポリツィオッテスコ風の水曜日](https://x.com/ChrisGwinnLA/status/2039456415111393356) (投稿者 [@ChrisGwinnLA](https://x.com/ChrisGwinnLA))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-19"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/118.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
(Poliziottesco Wednesday): Detective Rossi: Deep Heat (Commissario Rossi: la polizia in crisi nera). 
A crime wave has hit the city and the cops can't seem to get it together. Detective Rossi has had enough of the bureaucracy and the politicians tying his men's hands (and freeing the criminals to terrorize the city again!) - but can one hardnosed cop make a difference in a world gone mad? Maybe this nosey journalist can become an important ally!
```

<a id="commercial-product-case-20"></a>
<!-- Case 20: Foldable Smartphone Fashion Ad (by @Adam38363368936) -->
### ケース 20: [折りたたみスマートフォンのファッション広告](https://x.com/Adam38363368936/status/2039157138002780202) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-20"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/121.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Product: Color-shifting gradient foldable smartphone (e.g., light purple to ice blue gradient)

Style: Trendy fashion, energetic fast pace, high-end texture, no people, minimalist light and shadow, fashionable trend style
Tones: High-saturation contrasting colors, light purple gradient frosted glass texture, clean and bright, cinematic light and shadow
Camera Language: Macro close-up, fast rotating camera movement, orbiting camera movement, handheld dynamic camera movement, push-pull quick cuts, smooth transitions
Tempo: 15 seconds tight quick cut, beat-synced editing, sharp transitions

Visual Content:
The light purple gradient foldable phone rapidly rotates against a pure black background, with light flowing across the body; macro close-ups of the ultra-thin hinge structure, the glass texture of the outer screen, the brushed metal close-up of the camera module, and the extremely thin side bezel; quick cuts showing the moment the phone unfolds from folded state, the visual impact of the inner screen's ultra-narrow bezel; paired with simple trendy scenes such as a minimalist office desk, an art gallery corner, late-night city neon, or a trendy collectible display case; fashionable and energetic. No models throughout, focusing only on the product.

Sound Effects: Trendy electronic drum beats, metallic clinks, mechanical click sound of the screen unfolding, beat-synced sound effects
Quality: 4K high definition, commercial advertisement quality, smooth dynamics, vibrant colors
Requirements: Fast pace, tight transitions, high-end fashion, youthful energy, no people appearing.
```

<a id="commercial-product-case-21"></a>
<!-- Case 21: Travel Suitcase Buddy Montage (by @ChaseAIx) -->
### ケース 21: [旅の相棒になるスーツケースのモンタージュ](https://x.com/ChaseAIx/status/2045080469533057252) (投稿者 [@ChaseAIx](https://x.com/ChaseAIx))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-21"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/sAVFzyGI01SXuQGa.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
SHOT 1: ECU, 85mm push-in / 04:00 on a digital watch screen. A hand slams it. / SFX: alarm beep, palm slap.

SHOT 2: WS, 35mm handheld jolt / Rhythmic cut into the man jolting upright, grabbing the suitcase by the handle like a hand-shake, and swinging it off the bed in one motion. / SFX: mattress spring, leather creak.

SHOT 3: MCU, 50mm slide / Cut on action into a passport hitting a tray, followed by a pair of sunglasses. / SFX: plastic thud, metallic clink.

SHOT 4: Insert shot, 85mm rack focus / Match cut into the suitcase zipper closing with a satisfying, high-speed "zip." / SFX: fast zipper slide.

SHOT 5: Exterior Wide, 24mm low-angle / Object pass as the man and suitcase "sprint" into frame against the Great Pyramids. Sand kicks up. / SFX: desert wind, running footsteps in sand.

SHOT 6: Insert shot, 50mm handheld / Rhythmic cut into a chilled coconut being cracked open, the suitcase "sitting" on a beach chair beside him. / SFX: coconut crack, liquid splash.

SHOT 7: MCU, centered 50mm push-in / Match cut into a selfie-angle: The man leans his head against the suitcase like a best friend, the Eiffel Tower sparkling behind them. / SFX: camera shutter, city chatter.

SHOT 8: Bird's-eye insert, 35mm overhead / Cut on action into the suitcase wheels spinning furiously across Andean stone. / SFX: wheel hum, stone rattle.

SHOT 9: MS, 35mm pivot / Camera wipe into a chaotic market in Marrakech. The man maneuvers the suitcase through silk stalls; the suitcase "dodges" a vendor. / SFX: fabric rustle, distant flute, shouting.

SHOT 10: Insert shot, 50mm overhead / Match cut into a stamp slamming down onto a passport page. / SFX: heavy ink thud.

SHOT 11: WS, 24mm parallax / Whip pan transition into a speeding train window. The man’s reflection and the suitcase's reflection are side-by-side as mountains blur past. / SFX: train rhythm, wind whistle.

SHOT 12: MS to CU, 35mm glide into 85mm push-in / Sound bridge into the airport lounge. He rests his feet on the suitcase; they both "exhale" as the sun sets through the terminal glass. / SFX: muffled PA system, deep sigh.

SHOT 13: Insert to MCU, 50mm snap zoom / Smash cut to a front door lock turning. The man and suitcase "stumble" into the dark apartment, looking dusty but happy. / SFX: key turn, door creak.

SHOT 14: OTS, 35mm handheld / Rhythmic cut into the man kicking off his boots and the suitcase falling onto its side with a heavy, tired "flop." / SFX: boot thud, leather heavy impact.

SHOT 15: WS, 50mm pull-out / L-cut with a match from the floor to the bed. The man collapses onto the mattress; the suitcase "collapses" right next to him on the pillows. He flings an arm over the suitcase like a spouse. Lights fade. / SFX: mattress groan, collective exhale, silence.
```

<a id="commercial-product-case-22"></a>
<!-- Case 22: Top-Down Fashion Lookbook — Outfit Change Sequence (by @johnAGI168) -->
### ケース 22: [真上からのファッションルックブック — 衣装替え](https://x.com/johnAGI168/status/2040767631213363656) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-22"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2040767631213363656.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
prompt 👇

【风格】时尚杂志固定俯拍变装卡点（Top-Down Fashion Lookbook），电影质感，8K超清，丝滑卡点，极具冲击力的视觉节奏

【时长】13秒

【场景】固定俯拍视角（Bird's Eye View），镜头锁定正下方不移动。前景：模糊深棕色木质吊扇叶片缓慢旋转，偶尔遮挡镜头，营造空间景深。灰白纹理地毯，棕色方形靠垫。

【角色】年轻亚洲女性，黑色长直发，始终平躺地毯同一位置头枕靠垫，换装时主体位置固定，仅服装配饰道具和手部姿态丝滑闪切，@人物

[00:00-00:03] 造型1：慵懒丝绸（Silk Robe）

黑色丝绸吊带短裙与长袖睡袍，丝绸反射柔光。右侧地板放一杯红酒，右手举黑色遥控器指向镜头上方，神态慵懒。

[00:03-00:05] 造型2：纯白优雅（All White｜瞬间闪切）

全白系：白色挂脖上衣、白色百褶短裙、半透明袖套、白色细皮带。双手手腕交叉轻放胸前，姿态优雅。

[00:05-00:06] 造型3：狂野猫耳（Leopard Cat｜极速闪变）

豹纹紧身吊带上衣配白色百褶裙，黑色猫耳发饰，缎带choker，白色长袜与高跟鞋。双手随意举过头顶放靠垫边缘。

[00:06-00:08] 造型4：冷峻豹纹（Leopard Dress｜丝滑切换）

紧身豹纹连衣短裙，黑色长袜。双手自然放身体两侧地板，眼神冷峻直视镜头。

[00:08-00:09] 造型5：职场特工（Office Tie｜硬切）

白色修身短袖衬衫、黑色领带、豹纹短裙。左侧地板出现白色平板电脑，右侧出现银色小方包，左手轻放腹部上方。

[00:09-00:10] 造型6：暗黑摇滚（Rock Black｜瞬间变身）

全黑：黑皮夹克、黑背心、黑皮短裤、黑色过膝长筒袜、半指皮手套。怀里斜抱浅色木吉他。

[00:10-00:13] 造型7：复古惊艳（Vintage Qipao｜定格收束）

红黑印花复古无袖短款旗袍，左侧发际别一朵红花，黑色过膝长筒袜。右手持半开黑色折扇置于胸前，右侧地板摆红色高跟鞋。红黑配色收束全片。
```

<a id="commercial-product-case-23"></a>
<!-- Case 23: Premium Lifestyle Commercial — Vlog Selfie Style (by @johnAGI168) -->
### ケース 23: [高級ライフスタイル CM — Vlog 自撮り風](https://x.com/johnAGI168/status/2041374063243800793) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-23"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041374063243800793.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
prompt 👇

【风格】高级商业氛围短片（Premium Lifestyle Commercial），高清手机前置镜头质感（Vlog互动视角），电影写实色彩，面部柔光打光，注意分镜编排和对口型，单人出镜

【时长】15秒

【场景】卧室+调酒区一体空间，温馨台灯与紫黄霓虹氛围光交织，微醺暖调

【角色】完全参考@ 的人物外貌特征（顶级亚洲明艳神颜），穿深蓝蕾丝吊带裙、长卷发，全程形象高度一致

[00:00-00:03] 镜头1：POV慵懒起床（POV → Medium Shot 丝滑转场）

主观视角（POV），镜头从第一人称俯视角度对准床上盖着毯子的双腿，手伸入画面掀开被子，双腿落地起身。镜头随起身动作自然抬起并快速切至中景——女主已站在床边面对镜头，慵懒又带一丝霸道地说："睡什么睡，起来喝酒。"（中文口型精准同步）

[00:03-00:06] 镜头2：优雅倒酒（Medium Shot）

中景，机位切至卧室调酒区，背景台灯暖光与紫黄霓虹光映在墙面。女主拿起白酒瓶，手腕微倾，透明酒液沿瓶口流入银色量酒器，随后将量酒器中的酒液倒入杯中并加入橙汁，液体混合的色彩层次清晰可见。

[00:06-00:09] 镜头3：挤柠檬特写（Close-up）

近景动作特写。女主双手各持半个切开的青柠，用力对挤，柠檬汁水真实地滴落进调酒壶，汁液飞溅的细节清晰，随后抓起一把冰块丢入壶中，冰块碰撞发出清脆声响。

[00:09-00:12] 镜头4：摇酒（Close-up / Shake）

近景。女主双手持调酒壶举至脸侧，有节奏地快速摇晃，长卷发随动作轻微摆动，壶内冰块撞击声清脆卡点。她保持迷人微笑注视镜头，眼神明亮带笑。

[00:12-00:15] 镜头5：品尝与收尾（Medium Shot）

中景。女主手持一杯蓝黄渐变的精致鸡尾酒，杯中气泡缓缓上升。她轻抿一口，眉眼舒展露出满意的微醺神情，随后对镜头开心挥手，定格。
```

<a id="commercial-product-case-24"></a>
<!-- Case 24: Beat-Synced Waterproof Sneaker Film (by @madpencil_) -->
### ケース 24: [ビート同期の防水スニーカー映像](https://x.com/madpencil_/status/2075600475299447000) (投稿者 [@madpencil_](https://x.com/madpencil_))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-24"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075600475299447000.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second image-to-video, 9:16 vertical. The uploaded 15-second music track is the master timeline the video maps one-to-one to the track from first frame to last, with hard cuts on downbeats, single-frame flickers on hi-hats, speed ramps hitting their slow-point exactly on beat drops, and the final freeze landing on the track's last hit.

The madpencil sneaker from the reference keeps its exact design at all times: same silhouette, same nubuck and knit textured upper, same tonal "m" logo on the side panel, same madpencil wordmark on the midsole, same outsole and laces the shape, proportions, materials, and logos never change. But the COLORWAY of the shoe snaps to a new color on every beat: olive to coral red, to powder blue, to lemon yellow, to bubblegum pink, to lilac, to pure white, to matte black, cycling continuously each color change is an instant hard swap, like a colorway strobe, always tonal head-to-toe with the logo and midsole shifting to match. Critically, the shoe's MOVEMENT is continuous and unbroken across every color change: if it is rotating, the rotation carries on seamlessly through each swap; if a droplet is rolling, it keeps rolling; if water is mid-splash, the splash continues only the color jumps, never the motion, never the position, never the camera. The shoe is the only subject, floating hero-style, no feet, no people. This is a premium product film for a waterproof sneaker cut as a hyper-kinetic flicker edit: one shoe, every color, undefeated by water.

The structure: from 0 to 2 seconds, the cold open the sneaker floats center frame on a flat solid pastel backdrop, rotating slowly and continuously while its colorway strobes on every beat, single-frame macro flickers of knit weave, nubuck grain, and the "m" logo punching between, each macro in a different colorway. From 2 to 5 seconds, the first water hit a sheet of water flies at the shoe in a speed ramp: normal speed launch, extreme slow motion as the water wraps the toe and explodes into crystal droplets with halftone dots rippling outward and even inside the slow-motion, the colorway keeps snapping on the beat while the droplets hang frozen then full speed as every droplet beads and rolls off, the shoe bone dry. From 5 to 9 seconds, the detail flicker tour cuts every 0.2 to 0.4 seconds: laces pulled taut, water beading like mercury on the side panel, droplets sitting in the outsole tread refusing to soak, a droplet rolling across the madpencil midsole text, mist bouncing off the knit as spray every single detail shot in a different colorway, the backdrop always a contrasting solid pastel so shoe and background never share a color. From 9 to 12 seconds, the gauntlet a crown splash from below ramping slow at its peak, rain streaking past in whip-panned frames, a full dunk with the shoe rising out, ramping from slow underwater bubbles to a fast surface breach, water sheeting off instantly, colorway strobing through the entire sequence while the water physics run unbroken. From 12 to 15 seconds, the hero close the strobing slows with the track: color changes stretch from every beat to every two beats, then settle, the sneaker landing softly on a flat solid backdrop in its original olive-grey home colorway one slow push-in, a single last droplet rolling off the toe, halftone dots settling as it locks into a still magazine-cover frame.

Water physics stay crisp and glassy: sharp crown splashes, distinct suspended droplets, clean sheeting; droplets always bead and roll off, never absorb, never darken the material regardless of the current colorway; the shoe emerges instantly dry from every hit.

Visually: flat solid neon pastel backdrops only powder blue, lemon yellow, bubblegum pink, coral red, white snapping on beats and always contrasting the shoe's current color. No lights, bulbs, or glowing tubes; color from flat backdrops and soft studio light. Soft 35mm grain, gentle bloom, halftone ripples radiating from water impacts and pulsing on colorway swaps, chromatic aberration on flash frames, single-frame white flashes, quick black-and-white frames intercut.

Camera: one continuous orbiting hero rotation as the spine of the film, crash zooms to macro texture, focus hunting between droplet and logo, whip pans between details, speed ramps only on water impacts, then a locked slow push-in for the ending. Audio: follow the uploaded 15-second track end to end colorway snaps ticking on the beat like a visual hi-hat, deep sub whoosh into the ramps, crystal splash hits on slow-points, a clean water-drop plink on the final droplet, the video resolving exactly as the track resolves.
```

<a id="commercial-product-case-25"></a>
<!-- Case 25: Mangosteen Serum Product Reveal (by @ritesh_ai) -->
### ケース 25: [マンゴスチン美容液のプロダクトリビール](https://x.com/ritesh_ai/status/2076580389867692447) (投稿者 [@ritesh_ai](https://x.com/ritesh_ai))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-25"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2076580389867692447.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Use @ Image1 as the visual storyboard. 1 continuous shot, 10s, 9:16 vertical. Subject: NECTARY — a minimalist skincare extraction machine in translucent lilac acrylic and brushed gold — processes a whole mangosteen into @ Image2 , a violet-tinted vitamin C serum, in one unbroken transformation. Machine: Wide, squat, rounded-rectangle footprint, not tall or narrow. Translucent glossy lilac acrylic body, brushed gold metal accents. Flat rounded-rectangle top lid, "NECTARY" embossed flush into a front lid bar, same lilac tone as the body. Four round glass pillars at the outermost corners, filled with smooth violet fluid, no bubbles. Thin gold support rods set inboard of the pillars, running from lid to base. One unified opaque brushed-gold housing rides on those inner rods — short and wide like a rounded drum, wider than tall, flat underside, no neck or vessel shape. Two tall stadium-shaped clear glass slots cut into its front face. Stepped rounded-rectangle glass-and-gold base platform below. Reference: @ Image2 defines the exact bottle geometry and label. Location: Seamless lilac-to-violet gradient background, glossy mirror-reflective floor, soft studio environment, no other objects in frame. Visual Style: Ultra-clean CGI product cinematography, glossy and hyper-tactile, premium beauty-tech aesthetic. Camera: One continuous slow push-in for the full ten seconds, locked center axis, no cuts, no other movement. Lighting: Soft diffused overhead key light, warm gold rim light catching the housing and support rods, gentle volumetric glow rising from the base platform. [00:00–00:02] Wide shot. The machine in full view, a whole mangosteen — deep violet rind, small green calyx — resting on the base platform in the open gap beneath the raised gold housing. [00:02–00:04] The gold housing slides down along the inner rods, descending to enclose the stationary mangosteen. The fruit itself doesn't move. [00:04–00:07] With the housing lowered, violet rind and pearly white flesh swirl into a marbled gradient inside it, visible through the two glass slots, rising and deepening, tiny gold flecks suspended in the liquid. [00:07–00:08.5] The housing rises back up along the rods, revealing @ Image2 now resting on the platform where the fruit once sat. [00:08.5–00:10] The continuous push-in arrives close on @ Image2 alone, label clean and legible, soft violet glow beneath it. Audio: Soft mechanical hum, glass resonance, a telescoping slide as the housing lowers and rises, a rising crystalline shimmer as the liquid deepens, a gentle chime at the reveal. No music, no voiceover. Goal: A living product demonstration — one whole fruit, transformed into its own serum, in a single unbroken shot.
```

<a id="commercial-product-case-26"></a>
<!-- Case 26: Mumbai Suitcase Taxi Reveal (by @rahulnanda86) -->
### ケース 26: [ムンバイのスーツケースタクシーお披露目](https://x.com/rahulnanda86/status/2076874322145390605) (投稿者 [@rahulnanda86](https://x.com/rahulnanda86))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=commercial-product-case-26"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2076874322145390605.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Ultra-realistic handheld smartphone footage, vertical 9:16, recorded by a random bystander outside Mumbai International Airport at the arrivals pickup lane on a bright monsoon morning. The entire clip feels like genuine viral phone footage accidentally capturing an unbelievable new invention. Authentic smartphone characteristics throughout: slight handshake, autofocus breathing, rolling shutter, tiny exposure shifts as the camera moves between the shaded terminal and bright outdoors, realistic phone HDR, natural compression, subtle oversharpening, and no cinematic grading or CGI look.

The recording begins as a young Indian couple exits the arrivals terminal. The man wears a backpack and casually rolls a large cream-colored hard-shell suitcase beside him while the woman walks next to him carrying their toddler. Morning airport activity is calm—only a handful of taxis, app cabs, luggage trolleys, airport staff, and scattered travelers move through the pickup lane. The person filming casually follows them, assuming they're just another family leaving the airport.

Without warning, the man stops beside the curb and presses a hidden button on the suitcase handle.

Within seconds the suitcase transforms mechanically into a compact three-wheeled electric scooter. Wheels deploy smoothly from underneath, handlebars unfold upward and lock into place, the seat flips out, the footboard extends, and a lightweight transparent rain canopy automatically rises overhead from neatly folded panels. Every movement feels like a genuine engineered consumer product rather than science fiction. Nearby travelers stop, stare, smile, and instinctively pull out their phones to record.

The woman smiles and casually climbs onto the rear seat while holding the child securely. The transparent canopy settles into place above them. The tiny electric scooter quietly pulls away into the airport pickup lane, merging naturally with the light morning traffic. The bystander filming instinctively pans to follow them, taking a few quick steps while trying to keep them centered. A couple of people laugh in disbelief while another points toward the transforming luggage.

As the futuristic luggage scooter disappears down the airport road, the filmer quietly mutters in disbelief:

"Bhai... yeh toh future aa gaya."

The recording ends naturally while still following them into the distance.

Maximum realism. Looks exactly like accidental viral smartphone footage filmed outside Mumbai Airport on a quiet morning. No cinematic shots, no cuts, no impossible camera angles—only authentic handheld bystander footage with believable phone-camera imperfections throughout.
```

<a id="reference-driven"></a>

<a id="reference-driven"></a>
## 🖼️ 参照画像ベース

<a id="reference-driven-case-1"></a>
<!-- Case 1: Skeleton Pianist Miniature Diorama Performance (by @tea_story_hoshi) -->
### ケース 1: [骸骨ピアニストのミニチュアジオラマ演奏](https://x.com/tea_story_hoshi/status/2040614786933887043) (投稿者 [@tea_story_hoshi](https://x.com/tea_story_hoshi))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-1"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/011.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
I tried adapting it. The details still need more tuning, but the fact that it produced a good result in one pass is impressive.

<prompt>
Subject:
Subject 1: A cute and stylish skeleton girl. She wears a navy sailor-style jacket, a pink pleated skirt, and a wide-brimmed hat adorned with a small skull. Her skeleton fingers are highly flexible, delicate, and expressive. For consistency in appearance and character, please refer to the reference image.
Environment:
A high-quality 3D miniature diorama with a whimsical clay-animation style. A small white grand piano sits on a stage with a stone-like texture. Several friendly glowing white ghosts with simple black eyes, shaped like draped fabric, surround her. The setting is a dreamlike blue architectural space. Warm, fantastical light emanates from the ghosts and small lanterns. Toy-like texture.
Mood:
Eccentric, elegant, cozy, and slightly eerie. The performance is deliberate rather than chaotic, creating a magical and graceful impression.
Timeline:
[00:00-00:02] Shot 1: Wide-angle POV, slow push-in. A skeletal girl sits elegantly at the white grand piano on the stone stage. She raises her skeletal hands, slightly tucks her posture, snaps her head up to look straight ahead, and begins playing smoothly. Audio: a beautiful, elegant classical piano intro.
[00:02-00:03] Shot 2: Hard cut to a medium shot. Stable gimbal movement. She is fully in control of the melody. Her skeletal fingers press the keys with clear, readable motion in a smooth flowing cycle. Friendly glowing white ghosts sway and bounce gently in time with the rhythm. Audio: a fast-paced rhythmic classical piano melody perfectly synchronized with her finger movement.
[00:03-00:07] Shot 3: Slight tracking close-up focused on her face and the piano keys. She ends the performance with a dramatic finale and lifts her hands from the keys as the ghosts glow more brightly in the warm light. She turns toward the camera and gives a gentle nod. Audio: the final elegant piano chord re
```

<a id="reference-driven-case-2"></a>
<!-- Case 2: Storm Ship Princess vs Kraken (by @applete77191758) -->
### ケース 2: [嵐の船上の王女対クラーケン](https://x.com/applete77191758/status/2040450526819807277) (投稿者 [@applete77191758](https://x.com/applete77191758))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-2"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/015.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
This might not be perfect, but I thought it could still be useful, so I'm sharing it.
(Feel free to modify it.)

I turned internet search on for the first half.
It felt like the camera work got better with it on.

#TopviewAI #Seedance2
-----------------------------------
A cinematic, high-intensity anime sequence set on a pirate ship in a violent storm at night. Strong emphasis on physical realism, dramatic lighting, and dynamic camera control.

Environment & Physics
Heavy rain, strong wind, turbulent ocean <<<Image4>>>

Visible whitecaps continuously forming and breaking.
Ship motion:
Pitching (forward/back tilt)
Rolling (side tilt)
Deck instability affects all character movement (staggering, slipping)
Water spray, wet reflective surfaces, rope tension reacting to motion
Lighting (lightning effects)
Lightning functions as:
Rim light
Strobe effect
Creates sharp shadows, silhouettes, and dramatic reveals
Princess Setup <<<Image2>>>

Princess starts near the mast
Visibly anxious, struggling to balance due to pitching
Subtle stagger and unstable footing
Kraken Emergence & First Impact
<<<Image3>>>
Ocean splits, tentacles erupt through crest waves
Tentacles wrap the ship and slam the deck
Reaction:
Princess staggers
Crew panics: shouting, slipping, colliding
Destruction
Tentacle breaches the hull
Wood splinters, debris bursts
Interior partially floods
Movement to Attack Position
Princess regains footing
Grabs fallen knight's sword
Moves toward the bow only during the attack phase
Camera: aggressive tracking with ship pitching
Heroic Attack Sequence (insert slow motion)
Pre-Attack Build
Lightning flash -> freeze-like tension
Camera begins a slow zoom-in with easing toward the princess
Leap (slow motion starts)
Princess jumps
IMPORTANT:
Enter slow motion (about 0.3-0.5 seconds)
Rain droplets, hair tips, and cloth edges become visible in detail
Lightning acts as a strobe, freezing micro-movements
Slash (maximum zoom)
At the peak of motion:
Camera:
Ease-in zoom -> accelerate into a fast zoom
Action:
Sword swings
Effect:
Bright sword trail / afterimage
Clean, sharp "slash" feeling / impact frame
Motion blur + light streaks
```

<a id="reference-driven-case-3"></a>
<!-- Case 3: Maid Blade Dance: Mei vs Coco (by @MiraMusic_AI) -->
### ケース 3: [メイド剣舞：メイ対ココ](https://x.com/MiraMusic_AI/status/2040281710957666770) (投稿者 [@MiraMusic_AI](https://x.com/MiraMusic_AI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-3"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/019.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Title: "Maid Blade Dance - Mei vs. Coco"
Duration: "15 seconds"
Input:
A: "<<<Image1>>>"
B: "<<<Image2>>>"
Characters:
A:
Name: "Kirishima Mei"
Weapon: "Blade of Bewilderment (black-purple)"
B:
Name: "Sakuraba Coco"
Weapon: "Ribbon Spear (silver + red ribbon)"
Movement Core:
A: ["high-speed multi-hit slashes", "black-purple aura", "multiple blur afterimages"]
B: ["high-speed spear rotation", "silver-white aura", "spiral ribbon motion"]
Environment:
Location: "Japanese-style mansion corridor (moonlit, shoji-screen background)"
Lighting: "moonlight blue + shoji orange"
Atmosphere: "black and white dust"
Camera: "24mm to 70mm. High-speed tracking + sudden stops. Slow motion at impact (0.3x speed)."
Cuts:
- Cut: 1
Duration: "1.5 seconds"
Action: "Mei (left) and Coco (right) face each other from 10 meters apart. Mei half-draws her sword."
Camera: "slow horizontal pan (24mm)"
- Cut: 2
Duration: "1.5 seconds"
Action: "Mei fully draws the sword. A black-purple aura flashes for an instant. Mei moves straight toward Coco with afterimages."
Camera: "ultra-fast dolly-in toward Mei (50mm)"
- Cut: 3
Duration: "2 seconds"
Action: "Coco spins at high speed around the spear shaft. Mei's consecutive slashes strike the spear. White-blue sparks burst out. The ribbon spreads outward with centrifugal force."
Camera: "rotation centered on Coco (45mm)"
- Cut: 4
Duration: "1.5 seconds"
Action: "Mei holds her sword at chest height. Coco holds her spear horizontally. They read each other's next move."
Camera: "lateral tracking with anticipation (35mm)"
- Cut: 5
Duration: "2 seconds"
Action: "Mei unleashes seven consecutive slashes. Each slash leaves a trail of black light. Coco sweeps the ribbon to intercept, and the ribbon wipes away the black trails in white arcs."
Camera: "high-speed tracking pan toward Mei (50mm)"
- Cut: 6
Duration: "1.5 seconds"
Action: "Mei delivers a huge diagonal slash. The black-purple aura sweeps across half the screen. Coco braces her spear diagonally to receive it."
Camera: "track Mei's arc from a diagonal angle (50mm)"
- Cut: 7
Duration: "2 seconds"
Action: "Coco rotates her body while changing her spear stance. She thrusts three times at high speed in succession. Mei knocks them away with her blade."
Camera: "flash dolly-in plus rotation toward Coco (40mm)"
- Cut: 8
Duration: "2.5 seconds"
Action: "Sword and spear collide head-on. Sparks explode violently (black-purple vs. white-blue). Their hair ripples. Dust spreads outward in a radial burst."
Camera: "static, centered on the point of impact (70mm)"
Effect: "slow motion 0.3x"
- Cut: 9
Duration: "1.5 seconds"
Action: "Mei and Coco are blown several meters backward, drop to one knee, and glare at each other."
Camera: "pull backward away from both at the same time (35mm)"
- Cut: 10
Duration: "1 second"
Action: "Mei swings her sword once more. Coco resets her spear. They enter the starting stance for the next round."
Camera: "slow pull-back (24mm)"
Loop: "black and white dust separates and spirals. The battle continues forever."
Notes:
- "Mei: straight, sharp motion. Coco: curved, flowing motion."
- "Black-purple vs. white-blue sparks define their personalities."
- "Moonlight and shoji screens reinforce the Japanese duel atmosphere."
```

<a id="reference-driven-case-4"></a>
<!-- Case 4: Apocalyptic Rooftop Piano Farewell (by @liyue_ai) -->
### ケース 4: [終末の屋上でピアノに別れを告げる](https://x.com/liyue_ai/status/2040062803076341872) (投稿者 [@liyue_ai](https://x.com/liyue_ai))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/028.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Core theme: realism | grand epic scale | apocalyptic aesthetics | live-action performance
[Character and basic setup]
Character: use [@Image 1] as the reference. Reproduce the facial features, face shape, and hairstyle 100 percent. No beautification. Height: 1.75 meters.
Base outfit: black thin turtleneck sweater.
Scene: create an apocalyptic music video about a girl playing piano on a rooftop in the ruins of a city under a meteor shower. The background city is being struck by meteors. She plays and sings a farewell song to the world, and in the end disappears in the firelight of a meteor hitting her exact position.
Core content:
- The girl quietly plays piano and sings in the city ruins.
- Massive meteor-shower destruction, with many meteors falling one after another, all trailing long flames.
- Destruction effects must be shocking and realistic.
- Strong contrast between the girl's performance and the catastrophic background.
- A tragic yet beautiful ending of destruction, but it should not look painful.

Lyrics: "The wind is burning, the clouds are fleeing, the clock of the end times rings softly. Dust returns to earth, wind returns afar. My heart is calm as I go toward the end." (end on a high note)
Special requirements:
- Grand scale with shocking destruction effects.
- Strong contrast between the girl's singing performance and the background impact.
- A tragic, beautiful ending filled with apocalyptic aesthetics.
- The song's emotion should rise continuously from weak to strong, with a slow lyrical rhythm.
[Atmosphere and image quality]
Simulated equipment: IMAX film camera with Panavision C-series lenses, including simulated motion blur.
Color and tonality: Hollywood teal-and-orange tone, low saturation. Generate the footage in a realistic visual style.
```

<a id="reference-driven-case-5"></a>
<!-- Case 5: CINEMATIC 8mm Fisheye lens, FPV racing drone camera, hyper-fluid motion (by @itsPixieVerse) -->
### ケース 5: [映画的 8 mm 魚眼、FPV レースドローン、超流動モーション](https://x.com/itsPixieVerse/status/2040030453298811099) (投稿者 [@itsPixieVerse](https://x.com/itsPixieVerse))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-5"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/048.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[CINEMATIC] 8mm Fisheye lens, FPV racing drone camera, hyper-fluid motion. [@Image 1] (Lanky Knight, red coat) on a longboard. [@Image 2] (Steep coastal mountain road).
0-3s: [Extreme high-speed follow] [@Image 1] carves down the steep asphalt. The camera mimics an FPV drone, flying inches from the ground at blinding speed. The red coat whips violently in the wind.
3-6s: [360-degree barrel roll] [@Image 1] hits a hairpin turn, leaning horizontally. The camera executes a dizzying, hyper-fluid 360-degree roll over his head, maintaining focus on his armor reflecting the bright sky.
6-10s: [Under-board swoop & launch] [@Image 1] hits a ramp, launching into the air. The camera aggressively swoops underneath the board, capturing the massive ocean drop, before tilting up as [@Image 1] backflips.
10-15s: [Impact & rapid pull-back] [@Image 1] lands flawlessly, wheels smoking. The camera snaps backward in a rapid reverse-dolly motion, showcasing the majestic landscape as [@Image 1] speeds away.
```

<a id="reference-driven-case-6"></a>
<!-- Case 6: Reference-Driven Kung Fu Stunt Sequence (by @YaReYaRu30Life) -->
### ケース 6: [参照画像駆動のカンフースタント](https://x.com/YaReYaRu30Life/status/2039971048305930643) (投稿者 [@YaReYaRu30Life](https://x.com/YaReYaRu30Life))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-6"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/059.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Subject:@Image 1 Photorealistic
Image reference. A professional stuntman and kung-fu master performing full-body, high-speed, functional kung-fu.

Movement Rule:

Constant full-speed forward
```

<a id="reference-driven-case-7"></a>
<!-- Case 7: Ray tracing, Unreal Engine render, small town in heavy rain (by @Gwsubsa) -->
### ケース 7: [レイトレーシング、Unreal Engine レンダリング、豪雨の町](https://x.com/Gwsubsa/status/2040193631341174792) (投稿者 [@Gwsubsa](https://x.com/Gwsubsa))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-7"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/071.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Ray tracing, Unreal Engine render, small town in heavy rain. @image1 character with identical hairstyle, outfit, realistic skin, dim lighting, IMAX cinematic, 35mm lens, 4:3 ratio, grey-blue low saturation, film grain, soft god-rays, cold expression, smooth motion, glowing sword trail. 1–3s: Camera tilts up from feet to full body; rain splashes burst under steps. 3–6s: Close-up feet stepping forward, blue shockwave spreads; world desaturates, rain freezes mid-air; camera pulls back, blue aura flows from body. 6–9s: Upper-body close-up; hands gather at chest, suspended rain forms water sword; blue light converges, droplets create massive sphere. 9–12s: Side face close-up; faint blue glow, slash upward; sword dissolves, arc energy explodes with rain; camera follows sky cut, clouds split; golden dragon and fire dragon emerge flying.
```

<a id="reference-driven-case-8"></a>
<!-- Case 8: Moon Convenience Store Night Shift (by @zasuko_michiksa) -->
### ケース 8: [月面コンビニの夜勤](https://x.com/zasuko_michiksa/status/2039650311212872036) (投稿者 [@zasuko_michiksa](https://x.com/zasuko_michiksa))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-8"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/084.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Use `real-zasuko-2.0-character-sheet-dx.png` as the character reference. Start with a wide cinematic shot of the lonely convenience store on the moon before cutting inside. Create a photorealistic 15-second surreal live-action video of Michikusa Zasuko working a night shift at a convenience store.
```

<a id="reference-driven-case-9"></a>
<!-- Case 9: Rooftop Awakening to F-14 Transformation (by @john87445528) -->
### ケース 9: [屋上で覚醒し F-14 へ変形](https://x.com/john87445528/status/2039496153641660508) (投稿者 [@john87445528](https://x.com/john87445528))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-9"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/088.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Chapter 1 (0-15 seconds): Rooftop Awakening · Running and Leaping Down (Front to Back View). Style: rugged primitive realism using a 35mm handheld film camera, with natural grain and subtle shake. The dazzling direct sunlight of Chongqing noon creates high-contrast shadows and lens flares. Camera: a single continuous third-person handheld follow shot with no cuts, starting from a low front angle and smoothly transitioning to an over-the-shoulder / back view, following the protagonist Image 1 throughout. Atmosphere: high-altitude winds howl, dust and mist fly, and cloth, hair, and mechanical parts all show realistic physical motion. Sound effects: metallic echoes of mechanical high heels striking concrete, heavy rhythmic breathing, howling wind, operating mechanical joints, violent fabric flapping, sudden silence at the instant of the leap, followed by a high-speed wind-cutting shriek during descent. [Visual Reference / Description]: fully preserve the elegant female character from the reference image, wearing a white suit, silver mechanical chest plate and neck collar, silver mechanical hands, and silver high-heeled boots, with long straight black ponytail, delicate facial features, and large earrings. Physical features and clothing details must remain fully consistent. The scene takes place on the rooftop of Raffles City Chongqing, surrounded by skyscrapers, with the broad Yangtze River visible in the distance. [Timeline per Second] 0-4s: [Front Start] The handheld camera captures her full body from a low front angle. She stands at the rooftop edge, looking directly into the camera with a calm, determined expression. The mechanical cervical spine catches the noon sunlight, and her ponytail lifts in the high wind. She slowly turns around. 4-9s: [Over-the-Shoulder Follow · Full Sprint] The camera switches to an over-the-shoulder perspective and follows closely. She sprints across the concrete platform. Her mechanical high heels spark against metal with each step. The hem of the suit and the mechanical spine exoskeleton whip violently in the airflow. Dust kicks up from the roof, and the cloth simulation stays highly realistic. 9-12s: [Leaping Down] She suddenly jumps off. The instant her feet leave the ground, the camera dips slightly and switches to a fast downward tracking view. Her suit billows violently in the extreme airflow. The glass curtain walls of Raffles City streak upward on both sides, and motion blur erupts intensely. [Style and Quality Enhancement] Realistic 8K quality, ultra-fine mechanical texture and cloth physics, cinematic lighting and contrast, perfect motion blur, high dynamic range, no artifacts, coherent multimodal physical effects, stable cinematic image.

Chapter 2 (0-15 seconds): Freefall · Purple AITO M7 Enters the Frame. Style: rugged realism, 35mm handheld camera, natural grain, subtle organic shake. Camera: primarily handheld follow shots, with quick cuts between the protagonist's falling perspective and the ground car-chase perspective to create extreme tension. Maintain full real-time speed, with no slow motion. Lighting: dazzling high-contrast sunlight at Chongqing noon, strong reflections on the glass curtain walls of Raffles City, and heat haze rising from the road. Sound effects: wind-cutting shriek intensifies continuously -> engine roar approaching from a distance -> sharp tire friction on asphalt -> cyber-energy hum -> metallic thud at the moment of impact -> dull compression as four wheels land -> engine roar continues and grows stronger. [Visual Reference / Description] The protagonist remains the same female character from the reference image, preserving all details. Scene: on the Chongqing ramp road below Raffles City, a purple AITO M7 drives at high speed. It uses the upward slope of the ramp to launch naturally and precisely catch the protagonist as she falls from the rooftop. No slow-motion close-ups at any point; keep the rhythm realistic, high-speed, and cinematic. [Timeline per Second] Continuing from Video 1 and extending by 15 seconds. 0-4s: [Extreme Speed Fall · Overlooking the Ground] Protagonist Image 1 falls at high speed while maintaining a balanced gliding posture with both arms spread. The camera locks onto her back. The curtain walls of Raffles City streak upward on both sides, the ground rapidly expands, and motion blur becomes extreme. The frame quickly inserts a ground view: a purple AITO M7 races along the ramp road below Raffles City. The car emits a cyber blue-purple glow, the engine roars, and the tires leave two black marks on the asphalt. 4-9s: [Ramp Launch · Trajectory Intersection] The purple AITO M7 charges to the top of the ramp. Using the ramp's inertia, the front of the car lifts into the air and the sunroof slides open instantly. The camera alternates rapidly between the falling protagonist and the climbing AITO M7. She keeps a high-speed falling posture with arms spread, and the AITO M7 keeps accelerating up the ramp. The two trajectories converge rapidly, compressing time to the limit and maximizing tension. 9-11s: [Last Second · Posture Change · Precise Entry] With only one second left before the sunroof, the protagonist instantly pulls in her outstretched arms and sharply changes from a horizontal gliding posture to a vertical upright posture. Her legs point straight down toward the open sunroof of the airborne purple AITO M7. The action is swift, decisive, and completely without hesitation. In the next instant, she drops vertically into the open sunroof and lands in the driver's seat at extremely high speed. No slow motion at any point; the impact is realistic and violent. 11-13s: [Four Wheels Landing · Maintaining Drive] The body of the car compresses slightly under the force of catching her. All four wheels slam back to the asphalt. The suspension violently absorbs the double impact. Immediately after landing, the engine roar rises further. Without slowing or stopping, all four tires scrape the asphalt, leaving new black marks, and continue driving at full speed. 13-15s: [Stable Inside Car · Energy Accumulation] The AITO M7 continues high-speed driving. The camera tracks close to the side from a low angle as blue-purple energy patterns spread from the four wheels across the body. The sound of mechanical transmission rises subtly from the underside and keeps strengthening. The body vibrates slightly during the high-speed run. The precursor energy of the coming transformation surges and churns beneath the paint. [Style and Quality Enhancement] Realistic 8K quality, ultra-fine mechanical details and energy-light textures, cinematic volumetric light and heat haze, perfect speed blur, HDR glow, no artifacts, full real-time speed, no slow motion.

Chapter 3 (0-15 seconds): AITO M7 Transforms -> Becomes an F-14 -> Protagonist Stands on the Aircraft Back and Takes Off. Style: rugged realism, 35mm handheld film aesthetic, natural grain, subtle shake. Camera: multi-angle follow coverage including ground tracking, low angle close to the ground, aircraft side view, and protagonist first-person view, all following the aircraft tightly throughout the transformation. Transformation details must remain clearly visible. Atmosphere: light smoke and heat haze drift across the Chongqing road. Cyber blue-purple light refracts between buildings. Noon sunlight produces dazzling reflections and strong shadows across the metal surfaces. Sound effects: engine roar surges -> metal skin bursts and folds -> deep hydraulic tremor as the wings unfold -> metallic gripping sound as the protagonist climbs the exterior -> cockpit seal pops and is immediately drowned by wind noise -> explosive ignition of twin engines -> piercing shriek as the F-14 takes off and breaks the air -> powerful high-altitude wind overtakes the entire soundscape. [Visual Reference / Description] The purple AITO M7 completes a full transformation while driving on the Chongqing road, changing from a car into an F-14 fighter jet, as shown in Image 2. During the transformation, the protagonist clings to and climbs along the aircraft exterior in a dangerous and exposed position. She finally stands centered on the back of the F-14, legs slightly apart to stabilize her balance. Her white suit and ponytail whip violently in the extreme airflow. The F-14 takes off directly from the Chongqing road, and the protagonist remains standing firmly on its back. [Timeline per Second] 0-4s: [Road Acceleration · Transformation Start] The AITO M7 accelerates rapidly along the Chongqing road. Body panels burst open one after another and unfold. The hood rolls upward and becomes mechanical structure. The doors fold outward. The metal skin cracks along structural lines, revealing the cold mechanical interior. The protagonist climbs dangerously toward the top of the aircraft while gripping the transforming metal skeleton. She jumps and shifts position in sync with the aircraft's changing shape. The camera tracks every detail from close to the side of the aircraft. 4-6s: [Wings Unfold · Engines Fully Reassemble] The F-14's iconic swept wings snap open from the folded state and lock into place. The camera captures a low-angle near-ground full view of the wing deployment. Heat haze and dust are blasted up by the airflow from the wings. The twin engine nacelles violently reassemble into jet structures, emitting blue-purple thrust flames. The exhaust scorches the road surface. By now, the protagonist has climbed to the center of the aircraft's back, feet planted firmly, standing upright as the transformation completes. 6-8s: [Protagonist Stands on Aircraft Back · Takes Off] The instant the transformation completes, the protagonist stands fully upright on the back of the F-14. The hem of her white suit flies up in the strong airflow, and her ponytail extends horizontally. The silver mechanical parts reflect the noon sun intensely. The F-14's twin engines ignite at full power. The aircraft surges forward, the front wheel lifts, and the rear wheels leave the asphalt at the last possible moment. The nose pitches upward, carrying the protagonist into the Chongqing sky while she remains standing on its back. 8-15s: [Takeoff and Low City Skim · Protagonist Holds Position] The F-14 climbs vertically, then abruptly lowers its nose and skims over Chongqing at ultra-low altitude.
```

<a id="reference-driven-case-10"></a>
<!-- Case 10: Armor Assembly Street Counterattack (by @egeberkina) -->
### ケース 10: [装甲組み立てからの街頭反撃](https://x.com/egeberkina/status/2044809303878693242) (投稿者 [@egeberkina](https://x.com/egeberkina))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-10"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/TfQ7cL05pwwcaq06.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
100% real-life filmed texture, iPhone cinematic realism, handheld aggressive tracking, natural daylight with harsh shadows, motion blur on fast movement, micro camera shake from impacts, subtle lens dirt, grounded physics, no stylization, no fantasy glow everything must feel physically real.
Character Reference
Use @ image1 as exact human reference.
Face, body, proportions, clothing must remain identical.
No stylization drift.
Armor System
A modular high-tech combat suit (fictional, original design) assembles onto the body in real-time.
Design language:
industrial, mechanical, exposed joints, titanium + carbon fiber textures
subtle internal energy lines (amber/orange, NOT glowing like sci-fi magic)
all parts are PHYSICAL modules (no teleporting, no nanotech fantasy)
Environment
Destroyed urban street
cracked asphalt, burning cars, smoke, sparks, debris
cars abandoned, bus in background
dust particles reacting to movement
realistic chaos, no cinematic exaggeration
Enemies
Pack of 4–6 creatures
grey-black skin, rough organic texture
long limbs, aggressive animalistic movement
no fantasy glow, no stylized design
pure physical threat
TIMELINE 15s ONE TAKE
0–1s HOOK
Hero sprinting toward camera.
Monsters chasing from behind.
Suddenly
four armor modules fly in at extreme speed from off-screen.
SFX metallic WHOOSH + air displacement
1–2.5s FOOT ASSEMBLY
Boot modules SLAM onto feet mid-run.
He stomps a creature’s head and launches forward ~8 meters.
Camera shakes on impact.
2.5–4s LEG ASSEMBLY
Leg armor locks around thighs and hips while running.
He jumps onto a wall, runs 2 steps, pushes off.
4–5.5s WAIST CORE
Hip + core modules snap in.
He pivots mid-air, dodging a claw strike.
5.5–7s TORSO
Chest + spine plates LOCK together.
Heavy metallic clicks.
He slides under a truck while armor completes.
7–8s BACK IMPACT MOMENT
A creature attacks
He blocks with newly formed armor.
Impact feels HEAVY.
SFX metal hit + bone crack
8–9s ARMS
Arm + shoulder modules slam on.
He clenches fist.
Camera pushes in slightly.
9–10s HELMET
Helmet assembles in pieces over face.
Seals tight.
Eyes activate with subtle amber glow (NOT neon, NOT stylized)
10–12s COUNTERATTACK
Creatures leap.
He spins, blocks, grabs one
throws it ~20 meters into a burning car.
Explosion reacts physically.
12–15s FINAL STRIKE
He dashes forward.
Grabs creature’s limb.
Delivers a brutal palm strike
Creature crashes hard to ground.
No exaggerated blood keep it grounded.
ENDING SHOT
Hero slides into half-kneeling pose
Fire + smoke rising behind him.
Camera settles.
Breathing sound.
Cut to black.
Audio Direction
SFX
metal impacts, air displacement, footsteps, debris
no sci-fi sounds all grounded
Music
low cinematic pulse builds cuts abruptly at end
```

<a id="reference-driven-case-11"></a>
<!-- Case 11: Character reference @Image 1, convert to real-person live-action style (by @Adam38363368936) -->
### ケース 11: [画像 1 のキャラクターを実写人物化](https://x.com/Adam38363368936/status/2039646077230698743) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-11"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/103.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Character reference @[Image 1], convert to real-person live-action style. Model figure, cool white skin, slender arms, prominent bust and hips.
15-second handheld video with a sense of breathing, Japanese film style, warm orange backlight at dusk, slight film grain, low saturation color tone, no subtitles, no dialogue.
Environment: Sunset, under a concrete overpass, occasional vehicles passing on the road, pedestrian overpass, elevated road, main road traffic, warm orange backlight at dusk, flowing light and shadow from traffic.
Camera Movement: Handheld slight shaking throughout, sense of breathing, natural follow-up, no stabilizer, realistic cinematic feel.
Shot Breakdown (15 shots in 15 seconds):
00:00 | Shot 1: Handheld full body fixed, girl leaning sideways against a concrete railing, one hand on the railing; foreground is the leaning full-body posture, background is blurred traffic and warm yellow dusk, relaxed atmosphere.
00:01 | Shot 2: Handheld full body slight push-in, girl stands up and stretches her arms upwards, a shallow smile on her lips but emptiness in her eyes; foreground is backlit hair and stretching motion, background is blurred steel structure and flowing light spots, light and yet melancholic.
00:02 | Shot 3: Handheld full body follow shot, girl lightly jumps forward; foreground is the jumping dynamic, background is the bridge deck and blurred traffic, youthful and easygoing.
00:03 | Shot 4: Handheld close-up shot, girl brushes her bangs in side backlight, eyelashes dyed gold; foreground is the side face and hand, background is blurred railing and traffic, lazy and gentle.
00:04 | Shot 5: Handheld close-up of hands, fingertips lightly tracing the rough railing; foreground is fingertips and texture, background is dense traffic and warm orange dusk, delicate action.
00:05 | Shot 6: Handheld full body horizontal move, girl sits on the ground looking down at the traffic, eyes vacant; foreground is the sitting full body, background is moving car lights and steel structure, slightly heavy emotion.
00:06 | Shot 7: Handheld close-up slow push-in, girl looks up at the sky, the smile fades, showing sadness; foreground is the quiet face, background is the twilight clouds and buildings, restrained emotion.
00:07 | Shot 8: Handheld full body fixed, girl stands up and stretches her back, backlight outlines her silhouette; foreground is the stretching posture, background is concrete structure and traffic, lonely and clean.
00:08 | Shot 9: Handheld close-up shot; foreground is the tie and hands, background is blurred railing, gentle and fragile.
00:09 | Shot 10: Handheld close-up of eyes, eyelashes clearly defined in backlight, eyes hiding secrets; foreground is the light and shadow on the eyes, background is blurred dusk, delicate emotion.
00:10 | Shot 11: Handheld full body follow shot, girl turns and runs lightly; foreground is the running posture, background is the bridge corner, returning to easygoing.
00:11 | Shot 12: Handheld full body side move, girl runs past the corner, her figure cut by light and shadow; foreground is the light and dark silhouette, background is flowing light spots, realistic handheld feel.
00:12 | Shot 13: Handheld close-up shot, girl briefly smiles while looking down; foreground is the light and shadow on the lips, background is blurred railing, bright emotion.
00:13 | Shot 14: Handheld full body slow push-in, girl walks towards the end of the bridge and stretches her arms pointing into the distance; foreground is the backlit full body, background is the city dusk, quiet and healing.
00:14 | Shot 15: Handheld full body freeze frame, girl turns her back to the camera looking at the city, mixing ease and sadness; foreground is the back view of the flowing skirt, background is the vast dusk and river of cars, ending with negative space.
```

<a id="reference-driven-case-12"></a>
<!-- Case 12: Polar Bear Match-Cut Sword Duel Template (by @aimikoda) -->
### ケース 12: [ホッキョクグマのマッチカット剣闘テンプレート](https://x.com/aimikoda/status/2039380910278115454) (投稿者 [@aimikoda](https://x.com/aimikoda))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-12"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/112.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
FORMAT: 15s / free rhythm / 1 MATCH CUT / CONTINUOUS MOVE UNTIL MATCH CUT + IMMEDIATE ACTION FROM FIRST FRAME

SUBJECTS: A lone sword-bearing woman in weathered fur and leather fights a massive polar bear with desperate,
```

<a id="reference-driven-case-13"></a>
<!-- Case 13: Seven-Image Seamless Morphing Sequence (by @YaReYaRu30Life) -->
### ケース 13: [7 枚の画像によるシームレス変形](https://x.com/YaReYaRu30Life/status/2039474680235741681) (投稿者 [@YaReYaRu30Life](https://x.com/YaReYaRu30Life))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-13"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/114.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
[Basic Settings]
structure: Single continuous shot (no cuts)
progression: Morphing 7 images sequentially
visibility: Each image is clearly recognizable for only an instant (no stopping required)
transition: Always smooth and continuous
style: Cinematic, high-definition, dynamic, no flicker
[Prompt Body]
Start from <<<Image1>>>.
The footage proceeds in a completely seamless single shot, continuously transforming in the order of <<<Image1>>> -> <<<Image2>>> -> <<<Image3>>> -> <<<Image4>>> -> <<<Image5>>> -> <<<Image6>>> -> <<<Image7>>>.
The overall scene is not static; morphing occurs within a dynamic video where the camera is constantly moving.
However, the recognizability of the subject is maintained, and the composition is controlled to prevent collapse.
Each image has a peak state where it is clearly visible for an instant within the flow, but there is no stopping or holding.
Everything is expressed as a continuous "evolution within motion."
[Transformation Logic (Fixed order, no duplication)]
<<<Image1>>> -> <<<Image2>>>:
The camera begins transformation while smoothly pushing in forward
Gradual change in the order of outline -> parts -> color -> texture
Fine particle decomposition -> reconstruction
<<<Image2>>> -> <<<Image3>>>:
Tracking movement where the camera flows horizontally
The structure is rewritten by light scanning
Emitting lines flow, and the shape continuously changes
* Particle expression is prohibited
<<<Image3>>> -> <<<Image4>>>:
Orbit movement where the camera circles around the subject
The shape is stretched and transformed by spatial distortion and lens warp
<<<Image4>>> -> <<<Image5>>>:
The camera slightly pulls back and changes perspective (light dolly out + angle change)
The subject melts like liquid and is reformed while flowing
<<<Image5>>> -> <<<Image6>>>:
The camera accelerates momentarily, adding momentum to the movement
The subject fragments, scatters in space, and then reassembles into a new form
<<<Image6>>> -> <<<Image7>>>:
The camera stabilizes while converging back toward the center
Energy converges at the center and integrates into the final form through light and waves
[Camera Behavior (Important)]
- Always moving but controlled movement
- Allowed:
  - Push-in / Pull-out
  - Horizontal tracking
  - Orbit (circling)
  - Light perspective change
- Prohibited:
  - Sudden blur
  - Loss of subject
  - Unnatural jumps
[Constraints (Important)]
- Cut editing prohibited (complete single shot)
- Reuse of the same effect prohibited
- Flicker, noise, and breakdown prohibited
- Subject position / scale should not be significantly disrupted
- Each image must achieve a clearly visible state at least once
- All changes must be continuous and meaningful structural transformations
[Enhancement Keywords]
dynamic camera movement
cinematic motion flow
smooth continuous morphing
temporal coherence
high detail preservation
consistent subject identity
seamless transformation flow
```

<a id="reference-driven-case-14"></a>
<!-- Case 14: Stridex Sneaker Commercial (by @ShamsAmin56) -->
### ケース 14: [Stridex スニーカー CM](https://x.com/ShamsAmin56/status/2045084636695650511) (投稿者 [@ShamsAmin56](https://x.com/ShamsAmin56))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-14"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/K1jRd7vJAePuYplT.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Create a 15-second ultra-premium cinematic commercial for futuristic sneakers branded ‘Stridex’, using the provided reference image. Maintain exact design fidelity (materials, structure, colors).

Style: high-end sportswear campaign, cinematic, sharp, luxury-grade production, no motion blur, speed expressed through design only.

00:00 – 00:03
Extreme macro close-up of the sneaker surface (mesh, stitching, sculpted lines).
Lighting: dramatic studio highlights, soft shadows on pure white seamless background.
Camera: slow, controlled glide across textures.
00:03 – 00:06
Close-up tracking shot along the side profile, revealing aerodynamic curves and layered panels.
Focus on sharp lines and directional design elements that imply speed through form.
Camera: smooth lateral dolly, shallow depth of field.
00:06 – 00:09
Mid-shot rotation of the sneaker (angled 45°), showcasing sole engineering and silhouette.
Highlight structured geometry and streamlined outsole.
Lighting remains clean, premium, no visual effects.
00:09 – 00:12
Full product reveal. Sneaker centered on a white reflective surface.
Subtle reflection beneath enhances depth.
Camera: slow cinematic push-in toward the shoe.

00:12 – 00:15
Final hero frame:
Sneaker perfectly centered, sharp and still
Introduce bold ‘STRIDEX’ logo (modern sans-serif, slightly italicized)
Add minimal tagline below (optional): “Engineered for Speed”

Logo appears cleanly (fade or subtle scale-in, no flashy effects)
Lighting: balanced, high-end studio look, crisp shadows, premium finish.
```

<a id="reference-driven-case-15"></a>
<!-- Case 15: Image-Driven Prompt with Singing Cat (by @pan_soramame_da) -->
### ケース 15: [歌う猫を使った画像駆動プロンプト](https://x.com/pan_soramame_da/status/2040921171059752988) (投稿者 [@pan_soramame_da](https://x.com/pan_soramame_da))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-15"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2040921171059752988.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
に記述じゃなくて
画像で成功確率上がるかも🐈

ちなみに……
プロンプトに
反映させる文字を書かなくてOK！
画像から読み取ってくれる👍
歌も画像見て歌ってくれる😸

――――――――――
🤖確率が上がるコツ📝

・映像に反映したい日本語の画像を用意
・字幕系は1行ずつ反映してくれる
・字幕系以外は、1行＝1カットが無難
∟だけど1カットに複数表示したい場合は
複数行指定でOK！
※『蕎麦屋、コメ旨』のように
『、』を入れるとそれも反映されちゃう
――――――――――
🤖プロンプト例📝

＠図1はシーン内に登場する店の看板の文字参照。＠図1に書かれている文字の字形をそのまま忠実に再現して看板に使用すること。1行目の文字は1軒目の看板、2行目の文字は2軒目の看板、3行目の文字は3軒目の看板、4行目の文字は4軒目の看板に使用する。
～
～
通りの左右に1軒目と2軒目の店がある。左の店の看板に＠図1の1行目の文字、右の店の看板に＠図1の2行目の文字がそのまま書かれている。
――――――――――
```

<a id="reference-driven-case-16"></a>
<!-- Case 16: Character Reference Anime Prompt (by @Reiria123) -->
### ケース 16: [キャラクター参照アニメプロンプト](https://x.com/Reiria123/status/2041118339393826933) (投稿者 [@Reiria123](https://x.com/Reiria123))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-16"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041118339393826933.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
は↓

Use @Image1 as the character reference. Keep character design, hairstyle, ears, tail, outfit, and colors perfectly consistent.

【主体 / Subject】

A blue-haired fox girl with long flowing hair, large fluffy fox ears, and a huge fluffy tail.
She wears a shrine-maiden inspired outfit with loose sleeves and a short skirt.
She stands in a Japanese shrine setting with a red torii gate, autumn leaves falling around her.
Her expression is playful, energetic, slightly teasing.

【アクション / Action】

She performs an energetic, bouncy dance with frequent jumping motions.

Repeated light jumps in rhythm (ぴょんぴょん)
Knees bend deeply before each jump for natural motion
Hair, sleeves, and tail bounce dynamically with physics
Tail sways with exaggerated follow-through motion
Spins mid-jump once (360° quick spin)
Lands softly and immediately transitions into next jump
Arms swing wide, then pull inward for momentum
Ends with a high jump and playful pose on landing

👉 重要安定化指示

Clear leg bending and landing weight control
Natural gravity and smooth jump arcs
No body distortion during airtime
Tail follows delayed secondary motion
【カメラ / Camera】
Landscape 16:9, 15 seconds
Start: full-body wide shot (全身見せてジャンプ確認)
Slight low-angle to emphasize jump height
Gentle tracking to follow vertical movement
Subtle handheld bounce synced with jumps
Mid-section zoom during spin jump
End: slight push-in as she lands final pose
【スタイル / Style】
High quality 2D anime animation
Smooth, high frame consistency
Bright autu
```

<a id="reference-driven-case-17"></a>
<!-- Case 17: Cartoon to Live-Action Animals (by @MustafyOf) -->
### ケース 17: [アニメ動物を実写化](https://x.com/MustafyOf/status/2075913453416456407) (投稿者 [@MustafyOf](https://x.com/MustafyOf))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-17"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075913453416456407.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Use the uploaded reference video as the master reference. Recreate the entire scene in ultra-photorealistic live action while preserving the original video frame-by-frame.
Maintain the EXACT camera movement, lens, framing, composition, timing, pacing, shot transitions, lighting direction, environment, props, object placement, character blocking, and every action from the reference video. ONLY replace the cartoon characters with realistic live-action animals while keeping everything else unchanged.
CHARACTER CONSISTENCY
Tom is a realistic British Shorthair cat with:
• blue-gray plush fur
• white chest, muzzle and paws
• large amber eyes
• pink nose
• rounded face
• thick tail
• expressive eyebrows
• identical appearance in every frame
• identical fur pattern, facial proportions, eye color and body size throughout the video
Jerry is a realistic golden Syrian hamster with:
• soft golden-brown fur
• cream belly
• large rounded ears
• black shiny eyes
• tiny pink paws
• small pink nose
• realistic whiskers
• consistent body proportions in every frame
• identical appearance throughout the entire video
If other Tom & Jerry characters appear, replace them with realistic animals that preserve their personality, colors, proportions and expressions while remaining identical throughout the clip.
MOTION
Preserve every movement exactly.
The realistic animals must perform the exact same actions, walking cycle, head movement, eye movement, paw placement, facial expressions, timing and interactions as in the reference animation.
No new actions.
No altered timing.
No changed poses.
ENVIRONMENT
Keep the original environment exactly the same.
Do not modify:
• furniture
• decorations
• room layout
• colors
• props
• shadows
• reflections
• camera angle
• camera path
Everything except the characters must remain unchanged.
QUALITY
Hollywood-quality CGI.
Photorealistic animals.
Natural muscle movement.
Physically accurate fur simulation.
Realistic whiskers.
Subsurface scattering.
Realistic eye reflections.
Natural breathing.
Micro facial expressions.
Ultra detailed textures.
Soft cinematic lighting.
Shallow depth of field.
Global illumination.
Ray-traced reflections.
Macro photography realism.
4K HDR.
Disney-level VFX quality.
Live-action realism.
Extremely stable temporal consistency.
Perfect character identity consistency across all frames.
Do not redesign the characters.
Do not change the environment.
Do not change the camera.
Do not change the timing.
Do not add new objects.
Do not crop or zoom differently.
No flickering.
No morphing.
No identity drift.
No fur color changes.
No eye color changes.
No size changes.
No anatomy deformation.
No extra limbs.
No duplicate animals.
No cartoon textures.
No low-quality CGI.
No inconsistent lighting.
No frame-to-frame variation.
Maintain perfect temporal consistency and character consistency throughout the entire video.
```

<a id="reference-driven-case-18"></a>
<!-- Case 18: Locked Storyboard Reference Hierarchy (by @startracker) -->
### ケース 18: [固定ストーリーボードの参照階層](https://x.com/startracker/status/2075645228271497462) (投稿者 [@startracker](https://x.com/startracker))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-18"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075645228271497462.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
REFERENCE HIERARCHY:
Use the storyboard sheet as the exact guide for camera angles, blocking, composition, and shot order. Follow all nine panels in sequence without rearranging or omitting shots.
Use the canonical face reference as the locked facial design. Her face must remain consistent in every shot, especially close-ups: oval East Asian face shape, small scar on the left cheek, faint freckles, dark eyes, and one white/silver strand of hair at the left temple.

ENVIRONMENT:
A natural volcanic cavern with the established stone altar and ember-lit dais at one end. The altar is canonical and must remain unchanged.

All other areas of the cavern must consist entirely of raw, unshaped volcanic rock. No additional masonry, carved pillars, bridges, constructed platforms, ruins, architecture, or ornamental stonework elsewhere in the chamber.
The cavern functions as a natural arena with jagged rock walls, ledges at multiple elevations, glowing magma fissures across the floor, drifting embers, dust, and volcanic haze.

COLOR LOCK:
Warm, high-contrast volcanic color grade with obsidian blacks, ember orange, molten gold, and deep red highlights. Avoid cool, blue, cyan, or blue-grey tones.

STYLE LOCK:
Hyperreal photoreal 3D CGI cinematography with visible skin pores, realistic fabric fibers, raw stone texture, natural light falloff, volumetric dust, physically accurate firelight, and crisp surface detail. No painterly rendering, stylized illustration, artificial plastic skin, or flat game-like shading.

CAMERA:
Large-format 65mm cinematic sensor, extreme sharpness, high dynamic range, natural medium-format color rendering, 28mm lens, f/5.6. Use aggressive kinetic tracking, dramatic low angles, worm’s-eye framing, aerial scale shots, and controlled Dutch angles matching the storyboard rhythm exactly.
PRIMARY CHARACTER:
A hooded East Asian woman whose face exactly matches the canonical face reference.

She wears a heavy charcoal-black hooded cloak made from coarse, tattered woven fabric. The hood remains up. The cloak has frayed edges and small worn holes near the hem.
Underneath, she wears a cream or off-white dress with gold filigree embroidery. A thin strip of blue lining is visible only at the leg slit. She also wears a dark leather corset-style waist cinch and dark leather boots.

Her forearms and wrists must remain completely unarmored in every shot. Show only bare skin or plain dress-sleeve fabric.
ABSOLUTELY NO:
Bracers, vambraces, wrist wraps, gauntlets, leather guards, metal guards, decorative cuffs, or armor of any kind on her arms. This restriction also applies to the close-up of her hand gripping the sword hilt.

She carries exactly one sword with a plain, simple crossguard. It begins sheathed at her hip and remains sheathed throughout this sequence.
MAGMA CREATURE:
A hulking brute formed entirely from raw, cracked black obsidian rock, with bright orange-red magma glowing through deep fractures across its body.

Its skin must consist only of natural broken rock and molten magma.

ABSOLUTELY NO:
Metallic swirl patterns, engraved lines, ornamental designs, decorative etching, armor plating, artificial panels, crafted shoulder pieces, gauntlets, or manufactured surfaces anywhere on its body, shoulders, hands, or forearms.

Its mane and spinal crest are formed from a consistent liquid-fire texture. Its large clawed hands are bare cracked rock, glowing internally with magma.

SCALE LOCK:
At equal camera distance, the magma creature must remain approximately three times the woman’s height. Maintain this scale relationship consistently in every shot.
SCENE SETUP:
The sequence begins on the open cavern floor near the altar. Both figures start on the same ground level with no initial height advantage. Magma fissures glow beneath them while dust, embers, and volcanic haze move through the chamber.

Shot Sequence

1. Ground-Level Wide Two-Shot
Both figures face each other on level ground near the altar. The woman stands ready with her sword still sheathed. The magma creature towers over her. Glowing fissures spread beneath their feet.
2. Worm’s-Eye Creature Shot
From an extreme low angle, the magma creature roars and drives its bare rock claws into the cavern floor. It tears a massive natural boulder free and raises it overhead. Stone fractures, debris falls, and dust bursts around its hands.

The creature’s arms and shoulders must remain raw cracked rock with glowing magma veins—no armor, engravings, or artificial patterns.

3. Tight Hand Insert
Close-up of the woman’s bare hand crushing tightly around the sword hilt as she braces to spring.
Her wrist and forearm must show only bare skin or plain fabric. No bracers, wraps, cuffs, leather, or metal guards.

4. Dynamic Wide Throw
The magma creature hurls the boulder directly at her. The rock travels in a fast, streaking arc just above the cavern floor, scattering sparks, dust, and fragments in its wake.

5. Low Tracking Leap
Track from behind the woman at a low angle as she launches away from the camera and leaps vertically past the boulder’s path. The camera tilts upward with her movement.
Her cloak snaps violently in the air as she rises toward a jagged natural ledge high above. The sword remains sheathed at her hip.

6. Boulder Impact Detail
The boulder crashes into the exact location where she had been standing. The impact tears open a crater and sends rock shrapnel, dust, sparks, and glowing fragments outward.
7. Silhouette Landing Wide
The woman lands lightly on the high jagged ledge in silhouette against the magma glow. Her cloak settles around her. Her sword remains sheathed.

The ledge must be raw natural volcanic rock, not carved or constructed.

8. Extreme-Wide Aerial Establishing Shot
Reveal the full scale of the cavern. The woman appears small on the high ledge while the magma creature stands far below near the fresh crater.
Clearly establish the new vertical separation between them. Keep the altar, ember dais, magma fissures, jagged walls, and natural ledges visible.

Do not introduce additional architecture or ruins.
9. Smash Cut to Wide Low Angle
The magma creature begins climbing the raw volcanic wall toward her. Its bare rock claws gouge deep grooves into the stone as embers and fragments fall beneath it.

Its hands, forearms, shoulders, and body remain entirely raw cracked obsidian and magma, with no armor or decorative markings.

ACTING AND MOVEMENT:
The woman moves with controlled urgency, precise balance, and restrained fear. Her hand tightens around the sword hilt before she commits to the leap.
The magma creature moves with overwhelming weight and brute force. Every action should displace dust, stone, embers, and loose debris.

AUDIO:
Deep sub-bass magma rumble, ember hiss, thunderous creature roar, rock splitting and tearing free, heavy boulder movement, fast air-whoosh during the throw, cloak snap during the leap, explosive stone impact, shrapnel clatter, rushing dust, falling debris, and claws scraping violently against raw rock.

FINAL CONTINUITY LOCKS:
Maintain the exact facial identity from the canonical face reference. Preserve the cheek scar, faint freckles, single silver-white temple strand, hooded cloak, embroidered cream dress, narrow blue lining strip, dark waist cinch, dark boots, bare forearms, and single sheathed sword.
Maintain the creature’s three-to-one scale, raw obsidian-and-magma anatomy, liquid-fire mane and spinal crest, warm volcanic grade, natural cavern geometry, and established altar.
```

<a id="reference-driven-case-19"></a>
<!-- Case 19: VOLTIA Power-Drain Montage (by @itsPixieVerse) -->
### ケース 19: [VOLTIA 吸電モンタージュ](https://x.com/itsPixieVerse/status/2077526641207881830) (投稿者 [@itsPixieVerse](https://x.com/itsPixieVerse))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-19"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2077526641207881830.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Seedance 2 Prompt:

VOLTIA @Image1 — "World Goes Quiet" | Opening Titles. 15-second montage, 30 beats @ 0.5s each, dreamlike overcranked slow motion.

Treat each beat as a standalone frame of premium key art — every frame poster-worthy, clean and legible at a glance. One unified visual language across all 30 beats: high-end stylized anime-realism render, sharp graphic linework fused with cinematic 3D lighting, moody rain-slicked urban night-world of dead streetlamps and humming substations.

Color discipline: a suppressed core palette of ink black, deep asphalt gray, muted navy and cold off-white — broken only by three deliberate accents: her royal-blue jacket, coiling neon-magenta energy ribbons, and jagged yellow geometric lightning. Heavy chiaroscuro; when she drains a light source, the frame visibly dims and she becomes the only luminous thing in it. Atmosphere layers: drifting rain haze, floating dust motes caught in dying lamplight, faint electrical sparks, ozone shimmer; anamorphic streaks off every light source, fine grain, razor-thin focal planes.

The character — locked design, identical in every beat (match reference image): VOLTIA, an atmospheric drainer who absorbs electricity and light from the world. Sleek dark bob with blunt bangs, calm intense eyes that ignite electric-yellow when she pulls a charge. Royal-blue zippered jacket with high collar and chest pocket, high-waisted black wide-leg trousers pooling over her shoes, neon-magenta cuffs at her wrists. Neon-pink energy ribbons orbit and coil around her body; yellow angular lightning fractures off her fingertips. Her demeanor never breaks: quiet, controlled, unshakable — she brings stillness to everything she touches.

Shot design: no two beats framed alike. Rotate the full grammar — macro details (a fingertip meeting a lamppost, a magenta ribbon tightening around her wrist, one eye flaring yellow, the jacket zipper catching the last light) up to god's-eye views of a city grid going dark block by block around a single standing figure. Centered symmetry, hard diagonals, foreground occlusion through chain-link and rain, vast negative space of pure darkness, low-angle untouchable-presence hero frames, top-down shots of light draining toward her like water to a drain. Lighting shifts between rim-lit silhouette against one surviving neon sign, single hard key from a flickering streetlamp, magenta-and-yellow two-tone splits across her face, and near-total low key where only her ribbons draw her outline. Include 3–4 uninhabited world-building frames: a streetlamp dying, a blacked-out skyline, a substation gone silent, sparks settling on wet asphalt.

Story arc: open on the city's light and hum — then omens: lamps flicker, signs stutter. Introduce her in fragments — silhouette, ribbons, hands, eyes — before ever revealing her full face. Escalate through the drain: she walks and darkness follows, she raises a bolt and commands the charge, she stands mid-street as every window behind her goes black in sequence. Resolve on one climactic frame: VOLTIA alone in an absolutely lightless city, facing camera, eyes burning yellow, magenta ribbons spiraling around her, her power the only light left in the world. Micro drift or slow push-in only within each beat; no fast cuts inside a shot; silence as a weapon.
```

<a id="reference-driven-case-20"></a>
<!-- Case 20: Cleopatra Chamber Confession (by @kinovi_ai) -->
### ケース 20: [クレオパトラの宮殿告白](https://x.com/kinovi_ai/status/2077432255157604598) (投稿者 [@kinovi_ai](https://x.com/kinovi_ai))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-20"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2077432255157604598.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
3⃣

This is the final step, the Seedance2 prompt! Use the entire prompt below and you can alter it to your liking! Use the image you generated as the first frame be @Image1  . Be sure to upload the character sheet as
@Image2 and @Image3 .

"The first frame begins at @image1 .  VISUALS:

Scene 1: Classic 90s 2D hand-drawn animation style, set within the lavish interior of the royal barge. Cleopatra @image2  lounges gracefully on a plush, teal-blue velvet chaise longue. She is leaning softly against a massive, sand-colored stone column adorned with highly stylized, painted Egyptian lotus flower motifs. Behind her, rich, sweeping purple silk curtains are tied back with golden ropes, revealing warm, painterly walls etched with ancient hieroglyphs. She is dressed immaculately in a flowing, form-fitting white gown accented with translucent, sheer blue fabric that cascades beautifully over her arms. She wears heavy gold hoop earrings, a magnificent gold and lapis lazuli jeweled collar, and a gleaming golden cobra crown resting atop her sleek, chin-length black hair. Her posture is utterly relaxed yet completely commanding. She tilts her head back slightly, her striking face and heavy, purple-shadowed eyes turning toward the camera with a look of supreme confidence, aloofness, and undeniable, magnetic allure.

Scene 2: Cut to a medium-wide shot of Mark Antony @image3 standing near the entryway of the pavilion, his broad, heroic frame backlit by the warm, golden-hour Egyptian sunlight filtering in from the river. His deep red Roman cape drapes elegantly over his meticulously detailed, golden chest armor and white pleated tunic. He crosses his muscular, leather-braced arms over his chest. A confident, highly charming, and slightly arrogant smirk spreads across his face. One thick, dark eyebrow raises in a classic, perfectly animated expression of intrigued amusement as he takes in the sight of the Egyptian queen.

Scene 3: Close-up on Cleopatra. With a slow, deliberate, and buttery-smooth 2D animation cycle, she reaches toward a golden platter resting on a small table beside her. Her delicate, manicured fingers pluck a single, vibrant purple grape. She holds it up to the light, twirling it playfully, her large, expressive anime-influenced eyes sparkling with sharp intelligence and mischievous intent. She offers a soft, highly theatrical animated smile, her flawless, cel-shaded features glowing warmly in the ambient light.

Scene 4: Dynamic two-shot. Antony closes the distance between them with slow, purposeful, swaggering steps. The animation captures the weight and power of his movement. He stops beside her chaise and leans forward, resting one sturdy hand lightly on the carved wooden edge of her seat. The framing emphasizes the dynamic tension and chemistry between their contrasting designs—the rigid, metallic structure of the Roman general against the soft, flowing elegance of the Egyptian queen. Cleopatra looks up at him from beneath her dark lashes, her gaze coy and challenging, tilting her chin up to meet his eyes.

Scene 5: Tight, intensely romantic close-up, the quintessential 90s animation "chemistry" shot. The camera slowly pushes in as their faces draw closer. Antony’s initial arrogant smirk softens into a genuine, deeply captivated, and breathless smile, his dark eyes completely lost in hers. Cleopatra’s expression shifts from playful teasing to genuine, mutual fascination. The lighting design shifts to cast a soft, magical, and romantic glow across their faces, perfectly highlighting the intricate cel-shaded shadows. A gentle, perfectly animated breeze sweeps through the pavilion, lightly tossing Antony's wavy dark hair and lifting the sheer blue fabric of Cleopatra's dress in a graceful, sweeping motion.

AUDIO & DIALOGUE:

The sweeping, grand orchestral score from the previous scene seamlessly transitions into a playful, seductive, and rhythmic melody. Plucked pizzicato strings, a sultry, winding oboe, and the gentle, rhythmic chime of a tambourine create a classic, sophisticated animated "flirtation" motif.

Scene 1 SFX: The soft, luxurious rustling of heavy silk and sheer fabrics sliding against velvet. The subtle, distant, and peaceful lapping of the Nile river water against the wooden hull of the barge.

Scene 2 SFX: The heavy, metallic creak of leather straps and the soft clink of gold armor as Mark Antony shifts his weight, emphasizing his imposing physical presence.

Cleopatra (Voice incredibly smooth, rich, and dripping with playful, aristocratic sarcasm): "Tell me, General... do all Romans march onto foreign vessels looking quite so... dramatically brooding?"

Scene 4 SFX: The heavy, purposeful thud of Antony's leather sandals stepping onto the richly woven carpets, followed by the soft sound of his hand gripping the wood of the chaise.

Mark Antony (Voice deep, confident, and smooth, laced with a warm, rumbling chuckle): "Your Highness. I must admit, the reports of Egypt's treasures were severely understated."

Scene 5 SFX: A soft, melodic, and incredibly charming animated giggle from Cleopatra, syncing perfectly with the music as the string section swells into a lush, romantic, and soaring crescendo, holding on a beautiful, sustained chord as the scene gently fades."
```

<a id="reference-driven-case-21"></a>
<!-- Case 21: Rainy Reunion Under Lantern (by @umesh_ai) -->
### ケース 21: [街灯の下の雨の再会](https://x.com/umesh_ai/status/2077419339264016619) (投稿者 [@umesh_ai](https://x.com/umesh_ai))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=reference-driven-case-21"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2077419339264016619.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Prompt : Use the uploaded image as the exact visual reference: a peaceful forest clearing during steady evening rain, with a huge leafy tree, deep green cushioned bench, small wooden side table, wet grass, reflective puddles, drifting mist, and a vintage streetlamp casting warm golden light.

Create a gentle 15-second cinematic story featuring two old friends meeting after several years. Élodie, a quiet French landscape painter in a cream raincoat, sits on the bench with a closed sketchbook. Matteo, an Italian nature writer wearing an olive jacket, walks slowly through the rain carrying two cups of tea. Keep their faces, clothing, and appearance consistent throughout.

Scene 1: Wide aerial glide through rain-covered branches, gradually revealing the immense tree, glowing lamp, bench, and emerald clearing.

Scene 2: Ground-level macro shot moving through wet grass, tiny flowers, falling droplets, rippling puddles, and golden reflections.

Scene 3: Long side shot of Matteo walking toward the bench while Élodie watches quietly beneath the tree.

Matteo smiles: “Still painting the rain?”

Élodie replies softly: “Still trying.”

Scene 4: Close-up of Matteo placing the steaming cups on the table as Élodie opens her sketchbook.

Scene 5: Slow orbit around them sitting together, watching the mist drift through the clearing.

Scene 6: Distant pullback across a reflective puddle, framing them beneath the enormous tree as they quietly share tea and savour the rain.
```


<a id="surreal-vfx"></a>
## 🌀 シュール / VFX

<a id="surreal-vfx-case-1"></a>
<!-- Case 1: Zero-Gravity Katana Combat (by @MiraMusic_AI) -->
### ケース 1: [無重力の刀剣戦](https://x.com/MiraMusic_AI/status/2040584525781364874) (投稿者 [@MiraMusic_AI](https://x.com/MiraMusic_AI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-1"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/013.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Seedance 2.0

Zero-gravity combat scene.
If you also reference music, it can follow the beat surprisingly well.

prompt:

A continuous 15-second single-shot action sequence with no cuts or transitions.

Japanese-inspired anime action aesthetics, featuring a cool-toned palette of icy whites and soft blue illumination, with fragments drifting weightlessly in space. Dynamic movement, cinematic framing, and a dramatic atmosphere.

Scene:
A pristine, ethereal white environment where gravity has collapsed. The space feels surreal and dreamlike, filled with soft glowing light and floating debris suspended in midair, creating an otherworldly cinematic mood.

0-3s -- rising tension
The camera glides slowly through the space.
A lone character floats calmly, poised with a katana.

3-6s -- sudden motion
Opponents propel themselves off surfaces, closing in from multiple directions in zero gravity.

6-10s -- fluid combat
Movement unfolds in all directions.
She rotates gracefully midair, delivering precise, flowing strikes.
The camera follows her in a smooth, tumbling motion.

10-13s -- acceleration
She catches a surface briefly, then launches forward with force.
A rapid sequence of strikes disperses the surrounding opponents.

13-15s -- stillness
Figures drift slowly in silence.
She regains balance, floating motionless as the scene holds on a final frame.
```

<a id="surreal-vfx-case-2"></a>
<!-- Case 2: Whale in the Clouds Surreal Epic (by @chaosdotjpg) -->
### ケース 2: [雲を泳ぐクジラのシュールな叙事詩](https://x.com/chaosdotjpg/status/2040203827249398086) (投稿者 [@chaosdotjpg](https://x.com/chaosdotjpg))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-2"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/051.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Whale in the Clouds — A cinematic surreal epic short film, ultra-realistic magical realism. Late afternoon, a coastal city. Warm sunlight, sea mist swirling, towering cumulus clouds. Everything is calm… until the sky suddenly grows heavy.
Aerial shot: skyline,
```

<a id="surreal-vfx-case-3"></a>
<!-- Case 3: Abyss Diver Sea Creature Metamorphosis (by @AIARTGALLARY) -->
### ケース 3: [深海ダイバーが海洋生物へ変貌](https://x.com/AIARTGALLARY/status/2039964736419479576) (投稿者 [@AIARTGALLARY](https://x.com/AIARTGALLARY))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-3"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/082.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A diver floats motionless in pitch-black ocean depth, a single beam of light cutting through the dark. Bioluminescent veins begin threading across their body in accelerated time, skin shifting to iridescent obsidian scales, limbs fusing into massive finned appendages. The figure swells to monstrous proportions, displacing water in shockwave pulses. Final shot: a colossal sea creature dissolving into the abyss. WETA-level underwater VFX, deep teal and void-black tones.
```

<a id="surreal-vfx-case-4"></a>
<!-- Case 4: Interdimensional Megacity Rift Collapse (by @LudovicCreator) -->
### ケース 4: [異次元メガシティの裂け目崩壊](https://x.com/LudovicCreator/status/2039768597241725132) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/092.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A towering humanoid entity made of shifting translucent geometry appears above a megacity skyline, its body composed of overlapping dimensional planes reflecting alternate realities — hook at second two: the entity opens both hands and a vertical dimensional tear slices through the city.

Reality splits.

Two versions of the city begin occupying the same space.

Buildings phase through each other as competing timelines collide.

The destruction is dimensional and structural: streets fold into mirrored corridors, cars fall sideways into parallel gravity planes, and skyscrapers fragment into geometric shards as their alternate versions misalign.

Every movement of the entity widens the rift.

Entire districts slide into adjacent dimensions.

The gauntlet unfolds through a skyline progressively divided between worlds: street level where pedestrians phase between realities → mid-rise districts where buildings overlap in transparent duplicates → rooftop where entire towers rotate into perpendicular universes.

Aircraft vanish into dimensional folds.

Bridges twist into impossible angles.

Chase-cam flying through intersecting city layers as gravity shifts between realities.

Velocity ramp when the dimensional rift expands wide enough to swallow an entire city block.

Cut to aerial: the megacity now exists as two overlapping worlds drifting apart.

The dimensional entity stands between them.

Diegetic prismatic dimensional light reflecting through fractured architecture and overlapping skylines, cinematic multiverse distortion effects, particle fragments of shattered reality, 4K.
```

<a id="surreal-vfx-case-5"></a>
<!-- Case 5: Rainy Underground Alley Merge (by @Dheepanratnam) -->
### ケース 5: [雨の地下路地での融合](https://x.com/Dheepanratnam/status/2039796932562838010) (投稿者 [@Dheepanratnam](https://x.com/Dheepanratnam))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-5"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/096.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Rainy Underground Alley Merge
15-second surreal horror in a narrow rainy underground service alley, neon signs reflecting on puddles, steam rising from grates. 
[0-1.5s] Shot 1: Wide tracking shot, young woman in black leather jacket walks cautiously through rain, breath visible,
```

<a id="surreal-vfx-case-6"></a>
<!-- Case 6: Quantum Reality Fracture Street Rift (by @Dheepanratnam) -->
### ケース 6: [量子現実の破砕による街路の裂け目](https://x.com/Dheepanratnam/status/2039651240909435242) (投稿者 [@Dheepanratnam](https://x.com/Dheepanratnam))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-6"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/097.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Video prompt

Quantum Reality Fracture on City Street (Interdimensional Rift VFX)

Cinematic 15-second high-budget sci-fi horror sequence on a rain-slicked downtown city street at blue hour, towering skyscrapers and frozen traffic, epic scale 

[0-1.5s] Shot 1: Epic wide crane
```

<a id="surreal-vfx-case-7"></a>
<!-- Case 7: the eye suddenly opens (by @roco_kn_roco) -->
### ケース 7: [目が突然開く](https://x.com/roco_kn_roco/status/2039323186127630710) (投稿者 [@roco_kn_roco](https://x.com/roco_kn_roco))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-7"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/106.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
cinematic anime close-up shot of a character's eye, extreme macro, eyelashes and skin texture visible, soft breathing motion, eye slowly closing, calm and silent atmosphere, subtle ambient light reflection on eyelid

the eye is fully closed, slight twitch, micro camera push-in, tension building, no effects yet, natural realism

the eye suddenly opens

inside the iris: completely unknown abstract pattern, non-human geometry, fractal layers, asymmetric rotating structures, liquid-metal texture mixed with glowing particles, colors shifting between deep violet, cyan, and iridescent hues

energy distortion spreads from the pupil outward, like reality bending, subtle glitch + fluid simulation fusion (not digital glitch, more organic distortion), light leaking from inside the eye

thin energy veins extend across the sclera (white of the eye), faint luminescent cracks

camera continues slow push-in, reflections in the eye show impossible space (like another dimension or abstract void)

ultra detailed anime style, cinematic lighting, high contrast, no cartoon exaggeration, elegant and mysterious, no text
```

<a id="surreal-vfx-case-8"></a>
<!-- Case 8: They clash mid-air above a floating lava river (by @LudovicCreator) -->
### ケース 8: [浮遊する溶岩川の上空で激突](https://x.com/LudovicCreator/status/2039258991809773666) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-8"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/116.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A surreal volcanic sky realm where islands of black rock float above rivers of molten lava flowing through the air like suspended waterfalls. The sky burns with deep crimson clouds illuminated by lightning storms.

**Action:**

15.0s sequence. A blazing phoenix composed of flowing flame and glowing embers spirals upward through the volcanic sky. Opposing it is a massive storm griffin whose wings generate violent wind currents and lightning arcs.

They clash mid-air above a floating lava river. The phoenix dives through the griffin’s storm vortex while fire and lightning collide violently.

Velocity Ramp choreography: a lightning claw strike freezes in ultra-slow motion as sparks and embers scatter through the air before snapping back to real time as both creatures spiral downward.

**Camera:**

Fast aerial tracking through lava-lit clouds, briefly passing behind a floating rock formation before revealing the full aerial duel.

**Style & Constraints:**

Photorealistic fire simulation, volumetric storm clouds, ray-traced lava glow, cinematic lightning illumination, stable geometry, 8K.
```

<a id="surreal-vfx-case-9"></a>
<!-- Case 9: Creative Director Dimension Walk (by @lukasersil) -->
### ケース 9: [クリエイティブディレクターの次元歩行](https://x.com/lukasersil/status/2045070342553493833) (投稿者 [@lukasersil](https://x.com/lukasersil))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-9"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/KmTYi8555NBQZpyJ.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
CHARACTER: attached image — confident creative director, late 30s, slim build,
short dark hair, natural wide smile; walks with calm executive energy;
outfit morphs each jump to reflect the creative era
CAMERA: frontal tracking, eye-level, full-body, dolly backward with character,
never cuts away from him
COLOR GRADE: B&W flicker → warm gold → smoke grey → neon saturation →
VHS bleed → CRT glow → ring-light pop → hypersaturated chaos →
prompt-blue ambient → holographic cyan → code-green rain → pure white
TRIGGER: finger snap mid-stride → instant dimension jump
RULE: Era-appropriate outfit with each jump. Steady calm walk throughout — pace never changes, never runs, never slows.

JUMP_MODE: creative dimension hopping
SEQUENCE:
START: white photography infinity studio, already mid-stride, looks directly into camera — casual snap → trigger
1: 1920s silent film set — B&W grain, frozen actors around him, film reel flicker → trigger
2: baroque theater stage — candlelit gold, velvet curtains, powdered wig extras scatter → trigger
3: 1960s Madison Avenue agency — cigarette haze, Helvetica posters, typewriters clacking → trigger
4: 1970s disco inferno — mirror ball overhead, polyester crowd parts, bass in the air → trigger
5: 1980s MTV studio — neon grid floor, fog machines, VHS glitch at frame edges → trigger
6: 1990s startup office — CRT glow, dial-up chaos, developers spin in chairs → trigger
7: 2010s YouTube studio — ring light forest, green screens, vlogger mid-take loses his mind → trigger
8: TikTok hyperreality — split screens multiply, emoji swarm, comments scroll the air → trigger
9: AI generation space — prompt text rains vertically, landscapes bloom and dissolve around him → trigger
10: holographic metaverse — glitching NPC crowds, architecture stutters, reality framerate drops → trigger
11: data singularity — code waterfall, neurons fire, his outline becomes wireframe → trigger
12: white void — silence, only footstep echo, wide smile, still walking forward

FINAL: one last snap → seamless loop back to white studio, identical opening shot
```

<a id="surreal-vfx-case-10"></a>
<!-- Case 10: Abyssal Entity Altar Inscription — Dark Fantasy (by @Adam38363368936) -->
### ケース 10: [深淵の存在を刻む祭壇碑文 — ダークファンタジー](https://x.com/Adam38363368936/status/2041050710721339521) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-10"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041050710721339521.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
提示词 (Prompt)： 0-3s · 异界铭刻 低角度仰拍。深渊实体右手嵌入（Embedded）祭坛，暗黑脉络呈分形几何状（Fractal Geometry）在石板上疯狂寄生。裂缝喷涌出粘稠血肉触须，地面如肺部般大幅度搏动。背景宗门古建筑随之发生视觉上的横向位移震颤。 3-6s · 骨质畸变 环绕升降镜头。实体的脊椎如连锁反应般炸裂扭曲，黑曜石角冠从颅骨深处穿出。双臂缠绕液态黑烟，所经之处空气产生高温电弧感，悬挂灯笼因能量过载瞬间发生视觉坍塌式爆裂。 6-9s · 物质解构 拉远镜头。实体表皮呈现瓷器般的碎裂纹路，内部是蠕动的暗物质核心。指尖异化为长达半米的影刃，触碰木柱瞬间引发超速风化（Accelerated Decay），建筑结构化为黑烟升腾。 9-12s · 影潮吞噬 高空俯拍。实体振臂，身后黑暗塌缩后猛然爆发，形成千米级的黑红浪潮（Corrupted Tsunami）。阴影洪流所过之处，青石板路、石狮、楼阁全部被像素化撕裂并吞噬。 12-15s · 虚空终焉 脸部特写。背景中巨大的山门在黑洞引力下向中心拧麻花状折断。实体在死寂中缓步走近，瞳孔内是旋转的星云（Void Nebula）。它凝视镜头，画面产生强烈的胶片烧灼感与信号故障感（Glitch），最终归于绝对黑暗。
```

<a id="surreal-vfx-case-11"></a>
<!-- Case 11: Floating UI Color Wheel Scene Transformation (by @johnAGI168) -->
### ケース 11: [浮遊 UI カラーホイールによる場面変換](https://x.com/johnAGI168/status/2041001869435158629) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-11"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041001869435158629.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
即可得到同款视频！

Seedance 2.0 prompt 👇

生成一段15秒的高质量实拍风格特效短片，核心展示一位年轻女性通过滑动悬浮UI色环，实现场景与服装的无缝丝滑切换。注意分镜编排与转场节奏，画面需具备极佳的景深效果（Depth of field），人物面部始终保持清晰且光影立体。 【人物特征锁定】 全程锁定核心人物特征：年轻女性，标志性的金黄色短发，佩戴圆形金属边框眼镜。 【分镜与动作设计】 00:00-00:05：室内卧室夜景，背景有暖黄色的星星形状散景氛围灯串。人物头发微微扎起，穿浅米色长袖家居睡衣坐在床上。画面正前方悬浮着完整的半透明渐变彩色色环（UI交互元素）。人物微笑着看向镜头，伸出手自然地触碰并向右滑动发光的色环。 00:05-00:07：随着色环转动，无缝转场至明亮的室内窗边日景，阳光温暖。人物短发自然散落，瞬间换上鲜艳的亮橙色无袖紧身上衣和白色休闲裤，单手托腮，笑容灿烂。色环悬浮在画面右侧，光标高亮显示黄橙色区域。 00:07-00:09：无缝转场至户外公园日景，背景是高曝光的明亮绿树。人物靠在粗壮树干旁，换上薄荷绿色方领泡泡袖露脐短上衣和浅色高腰短裤，右手戴黑色半截皮手套，对着镜头俏皮眨眼，手指轻触嘴唇。色环悬浮右侧，光标高亮亮绿色。 00:09-00:11：无缝转场至户外开阔草地，背景蓝天白云。人物靠在灰白水泥矮墙上，穿简约深蓝紫色细吊带上衣，单手托下巴，表情慵懒清冷。色环移至画面左侧，光标高亮深紫色。 00:11-00:13：无缝转场至阳光明媚的户外樱花林，背景满是盛开的粉色樱花。人物换粉色细吊带上衣，单手轻轻撩动头顶头发，展现甜美治愈微笑。色环悬浮左侧，光标高亮粉红色。 00:13-00:15：无缝转场至户外传统中式建筑前，背景有虚化的红色柱子和古建飞檐。人物穿深红色偏焦糖色的露肩改良版中式旗袍上衣（带传统盘扣），姿态端庄优雅，单手放于锁骨处，眼神微垂看向镜头。色环悬浮左侧，光标高亮红色。 【特殊控制指令】 必须保证场景与服装的每次切换平滑无跳切感（丝滑转场），保持人物动作的延续性。每次切换时，人物的情绪微表情必须与当前的服装色彩氛围完美契合。配合画面色彩切换，可自动生成带有轻巧科技感UI音效及动感节奏的BGM。
```

<a id="surreal-vfx-case-12"></a>
<!-- Case 12: Fire Empress Transformation Sequence (by @LudovicCreator) -->
### ケース 12: [炎の女帝の変身シーケンス](https://x.com/LudovicCreator/status/2076365999100616875) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-12"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2076365999100616875.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Full magical transformation sequence: a fire empress suspended in an abstract volcanic void as ribbons of molten orange light orbit and wrap around her hair lifting like flame, black-and-gold armor forming in glowing ember panels, lava cracks igniting across the floor as a sun sigil blooms underfoot  the camera orbiting opposite the ribbons’ spin, each beat synced to a rising heroic chord, ending in a powerful hand-forward signature pose held against a blazing starburst. Stock-footage grandeur, played sincere.
```

<a id="surreal-vfx-case-13"></a>
<!-- Case 13: Sand Titan Desert Transformation (by @LudovicCreator) -->
### ケース 13: [砂の巨人への砂漠変身](https://x.com/LudovicCreator/status/2076970003404865992) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-13"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2076970003404865992.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second ultra-cinematic elemental transformation sequence in an endless desert during a colossal sandstorm at sunset.

A lone desert wanderer stands atop a towering dune beneath a crimson-orange sky. Powerful winds drive endless waves of sand across the landscape while ancient ruined temples emerge and disappear through the storm.

The atmosphere is vast, ancient, and awe-inspiring.

The camera slowly circles around the wanderer as the desert suddenly falls unnaturally silent. The wind stops for a single moment.

Then the sand begins moving.

Tiny grains rise from the dunes and spiral around the figure in elegant vortexes. The ground beneath their feet fractures as ancient symbols briefly emerge from beneath the desert.

The transformation begins.

Golden sandstone patterns spread across the skin. The body becomes increasingly mineral, muscles turning into sculpted layers of weathered stone while streams of flowing sand circulate beneath the surface like living veins.

The camera pushes closer as fingers become enormous sandstone claws. Cracks appear across the body, glowing softly with golden desert light while fine sand continuously pours through them.

The transformation accelerates.

The body grows dramatically larger with every heartbeat. Massive shoulders form from layered rock and compacted dunes. Flowing sand replaces hair, continuously blowing in the wind like an endless desert storm.

Entire dunes collapse and rise around the transformation. Ancient pillars, broken statues, and fragments of forgotten civilizations become embedded within the giant's body as if the desert itself is rebuilding an ancient guardian.

The surrounding sandstorm intensifies into a colossal rotating vortex. Lightning flashes inside the dust clouds while gigantic walls of sand spiral around the growing titan.

At the climax, the wanderer becomes an immense Sand Titan towering above the desert. The body is formed from sandstone, flowing dunes, ancient ruins, and living rivers of sand. Every movement releases avalanches cascading from its colossal limbs.

Final cinematic moment: the Sand Titan raises one enormous arm. The entire desert responds as gigantic dunes rise like ocean waves, creating a continent-sized sandstorm beneath a blazing sunset while the camera pulls back to reveal the titan dominating the endless horizon.

Style: ultra cinematic elemental realism, photoreal sand simulation, realistic sandstone formation, colossal environmental scale, desert storm physics, volumetric dust, ancient civilization aesthetic, monumental cinematography, AAA visual effects quality, no text, no overlays.

Audio: epic cinematic orchestral score, deep desert winds, shifting dunes, rock cracking, cascading sand, distant thunder within the sandstorm, ancient low-frequency resonance, massive elemental power.
```

<a id="surreal-vfx-case-14"></a>
<!-- Case 14: Escape Car Garbage Morph (by @LavrionX) -->
### ケース 14: [逃走車のごみ収集車変形](https://x.com/LavrionX/status/2077500080932671639) (投稿者 [@LavrionX](https://x.com/LavrionX))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=surreal-vfx-case-14"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2077500080932671639.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A hyper-real cinematic action sequence on a bright urban road in daytime. Clean streets, light traffic, buildings on either side. Sound design: distant sirens approaching, sharp metallic impacts, city ambience.

The video opens with a tight close-up of a sleek, angular metallic vehicle (Tesla-like design). Sudden gunfire—bullets hit the surface and ricochet cleanly, sparking off the body with sharp metallic pings. No visible shooters, only the sound of chaos and pursuit building.

Camera quickly pulls back to reveal the full car speeding forward.

Loud police sirens grow closer.

Without slowing down, the vehicle begins transforming—its clean metallic panels shift, split, and reconfigure. The smooth exterior degrades into a rough, boxy structure. Angles soften. Surfaces become dented, rusted, uneven.

Within seconds, the futuristic car becomes a grimy dumpster-style garbage truck, perfectly blending into the environment.

The vehicle immediately hard brakes and performs a sharp 180-degree skid turn, tires screeching, dust kicking up. It settles seamlessly into a roadside parking position like it belongs there.

Cut.

Police vehicles rush past the same road at high speed, sirens blaring, continuing the chase forward—completely missing it.

Foreground: a woman casually loading garbage into the back of the truck. She has braided hair, tattooed arms, long manicured nails, dressed like a regular worker but with subtle attitude.

She pauses, watches the police pass… then slowly turns toward camera and winks.

Ambient city sound returns. No hard cut.
```


<a id="templates-structured"></a>
## 📐 テンプレートと構造化形式

<a id="templates-structured-case-1"></a>
<!-- Case 1: Supercarrier Catastrophic Sinking (by @johnAGI168) -->
### ケース 1: [超大型空母の壊滅的沈没](https://x.com/johnAGI168/status/2040432247094870343) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-1"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/016.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
How does it look?

Seedance 2.0 text-to-video prompt below:

{"lang":"en","prompt":"Style and atmosphere: apocalyptic naval destruction, with low-saturation steel blue and gunmetal gray as the primary palette. Amber explosions and aviation-fuel flames tear through the gray field. Towering storm cumulonimbus clouds are lit from within by lightning. Rain lines cut across every surface. Telephoto compression layers destruction on top of destruction. Live-action brutal aesthetics--no clean CG gloss, only grit, weight, and mass. Motion description: an extreme long aerial drone pullback shows a supercarrier catastrophically listing to port in monstrous waves, with the flight deck tilted beyond forty-five degrees and seawater washing across it as a white sheet of surf. Three fighter jets break free of their tie-down chains at the same time, sliding sideways across the slick steel deck. Their landing gear scrapes metal and throws long chains of sparks, and the first jet flips over the deck edge into the churning gray sea. Hard cut to a handheld medium low-angle shot from water level looking upward--the carrier's hull towers overhead like a collapsing skyscraper. Barnacle-covered steel plates groan and bend, rivets eject one after another like automatic gunfire, and a structural crack splits open from the middle of the hull, with shockwaves rippling across the metal skin. Seawater pours through the widening rupture. Cut to a stable circling wide tracking shot--the carrier breaks in two at the fracture point, the bow plunging forward into a giant swell while the stern rises toward the sky, exposing propellers still spinning in the air. Tons of seawater cascade off the lifted stern like a cluster of waterfalls. Aviation fuel ignites on the sea surface--flames spread outward in a widening ring across the water, and twisted black smoke columns rise into the storm. An abnormal twenty-meter wave surges in from the left side of frame and slams head-on into the tilting bow. White spray explodes sixty meters into the air and swallows the entire forward structure. Static description: catastrophic structural failure of a Nimitz-class supercarrier. North Atlantic storm conditions--fifteen-meter swells, horizontal rain, and sixty-knot winds blowing the wave crests into mist. Thundercloud base at three hundred meters with internal lightning illumination. The flight deck is littered with loose aircraft, broken tie-down chains, and seawater. The hull is split open at the center, exposing interior deck layers. Aviation fuel burns on the sea surface. An abnormal giant wave approaches from port."}
```

<a id="templates-structured-case-2"></a>
<!-- Case 2: Reconstruction of Memory Shards (by @TechTalkNAVI) -->
### ケース 2: [記憶の断片を再構築](https://x.com/TechTalkNAVI/status/2040327899606306840) (投稿者 [@TechTalkNAVI](https://x.com/TechTalkNAVI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-2"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/018.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
{
 "effect_id": "ethereal_02",
 "title": "Reconstruction of Memory Shards",
 "visual_style": "Abstract Cinematic / Art Installation",
 "duration": "10s",
 "prompt": "A mesmerizing slow-motion shot of thousands of irregularly shaped crystal shards suspended in a void. Each shard acts as a perfect miniature prism, reflecting a different hyper-realistic sunset or starry night inside it. As if pulled by an unseen force, they begin to drift toward a central point, forming a perfect sphere. When they touch, they do not collide but merge seamlessly like liquid glass. The sphere ignites into a blindingly beautiful, soft internal pulse of pure white light, casting fractal patterns of light and shadow everywhere. Photorealistic glass rendering, intense reflection and refraction simulation, poetic atmosphere.",
 "vfx_technical_details": {
  "glass_shader": "Sub-surface scattering with complex refraction and dispersion (Abbe numbers).",
  "particle_attractor": "Force-field-based particle convergence with smooth merging simulation.",
  "lighting": "Dynamic HDR environment mapping inside each shard, with a strong internal light source upon merge."
 }
}

#capcutgenai
#capcutjapandiscord
#CapCutSeedance2
```

<a id="templates-structured-case-3"></a>
<!-- Case 3: Blueprint to Reality – Single-Story House Transformation (by @craftian_keskin) -->
### ケース 3: [設計図から現実へ — 平屋住宅の変形](https://x.com/craftian_keskin/status/2039053365666037902) (投稿者 [@craftian_keskin](https://x.com/craftian_keskin))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-3"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/024.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
{
 "video_prompt": {
 "duration": "15 seconds",
 "title": "Blueprint to Reality – Single-Story House Transformation",
 "style": "Architectural visualization, photoreal, modern farmhouse exterior, clean cinematic motion",

 "blueprint_reference": {
 "floors": 1,
 "footprint_shape": "Irregular L-plus-T shape",
 "layout_zones": {
 "top_left": "Master bedroom with large en-suite (double vanity, bathtub, shower, toilet)",
 "top_center": "Open lounge / sitting area with plants",
 "top_right": "Secondary bedroom + full bathroom",
 "center_left": "Walk-in closet / laundry adjacent to master bath",
 "center": "Open-plan kitchen with island, connected to dining room",
 "center_right": "Family room / playroom with colorful seating",
 "right": "Covered outdoor terrace / patio (open to sky)",
 "bottom_center": "Entry foyer leading to interior",
 "bottom_left": "Double attached garage (2-car, open indoor space, roofed)",
 "bottom_right_upper": "Bedroom 3 with shared bathroom",
 "bottom_right_lower": "Bedroom 4 with small private patio (open to sky)",
 "bottom_right_corner": "Small outdoor lounge / garden corner (open to sky)"
 }
 },

 "roof_rules": {
 "all_interior_rooms": "Fully covered with roof — master bedroom, all secondary bedrooms, bathrooms, kitchen, dining, family room, lounge, garage, foyer, hallways",
 "outdoor_spaces": "Open to sky — right-side terrace, bottom-right small patio, garden corner",
 "garage": "Roofed as part of main structure, no skylight"
 },

 "exterior_style_reference": {
 "roof_type": "Standing seam dark charcoal / black metal roof, low-to-mid pitch",
 "facade": "Light beige / warm white board-and-batten vertical siding",
 "trim": "Dark brown / black window frames and fascia",
 "garage_door": "Dark modern panel garage door, double-wide",
 "covered_porch": "Covered front entry and right-side patio with exposed wood beam columns",
 "windows": "Large black-framed rectangular windows matching each room's position"
 },

 "sequence": [
 {
 "time": "0:00–0:02",
 "action": "Clean white background. Crisp 2D top-down colored floor plan appears — exact layout with all rooms labeled, walls in bold black, rooms color-coded in warm wood tones and blue for bathrooms, gray for garage."
 },
 {
 "time": "0:02–0:05",
 "action": "Camera slowly pulls back. Floor plan glows softly. Thin white grid lines appear beneath the plan, establishing ground plane. Room walls begin to gently pulse, ready to rise."
 },
 {
 "time": "0:05–0:09",
 "action": "Walls begin extruding upward from the 2D plan — all interior walls rise simultaneously, preserving exact footprint. Garage walls, bedroom walls, k
```

<a id="templates-structured-case-4"></a>
<!-- Case 4: Martial-Arts Haute Couture Tailor (by @Adam38363368936) -->
### ケース 4: [武術オートクチュールの仕立て屋](https://x.com/Adam38363368936/status/2037359552849666514) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/027.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
SUBJECTS:
Character: a female haute couture tailor with an extremely lean build, arm muscles taut like steel wire, and eyes as cold and sharp as needles.
Wardrobe: a dark tactical vest incorporating qipao elements, bare arms, forearms wrapped with dark red silk bracers to increase friction, long slender fingers with metallic fingertip guards.
Movement style: a fusion of Wing Chun's short explosive power and Tai Chi's circular flow. The movement follows the rhythm of charge -> explosive strike -> instant stillness, emphasizing finger burst power and the tension of silk in the air.

ENVIRONMENT:
A dim, luxurious private studio. The background is a full wall of redwood spool racks, where thousands of color blocks create geometric beauty. In the center stands a giant black marble cutting table with a mirror-like surface. Above it hangs a single focused industrial cold light. Tiny fiber particles float in the air.

MOOD:
Extremely focused, elegant, ceremonial, and deadly. Her movements are as precise as a surgeon's, creating a highly oppressive visual sensation.

TIMELINE:
0:00-0:02: close-up / wide-angle POV. The tailor braces both hands on the black marble table and lowers her head in complete stillness. The camera rushes in at extreme speed. She suddenly raises her head and locks eyes with the lens. Her right hand snatches through empty air and catches a bolt of dark purple heavy silk that slides across the tabletop like a serpent.

0:02-0:05: rapid edit / handheld feel. The tailor throws the silk into the air. She moves like an afterimage, holding long silver shears in her right hand, performing a blind cut the instant the silk begins to fall. This is not ordinary tailoring--each cut carries the force of a martial-arts strike. The shears slice the air with a sharp tearing sound, and the fabric edge is perfectly clean and undisturbed.

0:05-0:07: moving shot. She side-steps to the far end of the worktable. With a sweep of one hand, several steel needles leap up from a pin cushion and hover in midair. She pushes with internal force, and the needles shoot like hidden weapons into distant hanging garment patterns. The needle tails tremble with a metallic ring.

0:07-0:10: continuous shot. The tailor begins controlling thread. She pulls out a gold filament and wraps it through the gaps of her fingers, manipulating the silk like puppet strings so it folds and forms itself automatically in midair. Every finger flick crackles with spark-like static electricity. She slams the table with her elbow, making the presser foot bounce upward, and catches it instantly, locking it onto the fabric.

0:10-0:12: match cut. The tailor spins sharply in place, and the hem of her outer garment spreads like a circular formation. She brings both hands together and yanks the formed suit collar tight. The final gold thread draws a perfect arc in the air and stitches itself shut. The action cuts from extreme speed into extreme slow motion.

0:12-0:15: stable POV. Dust settles. She lifts the finished gown with one hand and snaps it open in front of the camera. The lens focuses on the exquisite embroidery at the collar. She flicks a button with her nail--the button vibrates. She then turns and walks into the shadows, leaving only her back as the frame is completely covered by an expensive perfume mist that rises and fades out cleanly.
```

<a id="templates-structured-case-5"></a>
<!-- Case 5: Beat-Synced Outfit Transition Template (by @aimikoda) -->
### ケース 5: [ビート同期の衣装切り替えテンプレート](https://x.com/aimikoda/status/2040200435986817039) (投稿者 [@aimikoda](https://x.com/aimikoda))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-5"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/053.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
FORMAT: 15s / 145 BPM / 15 SHOTS / beat-synced routine

SUBJECT: @[image1].
WARDROBE: Sleep tee and lounge shorts at home. Tailored jacket, fitted top, trousers, and lace-up shoes outside.
```

<a id="templates-structured-case-6"></a>
<!-- Case 6: Dancing Skyscraper District Template (by @TechTalkNAVI) -->
### ケース 6: [踊る超高層ビル街テンプレート](https://x.com/TechTalkNAVI/status/2039928267323658399) (投稿者 [@TechTalkNAVI](https://x.com/TechTalkNAVI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-6"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/062.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
{
 "location": "Nishi-Shinjuku Skyscraper District (near Tokyo Metropolitan Government Building)",
 "duration": "10s",
 "prompt": "A wide cinematic shot of the Tokyo Metropolitan Government Building at sunset. As a deep bass sound hits, the massive twin towers begin to stretch and compress vertically like an accordion in perfect rhythm. Despite the rubber-like stretching, the glass and concrete textures remain perfectly sharp and realistic. The surrounding skyscrapers join the movement, swaying and leaning toward the center as if the entire city is dancing to a hidden beat. Reflection on the windows shifts realistically with the deformation.",
 "vfx_focus": [
 "Non-rigid body deformation (Squash and Stretch)",
 "Real-time reflection mapping during mesh warp",
 "Atmospheric depth and sunset lighting"
 ]
}
```

<a id="templates-structured-case-7"></a>
<!-- Case 7: Starlight Shadow / Stardust Silhouette (by @TechTalkNAVI) -->
### ケース 7: [星明かりの影／星くずのシルエット](https://x.com/TechTalkNAVI/status/2039904725639037110) (投稿者 [@TechTalkNAVI](https://x.com/TechTalkNAVI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-7"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/063.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
{
 "scene_id": 4,
 "title": "Starlight Shadow / Stardust Silhouette",
 "duration": "10s",
 "visual_style": "Fantasy / High-End Commercial",
 "prompt": "A person walks by a clean white wall in a bright, sunlit gallery. Their shadow follows them, but then gracefully stops and starts performing a rhythmic, elegant dance. The shadow is made of soft, shimmering dark-blue particles. As the person reaches out to high-five the wall, the shadow hand gently emerges into the 3D world as a translucent, glowing crystalline form, meeting the person's hand with a soft trail of light.",
 "vfx_technical_details": {
 "camera_work": "Smooth, cinematic tracking shot with a focus on the interaction point.",
 "shadow_FX": "Particle-based shadow simulation with soft edges and internal luminescence.",
 "transition_FX": "Seamless 2D-to-3D transition using a translucent glass shader and light trail effects.",
 "lighting": "Bright, warm afternoon sunlight to contrast with the cool-toned magical shadow."
 },
 "key_elements": [
 "Independent dancing silhouette",
 "Shimmering particle effects",
 "Translucent crystalline 3D hand",
 "Magical and inspiring atmosphere"
 ]
}
```

<a id="templates-structured-case-8"></a>
<!-- Case 8: Painterly Parkour POV Template (by @0xbisc) -->
### ケース 8: [絵画風パルクール POV テンプレート](https://x.com/0xbisc/status/2040041171460968728) (投稿者 [@0xbisc](https://x.com/0xbisc))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-8"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/083.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
SUBJECTS:

Main Subject: A parkour expert in POV perspective, defined by visible arms, hands, forearms, shoe tips, lower knees, grips, hand placements, wall runs, precise landings, slides, landing cushioning, and weight shifts.

Style: Painterly 3D, stylized on real human anatomy
```

<a id="templates-structured-case-9"></a>
<!-- Case 9: 360 POV Downhill Stair Run Template (by @aimikoda) -->
### ケース 9: [360 度 POV 下り階段ラン・テンプレート](https://x.com/aimikoda/status/2039827756083540361) (投稿者 [@aimikoda](https://x.com/aimikoda))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-9"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/090.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
FORMAT: 15s / 180 BPM / ONE CONTINUOUS SHOT / 360 POV downhill stair run, viral energy, max chaos

SUBJECTS: First-person cyclist, handlebars and front wheel flashing low in frame during drops and hard turns. Vendors, laundry, scooters, dogs, chickens, cars, and
```

<a id="templates-structured-case-10"></a>
<!-- Case 10: Food and Character Motion Template (by @Just_sharon7) -->
### ケース 10: [食べ物とキャラクターの動きテンプレート](https://web.archive.org/web/*/https://x.com/Just_sharon7/status/2039725656393875580) (投稿者 [@Just_sharon7](https://x.com/Just_sharon7))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-10"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/094.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
{
 "prompt": "Cinematic, hyper-realistic or stylized 3D/2.5D rendering of food and characters, with strong motion and dynamic camera work. Vibrant, saturated color grading with warm food tones (reds, oranges, yellows) contrasted by dramatic shadows or neon accents. Sweeping pans, close-ups on textures, slow-motion impacts, quick cuts. High detail on food surfaces including glossy sauces, steam, crumbs, splashes, and expressive character faces. Short, loopable or 'wait-for-it' format with satisfying payoff. Ultra-realistic textures, volumetric lighting, film grain, cinematic composition.",
 "style": {
 "render_type": "3D/2.5D",
 "lighting": "volumetric, cinematic",
 "color_grading": "vibrant, warm tones with dramatic shadows",
 "camera": "dynamic, sweeping pans, close-ups, slow-motion, quick cuts",
 "detail": "hyper-realistic textures, high detail food surfaces, expressive faces",
 "format": "short, loopable, satisfying payoff"
 },
 "resolution": "2K",
 "aspect_ratio": "9:16",
 "stylize": 250,
 "version": "2.0"
}
```

<a id="templates-structured-case-11"></a>
<!-- Case 11: Impossible Camera Kitchen Rush Template (by @Dheepanratnam) -->
### ケース 11: [不可能カメラのキッチンダッシュ](https://x.com/Dheepanratnam/status/2039568902481387645) (投稿者 [@Dheepanratnam](https://x.com/Dheepanratnam))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-11"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/098.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
FORMAT: 15s / single continuous impossible camera move / no dialogue STYLE: High-end commercial kitchen during dinner rush, gleaming stainless steel, flying ingredients, photorealistic micro-to-macro cinematic 8K 

Shot 01 (0:00–2:00): Camera starts at floor level on anti-slip
```

<a id="templates-structured-case-12"></a>
<!-- Case 12: Time-Freeze POV Burst Template (by @CharaspowerAI) -->
### ケース 12: [時間停止 POV バースト](https://x.com/CharaspowerAI/status/2039704453784191201) (投稿者 [@CharaspowerAI](https://x.com/CharaspowerAI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-12"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/099.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
{
 "shot": {
 "composition": "POV time-freeze with hands moving through frozen environment",
 "lens": "ultra-wide cinematic lens with subtle distortion",
 "camera_movement": "slow walk, precise hand movements, sudden time release burst"
 },
 "subject": {
 "description": "person moving while everything else is frozen mid-action",
 "wardrobe": "hands visible",
 "props": "frozen people, objects mid-air, suspended debris"
 },
 "scene": {
 "location": "busy city street",
 "time_of_day": "day",
 "environment": "people frozen mid-motion, objects suspended in air"
 },
 "visual_details": {
 "action": "walk through frozen crowd, move objects, sudden time resumes explosively",
 "special_effects": "time freeze particles, motion snap release",
 "hair_clothing_motion": "fabric still then snapping with time"
 },
 "cinematography": {
 "lighting": "clean daylight with sharp shadows",
 "color_palette": "natural tones with crisp contrast",
 "tone": "mind-bending, cinematic"
 },
 "audio": {
 "music": "slow ambient then explosive drop",
 "ambient": "silence then sudden chaos",
 "sound_effects": "time snap, object movement",
 "mix_level": "contrast silence and burst"
 }
}
```

<a id="templates-structured-case-13"></a>
<!-- Case 13: Astronaut First Spacewalk Template (by @BrennanErbz) -->
### ケース 13: [宇宙飛行士の初船外活動テンプレート](https://x.com/BrennanErbz/status/2039579736301781215) (投稿者 [@BrennanErbz](https://x.com/BrennanErbz))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-13"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/100.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
FORMAT: 15s / handheld close + slow cuts / 5 beats / sci-fi drama — astronaut's first spacewalk, orbital silence SUBJECTS: An astronaut, 40s, in a white EVA suit with a gold-visored helmet, tethered to the exterior of a space station, performing the first moments of a spacewalk.
```

<a id="templates-structured-case-14"></a>
<!-- Case 14: Golden Retriever Routine Template (by @0xbisc) -->
### ケース 14: [ゴールデンレトリバーの日常テンプレート](https://x.com/0xbisc/status/2039673040787956123) (投稿者 [@0xbisc](https://x.com/0xbisc))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-14"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/104.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
SUBJECTS:
Subject 1: Adult male, Western casual everyday home and outing attire, short jacket, basic T-shirt, long pants, everyday shoes; lean build, natural and efficient movements.
Subject 2: Golden Retriever, large head, broad chest, thick, fluffy fur; overall short and round
```

<a id="templates-structured-case-15"></a>
<!-- Case 15: Stylized 3D Barbershop Transformation Sequence (by @ShamiWeb3) -->
### ケース 15: [スタイライズ 3D 理髪店変身シーケンス](https://x.com/ShamiWeb3/status/2039372124079669655) (投稿者 [@ShamiWeb3](https://x.com/ShamiWeb3))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-15"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/115.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
{
 "title": "Stylized 3D Barbershop Transformation Sequence",
 "style": "Stylized 3D animation with exaggerated cartoon proportions, cinematic martial-arts-inspired choreography, rhythmic musical energy, ultra-smooth motion, expressive physics",

 "characters": {
 "dr_eraser": {
 "description": "Lean, almost skeletal barber-scientist with long fingers and oversized glasses that slip down his nose. Wears a bright yellow lab coat filled with strange tools (mini vacuum, magnifying glass, combs, razors, quirky gadgets).",
 "movement_style": "step → pause → spin, precise, calm, orchestral control over chaos"
 },
 "patient_plush": {
 "description": "Huge, soft, teddy-bear-like client with wild messy hair, extremely long drooping beard, and a stained oversized sweater.",
 "emotion": "nervous, trembling, comically overwhelmed, eyes tracking every movement"
 }
 },

 "environment": {
 "location": "Whimsical cartoon barbershop",
 "details": "Oversized mirrors reflecting exaggerated motion, warm golden lighting, steam curling like soft clouds, gleaming tools, hair accumulating like fluffy clouds"
 },

 "mood": "Absurd precision vs comedic fear; controlled elegance vs chaotic nervous energy",

 "timeline": [
 {
 "time": "0:00-0:02",
 "shot": "Close-up",
 "action": "Patient Plush shown with wild hair and massive beard. Dr. Eraser dramatically pulls oversized scissors, spins them on finger, snaps toward camera. Coat flares like wings. Plush reacts in exaggerated shock."
 },
 {
 "time": "0:02-0:05",
 "shot": "Mirror medium shot",
 "action": "Scissors cut rhythmically. Hair falls like confetti. Glasses magnify strands. Beard and hair begin transforming. Plush grips chair, eyes dart nervously."
 },
 {
 "time": "0:05-0:08",
 "shot": "Tracking shot",
 "action": "Scissors disappear. A giant straight razor appears like a sword. Beard shaved in stylized strips. Foam bursts like fireworks. Plush closes eyes tightly."
 },
 {
 "time": "0:08-0:11",
 "shot": "Slow motion",
 "action": "Hot towel spins through air, lands perfectly, then removed in one sharp motion revealing smooth skin. Plush touches face in disbelief."
 },
 {
 "time": "0:11-0:13",
 "shot": "Styling sequence",
 "action": "Pomade applied with theatrical precision. Hair reshaped into shiny cartoon-perfect style. Talc brush creates glowing powder cloud."
 },
 {
 "time": "0:13-0:15",
 "shot": "Final reveal",
 "action": "Chair spins to mirror. Patient Plush fully transformed. He touches face in awe. Dr. Eraser stands behind, spins scissors once, snaps them shut, nods confidently."
 }
 ],
}
```

<a id="templates-structured-case-16"></a>
<!-- Case 16: Impressionist Rowing Hands Template (by @0xbisc) -->
### ケース 16: [印象派のボートをこぐ手テンプレート](https://x.com/0xbisc/status/2039332336643248317) (投稿者 [@0xbisc](https://x.com/0xbisc))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-16"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/122.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
SUBJECTS:
Subject 1: First-person perspective hands (rendered in Monet impressionist oil painting brushwork, soft skin tones with no hard edges; both hands continuously hold the oar and perform extremely slow and even rowing motions, with stretched rhythm and natural pauses)
```

<a id="templates-structured-case-17"></a>
<!-- Case 17: Female Warrior — Structured Subject Prompt (by @noman23761) -->
### ケース 17: [女戦士 — 構造化された被写体プロンプト](https://x.com/noman23761/status/2041406971484815564) (投稿者 [@noman23761](https://x.com/noman23761))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=templates-structured-case-17"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041406971484815564.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
"SUBJECTS: A female warrior with shoulder-length hair, the ends naturally flipping outward, pressed backward and slightly disheveled by air resistance during high-speed movement. She wears a dark, form-fitting tactical suit combining real fabric and worn metal elements, with visible water stains, dust, and signs of use. A dual mechanical grappling hook system mounted on her back, capable of firing steel cables that retract to generate pulling force. The hook tips are metal impact heads used for attaching to or striking solid structures. The cable only triggers when support is lost or during a fall, and must latch onto a solid object before generating tension. Movement relies on: sliding, stepping, grappling pull, swinging, contact, and displacement through reaction forces. A massive stone hand connected to a giant’s body (not severed, the arm extending upward into the clouds), descending vertically into frame from the cloud layer. Enormous in scale, with a weathered, rough surface, no glow, no regular structure. Each downward press carries clear weight, acceleration, air compression, and impact inertia. ENVIRONMENT: A high-altitude fractured bridge structure with wet, slippery concrete surfaces, showing water traces, cracks, and scattered debris. The bridge is heavily damaged, with irregular टूट sections, exposed and bent rebar, and hanging steel cables. Below the bridge is an empty abyss, swallowed by fog, with no visible ground. A distant city appears low and ruined, with r
```

<a id="general-cinematic"></a>

<a id="general-cinematic"></a>
## 🎬 一般シネマティック

<a id="general-cinematic-case-1"></a>
<!-- Case 1: High-Heel Beat Sync Fashion Close-Up (by @TingFengAIAI) -->
### ケース 1: [ハイヒールとビートが同期するファッション接写](https://x.com/TingFengAIAI/status/2038904225548149011) (投稿者 [@TingFengAIAI](https://x.com/TingFengAIAI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-1"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/002.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Beauty beat-sync sequence:

0.0-1.3 seconds: close-up of nude CL high heels at the ankle on a marble floor, wrapped in premium gray sheer stockings that fit smoothly without wrinkles. A single sharp heel tap sound lands at 0.1 seconds. One 35-year-old Chinese woman wears premium gray ultra-thin stockings, nude Christian Louboutin heels, and a black satin long dress. She performs an ankle extension for 0.6 seconds and a heel-tap beat move for 0.2 seconds, timed precisely to 0.1-second accuracy.
1.3-5.0 seconds: the camera slowly pushes in with smooth, even motion and no shake, then cuts instantly to a gray-stocking foot close-up with strong camera-contrast in a 0.1-second switch, then instantly cuts to an extreme waist-and-abdomen close-up. The cut lands with another synchronized heel sound. The woman performs an arm extension for 0.7 seconds and a step accent for 0.4 seconds.
5.0-12.0 seconds: the camera performs a slight orbit, tracking the beat precisely with the movement range and no extra shake. It alternates between waist-abdomen close-ups and gray-stocking calf close-ups. The woman performs a turn for 0.9 seconds and a backbend accent for 0.5 seconds. The heels stay stable, the movement stays precise, and the stocking texture remains clearly visible. Heel sounds hit in sync with the turn and backbend.
12.0-15.0 seconds: freeze on a triple-layer close-up composition: waist-abdomen line close-up + gray-stocking leg close-up + red-sole heel close-up. A total of 22 beat points across the full sequence. The timing is relaxed but precise. Camera motion, heel sounds, and beat points are tightly aligned to maximize Seedance 2.0 performance.
--ar 16:9 --motion 8, soft-focus white light + glow, extremely premium look with strong control.
```

<a id="general-cinematic-case-2"></a>
<!-- Case 2: Mini Skateboard Escape in a Child Bedroom (by @anson7956) -->
### ケース 2: [子ども部屋でミニスケートボード脱出](https://x.com/anson7956/status/2038846411253657939) (投稿者 [@anson7956](https://x.com/anson7956))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-2"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/003.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
On the floor of a child's bedroom, a miniature girl rides a tiny skateboard at high speed, skimming just above the ground. Everything is scaled so massively that full-size toys and furniture feel gigantic. The camera follows closely from a low angle in a near one-take style, continuously moving deeper into the background. The video uses an ultra-wide lens, motion blur, depth of field, and cinematic lighting.
The speed increases in three stages.
In the first stage, she races through narrow passages like canyons between Lego city buildings, weaving agilely through blocks.
In the second stage, a giant ball rolls toward her from the front. She slips through the narrow gap between the ball and the wall, barely avoids falling blocks, and brushes past the tires of a moving miniature car.
In the third stage, she bursts through the gap between the pages of a picture book as the wind is about to close it, ducks beneath the armpit of a swaying plush toy, and finally leaps into the small gap of a toy box lid just before it shuts, disappearing into the darkness at top speed.
This is a thrilling, heart-pounding video packed with near escapes. The setting is a realistic child's room, using a miniature perspective to create an immersive, theme-ride-like experience that fully exploits giant obstacles and tiny gaps.
```

<a id="general-cinematic-case-3"></a>
<!-- Case 3: Rucker Park Grandma Showdown (by @techhalla) -->
### ケース 3: [ラッカー・パークのおばあちゃん対決](https://x.com/techhalla/status/2039114930461549008) (投稿者 [@techhalla](https://x.com/techhalla))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-3"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/023.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Raw mobile phone footage, vertical handheld shot, shaky cam, grainy texture. At the legendary Rucker Park basketball court at dusk, a heavy-set elderly woman in a floral dress and sneakers is dribbling a basketball against
```

<a id="general-cinematic-case-4"></a>
<!-- Case 4: Firefighter Baby Rescue Sequence (by @AITalesNBH) -->
### ケース 4: [消防士による赤ちゃん救出](https://x.com/AITalesNBH/status/2039072522650423445) (投稿者 [@AITalesNBH](https://x.com/AITalesNBH))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/026.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
The firefighter is entering the house, at the 3-second mark the firefighter is walking inside the house with furniture in fire around him, at the 5-second mark a burning tree piece falls in front of him, at the 8-second mark he finds a 3 old baby in a baby bed, the baby is coughing, the firefighter lifts the baby and hugs it, the firefighter gets out of the house, he gives the baby to an ambulance personnel
```

<a id="general-cinematic-case-5"></a>
<!-- Case 5: Ancient Costume Transformation Showcase (by @johnAGI168) -->
### ケース 5: [古代衣装への変身ショー](https://x.com/johnAGI168/status/2040058721158467975) (投稿者 [@johnAGI168](https://x.com/johnAGI168))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-5"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/029.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
You can generate the same style of video without using the @ symbol as well.

Seedance 2.0 all-purpose reference prompt below:

[Section 1: Gentle beauty appears] Time: 0-3 seconds. Framing and camera: static medium shot, no camera movement. Female styling and costume: long hair over the shoulders, ancient-style golden crown and dangling hair ornaments, fair skin and red lips. Show three outfits during this section: 1. black strapless long dress with red edging, gold embroidery, and a pearl tassel waist belt; 2. white robe with red sleeves over a gold-embroidered strapless top; 3. pure red slit dress with a red-and-gold embroidered dudou. Movement and expression: both arms dance with the rhythm, fingertips soft and graceful, expression gentle and seductive. Sound: ancient-style transformation BGM. Effects and environment: hard-cut outfit changes on the beat. Purple carpet, folding screen, and candle stands in the background, with purple mist throughout.
[Section 2: Cold elegance shift] Time: 3-6 seconds. Framing and camera: static medium shot. Female styling and costume: hairstyle and makeup unchanged. Show two outfits: 1. white robe and black skirt, black strapless top with intricate gold-and-blue embroidery and a high slit; 2. pink gauze outer layer over a pale blue and white floral-embroidered long dress. Movement and expression: arms rise and fall to cover the face and then open out, body light and graceful, expression turning poised and cool. Sound: ancient-style transformation BGM. Effects and environment: hard-cut transformation on the beat. Alternating warm and cool outfits with strong contrast.
[Section 3: Lively turn] Time: 6-11 seconds. Framing and camera: static medium shot. Female styling and costume: pink translucent gauze outer robe over a black-and-gold patterned strapless dress, with a thin purple sash at the waist. Movement and expression: back turned, then glance over the shoulder, raise one hand lightly, affectionate eyes, lively and playful pose. Sound: ancient-style transformation BGM. Effects and environment: hard-cut transition. Pink and purple lighting cross through drifting smoke.
[Section 4: High-frequency glamour] Time: 11-15 seconds. Framing and camera: static medium shot. Female styling and costume: rapidly cycle through three outfits: 1. deep red strapless long dress with a red-and-gold waist belt; 2. pure white wide-sleeved plain robe with a white belt; 3. pink-and-white split-color dress with light-blue bird embroidery on the chest. Movement and expression: both hands swing up and down in stacked motion with urgent drum hits, larger movement range, full commanding presence. Sound: ancient-style transformation BGM. Effects and environment: ultra-fast beat-synced outfit switching. Multiple colors hit in rapid succession, pushing visual extravagance to a climax.
```

<a id="general-cinematic-case-6"></a>
<!-- Case 6: Ginza at night, future cyberpunk (by @ChiakiAkagi) -->
### ケース 6: [夜の銀座、未来のサイバーパンク](https://x.com/ChiakiAkagi/status/2040232705477255363) (投稿者 [@ChiakiAkagi](https://x.com/ChiakiAkagi))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-6"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/037.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Ginza at night, future cyberpunk.
A female ninja is hiding, made transparent by optical camouflage.
She defeats an enemy ninja.
After the first attack, the optical camouflage is released.
The enemy ninja clones into three.
They fight moving at high speed with motion blur and afterimages.
The female ninja's punch sends the ninja flying, crashing into a neon sign high above.
```

<a id="general-cinematic-case-7"></a>
<!-- Case 7: stories of a hopper (by @starks_arq) -->
### ケース 7: [跳ねる者の物語](https://x.com/starks_arq/status/2040036602018451721) (投稿者 [@starks_arq](https://x.com/starks_arq))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-7"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/040.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
stories of a hopper. 

1 astronaut that's able to hop from location to location, anytime he wants.
```

<a id="general-cinematic-case-8"></a>
<!-- Case 8: A suspicious man stands in the center of Shibuya scramble crossing (by @roco_kn_roco) -->
### ケース 8: [渋谷スクランブル交差点の中央に立つ怪しい男](https://x.com/roco_kn_roco/status/2039962871149584691) (投稿者 [@roco_kn_roco](https://x.com/roco_kn_roco))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-8"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/043.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A suspicious man stands in the center of Shibuya scramble crossing. People around the man walk and cross like a time-lapse, centered around him. When he raises his right hand straight up and snaps his fingers, a wave occurs, and everyone except him stops moving like a mannequin.

Used Prompt 2
Protagonist: Hiromu, Age 19
```

<a id="general-cinematic-case-9"></a>
<!-- Case 9: Fishing Boat Crowd Phone Cam (by @maxescu) -->
### ケース 9: [漁船の群衆を捉えるスマホ映像](https://x.com/maxescu/status/2040095139511636166) (投稿者 [@maxescu](https://x.com/maxescu))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-9"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/044.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
aesthetic: phone held up in the middle of a packed crowd on the deck of a fishing boat
 audio: bass competing with ocean wind, waves crashing against the hull
 timeline:
 - "0-5s: Phone camera on the deck of a fishing boat at sea. Golden hour. The deck is PACKED
```

<a id="general-cinematic-case-10"></a>
<!-- Case 10: A girl falls rapidly through a digital tunnel (by @_3912657840) -->
### ケース 10: [デジタルトンネルを高速落下する少女](https://x.com/_3912657840/status/2039911660656484590) (投稿者 [@_3912657840](https://x.com/_3912657840))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-10"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/057.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A girl falls rapidly through a digital tunnel. The girl is panicking and flailing. She passes through a tunnel that twists and turns up, down, left, and right, then falls straight down. She lands softly on a rainbow cloud in a fancy world overflowing with light. She looks up and sees a large, rainbow-shining sun glowing in the sky. Backlight.
```

<a id="general-cinematic-case-11"></a>
<!-- Case 11: Skytree Railgun Launch Sequence (by @TechTalkNAVI) -->
### ケース 11: [スカイツリー・レールガン発射](https://x.com/TechTalkNAVI/status/2040100728627454339) (投稿者 [@TechTalkNAVI](https://x.com/TechTalkNAVI))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-11"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/060.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Scene: The Skytree transforms into a "super massive railgun" and fires a light projectile towards space.

Visuals:

First Stage: The exterior of the tower is purged, exposing complex superconducting coils inside. Intense discharge phenomena surround the area.

Middle Stage: As energy is charged, the entire power of Sumida Ward is sucked into the tower, causing a city-wide blackout. Only the tower glows white.

Final Stage: Firing. A pillar of light pierces the stratosphere, forming a giant aurora ring in space.

Lighting/Color: Cold white, purple discharge. Contrast between silence and roar.
```

<a id="general-cinematic-case-12"></a>
<!-- Case 12: A Hollywood movie trailer (by @SSSS_CRYPTOMAN) -->
### ケース 12: [ハリウッド映画の予告編](https://x.com/SSSS_CRYPTOMAN/status/2040217171918516475) (投稿者 [@SSSS_CRYPTOMAN](https://x.com/SSSS_CRYPTOMAN))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-12"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/065.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A Hollywood movie trailer. A Marvel-style action movie where an ordinary American high school student transforms into a hero and fights. I want to create various scenes with multi-cuts. The title is CRYPTOMAN
```

<a id="general-cinematic-case-13"></a>
<!-- Case 13: Cinematic Vertical 9:16 Sequence (by @Mayz1169) -->
### ケース 13: [映画的な縦型 9:16 シーケンス](https://x.com/Mayz1169/status/2039982387703296044) (投稿者 [@Mayz1169](https://x.com/Mayz1169))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-13"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/067.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Cinematic vertical 9:16 video. Two versions of Rapunzel from Tangled walk side by side toward the camera on a forest dirt path. On the LEFT: the original Disney 3D animated Rapunzel — large expressive cartoon eyes, stylized face with Disney animation proportions, luminous long
```

<a id="general-cinematic-case-14"></a>
<!-- Case 14: A giant glacier wall collapses into a fjord beside a coastal city (by @LudovicCreator) -->
### ケース 14: [沿岸都市のそばで巨大氷河壁がフィヨルドへ崩落](https://x.com/LudovicCreator/status/2040100791822721300) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-14"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/068.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A giant glacier wall collapses into a fjord beside a coastal city.

The falling ice triggers a massive water displacement wave that surges toward the harbor.

Camera sweeps over the collapsing glacier before racing toward the city as the water wall crashes into buildings and docks.

Icebergs smash through streets as the city floods.

Glacier collapse megaflood, iceberg destruction chaos, cinematic polar disaster scale, 4K.
```

<a id="general-cinematic-case-15"></a>
<!-- Case 15: A moonlit piano chase where the mouse (by @Dheepanratnam) -->
### ケース 15: [月明かりのピアノ追跡劇とネズミ](https://x.com/Dheepanratnam/status/2040060221733609969) (投稿者 [@Dheepanratnam](https://x.com/Dheepanratnam))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-15"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/072.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A moonlit piano chase where the mouse
turns the whole instrument into a trap.

What happens The mouse runs across piano keys, making playful notes. 

The cat stalks across the piano lid. The cat lunges, but the mouse slips into the piano. 

The cat gets nearly caught by the closing lid. Inside the piano, the mouse runs through strings and hammers. The cat’s tail gets plucked like an instrument. 

The cat crashes into the keyboard section, causing a chaotic musical explosion. Final gag: the mouse presses one neat final note while the cat pops out wearing sheet music on its head.
```

<a id="general-cinematic-case-16"></a>
<!-- Case 16: 15-second continuous single-shot cartoon sequence (by @Artedeingenio) -->
### ケース 16: [15 秒連続ワンカットのカートゥーン](https://x.com/Artedeingenio/status/2040054705183723711) (投稿者 [@Artedeingenio](https://x.com/Artedeingenio))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-16"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/077.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second continuous single-shot cartoon sequence.

No cuts. No scene transitions.

Soft watercolor illustration style, pastel colors, gentle textures, hand-drawn outlines, dreamy lighting, calm and magical tone

Scene:

A small animal character walking through a quiet meadow.
```

<a id="general-cinematic-case-17"></a>
<!-- Case 17: Steampunk Airship Battle at Sunset (by @Alin_Reaper05) -->
### ケース 17: [夕暮れのスチームパンク飛行船戦](https://x.com/Alin_Reaper05/status/2040017612105556403) (投稿者 [@Alin_Reaper05](https://x.com/Alin_Reaper05))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-17"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/080.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Victorian-era flying airships with brass gears and giant propellers battling over a cloudy mountain range at sunset, cannons firing, pirates swinging on ropes between ships, intricate mechanical details, sweeping aerial tracking shot with parallax, warm steampunk color palette, ultra-detailed, like Howl’s Moving Castle meets Pirates of the Caribbean, epic action.
```

<a id="general-cinematic-case-18"></a>
<!-- Case 18: Flip-Flops Jet Wing Tracking Shot (by @maxescu) -->
### ケース 18: [ビーチサンダルのジェット翼を追うショット](https://x.com/maxescu/status/2039639805592502504) (投稿者 [@maxescu](https://x.com/maxescu))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-18"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/087.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
aesthetic: Raw 35mm handheld, high altitude sun haze. One unbroken continuous tracking shot. No cuts. All real time. audio: Full constant jet engine roar, wind blast, no other sound. 

timeline: 
- 0-3s: Normal guy in baggy cargo shorts and flip flops is standing perfectly
```

<a id="general-cinematic-case-19"></a>
<!-- Case 19: Exterior of an ancient temple in the deep mountains (by @cdexsta) -->
### ケース 19: [深山にある古寺の外観](https://x.com/cdexsta/status/2039559243284844649) (投稿者 [@cdexsta](https://x.com/cdexsta))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-19"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/089.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
2.35:1 widescreen, 24fps, cinematic quality.
Exterior of an ancient temple in the deep mountains. The camera overlooks the temple roof amidst surging clouds, with mottled tiles and rising mist. The scene cuts to the interior, where a middle-aged monk sits cross-legged, with an ancient Buddha statue and flickering candlelight behind him. The camera slowly rotates 360 degrees, panning from the monk's side to a front close-up, capturing his slightly closed eyes and calm breathing.
```

<a id="general-cinematic-case-20"></a>
<!-- Case 20: Statue of Liberty Sunrise Storyboard (by @MrDasOnX) -->
### ケース 20: [自由の女神と日の出のストーリーボード](https://x.com/MrDasOnX/status/2045065813628186733) (投稿者 [@MrDasOnX](https://x.com/MrDasOnX))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-20"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/urrfA6BwbCGtYgie.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Shot list sequence:
1. Aerial establishing shot of the majestic Statue of Liberty standing tall on Liberty Island with Manhattan skyline and New York Harbor backdrop at sunrise
2. Slow push-in across the harbor waters toward the statue's base and pedestal
3. Wide shot of the full figure with flowing robes, tablet in left hand, and torch raised high catching first golden light
4. Close-up of the detailed copper crown with seven spikes and stern facial features in warm dawn glow
5. Pan up along the outstretched right arm to the illuminated torch with subtle flame flicker
6. Elegant long shot of the statue's profile against the rising sun and rippling harbor water
7. Smooth slide around the pedestal revealing inscribed tablet with "July IV MDCCLXXVI" date
8. Close-up of intricate folds in the copper robes and broken chains at the feet symbolizing freedom
9. Wide view from the water showing ferry boats in the distance and Ellis Island nearby
10. Serene shot of the star-shaped Fort Wood foundation and surrounding plaza with American flags
11. Tilt-up from the base along the massive structure emphasizing scale and grandeur
12. Golden sunrise rays piercing through light harbor mist with water reflections
13. Elevated angle capturing the perfect symmetry and iconic silhouette against the sky
14. Warm light transition as the sun rises higher, bathing the green patina copper in glowing tones
15. Final hero pull-back aerial shot revealing the full Statue of Liberty with New York City awakening in the background
Fast cinematic cuts, smooth micro camera movements per shot (push, pan, slide, tilt, orbit), physically accurate sunrise lighting and gentle water motion, realistic copper patina textures with subtle sheen and oxidation details, soft shadows and mist, ultra-realistic materials (copper, stone pedestal, water, sky), consistent exposure and warm color grading, no flicker, stable geometry, real-world motion blur, shallow depth of field where appropriate, HDR, ultra high definition, film-quality American historical and heritage cinematography.
```

<a id="general-cinematic-case-21"></a>
<!-- Case 21: Historical scene with dramatic lighting (by @AskVenice) -->
### ケース 21: [劇的照明で描く歴史場面](https://x.com/AskVenice/status/2039570736239595726) (投稿者 [@AskVenice](https://x.com/AskVenice))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-21"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/101.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Historical scene with dramatic lighting.

[0-3 seconds]
Opening shot: Venetian galley fleet approaches Constantinople at dawn, cannons blazing. Massive city walls loom in background, Byzantine banners fluttering defiantly.

[3-6 seconds]
Quick cut: Ottoman cannon
```

<a id="general-cinematic-case-22"></a>
<!-- Case 22: Rocket Surf Continuous Tracking Shot (by @maxescu) -->
### ケース 22: [ロケットサーフィンの連続追跡撮影](https://x.com/maxescu/status/2039308020006396033) (投稿者 [@maxescu](https://x.com/maxescu))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-22"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/107.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
ROCKET SURF.
STYLE: Gritty Cine Verite, 35mm handheld, natural shake. Continuous tracking shot. No cuts. All real-time.

LIGHTING: Bright, high-altitude sun, pure blue sky.

AUDIO: Rocket engine roar, wind, fiberglass creak.

TIMELINE: 0-3s:
```

<a id="general-cinematic-case-23"></a>
<!-- Case 23: Stand-Up Comedy Monologue Template (by @Adam38363368936) -->
### ケース 23: [スタンドアップコメディ独白テンプレート](https://x.com/Adam38363368936/status/2039286911265800297) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-23"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/120.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
A single stand-up comedian @[Image 1] with black hair, wearing a textured red dress, standing on a spotlighted stage @[Image 2]. Exaggerated and humorous expression, lively eyes, confident and rhythmic tone.
Dialogue: Have you noticed that people nowadays say they are 'lying flat,' but their bodies are more competitive than anyone else's! My friend constantly claims to be 'Buddhist-style'—not fighting or competing—yet their speed when grabbing red envelopes is so fast I can't even see it clearly! I just want to ask: Is your 'Buddhist-style' so effective that even the Buddha would want to send you a rocket?
Actions and Expressions:
 
- When saying “lying flat”: Spreading hands, looking helpless
​
- When saying “grabbing red envelopes”: Quickly flicking hands, performing a super-fast hand motion, eyes wide open
​
- Ending: Shrugging, grinning broadly, maximizing interaction
Scene: Black stand-up stage, strong spotlight illuminating the person, blurred silhouettes of the audience below, atmosphere of laughter, slight camera push-in, cinematic lighting, strong stage presence, real-shot texture, fast pace, 15-second short video effect. Shallow depth of field, enhanced light and shadow contrast, scene detail reconstruction, digital noise elimination, 4K high-definition quality.
```

<a id="general-cinematic-case-24"></a>
<!-- Case 24: Birthday Betrayal Restaurant Drama (by @Lighterkissan33) -->
### ケース 24: [誕生日の裏切りを描くレストランドラマ](https://x.com/Lighterkissan33/status/2045023927412637712) (投稿者 [@Lighterkissan33](https://x.com/Lighterkissan33))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-24"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/KT84c2TqktCYBHye.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
15-second modern short drama, upscale restaurant scene, warm gold tones contrasting with a
cold mood.

0-3 seconds: Medium shot, fixed angle. A beautiful girl is celebrating her birthday with friends,
raising a glass and laughing joyfully. Suddenly, the restaurant door is pushed open—her most trusted
best friend walks in arm-in-arm with her boyfriend. The laughter stops abruptly, and the girl's
hand, holding the glass, freezes in mid-air, her smile captivated.

4-8 seconds: The best friend's expression becomes awkward upon seeing the girl. She tries to pull
her boyfriend to move to another seat, but he shakes her hand and walks straight to the girl,
placing a gift box in front of her and saying "Happy Birthday." The best friend's face turns pale.
The girl looks at her boyfriend, then at her best friend, finally focusing on their hands—the best
friend is wearing the same bracelet her boyfriend said he "lost" a few days ago.

9-12 seconds: The girl doesn't speak, but quietly picks up her glass and drinks it all in one gulp.
Then she stands up and walks to her best friend. Everyone holds their breath, waiting. The girl
smiles and slowly pours the wine onto her best friend's limited-edition bag. The best friend's eyes
widen, as if she's about to scream. The girl holds her shoulder;

13-15 seconds: The girl leans close to her best friend's ear and whispers, "Next time you're
cheating, remember to hide what you shouldn't show first." The best friend turns pale, and the girl
turns and leaves gracefully. The camera pulls back to show the best friend standing there stiffly,
her boyfriend full of regret, ending with a low background music and whispers around them.
```

<a id="general-cinematic-case-25"></a>
<!-- Case 25: Ancient Parkour Costume-Change Sequence (by @Adam38363368936) -->
### ケース 25: [古代パルクールの衣装替え](https://x.com/Adam38363368936/status/2040980673851506798) (投稿者 [@Adam38363368936](https://x.com/Adam38363368936))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-25"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2040980673851506798.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
在下面，来试试！

Seedance2.0提示词

写实古风跑酷变装。女主【@图1】写实风格，面容白净，黑色波浪长发，黑色连衣裙，面部微汗眼神凌厉。15秒一镜到底手持跟拍。
场景：黄昏古镇，青石湿滑，冷暖影调。
动作逻辑：0-3s 踩翻茶摊，顺手扯下白衫披身，老板尖叫；3-6s 踩车空翻，空掉牛仔裤落入蒸笼，强抓路人马面裙，少女摔倒；6-9s 扶手滑翔穿袖，掠走银簪并滑跪挽发，老伯愣神；9-12s 窄巷墙跑系腰带，抄起红油纸伞带倒伞架，学徒绊倒；12-15s 桥顶定格，俯视众人，猛烈开伞遮面，眼神回眸转为凌厉。
质感：ARRI胶片质感，物理风阻逻辑，极致市井烟火气，路人反应真实，暴力跑酷美学。
```

<a id="general-cinematic-case-26"></a>
<!-- Case 26: Engine Internals — Piston Mechanical Detail (by @YaReYaRu30Life) -->
### ケース 26: [エンジン内部 — ピストンの機械ディテール](https://x.com/YaReYaRu30Life/status/2041068828457877598) (投稿者 [@YaReYaRu30Life](https://x.com/YaReYaRu30Life))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-26"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041068828457877598.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
の要素から少し知見が増して反映している印象
→エンジン内部、ピストン
プロンプトに入っていますが
それっぽい構造が増してます。
もう少しエンジンに関しての要素を出してオンにするとより良くなるかなーという気がします。

〇デメリットもある
ハンドル周りがちらっと映るシーンでの
不要なメーターが増える。

認識的にこれが車のハンドル周りって
いうものを検索すると何かとそれっぽくしてしまう可能性あり
```

<a id="general-cinematic-case-27"></a>
<!-- Case 27: 90s Japanese Romance Sim — Cel Animation Style (by @kinopioai_ai) -->
### ケース 27: [90 年代日本恋愛シミュレーション — セル画風](https://x.com/kinopioai_ai/status/2040814307487916415) (投稿者 [@kinopioai_ai](https://x.com/kinopioai_ai))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-27"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2040814307487916415.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
のみ
右　画像➕プロンプト

プロンプト公開
————————————————————-

90年代日本の恋愛シミュレーションゲーム画面、セル画調アニメ、くっきり輪郭線、桜色と暖色パステルカラー、画面下部に半透明ADVテキストウィンドウ常設、ノスタルジックで甘酸っぱい雰囲気。

ヒロイン：17歳、腰までの栗色ストレートロングヘア、前髪ぱっつん、琥珀色の大きな瞳、白セーラー服に紺スカーフとプリーツスカート、色白、頬にうっすら紅。全カットで顔と衣装の一貫性を維持。

[0-4s] 春の朝、満開の桜並木の高校校門。柔らかい朝陽、花びらがゆっくり舞う。画面奥からヒロインが歩いてくる。画面下部にテキストウィンドウ「4月——新しい季節が始まる」。淡いゴッドレイ。Camera: slow dolly in, smooth gimbal, wide to medium.

[4-8s] 午後の教室、窓から斜めに陽光。ヒロインが窓際でゆっくり振り返り、首をかしげてはにかんだ笑顔。画面下部にダイアログボックス、名前欄「藤宮 ひなた」。柔らかいディフューズドライティング。Camera: static medium shot, eye level, fixed framing.

[8-12s] 放課後の屋上、夕焼けのオレンジ空。ヒロインがフェンス越しに夕陽を見つめ、夕風が髪を揺らす。ゆっくり振り向き頬を赤らめる。ダイアログ「……来てくれたんだ」。golden hour逆光、髪にリムライト。Camera: slow dolly in, waist to bust, low angle.

[12-15s] 校庭の大きな桜の樹の下、magic hourの金色の光。ヒロインが胸の前で手を重ねうつむき、ゆっくり顔を上げて潤んだ瞳で微笑む。画面下部にゲーム選択肢ウィンドウ2つ。桜が舞う。金色レンズフレア、淡いボケ。Camera: slow dolly in to close-up, eye level, gentle smooth.

4K, Ultra HD, no deformation, natural smooth movements, stable picture, no flickering, no ghosting, sharp details. Generate video without subtitles.
```

<a id="general-cinematic-case-28"></a>
<!-- Case 28: Cinematic Directing Techniques — Multi-Shot Prompt (by @noman23761) -->
### ケース 28: [映画演出技法 — マルチショット・プロンプト](https://x.com/noman23761/status/2041409914954973216) (投稿者 [@noman23761](https://x.com/noman23761))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-28"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041409914954973216.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
The difference between “AI slop” and “this looks directed” is literally 2–3 prompt changes.
Seedance 2 Global access api :-
If you are just looking for an app to run Seedance 2 without business email and geo restrictions check out VadooAI
The “4-Part Prompt Formula” 🎬
Most people write vibes. Seedance wants structure.
Use this every time:
Subject → Action → Camera → Style
If you skip camera → you get random motion
If you skip action → you get stiff clips
2. The “Camera is King” rule 🎥
Seedance is basically a camera simulator.
Instead of: “girl walking in city”
Say: “tracking shot, slow dolly-in, 35mm lens, shallow depth of field”
That alone upgrades output quality massively
3. The “Don’t Describe the Image” hack 🖼️
If you’re using a reference image:
DO NOT re-describe it
Only describe motion + changes
Otherwise the model “reinterprets” your image and ruins it
4. The “Motion Intensity” trick ⚡
Seedance doesn’t infer speed.
“car drives” = boring
“car accelerates aggressively, motion blur, tires screeching” = cinematic
You have to explicitly define energy levels
```

<a id="general-cinematic-case-29"></a>
<!-- Case 29: East Asian Woman Portrait — Natural Smile (by @noman23761) -->
### ケース 29: [東アジア女性のポートレート — 自然な笑顔](https://x.com/noman23761/status/2041408928215408931) (投稿者 [@noman23761](https://x.com/noman23761))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-29"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041408928215408931.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
"beautiful young East Asian woman, long wavy chestnut brown hair, big smile, earphones in ears, wearing oversized white knit cardigan, denim shorts, white sneakers, holding red Coca-Cola can in right hand, playful and confident vibe, walking and dancing energetically down a sunny Paris cobblestone street, low angle dynamic camera, sudden surreal chaos: floating businessmen in black suits flying through the air with briefcases and white papers scattering everywhere, one businessman lying on the ground, girl completely unfazed and keeps dancing joyfully, pointing at camera, spinning, laughing, cinematic color grading, soft daylight, shallow depth of field, beautiful European architecture background, cafes and parked cars, final shot: girl walks away from camera down the long street, buildings suddenly light up with vibrant rainbow neon colors (pink, purple, blue, green, yellow) glowing on windows and balconies, dreamy atmosphere, highly detailed, 8k, masterpiece, smooth motion, perfect anatomy, natural physics"

Instead of reacting to chaos, she becomes the only stable element in the frame.
Everything else feels temporary, almost like background noise.

What’s interesting is how that changes the perception of the scene:
the chaos doesn’t feel dominant anymore — it feels irrelevant.

Same structure, completely different feeling.
```

<a id="general-cinematic-case-30"></a>
<!-- Case 30: Post-Apocalyptic Survival — Cinematic Setup (by @noman23761) -->
### ケース 30: [終末後のサバイバル — 映画的セットアップ](https://x.com/noman23761/status/2041405260762419692) (投稿者 [@noman23761](https://x.com/noman23761))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-30"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041405260762419692.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
"[CINEMATIC SETUP] Genre & Mood: Gritty Post-Apocalyptic Survival. Tense, visceral, and hyper-realistic. Film Stock & Lens: Shot on 35mm anamorphic lens, f/2.8 for shallow depth of field. Teal-orange desaturated color grade with earthy, dusty undertones. Lighting & Atmosphere: Dramatic volumetric Golden Hour light with heavy dust motes and heat haze. Character Description: An athletic woman in her late 20s, wearing weathered tactical leather armor and dirt-smudged skin. Her hair is wind-blown and messy; her expression is one of intense, lethal focus. Audio Style: Immersive spatial sound design. Detailed SFX of bowstring tension, rhythmic heavy breathing, wind howling through the canyon, and a high-velocity "thwack" on impact. [TIMELINE SECOND BY SECOND] 0-3s: [Extreme Close-up (ECU)] High-angle shot of the woman's face as she aims a mechanical compound bow. The bowstring is pulled taut against her cheek. Movie-level realistic facial features, no deformation, stable throughout. 3-4s: [Macro Cut] Extreme close-up of her iris. The pupil dilates sharply as she locks onto her target. Realistic light reflections in the eye. 4-8s: [Over-the-shoulder (OTS) Shot] The camera sits behind her shoulder on a jagged cliff edge. In the valley below, a herd of mutated, post-apocalyptic Cape Buffalo with thickened grey hide and jagged horns graze peacefully. Smooth camera push-in. 8-10s: [The Release & POV] She releases the arrow. Fast Tracking POV shot following the arrowhead at maximum veloc
```

<a id="general-cinematic-case-31"></a>
<!-- Case 31: Pixar Forest Clearing — 3D Animated Scene (by @SPEEDAI07) -->
### ケース 31: [ピクサー風の森の空き地 — 3D アニメーション](https://x.com/SPEEDAI07/status/2041393724622795014) (投稿者 [@SPEEDAI07](https://x.com/SPEEDAI07))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-31"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041393724622795014.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Seedance 2.0 Prompt

Pixar 3D animated forest clearing. Sunny day, god rays through trees, green grass, flowers. CHARACTERS: - Giant armored wolf: black fur, gold sword, yellow eyes, furious and humiliated, attacks with full rage - Tiny rooster: red comb, completely unbothered, bored expression, deflects everything with casual wing flaps SEQUENCE: 0-3s — Wolf roars, raises sword overhead, brings it down with full force. Rooster glances up, sighs, flicks one wing — sword deflects sideways. Sparks fly. Wolf stumbles forward from own momentum. Rooster examines wing casually, unbothered. 3-6s — Wolf swings horizontal slash. Rooster ducks under it yawning, taps sword away with wingtip. Wolf spins, overhead strike — rooster sidesteps one inch, sword hits ground, shockwave crater. Rooster hasn't changed expression once. 6-9s — Wolf goes berserk — rapid five-hit combo, sword blur. Rooster deflects each strike with alternating wings — tap, tap, tap, tap, tap. Casual rhythm like swatting flies. Last strike — rooster catches blade between two feathers. Stops it cold. Wolf strains, shaking. Can't move it. 9-12s — Rooster releases blade, wolf stumbles backward. Wolf charges with shoulder slam — rooster steps aside, wolf face plants into grass. Wolf up instantly, wild overhead — rooster flicks it away with tail feather. Sword spins out of wolf's grip, lands in tree trunk. 12-15s — Wolf stares at empty hands. Rooster turns, walks away slowly, doesn't look back. Scratches ground with one cla
```

<a id="general-cinematic-case-32"></a>
<!-- Case 32: Kitten Sneaking Snacks Under Covers (by @lynneatyoumind) -->
### ケース 32: [布団の中でおやつを盗む子猫](https://x.com/lynneatyoumind/status/2041334660173852807) (投稿者 [@lynneatyoumind](https://x.com/lynneatyoumind))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-32"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041334660173852807.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
prompt: A cute kitten secretly eating snacks under the covers in bed at night. Hears footsteps, panics, hides the snacks, and fakes sleep with soft purring. Owner opens the door, peeks in, then leaves. Coast clear — the kitten pulls the snacks back out and keeps munching. Dark cozy bedroom, moonlight, cinematic lighting, smooth animation.
```

<a id="general-cinematic-case-33"></a>
<!-- Case 33: Seedance 2.0 T2V Natural Speech Test (by @tanabe_fragm) -->
### ケース 33: [Seedance 2.0 T2V 自然発話テスト](https://x.com/tanabe_fragm/status/2041328307267088580) (投稿者 [@tanabe_fragm](https://x.com/tanabe_fragm))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-33"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041328307267088580.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
の問題でした😅
試しにt2vで喋らせたら、むしろKling 3.0より自然で驚きました。

Seedance 2.0はとにかくプロンプト依存が強いモデルですね📝
ここまで出力が変わるのは正直初めてです。
使用したプロンプトはこちら👇
-----------------------------------------
可愛らしいふっくらとした赤いトマトのキャラクターが、カメラに向かって直接話しかけている。完璧なリップシンクで「みんな、僕たちトマトを冷蔵庫に入れてない？実はそれ、NGなんだ！寒さで甘みが飛んじゃうから、常温で保存してね！食べる直前に少し冷やすのが一番美味しいよ！」と元気な声で喋っている。言葉のテンポに合わせて少し弾むような動きをする。ピクサー風の高品質な3Dアニメーションスタイル。背景は少しぼけたキッチン。
```

<a id="general-cinematic-case-34"></a>
<!-- Case 34: Paper Puppet Horror Animation (by @TomaAIbijo) -->
### ケース 34: [紙人形ホラーアニメーション](https://x.com/TomaAIbijo/status/2041409381162689021) (投稿者 [@TomaAIbijo](https://x.com/TomaAIbijo))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-34"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2041409381162689021.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Scene 1
horror animation. Flat paper-puppet look, rough textures, dark muted colors, slight projector flicker. 15-second vertical video (9:16), 5 cuts.

Cut1 (0-3s)
Night Japanese street, flickering streetlight. Young woman alone at bus stop. Paper cut-out style, slow push-in.

Cut2 (3-6s)
Behind the woman. Across the road a strange shadow figure stands. Its head slowly tilts.

Cut3 (6-9s)
Woman turns, close-up. Eyes widen. Background darkens like sliding kamishibai panel.

Cut4 (9-12s)
The shadow figure is suddenly much closer behind the bus stop sign. Face hidden, pale eyes glowing.

Cut5 (12-15s)
Extreme close-up of the figure. Screen flickers like old film. Whisper: “Miteita yo…” → cut to black.

Audio: low eerie hum, wind, wooden clack, whisper echo.

Scene 2
horror animation. Flat paper puppet look, rough paper texture, dark muted colors, slight projector flicker. 15-second vertical video (9:16), 5 cuts.

Cut1 (0-3s)
Black screen fades in to the same bus stop. The woman is gone. The streetlight flickers.

Cut2 (3-6s)
Camera slowly pans. The shadow figure now stands where the woman was.

Cut3 (6-9s)
Close-up of the ground. The woman’s phone lies on the pavement, screen still glowing.

Cut4 (9-12s)
Phone screen shows the camera app open. In the screen reflection, the shadow figure stands behind the viewer.

Cut5 (12-15s)
The figure suddenly fills the frame from behind the camera. Whisper: “Tsugi wa… kimi da.” → cut to black.

Audio: low eerie hum, distant wind, wooden kam
```

<a id="general-cinematic-case-35"></a>
<!-- Case 35: Red Desert Motorcycle Tracking Shot (by @LudovicCreator) -->
### ケース 35: [赤い砂漠を走るバイクの追跡ショット](https://x.com/LudovicCreator/status/2075520438239678846) (投稿者 [@LudovicCreator](https://x.com/LudovicCreator))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-35"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2075520438239678846.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
Stylized anime desert crossing beat: a futuristic motorcycle cuts across a vast red desert at midday, dust rising in long painterly ribbons behind the rear wheel. The rider leans forward against the heat shimmer, cloak snapping violently in the wind, solar panels and ruined towers flickering on the horizon. Wide tracking shot from the side, the bike slicing through waves of sand, wheels reduced to smear-frame circles. The rider’s visor catches the burning sun as the landscape bends with speed.
```

<a id="general-cinematic-case-36"></a>
<!-- Case 36: Pompeii DV Disaster Footage (by @venturetwins) -->
### ケース 36: [ポンペイ災害の DV 映像](https://x.com/venturetwins/status/2077080446341656956) (投稿者 [@venturetwins](https://x.com/venturetwins))

| 出力 |
| :----: |
| <a href="https://evolink.ai/seedance-2-0-prompts?utm_source=github&utm_medium=case_preview&utm_campaign=awesome-seedance-2.0-prompts&utm_content=general-cinematic-case-36"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-seedance-2.0-prompts/public/seedance_2_prompt_images/2077080446341656956.jpg" width="300" alt="Seedance 2.0 prompt preview frame"></a> |

**プロンプト:**

```
This is handheld documentary footage recorded on an early-2000s consumer DV camcorder from the streets of Pompeii at the moment Mount Vesuvius begins erupting. The footage feels like real, imperfect home video of ordinary people witnessing the beginning of a historic disaster.

The recording shows a busy street in Pompeii during the daytime, with merchants, families, children, laborers, and townspeople moving through the city. In the distance, Mount Vesuvius is visible above the rooftops. At first, people are going about normal daily life, but then a strange plume of smoke and ash begins rising from the volcano. The crowd gradually notices it. Some people stop and stare, some point toward the mountain, and others begin shouting to one another in confusion.

The camera moves through the street like someone in the crowd trying to capture what is happening. It shows frightened townspeople looking up at the sky, parents pulling children closer, merchants abandoning their stalls, and groups of people beginning to run as ash starts falling. The footage captures the shift from curiosity to fear as the eruption becomes impossible to ignore. There are natural cuts between wider views of the street, the mountain in the distance, and closer views of people reacting in panic.

The handheld camera shows natural shake, drifting framing, sudden reactive movement, autofocus mistakes as the person filming swings between the crowd and the volcano, slight exposure problems from bright daylight and ash in the air, and the imperfect look of old DV footage. The movement should feel urgent and unplanned, like someone trying to document the disaster while also staying safe.

Natural sound only: the noise of the street, footsteps on stone, people murmuring and then shouting, children crying, distant rumbling from the volcano, debris falling, and the panic of the crowd. No cinematic music added.

The result must feel like authentic, raw footage of ordinary people in Pompeii experiencing the beginning of the eruption of Mount Vesuvius, captured on an old DV camcorder.
```

<a id="related-repositories"></a>
## 🔗 関連リポジトリ

実行には隣接する API/skill を使い、このリポジトリはプロンプト発見面として維持します。

- [Seedance 2.0 API の例を読む](https://github.com/Evolink-AI/Seedance-2.0-Gateway-Service)
- [Seedance 2.0 skill をインストール](https://github.com/Evolink-AI/Seedance-2.0-Gateway-Service)
- [EvoLink API ドキュメントを読む](https://docs.evolink.ai?utm_source=github&utm_medium=docs&utm_campaign=awesome-seedance-2.0-prompts&utm_content=docs_link)

<a id="contributing"></a>
## 🤝 コントリビューション

提案前に [CONTRIBUTING.md](CONTRIBUTING.md) を確認してください。

<a id="license"></a>
## ⚖️ ライセンス

保守コードと文書は [Apache License 2.0](LICENSE) で提供されます。元のプロンプトとメディアの権利は各作者に帰属します。

<a id="copyright-notice"></a>
## ©️ 著作権に関する注意

公開された Seedance 2.0 プロンプトを学習・研究・ワークフロー参照のために整理しています。

<a id="acknowledge"></a>
## 🙏 謝辞

Seedance 2.0 の実験を公開してくださったクリエイターに感謝します。

[@liyue_ai](https://x.com/liyue_ai), [@TingFengAIAI](https://x.com/TingFengAIAI), [@anson7956](https://x.com/anson7956), [@genel_ai](https://x.com/genel_ai), [@Adam38363368936](https://x.com/Adam38363368936), [@Just_sharon7](https://x.com/Just_sharon7), [@BarlowHakusyaku](https://x.com/BarlowHakusyaku), [@ShadeLurk](https://x.com/ShadeLurk), [@ZaraIrahh](https://x.com/ZaraIrahh), [@drjoetw](https://x.com/drjoetw), [@johnAGI168](https://x.com/johnAGI168), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@MiraMusic_AI](https://x.com/MiraMusic_AI), [@aigeboku](https://x.com/aigeboku), [@applete77191758](https://x.com/applete77191758), [@mikeymansta](https://x.com/mikeymansta), [@CharaspowerAI](https://x.com/CharaspowerAI), [@TechTalkNAVI](https://x.com/TechTalkNAVI), [@Viafin23](https://x.com/Viafin23), [@songguoxiansen](https://x.com/songguoxiansen), [@JiahaoYang_art](https://x.com/JiahaoYang_art), [@techhalla](https://x.com/techhalla), [@craftian_keskin](https://x.com/craftian_keskin), [@AITalesNBH](https://x.com/AITalesNBH), [@nopinduoduo](https://x.com/nopinduoduo), [@gkxspace](https://x.com/gkxspace), [@ChiakiAkagi](https://x.com/ChiakiAkagi), [@xingsthatmatter](https://x.com/xingsthatmatter), [@tebasaki3D](https://x.com/tebasaki3D), [@starks_arq](https://x.com/starks_arq), [@simple__dev](https://x.com/simple__dev), [@sebatheepan](https://x.com/sebatheepan), [@sailorv321](https://x.com/sailorv321), [@roco_kn_roco](https://x.com/roco_kn_roco), [@maxescu](https://x.com/maxescu), [@kuranoayashi](https://x.com/kuranoayashi), [@itsPixieVerse](https://x.com/itsPixieVerse), [@chaosdotjpg](https://x.com/chaosdotjpg), [@aisavvy1](https://x.com/aisavvy1), [@aimikoda](https://x.com/aimikoda), [@aiehon_aya](https://x.com/aiehon_aya), [@adrianaia_](https://x.com/adrianaia_), [@_3912657840](https://x.com/_3912657840), [@ZikinArt](https://x.com/ZikinArt), [@YaReYaRu30Life](https://x.com/YaReYaRu30Life), [@ShamiWeb3](https://x.com/ShamiWeb3), [@SSSS_CRYPTOMAN](https://x.com/SSSS_CRYPTOMAN), [@Rufus87078959](https://x.com/Rufus87078959), [@Mayz1169](https://x.com/Mayz1169), [@LudovicCreator](https://x.com/LudovicCreator), [@IamEmily2050](https://x.com/IamEmily2050), [@Gwsubsa](https://x.com/Gwsubsa), [@Dheepanratnam](https://x.com/Dheepanratnam), [@David_eficaz](https://x.com/David_eficaz), [@ChrisTheNerv](https://x.com/ChrisTheNerv), [@Artedeingenio](https://x.com/Artedeingenio), [@Alin_Reaper05](https://x.com/Alin_Reaper05), [@AIARTGALLARY](https://x.com/AIARTGALLARY), [@0xbisc](https://x.com/0xbisc), [@zasuko_michiksa](https://x.com/zasuko_michiksa), [@naoyuki_okada](https://x.com/naoyuki_okada), [@john87445528](https://x.com/john87445528), [@cdexsta](https://x.com/cdexsta), [@NimEshed](https://x.com/NimEshed), [@ImperfectEngel](https://web.archive.org/web/*/https://x.com/ImperfectEngel), [@BrennanErbz](https://x.com/BrennanErbz), [@AskVenice](https://x.com/AskVenice), [@AngelNwoha](https://x.com/AngelNwoha), [@umitsuru_fire](https://x.com/umitsuru_fire), [@Yuupapa_free](https://x.com/Yuupapa_free), [@ChrisGwinnLA](https://x.com/ChrisGwinnLA), [@vladimircherner](https://x.com/vladimircherner), [@patchworkfilmuk](https://x.com/patchworkfilmuk), [@sravs_AI_labs](https://x.com/sravs_AI_labs), [@iX00AI](https://x.com/iX00AI), [@ivanka_humeniuk](https://x.com/ivanka_humeniuk), [@crayon1267](https://x.com/crayon1267), [@pan_soramame_da](https://x.com/pan_soramame_da), [@kinopioai_ai](https://x.com/kinopioai_ai), [@a_shimanski](https://x.com/a_shimanski), [@noman23761](https://x.com/noman23761), [@SPEEDAI07](https://x.com/SPEEDAI07), [@lynneatyoumind](https://x.com/lynneatyoumind), [@EHuanglu](https://x.com/EHuanglu), [@tanabe_fragm](https://x.com/tanabe_fragm), [@Reiria123](https://x.com/Reiria123), [@TomaAIbijo](https://x.com/TomaAIbijo), [@LavrionX](https://x.com/LavrionX), [@kinovi_ai](https://x.com/kinovi_ai), [@umesh_ai](https://x.com/umesh_ai), [@Ankit_patel211](https://x.com/Ankit_patel211)

*帰属、ライセンス、削除の修正は出典 URL を添えて issue でお知らせください。*

[出典付きの Seedance 2.0 プロンプトを contribution フローから共有してください。](CONTRIBUTING.md)