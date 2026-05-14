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

4. In Discord, use the slash command `/site_trancelate` and enter the URL you want to translate, the source language, and the target language.

Notes:
- This bot uses slash commands, so no prefix is needed.
- Language codes should follow the Google Translate language list.
- If the link is not an HTTP or HTTPS URL, the bot replies with an error embed.

## Commands
- `/site_trancelate <url> <input> <output>`: Generate a Google Translate URL for the given website.
- `/help`: Show command details and supported language-code information.

Example:

```
/site_trancelate url:https://example.com input:auto output=en
```

Response:

```
https://translate.google.com/translate?sl=auto&tl=en&u=https://example.com
```

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

4. Discord内でスラッシュコマンド `/site_trancelate` を実行し、翻訳したいURL、入力言語、出力言語を指定します。

補足:
- このBotはスラッシュコマンド方式のため、プレフィックスは不要です。
- 言語コードはGoogle翻訳の対応一覧にあるものを指定してください。
- `http` または `https` で始まらないリンクはエラーになります。

## コマンド一覧
- `/site_trancelate <url> <input> <output>`: 指定したサイトのGoogle翻訳URLを生成します。
- `/help`: コマンドの詳細と対応言語コードの案内を表示します。

例:

```
/site_trancelate url:https://example.com input:auto output=en
```

返却例:

```
https://translate.google.com/translate?sl=auto&tl=en&u=https://example.com
```

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
