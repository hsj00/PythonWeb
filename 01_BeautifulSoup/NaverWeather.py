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
html.close()

data1 = soup.find('div', {'class' : 'detail_box'}) # 영역 추출
# pprint(data1)
data2 = data1.findAll('dd')
# pprint(data2)

### 필요한 데이터 추출
fdust = data2[0].find('span', {'class':'num'}).text
ufdust = data2[1].find('span', {'class':'num'}).text
O3 = data2[2].find('span', {'class':'num'}).text

### 추출 데이터 출력
pprint(fdust)
pprint(ufdust)
pprint(O3)