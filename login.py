# @Time    : 2024/9/1 19:39
# @Author  : TwoOnefour
# @blog    : https://www.pursuecode.cn
# @Email   : twoonefour@pursuecode.cn
# @File    : login.py

from requests import post
import encrypt

def login_from_password(phonenum, password):
    dataTK = encrypt.get_dataTK(phonenum=phonenum, password=password, name="下次用RSA吧，别用AES了，太简单了(3小时)")
    res = post("http://10.19.1.1/vcpe/userAuthenticate/authenticate", data={
        "dataTk": dataTK,
    }, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        "WebVersion": "sctel_0925"
    })
    print(res.json())

def check_networking():
    return True if get("http://captive.apple.com", allow_redirects=False).status_code == 200 else False

if __name__ == "__main__":
    if check_networking():
        print("已经连接，退出")
        exit(0)
    login_from_password()