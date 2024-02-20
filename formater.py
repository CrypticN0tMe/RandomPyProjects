data = open(r"C:\Users\Crypt\Downloads\xato-net-10-million-passwords.csv", "r")

wordlist = []
stuff = data.read()

newstuff = stuff.replace("\n", '", _')
newnewstuff = newstuff.replace("_", '"')

wordlist.append(newnewstuff)

with open(r"C:\Users\Crypt\OneDrive\code\hey.txt", "w") as file:
    file.write(str(wordlist))
