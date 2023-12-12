import random
from string import ascii_lowercase, digits
flag = "ctn44vmunc{3ghgsy_uto_coo2_gc_2asyoxg1ec}"

chars = ascii_lowercase + digits

random.seed(2 ** 1337 - 1)

shuffled_chars = [i for i in chars]
random.shuffle(shuffled_chars)
shuffled_chars = "".join(shuffled_chars)


enc = ""
for i in flag:
    if i.isalnum():
        enc += chars[shuffled_chars.index(i)]
    else:
        enc += i

print(enc)
