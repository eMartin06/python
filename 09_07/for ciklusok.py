
from tracemalloc import start


a= 1

for _ in range(5):
    print(a)
    a +=1

c=1
b=5

lista=['A', 'B', 'C','d']
for x in lista:
    print (x)
    
# while c<b:
#     print(c)
#     c+=1
    
for i in range(2,101):
    print(i)

# for i in range(2,101,2):
#     print(i)
    
for n in range(101,2):
    print(n)
   
összeg=0    
for i in range(2,101):
    összeg=összeg+i
    print(összeg)

szám=0
while szám !=100:
    szám=szám+1
    print(szám)
    
szöveg=input("Kérem adja meg a nevét! ")
print(szöveg)
szöveghossz=len(szöveg)
print(szöveghossz)
print(szöveg[:2])
print(szöveg.find('e'))

for:
print(szöveg.upper)