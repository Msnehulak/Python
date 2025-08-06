import random
import requests
import pyperclip

response = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Symbols/Small_abc.txt')
alfabet = response.text.splitlines()

response = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Symbols/Big_ABC.txt')
Alfabet = response.text.splitlines()

response = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Symbols/Symbols.txt')
simbols = response.text.splitlines()

response = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Symbols/Numer.txt')
numer = response.text.splitlines()

while True:
    use = []

    # Default password cfg
    cfg = [16, # long
       1, #alfabet
       1, #Alfabet
       1, #simbols
       1, #numer
       ]
    print("use ./, to split the values and use 0/1 to true or false")
    print("How long, Small alfabet, Big alfabet, Bimbols, Numer")
    incfg = input(":").replace(".",",").split(",")
    for i in range(len(incfg)):
        cfg[i] = int(incfg[i].strip())

    if cfg[1] == 1:
        use += alfabet
    else:
        use += alfabet
    if cfg[2] == 1:
        use += Alfabet
    else:
        use += Alfabet
    if cfg[3] == 1:
        use += simbols
    else:
        use += simbols
    if cfg[4] == 1:
        use += numer
    else:
        use += numer

    random.shuffle(use)

    password = ""
    for i in range(cfg[0]):
        password += use[random.randint(0, len(use) - 1)]
    print(password)
    print("Passwoard is Copied to clipboard")
    pyperclip.copy(password)  # Copy to clipboard

    colone = "-"
    password = password.replace("/", "p")
    if len(password) > 61:
        for _ in range(len(password)):
            colone += "-"

    else:
        for _ in range(61):
            colone += "-"

    print(colone)