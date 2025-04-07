###### [English](./README.md) | 日本語 
# 概要
これは、VRChatのログファイルからワールド名とユーザ名をエクスポートするPythonスクリプトです。

# インストール
1. Python 3.7.X またはそれ以降のバージョンのPythonをダウンロードして、環境変数を設定する。<br/>
Python Official: https://www.python.org/downloads/ <br/>
Microsoft Store: https://apps.microsoft.com/detail/9ncvdn91xzqp

2. 以下のディレクトリにある VRChat のログを探す:<br/>
 C:/Users/"${username}"/AppData/LocalLow/VRChat/VRChat/output\_log_yyyy-mm-dd_hh-mm-ss.txt

3. ログをPythonスクリプトのあるディレクトリに移動する。<br/>

4. Pythonスクリプトのあるディレクトリの場所でターミナルを開き、以下の手順でPythonスクリプトを実行する:<br/>
```
python vrc_world_user_checker.py log_yyyy-mm-dd_hh-mm-ss.txt
```

5. outputというディレクトリに VRChat\_usrlog_yyyy-mm-dd_hh-mm-ss.txt という名前で、整形されたログファイルが出力される。<br/>

# オプション
```
optical argument:
  -v             ビデオの情報を出力ログに追加する。
  -r dirctory    該当するディレクトリ内のログファイルを変換する。
```

# 出力例
```
2025.03.28 17:26:24 World: かめりあんのワールド
2025.03.28 17:26:42  User: かめりあん
...
```

# 謝辞
[sunasaji](https://github.com/sunasaji) 様のソースコードを改変し、フォークさせていただきました。<br/>
ありがとうございます。

# ライセンス

これらのコードは、フォーク元に基づいてCC0ライセンスです。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

