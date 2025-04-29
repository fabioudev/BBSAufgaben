def gcd(a, b):
    Ergebnis = min(a, b)
    while not (a % Ergebnis == 0 and b % Ergebnis == 0):
        Ergebnis -= 1
    return Ergebnis


class Bruch(object):
    def __init__(self, zaehler, nenner):
        self.zaehler = zaehler
        self.nenner = nenner

    def erweitern(self, faktor):
        self.zaehler *= faktor
        self.nenner *= faktor

    def kuerzen(self, faktor):
        self.zaehler //= faktor
        self.nenner //= faktor

    def vollstaendigKuerzen(self):
        a = gcd(self.zaehler, self.nenner)
        self.zaehler //= a
        self.nenner //= a
