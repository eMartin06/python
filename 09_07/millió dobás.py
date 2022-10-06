from gettext import find
import random
dobáslista=[]

for _ in range(1000000):
    dobás=random.randint(1,6)
    
dobáslista.append(dobás)    
    
számláló=0    
if dobáslista == 6 :
    számláló+=1
print(számláló)