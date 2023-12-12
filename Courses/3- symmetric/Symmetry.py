import requests
import json


def encrypt_flag():
    url = "http://aes.cryptohack.org/symmetry/encrypt_flag/"
    response = requests.get(url)
    return response.json()['ciphertext']

def get_plain(plain,iv):
    url='https://aes.cryptohack.org/symmetry/encrypt'
    response=requests.get(url+'/'+plain+'/'+iv)
    return response.json()['ciphertext']

encrypt_flag = encrypt_flag()
iv=encrypt_flag[:32]

plain = get_plain(encrypt_flag[32:],iv)
print(bytes.fromhex(plain))

