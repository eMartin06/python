
barack=int(input("Hány mázsa barack van? "))
barack_ár=int(input("Hány forintba kerül a barack? "))
barack_érték=barack_ár*100*barack

korte=int(input("Hány mázsa körte van? "))
korte_ár=int(input("Hány forintba kerül a körte? "))
korte_érték=korte_ár*100*korte

if barack>korte:
    print("A barackból több mázsa van.")
    
elif barack<korte:
    print("A körtéből több mázsa van.")

else:
    print("egyenlő")

if barack_ár>korte_ár:
    print("A barack több forintba kerül.")

elif barack_ár<korte_ár:
    print("A körte több forintba kerül.")

else:
    print("egyenlő az áruk")

if barack_érték>korte_érték:
    print("A barack értéke nagyobb mint a körtélyé")
    
elif barack_érték<korte_érték:
    print("A körte értéke nagyobb mint a baracké")

else:
    print("A barack és a körte értéke egyenlő")