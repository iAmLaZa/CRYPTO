from Crypto.Util.number import *

a = 497
b = 1768
p = 9739

def add_point(p1, p2):
    if p1 == (0, 0):
        return p2
    if p2 == (0,0):
        return p1
    
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 and y1 == -y2:
        return (0, 0)

    lamda = 0
    if p1 == p2:
        lamda = ((3*pow(x1,2,p)+a) * inverse(2*y1, p))
    else:
        lamda = ((y2-y1) * inverse(x2-x1, p))
        
    x3 = (pow(lamda, 2) - x1 - x2) % p
    y3 = (lamda*(x1 - x3) - y1) % p 
    return (x3, y3)

'''
Input: P in E(Fp) and an integer n > 0
1. Set Q = P and R = O.
2. Loop while n > 0.
  3. If n ≡ 1 mod 2, set R = R + Q.
  4. Set Q = 2 Q and n = ⌊n/2⌋.
  5. If n > 0, continue with loop at Step 2.
6. Return the point R, which equals nP.
'''
P = (2339, 2213)
n = 7863
#1. Set Q = P and R = O.
Q = P
R = (0, 0)
while n > 0:
  #If n ≡ 1 mod 2, set R = R + Q.
  if n % 2 == 1:
      R = add_point(R, Q)
  #Set Q = 2 Q and n = ⌊n/2⌋.
  Q = add_point(Q, Q)
  n = n//2

print(R)