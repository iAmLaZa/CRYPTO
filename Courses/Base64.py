# get flag from base64 from string coded as bytes

import base64

base64_bytes = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
base64_string = bytes.fromhex(base64_bytes)
s = base64.b64encode(base64_string) # base64.b64decode(base64_string) -> get flag from base64 from string coded as bytes

print(s)

