import hashlib


hash = "de2a3f8d53d7aa5200ef995c6b26f8cf57189df86d986d93f8c2a926c0bd8f8e"
wordlist = open("/usr/share/wordlists/rockyou.txt")

while True:
    word = wordlist.readline().strip("\n")
    hash_test = hashlib.sha256(word.encode()).hexdigest()
    if hash_test == hash:
        print("shellmates{" + word + "}")
        exit()