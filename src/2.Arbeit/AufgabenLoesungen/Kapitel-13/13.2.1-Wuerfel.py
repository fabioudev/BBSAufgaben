from random import randint
class Wuerfel:
    def __init__(self):
        self.augen = randint(1, 6)

    def werfen(self):
        self.augen = randint(1, 6)


w = Wuerfel()
print(1 <= w.augen <= 6)