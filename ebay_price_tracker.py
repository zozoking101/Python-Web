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

link_1 = "https://www.ebay.com/itm/296049542116?epid=11056248077&hash=item44eded83e4:g:~U4AAOSwCjFlKWWX&amdata=enc%3AAQAIAAAAwDG0viestsl5HucQaqGUZKMI0RWmdNLErzHaSJ0pcSSO5mzbIk02g3QrA6GgWb6yOphqJ%2Fr7cmf%2F5FwP80%2F2MDyzg4illXAnO%2FqZZgcI8hQ9Oil7HIOiX4sPEk1gIdTaCBCPZDgaFWAuQvW95PhKrEnU21EOmTZ%2BERrI%2BHC3tRhL6oxAz1ElyOR9bUupYe2GDUM5QZDk4UpQBJBYBGSnkg42IjSsWIsTUEFmVkcD8W35LHiGKpkaq0CqIIjRBZAcFw%3D%3D%7Ctkp%3ABk9SR_a1rI_7Yg"
link_2 = "https://www.ebay.com/itm/175881796817?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20201210111451%26meid%3D290b07bda35e489cb48331bda76c0f98%26pid%3D101196%26rk%3D5%26rkt%3D5%26sd%3D186035177804%26itm%3D175881796817%26pmt%3D1%26noa%3D0%26pg%3D4429486%26algv%3DSimplAMLv5PairwiseWebWithBBEV2bAndUBSourceDemotionWithUltimatelyBoughtOfCoviewV1%26brand%3DSamsung&_trksid=p4429486.c101196.m2219&amdata=cksum%3A175881796817290b07bda35e489cb48331bda76c0f98%7Cenc%3AAQAIAAABMPzGgyhK8D4QCApcBuWVQe1qsoN395NgJVWTF7eo2rfipPwdfCio0EI4F5H%252Bx0wtS8%252Fu%252Fr%252FRUxEZ1KxNtbAGuwQqNawa9Mz45LW45pYy0nujBTNR8yzmSeFpOF8c7fdjt7U5xIaS6zeDD58Ipi6zoz%252BwiPL5U2q0NY%252FagTJzUHhxd7%252FwsGtkj3pcx9G2BKTMggK7x9D%252Fwdvkvr8RN1iksRmN%252BlbiOvv5E7MFspo17a59B0Wr6jEBr7mQF0iR%252BbTSQ9M6siMtnsjjeHmfbdbTWjqzGb1bhkm0cl5sESm%252BcttvLln9I7KWQ4LP%252B3WIZaxSo3ajoZaXlzw28MBkA0GGSoZSriA03Iv4LUmY7gxT6MqivYvoeg5Z7iY%252FLrvlzR1TtGflzb6nhH5vaA8tsmtWtyY%253D%7Campid%3APL_CLK%7Cclp%3A4429486&epid=4043682109"
link_3 = "https://www.ebay.com/itm/225837750805?hash=item3494fa9a15:g:hSoAAOSwqgdlQpVz&var=524944411977"
link_4 = "https://www.ebay.com/itm/166431247941?hash=item26c0134e45:g:GSUAAOSwksBlT2ty&amdata=enc%3AAQAIAAAAwGl0NCnF7AqBS3qmIwFrbPZdofe9ga3RK7Rq6pvhMcgc6TU%2F8oUcKV7onFOM%2BNojPv075ZOSqJz2E0K3OqB%2Fa6V1GYPAq%2BpYz4nRofXh9Ojmp%2BHje44T%2BAPwv%2FWMPSEFaSSuNTltkbO5UuFnybm%2BDfT0sY0AfkudvWS8D8QjT6Vz0Y2NYKowEBFcOG7DJMHKTwXho5ltBnJaRch2HY6xqB8gytIWjSa8fR%2BwpZyS3jA0udJbaI5IXYTKyinkDh6DRg%3D%3D%7Ctkp%3ABk9SR86T9Z37Yg"
link_5 = ""


link = [link_1]

for i in link:
    req = Request(i, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        header = soup.find("span", attrs={"class": "ux-textspans ux-textspans--BOLD"}).get_text()
        price = soup.find("span", attrs={"class": "ux-textspans"}).get_text()
        print(f'{header} : ${ctof(price)}')
        #price = soup.find('span',attrs={'itemprop':'price'})['content']
        #print(price)
        

       