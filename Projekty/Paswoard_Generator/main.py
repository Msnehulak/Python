import random

alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Alfabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
simbols  = [".", ",", "-", "_",";", ":", "=", "+", "+", "-", "*", "/"]
numer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Psword cfg
cfg = [16, # long
       1, #alfabet
       1, #Alfabet
       1, #simbols
       1, #numer
] 

use = []

# add simbols to use 
if cfg[1] == 1:
    use += alfabet
if cfg[2] == 1:
    use += Alfabet
if cfg[3] == 1:
    use += simbols
if cfg[4] == 1:
    use += numer

random.shuffle(use) # random

# print (paswoard)
paswoard = ""
for i in range(cfg[0]):
    paswoard += use[random.randint(0, len(use) - 1)]

print(paswoard)