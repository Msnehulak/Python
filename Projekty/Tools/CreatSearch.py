import requests

def savedata(seznam, nazev_souboru):
    with open(nazev_souboru, "w") as file:
        for item in seznam:
            file.write(item + "\n")

def loaddata(nazev_souboru):
    out = []
    with open(nazev_souboru, 'r', encoding='utf-8') as f:
        for radky in f:
            radky = radky
            out.append(radky)  # Přidá upravený řádek do seznamu
    return out
out = []
if True:
    # Movies
    Moviesout  = []
    Movies = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Movies.txt')
    Movies = Movies.text.splitlines()
    toadd = ['', 'IMBb', 'cast', 'awards', 'trailer', 'reviews', 'director', 'soundtrack', 'box office', 'release date', 'free to watch', 'where to watch', 
            'free to download', 'budget', 'runtime', 'language', 'country', 'rating', 'genre', 'production companies', 'distributor', 'writer', 
            'editor', 'cinematography', 'music composer']

    for i in range(len(Movies)):
        for x in range(len(toadd)):
            Moviesout.append(Movies[i] + ' ' + toadd[x])
    print(len(Moviesout), ' Movies')
    out.extend(Moviesout)

    # Series
    Seriesout = []
    Series = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/series.txt')
    Series = Series.text.splitlines()
    toadd = ['', 'IMBb', 'cast', 'awards', 'trailer', 'reviews', 'director', 'soundtrack', 'release date', 'free to watch', 'where to watch', 'free to download', 
            'seasons', 'episodes', 'network', 'status', 'premiere date', 'finale date']

    for i in range(len(Series)):
        for x in range(len(toadd)):
            Seriesout.append(Series[i] + ' ' + toadd[x])
    print(len(Seriesout), ' Series')
    out.extend(Seriesout)

    # Games
    Gamesout = []
    Games = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Games.txt')
    Games = Games.text.splitlines()
    toadd = ['', 'IMBb', 'cast', 'awards', 'trailer', 'reviews', 'director', 'soundtrack', 'release date', 'free download', 'cheats', 'platforms', 'publisher',
            'developer', 'genre', 'rating', 'game modes', 'engine', 'language', 'country', 'budget',]

    for i in range(len(Games)):
        for x in range(len(toadd)):
            Gamesout.append(Games[i] + ' ' + toadd[x])
            if True:  
                if Games == 'World of Warcraft':
                    Gamesout.append(Games[i] + ' ' + 'expansions')
                    Gamesout.append(Games[i] + ' ' + 'classes')
                    Gamesout.append(Games[i] + ' ' + 'raids')
                    Gamesout.append(Games[i] + ' ' + 'dungeons')
                    Gamesout.append(Games[i] + ' ' + 'achievements')
                elif Games == 'The Elder Scrolls V: Skyrim':
                    Gamesout.append(Games[i] + ' ' + 'mods')
                    Gamesout.append(Games[i] + ' ' + 'quests')
                    Gamesout.append(Games[i] + ' ' + 'characters')
                    Gamesout.append(Games[i] + ' ' + 'factions')
                    Gamesout.append(Games[i] + ' ' + 'dlc')
                elif Games == 'League of Legends':
                    Gamesout.append(Games[i] + ' ' + 'ranked')
                    Gamesout.append(Games[i] + ' ' + 'skins')
                    Gamesout.append(Games[i] + ' ' + 'agents')
                elif Games == 'Minecraft':
                    Gamesout.append(Games[i] + ' ' + 'mods')
                    Gamesout.append(Games[i] + ' ' + 'servers')
                    Gamesout.append(Games[i] + ' ' + 'skins')
                    Gamesout.append(Games[i] + ' ' + 'texture packs')
                    Gamesout.append(Games[i] + ' ' + 'worlds')
                elif Games == 'Counter-Strike: Global Offensive' or Games == 'Counter-Strike 2':
                    Gamesout.append(Games[i] + ' ' + 'skins')
                    Gamesout.append(Games[i] + ' ' + 'cases')
                    Gamesout.append(Games[i] + ' ' + 'knives')
                    Gamesout.append(Games[i] + ' ' + 'gloves')
                    Gamesout.append(Games[i] + ' ' + 'stickers')
                    Gamesout.append(Games[i] + ' ' + 'maps')
                    Gamesout.append(Games[i] + ' ' + 'ranked')
                    Gamesout.append(Games[i] + ' ' + 'esports')
                    Gamesout.append(Games[i] + ' ' + 'stickers')
                    Gamesout.append(Games[i] + ' ' + 'corshair')
                    Gamesout.append(Games[i] + ' ' + 'souvenir packages')
                elif Games == 'Valorant':
                    Gamesout.append(Games[i] + ' ' + 'skins')
                    Gamesout.append(Games[i] + ' ' + 'agents')
                    Gamesout.append(Games[i] + ' ' + 'ranked')
                    Gamesout.append(Games[i] + ' ' + 'esports')
                    Gamesout.append(Games[i] + ' ' + 'battle pass')
                    Gamesout.append(Games[i] + ' ' + 'maps')
                    Gamesout.append(Games[i] + ' ' + 'game modes')
                    Gamesout.append(Games[i] + ' ' + 'weapons')
                    Gamesout.append(Games[i] + ' ' + 'abilities')
                    Gamesout.append(Games[i] + ' ' + 'competitive mode')
                    Gamesout.append(Games[i] + ' ' + 'events')
                    Gamesout.append(Games[i] + ' ' + 'corshair')
                elif Games == 'Fortnite':
                    Gamesout.append(Games[i] + ' ' + 'skins')
                    Gamesout.append(Games[i] + ' ' + 'battle pass')
                    Gamesout.append(Games[i] + ' ' + 'emotes')
                    Gamesout.append(Games[i] + ' ' + 'weapons')
                    Gamesout.append(Games[i] + ' ' + 'maps')
                    Gamesout.append(Games[i] + ' ' + 'events')
                    Gamesout.append(Games[i] + ' ' + 'challenges')
                    Gamesout.append(Games[i] + ' ' + 'creative mode')
                    Gamesout.append(Games[i] + ' ' + 'save the world')
                    Gamesout.append(Games[i] + ' ' + 'cross-platform play')
                    Gamesout.append(Games[i] + ' ' + 'competitive mode')
                elif Games == 'Call of Duty: Warzone':
                    Gamesout.append(Games[i] + ' ' + 'skins')
                    Gamesout.append(Games[i] + ' ' + 'weapons')
                    Gamesout.append(Games[i] + ' ' + 'operators')
                    Gamesout.append(Games[i] + ' ' + 'battle pass')
                    Gamesout.append(Games[i] + ' ' + 'maps')
                    Gamesout.append(Games[i] + ' ' + 'events')
                    Gamesout.append(Games[i] + ' ' + 'competitive mode')
                elif Games == 'chess':
                    Gamesout.append(Games[i] + ' ' + 'openings')
                    Gamesout.append(Games[i] + ' ' + 'tactics')
                    Gamesout.append(Games[i] + ' ' + 'endgames')
                    Gamesout.append(Games[i] + ' ' + 'players')
                    Gamesout.append(Games[i] + ' ' + 'tournaments')
                    Gamesout.append(Games[i] + ' ' + 'chess variants')
                    Gamesout.append(Games[i] + ' ' + 'chess engines')
                    Gamesout.append(Games[i] + ' ' + 'chess puzzles')
                elif Games == 'Among Us':
                    Gamesout.append(Games[i] + ' ' + 'skins')
                    Gamesout.append(Games[i] + ' ' + 'hats')
                    Gamesout.append(Games[i] + ' ' + 'pets')
                    Gamesout.append(Games[i] + ' ' + 'maps')
                    Gamesout.append(Games[i] + ' ' + 'game modes')
                    Gamesout.append(Games[i] + ' ' + 'tasks')
                    Gamesout.append(Games[i] + ' ' + 'impostor strategies')
                    Gamesout.append(Games[i] + ' ' + 'crewmate strategies')
    print(len(Gamesout), ' Games')
    out.extend(Gamesout)

    # Company
    Companyout = []
    Company = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Company.txt')
    Company = Company.text.splitlines()
    toadd = ['', 'IMBb', 'revenue', 'employees', 'founded', 'headquarters', 'website', 'industry', 'products', 'services', 'subsidiaries',
            'founders', 'ceo', 'parent company', 'headquarters location', 'headquarters country', 'headquarters city', 'headquarters state', 'headquarters zip code',]

    for i in range(len(Company)):
        for x in range(len(toadd)):
            Companyout.append(Company[i] + ' ' + toadd[x])
    print(len(Companyout), ' Companies')
    out.extend(Companyout)

    # Colors
    Colorsout = []
    Colors = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Colors.txt')
    Colors = Colors.text.splitlines()
    toadd = ['', 'hex code', 'rgb value', 'cmyk value', 'hsl value', 'lab value', 'xyz value', 'pantone value', 
            'web safe color', 'color family', 'color meaning', 'color symbolism', 'color psychology', 'color associations', 'color trends']

    for i in range(len(Colors)):
        for x in range(len(toadd)):
            Colorsout.append(Colors[i] + ' ' + toadd[x])
    print(len(Colorsout), ' Colors')
    out.extend(Colorsout)

    # States
    Statesout = []
    States = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/States.txt')
    States = States.text.splitlines()
    toadd = ['', 'capital', 'population', 'area', 'largest city', 'statehood date', 'abbreviation', 'flag', 'motto', 
            'nickname', 'time zone', 'geographical features', 'economy', 'tourist attractions', 'history', 'culture',
            'government', 'education', 'transportation', 'environmental issues']

    for i in range(len(States)):
        for x in range(len(toadd)):
            Statesout.append(States[i] + ' ' + toadd[x])
    print(len(Statesout),' States')
    out.extend(Statesout)

out.append('Github')
out.append('Gemini')
out.append('chatgpt')

print('Total:', len(out), 'items')

savedata(out, 'RandomSearch.txt')

