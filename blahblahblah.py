#goal: start with fiest charecter build to last c, cr, cry, cryp, crypt

import win32api

z = win32api.GetUserName() #Z == username crypt
x = z.__len__()            # says that crypt has 5 characters

for i in range(x):         # loops 5 times
    print(z.)               # prints crypt