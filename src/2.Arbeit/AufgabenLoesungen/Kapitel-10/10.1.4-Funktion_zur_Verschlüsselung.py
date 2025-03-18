"""
Die Aufgabe ergibt keinen sinn sie möchte eine Lösung welche nicht heruasgefunden werden kann, ich werde Herr Jess darauf ansprechen!
"""

def encrypt(inputText, inputKey):

    resultText = ""

    for charChr in inputText:

        charOrd = ord(charChr) + inputKey

        resultOrd = 64

        if charOrd > 90:

            while charOrd > 90:

                resultOrd += 1

                charOrd -= 1

        else:

            resultOrd = charOrd

        resultText += chr(resultOrd)

    return resultText


print(encrypt("ASTERIX", 3))

