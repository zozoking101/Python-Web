from urllib.request import urlopen as get
from bs4 import BeautifulSoup

b_url = 'https://www.w3schools.com/html/'
n_url = 'html_intro.asp'
s_url = 'html_exam.asp'

page_count = 0


def start(base_url, next_url, stop_url):
  global page_count
  print('Getting url..')
  full_url = base_url + next_url
  print(f'Looking into {full_url}')
  html_doc = get(full_url)

  print(f'Cleaning page..')
  soup = BeautifulSoup(html_doc.read(), 'html.parser')

  print(f'Looking for important data..')
  heading = soup.find('h1')
  header = heading.text

  nav = soup.find('div', {'class': 'w3-clear nextprev'})
  url_save = []
  for nav in nav.findAll('a'):
      url_save.append(nav.get("href"))

  u_d = soup.find('div', {'id': 'main'})

  d = soup.find('div', {'id': 'mainLeaderboard'})
  d.decompose()

  d = soup.findAll('div', {'class': 'w3-clear nextprev'})
  for i in d:
      i.decompose()

  page = f'{header}\n\n{u_d.text}'

  page_count += 1

  print('Writing to file..')
  filename = f"data/{page_count}_{header.replace(' ', '_')}.txt"

  with open(filename, 'w') as f:
    f.write(page)

  print(f'{header} page saved.\nNumber of saved page: {page_count}\n')

  if url_save[1] != stop_url:
    start(base_url, url_save[1], stop_url)

  return page_count


start(b_url, n_url, sum)