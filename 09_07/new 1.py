
'''
a = 3
b = 5
'''
a = int(input('kérek egy számot')) #típuskonverzió
b = int(input('kérek egy másik számot'))
c = a+b
8

a = int(input('kérek egy számot')) #típuskonverzió
b = int(input('kérek egy másik számot'))
c = a+b
35

print(a)
print(b)
print(a+b)
print(c)

print(f'Az {a} és {b} összege {c}-vel egyenlő')

if a>b:
    print(f'a nagyobb mint b')
    print(f'{a} nagyobb mint {b}')
elif b>a:
    print(f'b nagyobb mint a')
    print(f'{b} nagyobb mint {a}')
else:
    print(f'A két szám egyenlő')

if a%2 ==0:
    print('páros')
else:
    print("páratlan")
    
    
# ---------------------
# Feladat
# kérjen 3 számot. háromszög oldalai
# számolja ki a területet és kerülettek

import math

a = int(input('kérek egy számot ')) 
b = int(input('kérek egy második számot '))
c = int(input('kérek egy harmadik számot ')) 

K = a+b+c
s = K/2
T = s*math.sqrt(s-a)*(s-b)*(s-c)
print("A háromszög Kerülete =",K,"cm","és Területe=",T,"cm")
