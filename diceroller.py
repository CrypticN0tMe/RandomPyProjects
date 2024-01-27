import random
Rolls = input("How many rolls: ")

# is valid integer input?
try:
    Rolls = int(Rolls)
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Roll and print results
for x in range(Rolls):
    print(random.randint(1, 6))
