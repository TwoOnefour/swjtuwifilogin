# @Time    : 2024/9/1 19:39
# @Author  : TwoOnefour
# @blog    : https://www.pursuecode.cn
# @Email   : twoonefour@pursuecode.cn
# @File    : login.py

from requests import post
import encrypt


def login_from_password(phonenum, password, name):

    dataTK = encrypt.get_dataTK(phonenum=phonenum, password=password, name=name)
    res = post("http://10.19.1.1/vcpe/userAuthenticate/authenticate", data={
        "dataTk": dataTK,
    }, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        "WebVersion": "sctel_0925"
    })
    print(res.json())
    if res.json()["result"] == "2":
        for i in res.json()["pointList"]:
            unbind(i)

        login_from_password(phonenum, password, name)  # 递归一次

def unbind(info):
    res = post("http://10.19.1.1/vcpe/userAuthenticate/unBindPortalUserMac", json=info,
                        headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
                            'Content-Type': 'application/json;charset=UTF-8',
                            "WebVersion": "sctel_0925"
                        })
    print(res.json())


if __name__ == "__main__":
    login_from_password("", "", "拿下了，这把确实比较有难度")
