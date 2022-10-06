#5c
# Naponta legalább 2,5 liter folyadékot kell fogyasztanunk,
# és ivásból nem vagyunk valami jók.  Írjunk programot,
# amelyik bekéri, hogy egy-egy alkalommal hány decit ittunk!
# Teszi mindezt addig, amíg 0 értéket nem adunk meg.
# Minden bekéréskor kiírja, hogy addig hány litert ittunk összesen,
# és ha elérjük a 2,5 litert, akkor erről is megemlékezik.
# 3,5 liter fölött kilép, szépen elbúcsúzva tőlünk.


# megittliter=[]
# összeg=0

# while megittliter != 0:
#     megitt=int(input("Kérlek írd le hogy mennyi litert ittál meg ma! Írd hogy 0 ha kiakarsz lépni. "))
#     if megittliter == 0:
#         break
#     elif megittliter != 0:
#         megittliter.append(megitt)
#         print(megittliter)
    
    
# for liter in megittliter:
#     összeg += megittliter

# if összeg == 2.5:
#     print("Elérted a 2.5 litert!")

# if összeg > 3.5:
#     print("Megittál 3.5 liter fölött! Ügyes vagy! Szia!")
   
össz=0

#walrus (=rozmár) operátor: értéket ad és vissza  is tér vele
while össz <=35 and (ivás:=int(input('Hány decit ittál? '))):
    print(f'Már {(össz:=össz+ivás)/10:3.1f}littert ittál.')
    if össz >= 35:
        print('Már sikerült elérned a 2,5 litert.')
print('Béka nől a hasadba\'!')
    
    

# víz=0
# max=35
# oké=25

# while víz <= oké:
#     eddig=int(input('Hány deciliter folyadékot fogyasztott'))
#     víz=víz+eddig
#     print(víz)
# print('Megittad a napi bevitelt. ')
# while víz < max:
#     még=int(input('Hány deciliter folyadékot fogyasztott? '))
#     víz=víz+még
#     print('Eddig',víz,'dl folyadékot fogyasztottál')
# print('Szia!')
    
