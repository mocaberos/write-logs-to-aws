### Amazon CloudWatch Logsにログを書き込むためのスクリプト

ローカルに出力されたログをCloudWatch Logsにアップロードする

## requirements
- python >= 3.9
- watchtower(pythonモジュール)

## write-logs-to-aws
CloudWatch Logs の指定のロググループ＆ログストリームにログを出力する
```bash
$ ./write-logs-to-aws log_group log_stream log_message
$ ./write-logs-to-aws '/aws/some-system' 'sample-stream' 'hello-world'
$ # ログメッセージをファイルで指定する場合
$ ./write-logs-to-aws '/aws/some-system' 'sample-stream' -f './logs.txt'
```

## write-logs-to-aws-from-stdin
CloudWatch Logs の指定のロググループ＆ログストリームにログを出力する  
標準入力からログを取り込み、CloudWatch Logsにアップロードするので、他のアプリケーションの出力をこのスクリプトにリダイレクトして使用する
```bash
$ some command | ./write-logs-to-aws-from-stdin log_group log_stream
$ echo 'Some logs' | ./write-logs-to-aws-from-stdin '/aws/some-system' 'sample-stream'
```
1秒ごとログメッセージを出力する`test.py`の場合  
下記のコマンドで、`test.py`の出力はCloudWatch Logsにアップロードされる。
```bash
$ python3 test.py | ./write-logs-to-aws-from-stdin '/aws/some-system' 'sample-stream'
```
