# Funktionsdefinitionen
def verschiebung(zeichen, schluessel):
    basis = ord('A')
    zahl = ord(zeichen) - basis
    neueZahl = (zahl + schluessel) % 26
    neuesZeichen = chr(basis + neueZahl)

    return neuesZeichen


def verschluesselung(text, schluessel):
    verschluesselt = ''
    for zeichen in text:
        if 'A' <= zeichen <= 'Z':
            verschluesselt += verschiebung(zeichen, schluessel)
        else:
            verschluesselt += zeichen  # Nicht-Buchstaben bleiben unverändert
    return verschluesselt

"""Aufgabe:"""
# Funktionsdefinition zur Entschlüsselung
def entschluesselung(inputText, inputKey):
    inputKey = -inputKey
    return verschluesselung(inputText, inputKey)