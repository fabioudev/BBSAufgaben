# Funktionsdefinitionen

def schaltjahr(jahr):
    # jahr: int
    # return: Wahrheitswert
    # Beispiele
    """
    >>> schaltjahr(2012)
    True
    >>> schaltjahr(2100)
    False
    >>> schaltjahr(2000)
    True
    """

    if (jahr % 400 == 0) or ((jahr % 4 == 0) and not (jahr % 100 == 0)):
        return True
    else:
        return False


def anzahlTageImMonat(monat, jahr):
    # monat: natürliche Zahl aus dem Bereich 1..12
    # jahr: natürliche Zahl
    # return: natürliche Zahl aus dem Bereich 1..31
    # Beispiele:
    """
    >>> anzahlTageImMonat(2, 2012)
    29
    >>> anzahlTageImMonat(3, 2012)
    31
    """

    if monat in [1, 3, 5, 7, 8, 10, 12]:
        anzahl = 31
    elif monat in [4, 6, 9, 11]:
        anzahl = 30
    elif schaltjahr(jahr):
        anzahl = 29
    else:
        anzahl = 28
    return anzahl


def naechstesDatum(datum):
    # datum: Tupel mit 3 Zahlen zur Datumsbeschreibung
    # return: Tupel zur Beschreibung des Folgedatums
    # Beispiele:
    """
    >>> naechstesDatum((21, 1, 2012))
    (22, 1, 2012)
    >>> naechstesDatum((31, 1, 2012))
    (1, 2, 2012)
    >>> naechstesDatum((31, 12, 2012))
    (1, 1, 2013)
    """

    (tag, monat, jahr) = datum
    if tag < anzahlTageImMonat(monat, jahr):
        tag = tag + 1
    elif monat < 12:
        tag = 1
        monat = monat + 1
    else:
        tag = 1
        monat = 1
        jahr = jahr + 1
    return (tag, monat, jahr)


# Testaufrufe

print(naechstesDatum((31, 1, 2021)))