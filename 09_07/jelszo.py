
bejutott= False

while not bejutott:
    felhasznalonev=input('Kérem adja meg a felhasnálónevet. ')
    jelszó = input('Kérem adja meg a jelszót. ')
    if felhasznalonev == 'bori99' and jelszó == 'kismehe<3':
        print('a belépés megengedve.')
        bejutott = True
    else:
        print ('belépés megtagadva')