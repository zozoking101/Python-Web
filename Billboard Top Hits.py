import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100/"
res = requests.get(url)
print(res)

soup = BeautifulSoup(res.text, 'lxml')

songs = soup.select("li h3")
top_100 = [song.text[14:][0:-5] for song in songs[:100]]
i = 0
for song in top_100:
    i += 1
    print(f"{i} - {song}")
    
