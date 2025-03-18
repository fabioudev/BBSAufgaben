def zahlToMonat(zahl):
    # zahl: Zahl aus dem Bereich 1..12
    # return: Zeichenkette

    if zahl == 1:
        monatsname = 'Januar'
    elif zahl == 2:
        monatsname = 'Februar'
    elif zahl == 3:
        monatsname = 'Maerz'
    elif zahl == 4:
        monatsname = 'April'
    elif zahl == 5:
        monatsname = 'Mai'
    elif zahl == 6:
        monatsname = 'Juni'
    elif zahl == 7:
        monatsname = 'Juli'
    elif zahl == 8:
        monatsname = 'August'
    elif zahl == 9:
        monatsname = 'September'
    elif zahl == 10:
        monatsname = 'Oktober'
    elif zahl == 11:
        monatsname = 'November'
    elif zahl == 12:
        monatsname = 'Dezember'

        """Es muss nur das hinzugefügt werden"""
    else:
        monatsname = ""

    return monatsname