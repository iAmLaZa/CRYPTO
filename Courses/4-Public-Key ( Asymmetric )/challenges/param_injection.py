import pwn
import json
import hashlib
from Crypto.Cipher import AES

host = "socket.cryptohack.org"
port = 13371


def exploit():
    pr = pwn.connect(host, port)
    try:
        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        #p = int(line['p'][2:].strip('f'), 16)
        p = int(line['p'], 16)
        g = int(line['g'], 16)
        A = int(line['A'], 16)

        payload = json.dumps({"p":hex(p),"g":hex(g),"A":hex(p)})
        print(payload, len(payload))
        pr.sendlineafter(": ", payload)

        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        B = int(line['B'], 16)

        payload = json.dumps({"B":hex(p)})
        print(payload, len(payload))
        pr.sendlineafter(": ", payload)

        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        print(line)

        iv = bytes.fromhex(line['iv'])
        encrypted_flag = bytes.fromhex(line['encrypted_flag'])
        sha1 = hashlib.sha1()
        secret = 0
        sha1.update(str(secret).encode())
        key = sha1.digest()[:16]
        aes = AES.new(key, AES.MODE_CBC, iv)
        print(aes.decrypt(encrypted_flag))
    finally:
        pr.close()

exploit()


