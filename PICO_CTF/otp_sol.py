from pwn import *

remote = remote('mercury.picoctf.net', 41934)
remote.recvuntil('This is the encrypted flag!\n')
flag = remote.recvlineS(keepends = False)
flag = hex(int(flag, 16))
payload =  b'a' * 49968
remote.sendline(payload)
payload =  b'a' * 32
remote.sendline(payload)
remote.recvuntil('Here ya go!\n')
crypted = remote.recvlineS(keepends = False)
remote.recvuntil('Here ya go!\n')
crypted = remote.recvlineS(keepends = False)
crypted = hex(int(crypted, 16))

payl = 0x6161616161616161616161616161616161616161616161616161616161616161
flag = 0x345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d
crypted = 0x346303d1902033d1959003d1903553d1951553d1907593d1951511a3d190505
print(flag)
print(crypted) 
print(payl)
flag_asci = '{:x}'.format(flag^crypted^payl)
print('flag : '+bytes.fromhex(flag_asci).decode('utf-8'))