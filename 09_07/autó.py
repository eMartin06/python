#feladat
#név
#autómárka
#gyártó ország
#végsebbeség


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
