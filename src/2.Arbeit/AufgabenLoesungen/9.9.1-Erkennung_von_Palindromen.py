userInput = input("Enter the a word to check for palindrom: ")

reversedInput = ""

for i in range(len(userInput)):
    reversedInput = userInput[i] + reversedInput

print("The rotated word is: ", reversedInput)

if userInput == reversedInput:
    print("The word is a palindrom!")
else:
    print("the word is not a palindrom!")