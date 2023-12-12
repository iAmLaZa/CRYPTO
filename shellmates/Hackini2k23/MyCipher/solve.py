from pwn import xor
from Crypto.Util.number import bytes_to_long,long_to_bytes, getPrime

def Decryptphase1(string):
    return xor(string, b'leet')

def Decryptphase2(enc):
    e = 65537
    p = 61571454303089397514579603620349373049341652571832994202527081254304368292533
    q = 59664824358038218622178548968528898444289564045465867369823072940589283303949
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    return long_to_bytes(pow(bytes_to_long(enc),d,p*q))

def Decryptphase3(val):
    res=b''
    start = 0
    
    if len(val)%2 == 0:
        end = len(val) -1
    else:
        end = len(val)
        
    for i in range(start,end , 2 ):
        res += long_to_bytes(val[i])
        
    end = 0
    if len(val)%2 == 0:
        start = len(val)-1
    else:
        start = len(val)-2
    for i in range(start,end , -2 ):
        res += long_to_bytes(val[i])
    return res

def decrypt(enc):
    return Decryptphase1(Decryptphase2(Decryptphase3(enc)))
enc = open("enc.bin","rb").read()
print(decrypt(enc))
