# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
# import requests

# link = "https://www.jumia.com.ng/apple-iphone-14-pro-max-6.7-1tb-nano-sim-deep-purple-259217772.html?gclid=Cj0KCQiAr8eqBhD3ARIsAIe-buPAQ1r4uTVXghq6gntA7EozD4mW4ETPHJ_XBymVTJux6RUsEmubadwaAoD5EALw_wcB"

# request = Request(link, headers = {'User Agent': 'Mozilla/5.0'})

# webpage = urlopen(request)
# with requests.Session() as c:
#     soup = BeautifulSoup(webpage, 'html5lib')

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import re

def ctof(currency_string):
    # Remove non-numeric characters and convert to float
    cleaned_string = re.sub(r'[^\d.]', '', currency_string)
    float_value = float(cleaned_string)
    return '{:.2f}'.format(float_value)

# Update the link of the item
link_1 = "https://www.jumia.com.ng/apple-iphone-14-pro-max-6.7-1tb-nano-sim-deep-purple-259217772.html?gclid=Cj0KCQiAr8eqBhD3ARIsAIe-buPAQ1r4uTVXghq6gntA7EozD4mW4ETPHJ_XBymVTJux6RUsEmubadwaAoD5EALw_wcBhttps://www.ebay.com/itm/296049542116?epid=11056248077&hash=item44eded83e4:g:~U4AAOSwCjFlKWWX&amdata=enc%3AAQAIAAAAwDG0viestsl5HucQaqGUZKMI0RWmdNLErzHaSJ0pcSSO5mzbIk02g3QrA6GgWb6yOphqJ%2Fr7cmf%2F5FwP80%2F2MDyzg4illXAnO%2FqZZgcI8hQ9Oil7HIOiX4sPEk1gIdTaCBCPZDgaFWAuQvW95PhKrEnU21EOmTZ%2BERrI%2BHC3tRhL6oxAz1ElyOR9bUupYe2GDUM5QZDk4UpQBJBYBGSnkg42IjSsWIsTUEFmVkcD8W35LHiGKpkaq0CqIIjRBZAcFw%3D%3D%7Ctkp%3ABk9SR_a1rI_7Yg"
link_2 = "https://www.jumia.com.ng/samsung-galaxy-s23-ultra-5g-12gb256gb-mobile-beige-249442614.html"
link_3 = "https://www.jumia.com.ng/tecno-spark-10-pro-6.8-8gb-ram256gb-rom-android-13-free-gift-235578422.html"
link_4 = "https://www.jumia.com.ng/infinix-zero-30-5g-6.78-256gb-rom12gb-ram-android-13-gold-260175457.html"
link_5 = "https://www.jumia.com.ng/t20-10.4-4gb-ram-64gb-rom-8mp-camera-5mp-selfie-lte-8200mah-ocean-blue-nokia-mpg1652365.html"


link = [link_1, link_2]
for i in link:
    req = Request(i, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        header = soup.find("h1", attrs={"class": "-fs20 -pts -pbxs"}).get_text()
        price = soup.find("span", attrs={"class": "-b -ltr -tal -fs24 -prxs"}).get_text()
        print(f'{header} : N{ctof(price)}')
        #price = soup.find('span',attrs={'itemprop':'price'})['content']
        #print(price)