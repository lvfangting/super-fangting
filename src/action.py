# Author:"lvfangting"
# Date:2022/6/2 17:27
# encoding:"utf-8"
import time
from telnetlib import EC

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.config import*


# 元素定位方式
wayList = ["id", "xptah", "accessibilityId", "className"]

def startup():
    global driver
    driver = webdriver.Remote(url, desired_caps)


def clickAction(type, element):
    if type == wayList[0]:
        driver.find_element(By.ID, element).click()
    if type == wayList[1]:
        driver.find_element(By.XPATH, element).click()
    if type == wayList[2]:
        driver.find_element(MobileBy.ACCESSIBILITY_ID, element).click()

# 输入事件
def sendKeysAction(type, element, content):
    if type == wayList[0]:
        driver.find_element(By.ID, element).send_keys(content)
    if type == wayList[1]:
        driver.find_element(By.XPATH, element).send_keys(content)
    if type == wayList[2]:
        driver.find_element(MobileBy.ACCESSIBILITY_ID, element).send_keys(content)


# 滑动事件
def swipeAction(direction):
    '''
    滑动事件
    :param direction: 方向
    :return:
    '''
    screen_size = driver.get_window_size()   #返回一个当前屏幕宽高的字典
    x = screen_size['width']
    y = screen_size['height']

    if direction == "up":
        driver.swipe(x/2, y*3/4, x/2, y/4)         # 向上滑
    if direction == "down":
        driver.swipe(x/2, y/4, x/2, y*3/4)         # 向下滑
    if direction == "right":
        driver.swipe(x/4, y/2, x*3/4, y/2)         # 向右滑
    if direction == "left":
        driver.swipe(x*3/4, y/2, x/4, y/2)         # 向左滑

# 捕获toast
def catchToast(type,elementValues):
    if type == wayList[1]:
        catchedText = driver.find_element(MobileBy.XPATH, elementValues)
        return catchedText.text

def toast_exist(self, toastmessage):
    toast_loc = ("xpath", "//*[contains(@text,'%s')]" % toastmessage)
    try:
        WebDriverWait(self.driver, 5, 0.2).until(EC.presence_of_element_located(toast_loc))
      # 获取文本内容
        driver.find_element(By.XPATH, toast_loc).text
        return True
    except:
        return False

# 某个元素在当前页面是否存在
def elementIsExist(type, elementValues):
    try:
        if type == wayList[1]:
            driver.find_element(By.XPATH, elementValues)
        elif type == wayList[0]:
            driver.find_element(By.ID, elementValues)
        elif type == wayList[2]:
            driver.find_element(MobileBy.ACCESSIBILITY_ID, elementValues)
        elif type == wayList[3]:
            driver.find_element(By.CLASS_NAME, elementValues)
        return True
    except Exception as e:
        return False







