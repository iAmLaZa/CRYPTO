from  pwn import xor


string = 'label'
xored = "".join(chr(ord(a) ^ 13) for a in string)
print(xored)

# xor label with 13
label = xor('label', 13)
print(label)



# Given values on the challenge question

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


# Solving for individual key values

key2 = xor(bytes.fromhex(key1_2), key1)
key3 = xor(bytes.fromhex(key2_3), key2)

key1_2_3 = xor(bytes.fromhex(key1_2), key3)


flag = xor(bytes.fromhex(flag_key123), key1_2_3)


print(flag.decode())


bytes_string = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(255):
    results = [chr(a ^ i) for a in bytes_string]
    flag = "".join(results)
    if "crypto" in flag:
        print(flag)
        break
#########################################

message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
 
result = xor(message[:7], "crypto{")
key = result.decode() +'y'
key = (key * (len(message)//len(key)+1))[:len(message)]
print(xor(message, key))


