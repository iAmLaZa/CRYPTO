from Crypto.Cipher import AES

import requests
import hashlib
import sys
import binascii

result = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ciphertext_hex = result.json()["ciphertext"]

with open('words', 'r') as f:
    for word in f:
        word = word.strip()
        attempted_key = hashlib.md5(word.encode()).hexdigest()

        ciphertext = bytes.fromhex(ciphertext_hex)
        key = bytes.fromhex(attempted_key)
        cipher = AES.new(key, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(ciphertext)
            result = binascii.unhexlify(decrypted.hex())
            if result.startswith('crypto{'.encode()):
                print("key is %s" % word)
                print(result.decode('utf-8'))
                sys.exit(0)
        except ValueError as e:
            continue