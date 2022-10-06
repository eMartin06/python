import math
import random


# r=int(input("Adja meg hogy hány cm legyen a sugár! "))
# m=int(input("Adja meg hogy hány cm legyen a magasság! "))

r=random.randint(2,10)
m=random.randint(2,10)

Ta= math.pow(r*2)*math.pi
Tp= 2*math.pi*r*m
terfogat= Ta*m
felszin= 2*Ta+Tp

print=(f"{terfogat:10.2f}cm")
print=(f"{felszin:10.2f}cm")
