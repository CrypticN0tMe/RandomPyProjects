def normal():
    print("\nNormal pyrimad: ")
    for i in range(int(rows)):
     x = "* "
     x = x*i
     print(f'{x: ^40}')

def invert():
    print("\nReversed pyrimad: ")
    for i in range(int(rows)):
        x = "* "
        x = x*(int(rows)-i)
        print(f'{x: ^40}')

def left():
    print("\nLeft pyrimad: ")
    for i in range(int(rows)):
        x = "* "
        x = x*i
        print(f'{x: <40}')

def right():
    print("\nRight pyrimad: ")
    for i in range(int(rows)):
        x = "* "
        x = x*i
        print(f'{x: >40}')
def box():
    col = input("How many colums? ")
    print("\nBox: ")
    for i in range(int(rows)):
     i = "◊ "
     i = int(col) * i
     print(f'{i: ^30}')

print("\n1: Normal\n2: Invert\n3: Left\n4: Right\n5: Box\n6: All")
option = input("Enter option: ")
rows = input("How many rows? ")

if int(option) == 1:
    normal()
if int(option) == 2:
    invert()
if int(option) == 3:
    left()
if int(option) == 4:
    right()
if int(option) == 5:
    box()
if int(option) == 6:
    normal()
    invert()
    left()
    right()
    box()