## Naver Webtoon title extract

### module import
from bs4 import BeautifulSoup
from pprint import pprint
import requests

### webpage open & parse
html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

### elements extract for all days
data1_list = soup.findAll('div', {'class':'col_inner'})

### list for each title of daily webtoon
week_title_list = []

for data1 in data1_list:
    data2 = data1.findAll('a', {'class':'title'}) # a 태그, class 속성, title 속성값 검색

    ### title text extracting 02
    title_list = [t.text for t in data2]

    ## ~/TitleExtract_simple.py와 같은 결과
    # week_title_list.extend(title_list) # 단순 추가, 1차원 형태로 작성 extend
    week_title_list.append(title_list) # 요일별로 나눠서 추가, 2차원 형태로 작성 append

pprint(week_title_list)

'''
### elements extract for all days
data1 = soup.find('div', {'class':'col_inner'})
data2 = data1.findAll('a', {'class':'title'}) # a 태그, class 속성, title 속성값 검색

## title text extracting 01
title_list = []
for t in data2:
    title_list.append(t.text)

pprint(title_list)
'''