import pyautogui
import time

pyautogui.rightClick()
time.sleep(0.0001)
pyautogui.typewrite(["up","up","up","up","up","enter"],interval=0.0001)

# # 翻訳拡張機能起動
# pyautogui.hotkey('shift', 'alt', 't')
# time.sleep(0.5)
# pyautogui.typewrite(["tab","tab","enter"],interval=0.1)

# # アドレスバーに移動し、翻訳ボタンを押下
# pyautogui.hotkey('ctrl', 'l')
# time.sleep(0.5)
# pyautogui.typewrite(["tab","tab","tab","enter"],interval=0.1)

# time.sleep(0.5)
# pyautogui.press('tab')
# time.sleep(0.1)
# pyautogui.hotkey('shift', 'tab')
# time.sleep(0.1)
# pyautogui.press('enter')
