
import time
from Crypto.Util.number import long_to_bytes , bytes_to_long
import hashlib


{
    'option' : 'get_flag',
}
{
   
    "input_data" : "deadbeef"
}
FLAG = b'crypto{lazarus_come_forth}'


def generate_key():
    current_time = int(time.time())
    print(current_time)

    key = long_to_bytes(current_time)
    print(len(hashlib.sha256(key).digest()))
    return hashlib.sha256(key).digest()


def encrypt(b):
    key = generate_key()
    assert len(b) <= len(key), "Data package too large to encrypt"
    ciphertext = b''
    for i in range(len(b)):
        ciphertext += bytes([b[i] ^ key[i]])
    print(ciphertext)
    return ciphertext.hex()


class Challenge():
    def __init__(self):
        self.before_input = "Gotta go fast!\n"

    def challenge(self, your_input):
        if not 'option' in your_input:
            return {"error": "You must send an option to this server"}

        elif your_input['option'] == 'get_flag':
            return {"encrypted_flag": encrypt(FLAG)}

        elif your_input['option'] == 'encrypt_data':
            input_data = bytes.fromhex(your_input['input_data'])
            return {"encrypted_data": encrypt(input_data)}

        else:
            return {"error": "Invalid option"}


"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""

from pwn import *
import json 
r = remote('socket.cryptohack.org', 13372)

# Wait for the initial prompt
r.recvuntil(b"Gotta go fast!\n")

# Define the input data as a dictionary
input_data = {
    "option": "get_flag"
}

# Send the input as JSON
r.sendline(json.dumps(input_data))

# Receive and parse the response as JSON
response = json.loads(r.recvline())

# Handle the response
if "error" in response:
    print(f"Error: {response['error']}")
else:
    encrypted_flag = response["encrypted_flag"]
    print(f"Encrypted Flag: {encrypted_flag}")
    input_data = {
    "option": "encrypt_data",
    "input_data": encrypted_flag
    }
    # Send the input as JSON
    r.sendline(json.dumps(input_data))

    # Receive and parse the response as JSON
    response = json.loads(r.recvline())
    print(f"plaintext: {bytes.fromhex(response['encrypted_data'])}")  
    

# Close the connection
r.close()
