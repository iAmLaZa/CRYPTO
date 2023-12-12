"""
P=(xP​,yP​), then P+(xP,xP+yP)=OP+(xP​,xP​+yP​)=O
. In other word, −P=(xP,xP+yP)−P=(xP​,xP​+yP​)
"""

#Q=−P=(8045,(8045+6936)mod9739)=(8045,2803) 
x1 , y1 = 8045 , 6936
p= 9739 
print(x1 , (x1+y1) % p)