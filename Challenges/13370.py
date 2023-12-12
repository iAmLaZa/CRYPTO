import base64
import os
from pwn import *

FLAG = 'crypto{lazarus_come_forth}'


def xor_flag_with_otp():
    flag_ord = [ord(c) for c in FLAG]
    otp = os.urandom(20)
    xored = bytearray([a ^ b for a, b in zip(flag_ord, otp)])
    # make sure our OTP doesnt leak any bytes from the flag
    for c, p in zip(xored, flag_ord):
        assert c != p

    return xored


class Challenge():
    def __init__(self):
        self.before_input = "No leaks\n"

    def challenge(self, your_input):
        if your_input == {"msg": "request"}:
            try:
                ciphertext = xor_flag_with_otp()
            except AssertionError:
                return {"error": "Leaky ciphertext"}

            ct_b64 = base64.b64encode(ciphertext)
            return {"ciphertext": ct_b64.decode()}
        else:
            self.exit = True
            return {"error": "Please request OTP"}


"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""

challenge_instance = Challenge()

# Input to get the encrypted flag
input_data = {
    "msg": "request"
}

# Assuming 'FLAG' is defined and the 'encrypt' function is implemented
response = challenge_instance.challenge(input_data)
print(response)
print(base64.b64decode(response["ciphertext"]))
ciphertext = base64.b64decode(response["ciphertext"])
"""
# OTP decode function without giving otp bruteforce
def decode(cypher):
    # bruteforce otp value plaintext start with crypto{ and end with } without having OTP
    while True:
        otp = os.urandom(20)
        xored = bytearray([a ^ b for a, b in zip(cypher, otp)])
        # bytes to char chr()
        flag_chr = [chr(c) for c in xored]
        flag_chr = ''.join(flag_chr)
        print(flag_chr)
        if flag_chr[0:6] == b'crypto':
            return xored
        else:
            continue
decode(base64.b64decode(response["ciphertext"]))

cypher =b'h\x8fB\x84*\x8d\xa9\xe6d\xa1\x0c\x9cc?U9\x1c\xef\x9f\x83'
otp = b'\x0b\xfd;\xf4^\xe2\xd2\x8a\x05\xdbm\xee\x16L\nZs\x82\xfa\xdc'

print(bytearray([a ^ b for a, b in zip(cypher, otp)]))
"""

def xor_ciphertext_with_otp(ciphertext, otp):
    xored = bytearray([a ^ b for a, b in zip(ciphertext, otp)])
    return xored


# Generate an OTP of the same length as the ciphertext
otp = os.urandom(20)

# XOR the ciphertext with the OTP to obtain the flag
flag = xor_ciphertext_with_otp(ciphertext, otp)

# Print the flag
print("Flag:", flag)