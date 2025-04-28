# Implementieren Sie hier alle Funktionen in einer Datei.
# 1) naechste_primzahl(a)
# 2) primzahlen_in_intervall(a, b)
# 3) primfaktoren(n)

def primzahl(n):
    prim = True
    if n == 1:
        prim = False
    else:
        i = 2
        while i <= n - 1:
            if n % i == 0:
                prim = False
            i += 1
    return prim

def naechste_primzahl(a):
    jetzigePrimzahl = a
    jetzigePrimzahl += 1
    while not primzahl(jetzigePrimzahl):
        jetzigePrimzahl += 1
    return jetzigePrimzahl

def primzahlen_in_intervall(a, b):
    zahlAnfang = a
    zahlEnde = b
    primzahlen = []
    for i in range (zahlAnfang, zahlEnde):
        if primzahl(i):
            primzahlen.append(i)
    return primzahlen

def primfaktoren(n):
    primfaktoren = []
    teiler = 2
    while n > 1:
        while n % teiler == 0:
            primfaktoren.append(teiler)
            n //= teiler
        teiler += 1
    return primfaktoren

print(naechste_primzahl(17))
print(primzahlen_in_intervall(10, 20))
print(primfaktoren(60))