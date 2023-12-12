from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import unhexlify

BLOCK_SIZE = 16

ct = unhexlify("e0e90f1f918ee114086e16d635da2144e31db14d4835d1b3998c1f16130fce73bd2afe3497cb05d6262393c7d210ba27")
key = unhexlify("8b729dada26bf7e4bba2fac435146805")
iv = unhexlify("29e1177a276c7aae4562b391cc648c96")

cbc = AES.new(key, AES.MODE_CBC, iv)
pt = cbc.decrypt(ct)
print(unpad(pt, BLOCK_SIZE).decode())