import encoder
import decoder

space = 32
a = 97
b = 98
c = 99
d = 100
e = 101
f = 102
g = 103
h = 104
i = 105
j = 106
k = 107
l = 108
m = 109
n = 110
o = 111
p = 112
q = 113
r = 114
s = 115
t = 116
u = 117
v = 118
w = 119
x = 120
y = 121
z = 122

known = ("ls" or "encode" or "decode")

print("ls - lists dec values with coresponding letter \nencode - encodeds test using decimal\ndecode - decodeds decimal into acsii")

tell = input("whats the cmd? ")

#decode
if tell == "decode":
    decoder.run()

#encode
if tell == "encode":
    encoder.run()

#list the dec values with coresponding letter
if tell == "ls":
    print(" a = 97\n b = 98\n c = 99\n d = 100\n e = 101\n f = 102\n g = 103\n h = 104\n i = 105\n j = 106\n k = 107\n l = 108\n m = 109\n n = 110\n o = 111\n p = 112\n q = 113\n r = 114\n s = 115\n t = 116\n u = 117\n v = 118\n w = 119\n x = 120\n y = 121\n z = 122")