userInput = input("Enter the a word to check for palindrom: ")

reversedInput = ""

"""
#Möglichkeit 1
for i in range(len(userInput)):
    reversedInput = userInput[i] + reversedInput
"""
"""
#Möglichkeit 2
for i in userInput:
    reversedInput = i + reversedInput
"""
#Möglichkeit 3
i = 0
while i < len(userInput):
    reversedInput = userInput[i] + reversedInput
    i = i + 1

print("The rotated word is: ", reversedInput)

if userInput == reversedInput:
    print("The word is a palindrom!")
else:
    print("the word is not a palindrom!")