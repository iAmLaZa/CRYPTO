import primefac
n = 510143758735509025530880200653196460532653147
p = primefac.ecm(n)
q = n // p
print(min(p, q))

from sympy.ntheory import factorint

factorint(510143758735509025530880200653196460532653147)


from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
from factordb.factordb import FactorDB

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373


f = FactorDB(n)
f.connect()
p , q = f.get_factor_list()

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
pt = pow(ct, d, n)
flag = long_to_bytes(pt)
print(flag)