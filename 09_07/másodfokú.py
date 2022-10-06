import math, cmath

a=input('Kérem a másodfokú egyenlet főegyütthatóját: ')
a= float(a)
while a==0:
    print('Ez nem lesz másodfokú egyenlet; nem oldom meg.')
    a= input('Kérem a másodfokú egyenlet főegyütthatóját: ')
    a= float(a)

b=input('Kérem az elsőfokú tag együtthatóját: ')
c=input('Kérem a konstans tagot: ')
b= float(b)
c=float(c)

d= b*b-4*a*c
print('A diszkrimináns értéke', d)

# if d>=0:
#     print("van valós megoldás.")
#     x1= (-b-math)