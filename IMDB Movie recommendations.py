# import requests
# from bs4 import BeautifulSoup

# url = "https://m.imdb.com/chart/top/?ref_=nv_mv_250"
# res = requests.get(url)
# print(res)

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
movie_list = soup.find('tbody', {'class': 'lister-list'})

rank_list = []
name_list = []
year_list = []
rate_list = []

for movie in movie_list.find_all('tr'):
    rank = movie.find('td', {'class': 'titleColumn'}).get_text(strip = True).split('.')[0]
    name = movie.find('td', {'class': 'titleColumn'}).a.text
    year = movie.find('td', {'class': 'titleColumn'}).span.text.strip('()')
    rate = movie.find('td', {'class': 'ratingColumn imdbRating'}).get_text(strip = True)
    #print(rank, name, year, rate)
    rank_list.append(rank)
    name_list.append(name)
    year_list.append(year)
    rate_list.append(rate)

df = pd.DataFrame()
df['rank'] = rank_list
df['title'] = name_list
df['year'] = year_list
df['rating'] = rate_list
df.to_csv('imdb_top_250_python.csv', index = False)