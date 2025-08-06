import random
import requests

response = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Symbols/Small%20abc.txt')
alfabet = response.text.splitlines()

response = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Symbols/Big%20ABC.txt')
Alfabet = response.text.splitlines()

response = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Symbols/Symbols.txt')
simbols = response.text.splitlines()

response = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Symbols/Numer.txt')
numer = response.text.splitlines()

print(alfabet)
print(Alfabet)
print(response)
print(numer)

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