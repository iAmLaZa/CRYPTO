from Crypto.Cipher import AES
import base64
import random

MIN_RANGE = 1
MAX_RANGE = 10000000000
ENCRYPT_MSSG = "Message to encrypt : "
OUT_FILENAME = "enc"
DEFAULT_SEED = 10
KEY_LEN = 16

genKey = lambda : bytes([random.randint(0, 255) for _ in range(KEY_LEN)])

class Encryptor:
    def __init__(self, seed = DEFAULT_SEED):
        self.__seed = seed
    
    def setSeed(self):
        random.seed(self.__seed)

    def pad(self, plaintext):
        padding = b' ' * (16 - len(plaintext) % 16)
        return plaintext + padding

    def encrypt(self, mssg):
        plaintext = mssg.encode()
        plaintext = self.pad(plaintext)
        key = genKey()
        print(key)
        cipher = AES.new(key, AES.MODE_ECB)

        ciphertext = cipher.encrypt(plaintext)

        return base64.b64encode(ciphertext).decode()
    def decrypt(self, ciphertext ):
        ciphertext = base64.b64decode(ciphertext)
        key = b'\x10\xdb\xf7\x07i\xec\xfb\x8eR\x11\xfa\xa7&\x7f\xb8\x16'
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext)

        return plaintext.decode()
    
#key = genKey()

# creating a new instance of the encryptor
encryptor = Encryptor()

# setting the __seed to a random unpredictable value
encryptor.__seed = random.randint(MIN_RANGE, MAX_RANGE)

# updating the random seed value
encryptor.setSeed()

# readin user input 
mssg = input(ENCRYPT_MSSG)
"""
random.seed give as always the same value
sooo we need to find the seed and encrypt again the message and we get key and we decrypt the flag
# encrypting the uesr input
enc = encryptor.encrypt(mssg)
plain = encryptor.decrypt(enc)
print(plain)

#plain = encryptor.decrypt(enc)
seed= encryptor.__seed
#print(seed)

ec = Encryptor(seed=seed)
ec.setSeed()
enc1 = ec.encrypt("laza")




with open(OUT_FILENAME, "w") as f:
    f.write(enc)
"""
# read enc file
enc = open(OUT_FILENAME, "r").read()
plain = encryptor.decrypt(enc)
print(plain)

