inputChar = input("Gib ein Zeichen (A-Z) ein: ")

inputKey = int(input("Gib den Schlüssel ein: "))

inputOrd = ord(inputChar) + inputKey

resultOrd = 64

if inputOrd > 90:
    while inputOrd > 90:
        resultOrd += 1
        inputOrd -= 1
else:
    resultOrd = inputOrd

resultChar = chr(resultOrd)

print(resultChar)