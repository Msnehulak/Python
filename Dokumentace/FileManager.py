# out[0] = line1 out[5] = line6
def loaddata(nazev_souboru):
    out = []
    with open(nazev_souboru, 'r', encoding='utf-8') as f:
        for radky in f:
            radky = radky.strip().strip(',')
            out.append(radky)  # Přidá upravený řádek do seznamu
    return out

data = loaddata('file name')
