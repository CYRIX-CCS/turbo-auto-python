#if statement

if (3==7):
    print("Three is equal to seven")
else:
    print("Three is not equal to seven")

print("Please input your name: ")
name = input()

if (name == 'Cyril' or name == 'Afumbom'):
    print("Hello bro. How are you doing?")
else:
    print("Invalid input!!")

# elif statement
print("Input your name:")
name1 = input()
print("Input your age: ")
age = input()

if (name1 == 'Alice'):
    print("Hello, Alice")
elif age < 12:
    print("You are not Alice.")