import math

r=int(input("Adja meg a kúp rádiuszát! "))
H=int(input("Adja meg a kúp magasságát! "))
s=int(input("Adja meg a kúp átfogoját! "))

R=math.pow(r,2)
T1=R*3.14
T2=r*3.14*s

V=R*3.14*H/3

A=T1+T2

print(f'A kúp felszíne {A} cm és a térfogata {V} cm.')