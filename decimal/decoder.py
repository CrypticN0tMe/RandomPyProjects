#lowercase = 97 - 122
#uppercase = 65 - 90

def run():
    decode = input("what would you like to decode? ")
    text = decode
    decoded1 = text.replace("97", "a")
    decoded2 = decoded1.replace("98", "b")
    decoded3 = decoded2.replace("99", "c")
    decoded4 = decoded3.replace("100", "d")
    decoded5 = decoded4.replace("101", "e")
    decoded6 = decoded5.replace("102", "f")
    decoded7 = decoded6.replace("103", "g")
    decoded8 = decoded7.replace("104", "h")
    decoded9 = decoded8.replace("105", "i")
    decoded10 = decoded9.replace("106", "j")
    decoded11 = decoded10.replace("107", "k")
    decoded12 = decoded11.replace("108", "l")
    decoded13 = decoded12.replace("109", "m")
    decoded14 = decoded13.replace("110", "n")
    decoded15 = decoded14.replace("111", "o")
    decoded16 = decoded15.replace("112", "p")
    decoded17 = decoded16.replace("113", "q")
    decoded18 = decoded17.replace("114", "r")
    decoded19 = decoded18.replace("115", "s")
    decoded20 = decoded19.replace("116", "t")
    decoded21 = decoded20.replace("117", "u")
    decoded22 = decoded21.replace("118", "v")
    decoded23 = decoded22.replace("119", "w")
    decoded24 = decoded23.replace("120", "x")
    decoded25 = decoded24.replace("121", "y")
    decoded26 = decoded25.replace("122", "z")
    decoded27 = decoded26.replace(" ", "")
    decoded28 = decoded27.replace("32", " ")

    print(decoded28)