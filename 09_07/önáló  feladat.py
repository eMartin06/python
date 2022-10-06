
OLVADÁSI_PONT= 1539
FORRÁSI_PNT= 2750

hőfok=int(input("Hőfok: "))
hőfok=float(input("Hőfok: "))

if hőfok < OLVADÁSI_PONT:
    print("szilárd")
if hőfok < FORRÁSI_PNT:
    print("Folyékony")
else:
    print("Gáz")