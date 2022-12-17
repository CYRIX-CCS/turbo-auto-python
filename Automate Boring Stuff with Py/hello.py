# This program says hello and asks for my name

print('Hello World')
print("What is your name?")

myName = input()

print('It is nice to meet you  '+ myName)
print()
print('The length of your name is: ')
print(len(myName))
print("What is your age? ")
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')

print("Input two numbers: ")
number1 = input()
number2 = input()

if((number1 == 0) & (number2 == 0)):
    print("Nice choice! Run the program again")
else: 
    print("Input random numbers")
