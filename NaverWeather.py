## Web crawling from Naver weather

### import module
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

### getting information from Naver weather
html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text, 'html.parser')
# pprint(soup)

data1 = soup.find('div', {'class' : 'detail_box'}) # 영역 추출
# pprint(data1)

data2 = data1.findAll('dd')
# pprint(data2)

fdust = data2[0].find('span', {'class':'num'}).text
# f_dust_state = data2[0].find().text
ufdust = data2[1].find('span', {'class':'num'}).text
O3 = data2[2].find('span', {'class':'num'}).text

pprint(fdust)
# pprint(f_dust_state)
pprint(ufdust)
pprint(O3)