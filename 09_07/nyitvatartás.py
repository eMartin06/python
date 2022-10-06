
ora = int(input("Hány óra van? "))
if ora >= 8 and ora <16:
    print(f'A bolt nyitva van')
    meg_ennyit_van_nyítva= 16-ora
    print(f'Ennyi  órád van még még ma boltba menni: {meg_ennyit_van_nyítva}')
else:
    print(f'A bolt zárva van')