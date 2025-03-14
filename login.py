# @Time    : 2025/3/14 14:24
# @Author  : TwoOnefour
# @blog    : https://www.voidval.com
# @Email   : twoonefour@voidval.com
# @File    : login.py

# 这是教学区的登陆脚本
import requests
from urllib import parse

# override default parse


def quote(s):
    return parse.quote(s, "!'()*-._~")


userId = "" # 账号（明文）
password = "g" # 密码(明文）
url = "http://192.168.189.136/eportal/InterFace.do?method=login" # 门户url，自己抓包
# 下面这个参数自己抓包，一般是url后面params的一长串字符
queryString = "wlanuserip%3D4df84511326d1517d302ff4ef7b6661b%26wlanacname%3Dad2a18598f6edfa5%26ssid%3Dc1cadd92d30be06d%26nasip%3Dbc3a5111bbeef2b19e9d2f01e2a4536e%26mac%3D33d96316b8a6cfde246857f83a9aafd8%26t%3Dwireless-v2%26url%3D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30"
params = {
    "userId": quote(userId),
    "password": quote(password),
    "service": "",
    "queryString": queryString,
    "operatorPwd": "",
    "operatorUserId": "",
    "validcode": "",
    "passwordEncrypt": False,
}


res = requests.post(url, data=params)

