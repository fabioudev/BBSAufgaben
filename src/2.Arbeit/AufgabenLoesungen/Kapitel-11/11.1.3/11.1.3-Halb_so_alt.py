# Import von Bausteinen
from tageszaehlen import *
# Verwendung der Bausteine
# Initialisierung
datumGeburt = (11, 11, 2002)
datumHeute = (1, 1, 2021)
# Verarbeitung
anzahlTage = 0
datum = datumGeburt
while datum != datumHeute:
    datum = naechstesDatum(datum)
    anzahlTage = anzahlTage + 1
anzahlTage = anzahlTage / 2
datum = datumGeburt
while anzahlTage > 0:
    datum = naechstesDatum(datum)
    anzahlTage = anzahlTage - 1
# Ausgabe
print("geboren am:", datumGeburt)
print("heute:", datumHeute)
print("halb so alt am:", datum)