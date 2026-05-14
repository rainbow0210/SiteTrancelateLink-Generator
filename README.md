# Discord_SiteTrancelateLink-Generator

## Download
[Click](https://github.com/rainbow0210/SiteTrancelateLink-Generator/archive/refs/heads/main.zip)
## Table content

* [English](https://github.com/rainbow0210/SiteTrancelateLink-Generator/#English)
* [Japanese](https://github.com/rainbow0210/SiteTrancelateLink-Generator/#Japanese)

# English
## Expanation
The bot work discord.

Typing link. And, This link change site trancelate link generate.

## Operating Enviroment
* Python 3.10.10

* py-cord 2.4.0

* python-dotenv

## How to use?
1. Install required packages:

```
pip install py-cord python-dotenv
```

2. Create a `.env` file in the project root and write your bot token:

```
token=YOUR_BOT_TOKEN
```

3. Run the bot:

```
python bot.py
```

4. In Discord, use the slash command `/site_trancelate` with this format:

```
/site_trancelate url:https://example.com input:auto output:en
```

Notes:
- `url` must be an `http` or `https` link.
- `input` is the source language. Use `auto` if you want automatic detection.
- `output` is the target language.
- Language codes should follow the Google Cloud language support list.
- This bot uses slash commands, so no prefix is needed.

Command details from `/help`:
- `/help`: Show the command details.
- `/site_trancelate [url] [input language] [output language]`: Convert a website URL into a Google Translate URL.
- Language codes: use the ISO-639 codes shown in the Google Cloud language support list. ( https://cloud.google.com/translate/docs/languages )

## Commands
- `/site_trancelate`: Generate a Google Translate URL for the given website.
- `/help`: Show the command details and language-code guidance.

## LICENCE
MIT LICENCE↓

[https://github.com/rainbow0210/SiteTrancelateLink-Generator/blob/main/LICENCE](https://github.com/rainbow0210/SiteTrancelateLink-Generator/blob/main/LICENCE)

## Extension library and use data
Sorry, almost japanese site...

* Python:[https://www.python.org/](https://www.python.org/)

* Py-cord:[https://github.com/Pycord-Development/pycord](https://github.com/Pycord-Development/pycord)

* Python-dotenv:[https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)

* 【Python】discord.pyが開発終了ということなのでpycordに乗り換えよう:[https://qiita.com/melonade/items/25c038e8e4e6800aa639](https://qiita.com/melonade/items/25c038e8e4e6800aa639)

* pythonで環境ファイルを読み込む:[https://zenn.dev/nakashi94/articles/9c93b6a58acdb4](https://zenn.dev/nakashi94/articles/9c93b6a58acdb4)

* Pythonで先頭のn文字を削除する:[https://www.relief.jp/docs/python-remove-first-n-characters-from-string.html](https://www.relief.jp/docs/python-remove-first-n-characters-from-string.html)

* Pythonで末尾のn文字を削除する:[https://www.relief.jp/docs/python-remove-last-n-characters-from-string.html](https://www.relief.jp/docs/python-remove-last-n-characters-from-string.html)

* 【やってみた】Discordのスラッシュコマンド"/hoge"をpythonで自作してみる...!:[https://tektektech.com/discord-custom-slash-command/](https://tektektech.com/discord-custom-slash-command/)

* Discord Embed Generator:[https://cog-creators.github.io/discord-embed-sandbox/](https://cog-creators.github.io/discord-embed-sandbox/)

* 図解！Pythonのif文でand、orによる複数条件の指定方法を徹底解説！:[https://ai-inter1.com/python-if-andor/](https://ai-inter1.com/python-if-andor/)

* Google Cloud 言語サポート:[https://cloud.google.com/translate/docs/languages](https://cloud.google.com/translate/docs/languages)

* Googleウェブサイト翻訳ツールを自作して多言語ホームページに自動翻訳する:[https://spoke.cloud/ja/gtranslate-using-js/](https://spoke.cloud/ja/gtranslate-using-js/)

# Japanese
## 概要
Discord上で動作する、入力されたリンクのサイトを指定された言語に変換するリンクを生み出すbotです。

## 動作確認済み環境
* Python 3.10.10

* py-cord 2.4.0

* python-dotenv

## 使い方
1. 必要パッケージをインストールします。

```
pip install py-cord python-dotenv
```

2. プロジェクトルートに `.env` ファイルを作成し、Botのトークンを記述します。

```
token=YOUR_BOT_TOKEN
```

3. Botを起動します。

```
python bot.py
```

4. Discord内でスラッシュコマンド `/site_trancelate` を次の形式で実行します。

```
/site_trancelate url:https://example.com input:auto output:en
```

補足:
- `url` には `http` または `https` のURLを指定します。
- `input` は変換元の言語です。自動判定したい場合は `auto` を使えます。
- `output` は変換先の言語です。
- 言語コードはGoogle Cloud 言語サポートの一覧にあるISO-639コードを指定します。
- このBotはスラッシュコマンド方式のため、プレフィックスは不要です。

`/help` の内容:
- `/help`: コマンドの詳細を表示します。
- `/site_trancelate [url] [input language] [output language]`: サイトURLをGoogle翻訳URLに変換します。
- 言語コード: Google Cloud 言語サポート一覧にあるISO-639コードを使います。( https://cloud.google.com/translate/docs/languages )

## コマンド一覧
- `/site_trancelate`: 指定したサイトのGoogle翻訳URLを生成します。
- `/help`: コマンドの詳細と対応言語コードの案内を表示します。

## ライセンス
MIT LICENCE↓

[https://github.com/rainbow0210/SiteTrancelateLink-Generator/blob/main/LICENCE](https://github.com/rainbow0210/SiteTrancelateLink-Generator/blob/main/LICENCE)

## 利用したもの、参考にしたサイト
* Python：[https://www.python.org/](https://www.python.org/)

* Py-cord：[https://github.com/Pycord-Development/pycord](https://github.com/Pycord-Development/pycord)

* Python-dotenv：[https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)

* 【Python】discord.pyが開発終了ということなのでpycordに乗り換えよう：[https://qiita.com/melonade/items/25c038e8e4e6800aa639](https://qiita.com/melonade/items/25c038e8e4e6800aa639)

* pythonで環境ファイルを読み込む：[https://zenn.dev/nakashi94/articles/9c93b6a58acdb4](https://zenn.dev/nakashi94/articles/9c93b6a58acdb4)

* Pythonで先頭のn文字を削除する：[https://www.relief.jp/docs/python-remove-first-n-characters-from-string.html](https://www.relief.jp/docs/python-remove-first-n-characters-from-string.html)

* Pythonで末尾のn文字を削除する：[https://www.relief.jp/docs/python-remove-last-n-characters-from-string.html](https://www.relief.jp/docs/python-remove-last-n-characters-from-string.html)

* 【やってみた】Discordのスラッシュコマンド"/hoge"をpythonで自作してみる...!：[https://tektektech.com/discord-custom-slash-command/](https://tektektech.com/discord-custom-slash-command/)

* Discord Embed Generator：[https://cog-creators.github.io/discord-embed-sandbox/](https://cog-creators.github.io/discord-embed-sandbox/)

* 図解！Pythonのif文でand、orによる複数条件の指定方法を徹底解説！：[https://ai-inter1.com/python-if-andor/](https://ai-inter1.com/python-if-andor/)

* Google Cloud 言語サポート：[https://cloud.google.com/translate/docs/languages](https://cloud.google.com/translate/docs/languages)

* Googleウェブサイト翻訳ツールを自作して多言語ホームページに自動翻訳する：[https://spoke.cloud/ja/gtranslate-using-js/](https://spoke.cloud/ja/gtranslate-using-js/)
