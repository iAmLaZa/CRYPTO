# decode with decalage 

data = open('ch7.bin', 'rb').read()
out = ''
for key in range(26):
    for d in data:
        out += chr(ord(d)-key)
    print (out)

    