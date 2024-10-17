# @Time    : 2024/9/26 10:26
# @Author  : TwoOnefour
# @blog    : https://www.pursuecode.cn
# @Email   : twoonefour@pursuecode.cn
# @File    : RSA.py

from Crypto.Hash import SHA256
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from requests import post
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

def A(password, pwd_key):
    return SHA256.new((pwd_key + password).encode('utf-8')).hexdigest()


def encrypt(plain, public_key):  # 你不会以为加个js我就不会写了吧
    key = RSA.importKey(public_key)

    cipher = Cipher_pkcs1_v1_5.new(key)
    cipher_text = b64encode(cipher.encrypt(plain.encode('utf-8')))
    # print(cipher_text.decode('utf-8'))
    return cipher_text.decode('utf-8')



def encrypt_data(e, t=None, i=None):
    """Encrypts a message using RSA and then AES.

    Args:
        e: The message to be encrypted.
        t: The AES key. If None, a default key is used.
        i: The AES initialization vector (IV). If None, a default IV is used.

    Returns:
        The encrypted message as a Base64 encoded string.
    """
    public_key = """-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0bS+TqzQwUXRH1Rvn2Pd\nYd3xGWtZSC2gjFhDdws8UGAk4Y/pS/KPZ38EIOZzuPa5Y7TIDTwPISfVe1elDiVL\nZD0s4L9U6QwTwo2J45C+7HuiggQWGxvnCxSI6fxij8EUZ0P/Tsth+VwipMLEl9I3\nhQiijiz6Cg/hoyLDeZsBbEaE6hgnTF1CD99LNiTi5ZODHv0Zr6VCH0LMXRp4zNjS\no3DIr8ZmwuVVraIrzP0ySWRAuBI0pHb/IY0bn/zdiYsdVeWr/z98rNw8gDwx6Mcr\nuu//vrK3x2FHxERBTNgHzCBaPijAICNj4S9/vhfuaeXYGp0hPg4NfFwtgtQmF+6Y\n8wIDAQAB\n-----END PUBLIC KEY-----"""
    rsa_encrypted = encrypt(e, public_key)

    T = ["s", "b", "2", "5", "0"]
    default_key = "".join(I(["G", "2", "I", "5", "8", "9", "0", "8", "7", "K", "1", "K", "0", "9", "5", "G"], len(T))).lower()
    default_iv = "".join(I(["1", "J", "2", "5", "4", "6", "I", "1", "K", "J", "2", "0", "K", "8", "H", "7"], len(T))).lower()

    key = t if t else default_key.encode('utf-8')
    iv = i if i else default_iv.encode('utf-8')

    cipher_aes = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher_aes.encrypt(pad(rsa_encrypted.encode('utf-8'), AES.block_size))

    return b64encode(ciphertext).decode('utf-8')

def I(e, t):
    """Shifts letters in a string by a given amount.

    Args:
        e: The string to shift.
        t: The shift amount.

    Returns:
        The shifted string.
    """
    return "".join([
        chr(((ord(char.lower()) - ord('a') - t) % 26) + ord('a')).upper() if 'a' <= char.lower() <= 'z' else char
        for char in e
    ])

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
    return "{" + f'"accout":"{str(phonenum)}","pwd":"{pwd}","name":"{name}","business_type":"{business_type}","law_token":"vcpe"' + "}"


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

if __name__ == "__main__":
    print(
    decrypt_data("jF7XJ31Vnyfy0SK0AzxsZ4VO7Knbn1Dw13AeWRdQflWnOuRR%2BRV3cXIhAsY7OSGVTvzJh3G%2BWJI2tWNQxUL5nHBGgK4NZJljNFsVyhkI%2BpADwP993v62CksquyxMOsSPXtWa0%2F%2FObvhd6hfGBGP%2FCBZSFhw7jSAADVWHrFjvo68mfcfR37EyFUeO3L0IRLwI"
                 ))
