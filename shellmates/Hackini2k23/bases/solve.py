encoded  = 'RzRaVE1PQldHVTNFR05TREdaQ0RNTUpYR1EzREtOWlRHNUJETU1SVEdRWkRJTVpUR0kyREtSUlRHRVpUTU5LR0dNWlRHTVJWSVlaVE1NWlVHNUNBPT09PQ=='
from base64 import b64decode,b32decode,b16decode

print(b16decode(b32decode(b64decode(encoded))))

