# Author:"lvfangting"
# Date:2022/6/5 16:57
# encoding:"utf-8"
# 字典-登录失败原因及xpath相对路径
loginFailureReason = {
    "手机号填写错误": "//*[@text = '手机号填写错误']",
    "请输入正确的手机号": "//*[@text = '请输入正确的手机号']",
    "请输入密码": "//*[@text = '请输入密码']",
    "账号密码错误": "//*[@text= '帐号或密码错误']",
}

for failureReason in loginFailureReason:
    if failureReason is not None:
        print(loginFailureReason.get(failureReason))