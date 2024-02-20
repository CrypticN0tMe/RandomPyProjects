wl = open(r"C:\Users\Crypt\OneDrive\code\hey.txt", "r")

myne = wl.read()

serach = input("Whats the keyword? ")

if serach == str("ls"):
    print(myne)
    quit

x = myne.__contains__(serach)

if x == True or serach == str("ls"):
    print("Found: " + str(serach))
else:
    print('Not found')
    file = open(r"C:\Users\Crypt\OneDrive\code\hey.txt", 'a')
    file.writelines(str(' "') + serach + str('",'))