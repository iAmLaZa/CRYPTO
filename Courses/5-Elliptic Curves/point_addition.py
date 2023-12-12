from Crypto.Util.number import*

a = 497
b = 1768
p = 9739

'''
(a) If P = O, then P + Q = Q.
(b) Otherwise, if Q = O, then P + Q = P.
(c) Otherwise, write P = (x1, y1) and Q = (x2, y2).
(d) If x1 = x2 and y1 = - y2, then P + Q = O.
(e) Otherwise:
  (e1) if P ≠ Q: λ = (y2 - y1) / (x2 - x1)
  (e2) if P = Q: λ = (3x12 + a) / 2y1
(f) x3 = λ2- x1 - x2,     y3 = λ(x1 - x3) - y1
(g) P + Q = (x3, y3)
'''

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

P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)
#S(x,y) = P + P + Q + R

s = add_point(P,add_point(P, add_point(Q, R)))
print(s)