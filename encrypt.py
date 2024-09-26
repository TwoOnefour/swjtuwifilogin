# @Time    : 2024/9/26 10:26
# @Author  : TwoOnefour
# @blog    : https://www.pursuecode.cn
# @Email   : twoonefour@pursuecode.cn
# @File    : RSA.py

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from requests import post


def A(password, pwd_key):
    return SHA256.new((pwd_key + password).encode('utf-8')).hexdigest()


def encrypt_data(e, t=None, i=None):
    k = b'a01b23c45d67e89f'
    M = b'09a18b27c36d45ef'

    if t and i:
        k = t.encode()
        M = i.encode()

    cipher = AES.new(k, AES.MODE_CBC, M)
    e_bytes = e.encode()
    encrypted_data = cipher.encrypt(pad(e_bytes, AES.block_size))
    return b64encode(encrypted_data).decode()

def decrypt_data(encrypted_data, t=None, i=None):
    k = b'a01b23c45d67e89f'
    M = b'09a18b27c36d45ef'

    if t and i:
        k = t.encode()
        M = i.encode()

    encrypted_data = b64decode(encrypted_data)
    cipher = AES.new(k, AES.MODE_CBC, M)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data.decode()

def data_struct(phonenum, pwd, name, business_type="IT"):
    return "{" + f'"accout":"{str(phonenum)}","pwd":"{pwd}","name":"{name}","business_type":"{business_type}"' + "}"


def get_pwdkey(phonenum):
    return post("http://10.19.1.1/vcpe/userAuthenticate/queryUserAuthenticatePwdKey", data={
        "accout": phonenum,
    },headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        "WebVersion": "sctel_0925"
    }).json()["data"]["pwd_key"]


def get_dataTK(phonenum, name, password):
    # 获取pwd_key
    pwd_key = get_pwdkey(phonenum)
    # 格式化数据
    data = data_struct(phonenum, A(password=password, pwd_key=pwd_key), name)
    # 加密
    return encrypt_data(data)
