import requests

def savedata(seznam, nazev_souboru):
    with open(nazev_souboru, "w") as file:
        for item in seznam:
            file.write(item + "\n")

out = []

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


print(len(out))

savedata(out, 'RandomSearch.txt')

