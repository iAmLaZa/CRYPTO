import requests
import json
from Crypto.Util.strxor import strxor
from pwn import xor

def get_cookie():
	url='https://aes.cryptohack.org/flipping_cookie/get_cookie/'
	response=requests.get(url)

	return response.json()

def get_flag(cookie,iv):
	url='https://aes.cryptohack.org/flipping_cookie/check_admin/'
	response=requests.get(url+'/'+cookie+'/'+iv)

	return response.json()

data=get_cookie()['cookie']

iv=bytes.fromhex(data[:32])


text=b'admin=False;expi'  #taking only the initial block... since that's only required
forge_text=b'admin=True;expir'

xor_result=xor(iv,text)
forge_iv=xor(xor_result,forge_text).hex()
print(len(forge_iv))
print(get_flag(data[32:],forge_iv))