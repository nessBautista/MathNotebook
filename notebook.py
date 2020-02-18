from vector import Vector 
from math import acos
#Initial operations
v1 = Vector([1,2,3])
v2 = Vector([1,2,3])
v3 = Vector([-1,2,3])
print(v1)
print(v1 == v2)
print(v1 == v3)

#Basic Operation: Plus, Minus, Scalar multiplication
#Addition
v1 = Vector([8.218,-9.341])
v2 = Vector([-1.129, 2.111])
print(v1.plus(v2))
#Substraction
v1 = Vector([7.119, 8.215])
v2 = Vector([-8.223, 0.878])
print(v1.minus(v2))
#Multiplication
v1 = Vector([1.671, -1.012, -0.318])
print(v1.times_scalar(7.41))
#Magnitude
v1 = Vector([-0.221, 7.437])
v2 = Vector([8.813, -1.331, -6.247])
v3 = Vector([5.581, -2.136])
v4 = Vector([1.996, 3.108, -4.554])
print(v1.magnitude())
print(v2.magnitude())
print(v3.normalized())
print(v4.normalized())

#Dot product 
v1 = Vector([7.887, 4.138])
w1 = Vector([-8.802, 6.776])
v2 = Vector([-5.955, -4.904, -1.874])
w2 = Vector([-4.496, -8.755, 7.103])

v3 = Vector([3.183, -7.627])
w3 = Vector([-2.668, 5.319])
v4 = Vector([7.35, 0.221, 5.188])
w4 = Vector([2.751, 8.259, 3.985])

print(v1.dot(w1))
print(v2.dot(w2))
print(v3.angle(w3))
print(v4.angle(w4, in_degrees=True))
#Parallels and ortogonal
v1 = Vector([-7.579, -7.88])
w1 = Vector([22.737, 23.64])

v2 = Vector([-2.029, 9.97, 4.172])
w2 = Vector([-9-231, -6.639, -7.245])

v3 = Vector([-2.328, -7.284, -1.214])
w3 = Vector([-1.821, 1.072, -2.94])

v4 = Vector([2.118, 4.827])
w4 = Vector([0,0])

print(v1.is_parallel_to(w1))
print(v2.is_parallel_to(w2))
print(v3.is_parallel_to(w3))
print(v4.is_parallel_to(w4))

print(v1.is_ortoghonal_to(w1))
print(v2.is_ortoghonal_to(w2))
print(v3.is_ortoghonal_to(w3))
print(v4.is_ortoghonal_to(w4))


#Test error exception
#v1 = Vector([0,0])
#print(v1.normalized())

