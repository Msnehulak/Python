import requests

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
out.extend(Companyout)

print(len(out))



