"""
1秒ごとログメッセージを出力する、テスト用スクリプト
"""

from time import sleep

for i in range(10):
    print(f'AAAAAAAA - {i}', flush=True)
    sleep(1)
