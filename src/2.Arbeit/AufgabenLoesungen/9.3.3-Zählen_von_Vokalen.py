#Möglichkeit 1
userInput = input("Please enter a text: ")

options = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

counter = 0

for i in userInput:
    if i in options:
        counter = counter + 1

print("There are ", counter, "vocals in your text")

"""
#Möglichkeit 2
userInput = input("Please enter a text: ")

options = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

counter = 0

for i in userInput:
    if i == "A" or i =="E" or i =="I" or i =="O" or i =="U" or i =="a" or i =="e" or i =="i" or i =="o" or i =="u":
        counter = counter + 1

print("There are ", counter, "vocals in your text")
"""

"""
#Code für die richtige Antwort in der Aufgabe:
userInput = input()

options = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

counter = 0

for i in userInput:
    if i in options:
        counter = counter + 1

print(counter)
"""