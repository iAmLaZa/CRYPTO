msg = 'this message and the flag are encrypted with AES-CTR'
encrypted_msg = '7a35feb81c72621b35418da53b743687663f5531cdc29f055b15669cc2afbc48c2d00a05821b86123b484fab084e02a9b97a4480'
encrypted_flag = '7d35f2a75072661c235391834f4707972e78622298c89d574e01658294d0ed15f2fd1e45924d9f'

from pwn import xor
key = xor(bytes.fromhex(encrypted_msg), msg.encode())
flag = xor(bytes.fromhex(encrypted_flag), key)
print(flag)


