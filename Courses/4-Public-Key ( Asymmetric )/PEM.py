# ----------------------------------------- RSA third part read private key from PEM file  -------------------------
from Crypto.PublicKey import RSA
# read private key from PEM file
key = RSA.importKey(open('privacy_enhanced_mail.pem').read())
# print private key decimale value
print(key.d)