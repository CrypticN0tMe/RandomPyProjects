import TheBigWordlist
import time
wordlist = TheBigWordlist.Wordlist
startTime = time.time()


def digitGuess():
  for Num in range(99999999):
     print(Num)
     if Num == int(pw):
          endTime = time.time()
          elapsedtime = startTime - endTime
          print("The password is: " + str(Num) + str(" Elapsed time: ") + str(elapsedtime))
          break
     
def pwGuess():
   for i in range(wordlist.__len__()):
      serach = wordlist[i]
      print(str("guess: ") + str(i) + str(" >     |") + str(serach))
      if pw == serach:
         print("the password is: " + str(serach))
         break
      
print("1: Guess the number \n2: Guess the password")
choice = input("what type would you like to do? ")

pw = input("whats the password? ")

choice = int(choice)
if choice == 1:
   digitGuess()
if choice == 2:
   pwGuess()