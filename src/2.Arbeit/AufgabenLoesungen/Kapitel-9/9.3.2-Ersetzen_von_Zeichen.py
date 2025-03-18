textInput = input("Please enter a text: ")

oldCharinput = input("Please enter a character that will be replaced: ")

newCharInput = input("Please enter a text that will replace your choice: ")

result = ""

for i in textInput:

    if i == oldCharinput:
        i = newCharInput

    result = result + i

print("Your result is: ", result)

"""
#Code für die richtige Antwort in der Aufgabe: 
textInput = input()

oldCharinput = input()

newCharInput = input()

result = ""

for i in textInput:

    if i == oldCharinput:
        i = newCharInput

    result = result + i

print(result)
"""