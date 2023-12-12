#print(pow(101,37,22663))
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
e = 65537 
p = 17 
q = 23
N= p*q
phi = (p-1)*(q-1)
d = pow(e,-1,phi)
print(pow(12,e,N)) # 12 is the message
print(pow(301,d,N)) # 301 is the encrypted message

# ----------------------------------------- RSA second part  -------------------------

p = 857504083339712752489993810777

q = 1029224947942998075080348647219


# totient of N
phi = (p-1)*(q-1)   
print(phi %  (p*q))

e = 65537
# prive key
d = pow(e,-1,phi)
print('d = ',d)

c = 77578995801157823671636298847186723593814843845525223303932
print('decrypted message = ',pow(c,d,N))


