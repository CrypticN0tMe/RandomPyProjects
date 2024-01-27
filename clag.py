def is_even(number):
    if number % 2 == 0: # number = 4, 2 goes into 4 2 times no remainder so its == to 0 so print even
        print(number, "is even.")
    else:
        print(number, "is odd.")

number = int(input("Enter a number: "))
is_even(number)
