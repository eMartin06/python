#között a ,,nap őse˝ versenyre. Aki tíz bogyónál kevesebbet hoz, az ,,zsenge˝
#aki husznál többet, az ,,nagy koponya˝, mindenki más pedig ,,gyüjtögető˝
#minősitést kap
 


név=input('Mi az ős neve? ')
bogyók= int(input("Hány bogyója van? "))

if bogyók <10:
    minősités= "zsenge"
elif bogyók > 20:
    minősités = 'Nagy koponya'
else:
    minősités= 'gyüjtögető'

print(f'{név} egy {minősités}.')