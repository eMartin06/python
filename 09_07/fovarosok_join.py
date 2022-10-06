#import random



fovarosok=[]
fovarosok= ["Bécs", "Bern", "Párizs", "London", "Budapest", "Varsó", "Prága", "Róma", "Madrid", "Helsinki", "Moszkva",]
fváros = None
while fváros !='':
    print ('fvárosk jelenleg:' , ', '.join(fovarosok))
    fváros = input("Kérek egy fvársot! ")
    if fváros !="":
        fovarosok.append(fváros)
#n = random.randint(1,len(fovarosok)-1)

for index, főváros in enumerate(fovarosok): #enumerate: számozd be!
    print(index, főváros)

#n = int(subset)
#print('A számítógép szerint ez a főváros a legszebb:', fovarosok[n])

while len(fovarosok)> 0:
    print('fovarasaink:', ', '.join(fovarosok))
    melyik=input('Melyik főváros a legszebb, válaszd ki! ')
    if melyik in fovarosok:
        fovarosok.remove(melyik)
    elif melyik == '':
        break
    else:
        print('Ilyen város nincs a listába')
    