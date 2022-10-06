import random

#1= fej és a 2 = írás

dobás=random.randint(1,2)
if dobás ==1:
    print('fej')
elif dobás ==2:
    print('írás')
    

print(random.choice['fej','írás'])