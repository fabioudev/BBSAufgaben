 # Initialisierung
L = ['Meier', 'Bauer', 'Moser', 'Molitor', 'Martin']

# Verarbeitung
trifftzu = True
for name in L:
    if name[0] != 'M':
        trifftzu = False


# Ausgabe
if trifftzu:
    print('Alle Namen fangen mit M an.')
else:
    print('Nicht alle Namen fangen mit M an.')