def postpone(inputChar, inputKey):

    inputOrd = ord(inputChar) + inputKey
    resultOrd = 64

    if inputOrd > 90:
        while inputOrd > 90:
            resultOrd += 1
            inputOrd -= 1
    else:
        resultOrd = inputOrd
    resultChar = chr(resultOrd)
    return resultChar

print(postpone('P', 7))
print(postpone('A', 3))
print(postpone('T', 10))
print(postpone('Z', 1))
print(postpone('X', 2))