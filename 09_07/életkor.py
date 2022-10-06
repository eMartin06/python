
'''
nev = input("Kérem adja meg a nevét ")
print(nev)
ÉV = 2022
udv = (f'Üdvözöllek {nev}')
print(udv,"szép napot kívánok neked", sep=" ")
eletkor = int(input("kérem adja meg a születési évét "))
eletk = ÉV- eletkor

if eletk < 14:
    print=("Te általános iskolás vagy.")

if eletk >= 14 and eletk < 18:
    print("Te középiskolás vagy.")

if eletk >= 18:
    print("Te felnőtt vagy.")
    
'''

#feladat
#név
#autómárka
#gyártó ország
#végsebbeség

'''
név=input("Mi a gépjármű neve? ")
autómárka=input("Mi a(z) "+név+" márkája? ")
gyártóország=input("Hol készül a(z) "+név+ "? ")
végsebbeség=int(input("Mennyivel megy a(z) " +név+ "? "))
mondat1 = gyártóország + ' vidéken készül a(z) ' +név+ ", ami " + str(végsebbeség)+ 'km/h'
print(mondat1)

#str.format() a következő 5 példa
mondat2 = '{} Vidékein készül a {}, ami {} km/h végsebességre lépes.'.format(gyártóország, név, végsebbeség)

print(mondat2)

#számozható
mondat3a = '{0} vidékein készül a {1}, ami {2} km/h végsebességre képes.' .format(gyártóország, név, végsebbeség)
print(mondat3a)

#elnevezhető
mondat4a = '{g} vidékein készül a {n}, ami {v} km/h végsebességre képes.' .format(g=gyártóország, n=név, v=végsebbeség)
print(mondat4a)

#vegyes
mondat3a = '{0} vidékein készül a {1}, ami {v} km/h végsebességre képes.' .format(gyártóország, név, v=végsebbeség)
print(mondat3a)

#f' string
mondat6a = f'{gyártóország} vidékein készül a {név}, ami {végsebbeség} km/h végsebességre képes.' 
print(mondat6a)

#testreszabható, a változók értékének egyszerű kiírása
print(f'{gyártóország=}, {név=}, {végsebbeség=}')
'''
#Olvassuk be, hogy hány picula egy mütyürke nettó ára, majd írjuk ki
#a bruttó árakat a német (19%), a brit (20%), a cseh (20%),
#a lengyel (23%) és a ma
#

NÉMET= 19
BRIT= 20
CSEH = 21
LENGYEL= 23
MAGYAR= 27

nettó_ár=float(input('Hogyér\' adnak egy mütyürkét'))
print=(f'A mütyürke bruttó árai:')
print=(f'{nettó_ár*(1+NÉMET/100):10.2f} picula Németországban')

print=(f'{nettó_ár*(1+BRIT/100):10.2f} picula a ködösben')