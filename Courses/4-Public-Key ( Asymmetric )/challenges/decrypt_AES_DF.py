from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import inverse
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode())
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    try :
        if is_pkcs7_padded(plaintext):
            return unpad(plaintext, 16).decode('ascii')
        else:
            return plaintext.decode('ascii')
    except :
        pass


g = 2
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
A= 112218739139542908880564359534373424013016249772931962692237907571990334483528877513809272625610512061159061737608547288558662879685086684299624481742865016924065000555267977830144740364467977206555914781236397216033805882207640219686011643468275165718132888489024688846101943642459655423609111976363316080620471928236879737944217503462265615774774318986375878440978819238346077908864116156831874695817477772477121232820827728424890845769152726027520772901423784
b = 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944
B= 1241972460522075344783337556660700537760331108332735677863862813666578639518899293226399921252049655031563612905395145236854443334774555982204857895716383215705498970395379526698761468932147200650513626028263449605755661189525521343142979265044068409405667549241125597387173006460145379759986272191990675988873894208956851773331039747840312455221354589910726982819203421992729738296452820365553759182547255998984882158393688119629609067647494762616719047466973581
shared_secret = pow(A,b,p)
iv = '737561146ff8194f45290f5766ed6aba'
ciphertext = '39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c'


flag = decrypt_flag(shared_secret, iv, ciphertext) 
print(flag)


p = '0xde26ab651b92a129'
g =  '0x2' 
A = '0x134363e72ef66c00'
B = '0xf19eb055223140'
iv = '157ea53b2c3371919866bcddd291adf1'
encrypted_flag = '67e29af93b42c14244bab867f3e0c0c873f3dc1ef35fe72add137d12446b347b'


p = int(p, 16)
print('p',p)
g = int(g, 16)
print('g',g )
A = int(A, 16)
print('A',A)
B = int(B, 16)
print('B',B)
a= 7665764431027655738
b= 1568073818339345044
sc = pow(A,b,p)
shared_secret = pow(B,a,p) 
print(decrypt_flag(shared_secret, iv, encrypted_flag))
print(decrypt_flag(sc, iv, encrypted_flag))

from sympy import mod_inverse

def discrete_log(a, b, m):
    # Calculate the modular inverse of 'a' mod 'm'
    a_inv = mod_inverse(a, m)
    
    # Compute the discrete logarithm
    return  pow(a_inv, b, m)


result = discrete_log(68009949567004992, 2, 16007670376277647657)
print(f"The discrete {result}")


# https://www.alpertron.com.ar/DILOG.HTM to get a nd b from A and B

""" 
from pwn import *
import json
from math import log


con = remote('socket.cryptohack.org', 13379)

print(con.recv().decode())
print(con.recv().decode())

data = {}
# Downgrade to 64
supported = ["DH64"]
data['supported'] = supported
data = str(data).replace('\'', '"')
con.send(data)

print(con.recv().decode())
data = con.recv().decode().split('\n')[0]
print('data: ', data)
#data = {}
#data["chosen"] = "DH64"
#data = str(data).replace('\'', '"')
con.send(data)

print(con.recv().decode())
data = con.recv().decode().split('\n')
alice_data = json.loads(data[0])
p = int(alice_data['p'], 16)
print('p: ', p)
g = int(alice_data['g'], 16)
print('g: ', g)
A = int(alice_data['A'], 16)
print('alice data: ', alice_data)
begin_ind = data[1].find('{')
bob_data = json.loads(data[1][begin_ind:])
print('bob data: ', bob_data)
begin_ind = data[2].find('{')
alice_second_data = json.loads(data[2][begin_ind:])
print('alice data: ', alice_second_data)
"""