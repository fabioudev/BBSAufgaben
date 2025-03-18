userInput = input("Enter a word wich consists of capital letters: ")

result = ""

for i in userInput:

    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        i = i + "B" + i

    result = result + i

print("Your encrypted answer is: ", result)

"""#Code für die Richtige Antwort in der Aufgabe:
userInput = input()

result = ""

for i in userInput:

    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        i = i + "B" + i

    result = result + i

print(result)

"""