# extended Euclidean function

def extended_euclidean(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, x, y) = extended_euclidean(b, a % b)
        return (d, y, x - y * (a // b))
    
p = 26513 
q = 32321

a , u ,v = extended_euclidean(p, q)

from GCD import euclid

gcd = euclid(p, q)
print("gcd = ", gcd)
print(p*u + q*v == gcd)