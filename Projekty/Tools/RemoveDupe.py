def loaddata(nazev_souboru):
    out = []
    with open(nazev_souboru, 'r', encoding='utf-8') as f:
        for radky in f:
            radky = radky.strip().strip(',')
            out.append(radky)
    return out

filename = input("Enter the filename: ")
data = loaddata(filename)

# Odstraní duplicity a zachová původní pořadí
data = list(dict.fromkeys(data))

for i in range(len(data)):
    print(data[i])

input("Press Enter to exit...")  # Umožní uživateli vidět výstup před ukončením programu