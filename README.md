# ずっこけぬこゲーム / Zukkoke Nuko Game

## 日本語

Streamlitの中に、Matter.jsで作った1人用の落ち物合体ゲームを埋め込んだプロトタイプです。

このゲームは、商用を目的としない無料のゲームとして制作しています。

### 起動

```powershell
streamlit run app.py
```

### 機能

- Web/スマホ表示対応
- 日本語、英語、フランス語、韓国語、中文簡体、中文繁体、タイ語、インドネシア語、ベトナム語のUI切替
- BGM ON/OFF
- ブラウザごとのベストスコア保存

### 構成

- `app.py`: Streamlitの外枠。ぬこ画像、BGM、Matter.jsをHTMLへ埋め込みます。
- `game_template.html`: ゲーム本体。
- `assets/nuko.png`: ぬこ素材。
- `assets/bgm.mp3`: BGM。ゲーム内の `BGM ON/OFF` ボタンで切り替えます。
- `assets/matter.min.js`: 物理エンジン。

ゲーム状態はブラウザ内のJavaScriptで動きます。複数人が同じStreamlit URLを開いても、それぞれ別の1人用ゲームとして遊べます。

### 出典・クレジット

元投稿・素材出典:
[ぺろり](https://x.com/maid_Pelori) / [@maid_Pelori](https://x.com/maid_Pelori) さん

https://x.com/maid_Pelori/status/2066760278558302679?s=20

BGM:
のら猫ミケ太の日常 @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL

https://www.youtube.com/watch?v=vwqzLQu3kvc

## English

This is a prototype single-player falling merge game built with Matter.js and embedded in Streamlit.

This game is made as a free, non-commercial game.

### Run

```powershell
streamlit run app.py
```

### Features

- Web and mobile-friendly layout
- UI language selector for Japanese, English, French, Korean, Simplified Chinese, Traditional Chinese, Thai, Indonesian, and Vietnamese
- BGM ON/OFF toggle
- Best score saved per browser

### Project Structure

- `app.py`: Streamlit wrapper. Embeds the nuko image, BGM, and Matter.js into the HTML.
- `game_template.html`: Main game implementation.
- `assets/nuko.png`: Nuko image asset.
- `assets/bgm.mp3`: BGM, controlled by the in-game `BGM ON/OFF` button.
- `assets/matter.min.js`: Physics engine.

Game state runs in browser-side JavaScript. Multiple people can open the same Streamlit URL and each play an independent single-player session.

### Credits

Original post / asset source:
[ぺろり](https://x.com/maid_Pelori) / [@maid_Pelori](https://x.com/maid_Pelori)

https://x.com/maid_Pelori/status/2066760278558302679?s=20

BGM:
のら猫ミケ太の日常 @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL

https://www.youtube.com/watch?v=vwqzLQu3kvc
