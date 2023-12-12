from Crypto.Util.number import inverse

"""
x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17 
    
"""
N = 5 * 11 * 17
N1 = N // 5
N2 = N // 11
N3 = N // 17

X1 = inverse(N1, 5)
X2 = inverse(N2, 11)
X3 = inverse(N3, 17)

print( (2 * N1 * X1 + 3 * N2 * X2 + 5 * N3 * X3) % N )  