pw = input("whats the password? ")

def guess():
  for Num in range(99999):
     print(Num)
     if Num == int(pw):
          print("The password is " + str(Num))
          break
     
guess()