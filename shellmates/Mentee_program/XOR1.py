import binascii


KEY = "simpleXor"

enc = b'4\x06\x02\x14L\x0f7\rRRI%\x15\x1e\x00x\x06\x01S\x10\x02\x05\x1eE>\x03\x13\x14I\x1e\x18\t\t4\x02\x13\x07\x0c\x1e\x0b\x14U*0;\x006\\=\x1c**X\x13\x1d\x1d29":\x1b\x1d\x0b\x03^"/;**^6\x0e'
msg = ""
l = len(KEY)

# xor enc with key 
plain = [chr(enc[i] ^ ord(KEY[i % l])) for i in range(len(enc))]
print("".join(plain))