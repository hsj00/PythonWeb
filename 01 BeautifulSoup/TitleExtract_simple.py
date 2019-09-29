## Naver Webtoon title extract

### module import
from bs4 import BeautifulSoup
from pprint import pprint
import requests

### webpage open & parse
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

### elements extract for all days
data1 = soup.findAll('a', {'class':'title'})
week_title_list = [t.text for t in data1]
pprint(week_title_list)