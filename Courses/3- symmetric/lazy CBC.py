import requests

url_base = 'http://aes.cryptohack.org/lazy_cbc'

BLOCK_SIZE = 16
ZERO = b'\0' * 16

def hack():
  response = requests.get(url="%s/encrypt/%s" % (url_base, ZERO.hex())).json()

  # This is E_K(K) since our plaintext is 0
  ciphertext = bytes.fromhex(response['ciphertext'])

  # This is 0 || E_K(K), which makes 0 be the ciphertext
  # which is XOR'd with K after E_K(K) is decrypted.
  ciphertext = ZERO + ciphertext
  response = requests.get(url="%s/receive/%s" % (url_base, ciphertext.hex())).json()

  # Now, we can extract the decrypted output, which is D_K(0) || K, and pull out K.
  plaintext = bytes.fromhex(response['error'][len('Invalid plaintext: '):])
  key = plaintext[BLOCK_SIZE:] # K is the second block

  response = requests.get(url="%s/get_flag/%s" % (url_base, key.hex())).json()
  return bytes.fromhex(response['plaintext']).decode()

if __name__ == '__main__':
  flag = hack()
  print(flag)