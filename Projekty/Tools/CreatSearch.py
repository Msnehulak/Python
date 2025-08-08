import requests

out = []

# Movies
Movies = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Movies.txt')
Movies = Movies.text.splitlines()
toadd = ['', 'IMBb', 'cast', 'awards', 'trailer', 'reviews', 'director', 'soundtrack', 'box office', 'release date', 'free to watch', 'where to watch', 
         'free to download', 'budget', 'runtime', 'language', 'country', 'rating', 'genre', 'production companies', 'distributor', 'writer', 
         'editor', 'cinematography', 'music composer']

for i in range(len(Movies)):
    for x in range(len(toadd)):
        out.append(Movies[i] + ' ' + toadd[x])

# Series
Series = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/series.txt')
Series = Series.text.splitlines()
toadd = ['', 'IMBb', 'cast', 'awards', 'trailer', 'reviews', 'director', 'soundtrack', 'release date', 'free to watch', 'where to watch', 'free to download', 
         'seasons', 'episodes', 'network', 'status', 'premiere date', 'finale date']

for i in range(len(Series)):
    for x in range(len(toadd)):
        out.append(Series[i] + ' ' + toadd[x])
        
print(len(out))



