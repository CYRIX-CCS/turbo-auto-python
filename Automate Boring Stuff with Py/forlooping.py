#introduction to for and range()
print('My name is')
for i in range(2):
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num 
print(total)

#starting, stopping and stepping
for i in range(12,16):
    print(i)
for i in range(0,10,3):
    print(i)