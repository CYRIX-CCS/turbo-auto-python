def a():
 print('a() starts')
 b()
 d()
 print('a() returns')
def b():
 print('b() starts')
 c()
 print('b() returns')
def c():
 print('c() starts')
 print('c() returns')
def d():
 print('d() starts')
 print('d() returns')
a()
print()
print()


def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
            print('Error: Invalid argument.')
print(spam(2))
print(spam(0))
print(spam(42))