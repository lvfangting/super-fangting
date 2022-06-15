# Author:"lvfangting"
# Date:2022/6/2 16:50

# 设备初始化
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'LIO_AN00',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',
    'resetKeyboard': "true",
    # 'unicodeKeyboard': "true"
    "automationName": "UIAutomator2"
}
# appuim地址
url = "http://localhost:4723/wd/hub"


