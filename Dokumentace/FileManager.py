# out[0] = line1 out[5] = line6
def loaddata(nazev_souboru):
    out = []
    with open(nazev_souboru, 'r', encoding='utf-8') as f:
        for radky in f:
            radky = radky.strip().strip(',')
            out.append(radky)  # Přidá upravený řádek do seznamu
    return out

data = loaddata('file name')


def savedata(seznam, nazev_souboru):
    with open(nazev_souboru, "w") as file:
        for item in seznam:
            file.write(item + "\n")

list = ["data1", "data2", "data3"]
savedata(list, "file name")

