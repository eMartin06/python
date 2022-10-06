
kedd=int(input("Hány forintott költöttél el kedden? "))
szerda=int(input("Hány forintott költöttél el szerdán? "))

if kedd>szerda:
    print("Kedden többet költöttél,",kedd,"Ft-ot.")
    
elif kedd<szerda:
    print("Szerdán többet költöttél,",szerda,"Ft-ot.")
    
else:
    print("Kedden és szerdán ugyanannyit költöttél.")