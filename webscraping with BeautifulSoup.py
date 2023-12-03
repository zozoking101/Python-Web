from bs4 import BeautifulSoup
import requests
url = 'https://beautiful-soup-4.readthedocs.io/en/latest/'
response = requests.get(url)
print(response)
raw_code = response.text
#print(raw_code)

soup = BeautifulSoup(raw_code, 'html.parser')

#print(soup.title)
#print(soup.h2)

# var_1 = soup.find_all("div")
# print(var_1)

# var_2 = soup.find_all("a")
# for x in var_2:
#     print(x.string)

# var_3 = soup.find_all(id="quick-start")
# print(var_3)

# var_4 = soup.find_all(class_="section")
# print(var_4)

# var_5 = soup.select("h2")
# print(var_5)

# var_6 = soup.select("#quick-start")
# print(var_6)

# var_7 = soup.select(".section")
# print(var_7)

# var_8 = soup.select("#making-the-soup > h1")
# print(var_8)

var_9 = soup.select("a[href='#installing-beautiful-soup']")
print(var_9)

var_10 = soup.select()