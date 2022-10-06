# Prog tételek csoportosítása
# Egy szorzathoz egy érték
t=[3,8,2,4,5,1,6]
t1=['d', 'f', 'g', 'h', 'j', 'k', 'k', 'u']

# osszeg=0
# for num in t:
#     osszeg = osszeg + num

# print("Összeg: ", osszeg)


# osszeg=0
# szorzat=1
# konkat = ' ' //konkatenáció
# for num in t:
#     osszeg = osszeg + num
#     szorzat = szorzat * num
#     konkat = konkat +num
# print("Összeg: ", osszeg)
# print("Szorzat: ", szorzat)
# print("Szorzat: ", szorzat)

#megszámol = lent(t)
# count = 0
# for num in t:
#     if num > 5:
#         count = count +1

# print("5-nél nagyobb: ", count)


# n = len(t)
# ker = 5

# i = 0
# while i < n and t[i] != ker:
#     i = i +1

# if i<n:
#     print("Van ilyen: ", ker)
# else:
#     print("Nincs ilyen: ", ker)

n=len(t)
ker = 5

i=0
while t[i] != ker:
    i = i +1
    
print("Hányadik helyen van: ", i+1)