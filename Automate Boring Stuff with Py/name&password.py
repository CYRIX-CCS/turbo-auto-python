while True:
    print("What is your name?")
    name = input()
    if name == 'Joe':
        continue
    print("What is your password?")
    password = input()
    if password == 'swordfish234':
        break
print("Access Granted!")