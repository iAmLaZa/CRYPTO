print( 11 % 6 ) 
print(8146798528947 % 17) 


# Fermat's little theorem to calculate x = base^exp mod prime
def fermat_theorem_mod(base, exp, prime):
    if exp == prime:
        return base
    elif exp + 1 == prime and base % prime != 0:
        return 1
    else:
        return -1
print(fermat_theorem_mod(273246787654, 65536, 65537))#  == 1

print(pow(273246787654, 65536, 65537))

# calculate inverse    
from Crypto.Util.number import inverse
print(inverse(3, 13))