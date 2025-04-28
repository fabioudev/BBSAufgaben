L = ['Meier', 'Bauer', 'Moser', 'Molitor', 'Schmitt', 'Ludwig', 'Schmitt']
name = 'Schmitt'

def letzter_index(list, nameInput):
    ergebnis = -1
    for i in range (len(list)):
        if list[i] == nameInput:
            ergebnis = i
    return ergebnis

print(letzter_index(L, name))