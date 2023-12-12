enc = 'pottl tlhjgoqqo'
plain = 'hello louisette'

# remove spaces
enc = enc.replace(' ', '')
plain = plain.replace(' ', '')

# get dict of enc to plain
d = {}
for i in range(len(enc)):
    d[enc[i]] = plain[i]

enc = 'ytkwbjmilmqy'
plain = 'flagmicroctf'


for i in range(len(enc)):
    d[enc[i]] = plain[i]
    
# rebuild flag if alphaet else keep as is
cipher = 'bjmilmqy{qpkq_fk5_gjbzto_miezq0_mp1xw}'

# find the key for the cipher to permute bjmilmqy to microctf
key = ''
for i in cipher:
    if i in d:
        key += d[i]
    else:
        key += i
print(key)

