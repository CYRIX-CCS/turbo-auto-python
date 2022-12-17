import random, sys

for i in range(4):
    print(random.randint(0,9))

while True:
    print("Type 'leave' to exit")
    exit = input()
    if exit == 'leave':
        sys.exit()
    print('You typed '+ exit +'')
