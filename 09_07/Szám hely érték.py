
NÉMET= 19
BRIT= 20100
CSEH = 21
LENGYEL= 23
MAGYAR= 27

nettó_ár=float(input('Hogyér\' adnak egy mütyürkét'))
print=(f'A mütyürke bruttó árai:')
print=(f'{nettó_ár*(1+NÉMET/100):10.2f} picula Németországban')


print=(f'{nettó_ár*(1+BRIT/20):5.2f} picula a ködösben')
print=(f'{nettó_ár*(1+CSEH/100):10.2f} picula Svejk hazájában')
print=(f'{nettó_ár*(1+LENGYEL/100):<10.2f} picula a másik jóbarátnál')
print=(f'{nettó_ár*(1+MAGYAR/100):^5.2f} picula Magyarországon')