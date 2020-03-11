from selenium import webdriver
import pyautogui
import time
import random

driver = webdriver.Chrome()
driver.get("https://login.taobao.com")
driver.maximize_window()

# 跳过webdriver
def rTime():
    return random.random()*2
# #模拟鼠标，键盘
time.sleep(rTime())
pyautogui.press('f12')
time.sleep(rTime())
pyautogui.moveTo(976,119)
time.sleep(rTime())
pyautogui.click(clicks=1)
time.sleep(rTime())
# 输入文本
#注意：将输入法切换到系统默认输入的英语
pyautogui.typewrite('Object.defineProperties(navigator,{webdriver:{get:()=>undefined}});')
time.sleep(rTime())
pyautogui.press('enter')
time.sleep(rTime())
pyautogui.press('f12')
time.sleep(rTime())
# 1191,335
pyautogui.moveTo(1191,335,duration=2)
pyautogui.click()

# 输入账号和密码
# 1000,480
pyautogui.moveTo(1000,480,duration=2)
pyautogui.click()
pyautogui.typewrite("密码")
# 1000,415
pyautogui.moveTo(1000,415,duration=2)
pyautogui.click()
pyautogui.typewrite("账号(手机号)")

# 1030,539
pyautogui.moveTo(1030,539,duration=3)
pyautogui.click()