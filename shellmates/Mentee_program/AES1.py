from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify

BLOCK_SIZE = 16

ct = unhexlify("9feac7ca324dc3b92d2371e8e1e723ccc7d6a6c973a241871bcc7ea7d98d7059")
key = unhexlify("85a228f4ac3dc671566213469994e42c")

ecb = AES.new(key, AES.MODE_ECB)
pt = ecb.decrypt(ct)
print(unpad(pt, BLOCK_SIZE).decode())