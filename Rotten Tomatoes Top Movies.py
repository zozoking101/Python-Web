# import requests
# from bs4 import BeautifulSoup

# url = "https://editorial.rottentomatoes.com/guide/popular-movies/"
# res = requests.get(url)
# print(res)

# soup = BeautifulSoup(res.text, 'lxml')

# movies = soup.select("h2 a")
# top_years = soup.find_all(class_="subtle start-year")
# top_scores = soup.find_all(class_="tMeterScore")
# top_movies = [movie.text for movie in movies]

# i = 0
# j = 0
# k = 0
# for movie in top_movies:
#     i += 1
#     print(f"{i} - {movie}")
# for score in top_scores:
#     j += 1
#     print(f"{j} - {score.text}")
# for year in top_years:
#     k += 1
#     print(f"{k} - {year.text}")

# import requests
# from bs4 import BeautifulSoup


# class Movie:
#     def __init__(self, name, year, score):
#         self.name = name
#         self.year = year
#         self.score = score

#     def __str__(self):
#         return f"{self.name} ({self.year}) - {self.score}"


# url = "https://editorial.rottentomatoes.com/guide/popular-movies/"
# res = requests.get(url)
# soup = BeautifulSoup(res.text, 'lxml')

# movies = soup.select("h2 a")
# top_years = soup.find_all(class_="subtle start-year")
# top_scores = soup.find_all(class_="tMeterScore")

# top_movies = [movie.text for movie in movies]

# all_movies = []
# i = 0
# for i in range(len(top_movies)):
#     movie = Movie(top_movies[i], top_years[i].text, top_scores[i].text)
#     all_movies.append(movie)

# for movie in all_movies:
#     print(movie)

import requests
from bs4 import BeautifulSoup


class Movie:
    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.score}"


url = "https://editorial.rottentomatoes.com/guide/popular-movies/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.select("h2 a")
top_years = soup.find_all(class_="subtle start-year")
top_scores = soup.find_all(class_="tMeterScore")

top_movies = [movie.text for movie in movies]

# Check if the lengths of the lists are equal
list_lengths = [len(top_movies), len(top_years), len(top_scores)]
if not all(length == list_lengths[0] for length in list_lengths):
    print("Error: List lengths are not equal. Skipping invalid entries.")
else:
    all_movies = []
    for i in range(len(top_movies)):
        movie = Movie(top_movies[i], top_years[i].text, top_scores[i].text)
        all_movies.append(movie)

    for movie in all_movies:
        print(movie)
