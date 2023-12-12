e = 65537
N = 1018261336751023520497560395829454421245429586704872293236600679847605951423419167478189648109263
flag  = 713822463491939628949080236459794906441914407944768290378695739068636927695199214947719158013040

from Crypto.Util.number import inverse , long_to_bytes
from factordb.factordb import FactorDB

#factorize N 
f = FactorDB(N)
f.connect()
p,q = f.get_factor_list()
phi = (p-1)*(q-1)
d = inverse(e,phi)
print(long_to_bytes(pow(flag,d,N)).decode())