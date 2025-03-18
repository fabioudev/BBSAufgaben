"""Ergebnis wird nur als Halbrichtig angezeigt obwohl es Richtig ist ich werde Herr Jess darauf ansprechen!"""
from random import randint

def wuerfel():
    result = randint(1, 6)
    return result

def main():
    for i in range(3):
        print(wuerfel())

if __name__ == "__main__":
    main()