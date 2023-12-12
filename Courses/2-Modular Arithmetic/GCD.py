# Euclid Algo 

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

a = 66528
b = 52920
print(euclid(a,b))
