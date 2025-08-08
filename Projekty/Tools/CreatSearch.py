import requests

out = []

Movies = requests.get('https://raw.githubusercontent.com/Msnehulak/Python/refs/heads/main/Data/Dictionary/Movies.txt')
Movies = Movies.text.splitlines()
print(Movies)