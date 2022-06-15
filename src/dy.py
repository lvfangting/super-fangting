# Author:"lvfangting"
# Date:2022/6/2 16:49
# coding=utf-8
import os
import time
import action
from src.data import *


# 清除app数据
os.popen("adb shell pm clear com.ss.android.ugc.aweme")

# 启动APP
action.startup()
print("INfo：app已启动")
time.sleep(3)

# 首页弹窗处理
for popupName in dict_popup:
    if action.elementIsExist(action.wayList[1], dict_popup.get(popupName)):
        action.clickAction(action.wayList[1], dict_popup.get(popupName))
        print("INFo:" + popupName + "弹窗点击成功")
        time.sleep(3)
    else:
        print("INFo:" + popupName + "元素未找到")


time.sleep(3)
action.swipeAction("up")
print("INfo：向上滑动")

time.sleep(2)
action.swipeAction("down")
print("INfo：向下滑动")


time.sleep(2)
action.swipeAction("right")
print("INfo：向右滑动")

time.sleep(2)
action.swipeAction("left")
print("INfo：向左滑动")

# 点击拍摄按钮调起登录
action.clickAction("id", "com.ss.android.ugc.aweme:id/ou0")
print("INfo:点击拍摄按钮调起登录")

time.sleep(2)
action.clickAction("accessibilityId", "密码登录，按钮")
print("INFo:选择'密码登录'")

# time.sleep(2)
# action.clickActionAccessibilityId("同意并登录, 按钮")
# print("INFo:点击【同意并登录】button，同意隐私协议")

time.sleep(2)
action.sendKeysAction("id", "com.ss.android.ugc.aweme:id/k1l", phone)
print("INfo:输入手机号")

time.sleep(2)
action.sendKeysAction("id", "com.ss.android.ugc.aweme:id/kxf", passwd)
print("INFo:输入密码")

time.sleep(2)
try:
    action.clickAction("id", "com.ss.android.ugc.aweme:id/loy")
    print("INFo:勾选隐私协议")
except Exception as e:
    print("未定位到隐私协议勾选框，跳过~")

time.sleep(2)
action.clickAction("accessibilityId", "登录, 按钮")
time.sleep(0.5)
# 判断是否登录成功
for failureReason in loginFailureReason:
    if action.elementIsExist("xpath", loginFailureReason.get(failureReason)):          # 输入框红字报错
        print("INFo:登录失败，失败原因为：" + failureReason)
    elif action.catchToast("xpath", loginFailureReason.get(failureReason)) is not None:   # toast提示报错
        print("INFo:登录失败，失败原因为toast：" + failureReason)

    else:
        print("INFo:登录成功")
