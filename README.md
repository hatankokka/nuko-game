# ずっこけぬこゲーム

Streamlitの中に、Matter.jsで作った1人用の落ち物合体ゲームを埋め込んだプロトタイプです。

## 起動

```powershell
streamlit run app.py
```

## 構成

- `app.py`: Streamlitの外枠。ぬこ画像とMatter.jsをHTMLへ埋め込みます。
- `game_template.html`: ゲーム本体。
- `assets/nuko.png`: 提供画像から切り抜いたぬこ素材。
- `assets/bgm.mp3`: BGM。ゲーム内の `BGM ON/OFF` ボタンで切り替えます。
- `assets/matter.min.js`: 物理エンジン。

ゲーム状態はブラウザ内のJavaScriptで動きます。複数人が同じStreamlit URLを開いても、それぞれ別の1人用ゲームとして遊べます。

## BGM

音源: のら猫ミケ太の日常 @ フリーBGM DOVA-SYNDROME OFFICIAL YouTube CHANNEL
https://www.youtube.com/watch?v=vwqzLQu3kvc
