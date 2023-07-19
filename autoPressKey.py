# pip install pyautogui

import time
import pyautogui

def type_key_every_five_seconds():
    """
    1のキーを10回繰り返し、5秒ごとに入力する関数
    """
    for _ in range(10):  # 10回繰り返すループ
        pyautogui.press('1')  # '1'のキーを入力
        time.sleep(5)  # 5秒間待機

if __name__ == "__main__":
    type_key_every_five_seconds()  # 関数の呼び出し