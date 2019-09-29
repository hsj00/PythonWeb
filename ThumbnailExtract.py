## Naver Webtoon title extract

### module import
from bs4 import BeautifulSoup
from pprint import pprint
import requests, re, os
from urllib.request import urlretrieve # add module

### create the forlder to save files
try:
    if not (os.path.isdir('images')): # 해당 경로(path)에 ('images') 디렉토리가 없으면 (if, .isdir)
        os.makedirs(os.path.join('images')) # 폴더를 만들기(makedirs) -> 'images'를 해당 경로(path)에 추가(join)
except OSError as e: 
    if e.errno != errno.EEXIST:
        print("Failed to create folder!")
        exit()

### webpage open & parse
html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

### elements extract for all days
data1_list = soup.findAll('div', {'class':'col_inner'})

### whole webtoon list
li_list = []
for data1 in data1_list:
    ## title and thumbnail extract
    li_list.extend(data1.findAll('li')) # find and merge in li_list

### thumbnail  and title extract
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    # print(title, img_src)
    # title = re.sub('[^0-9a-zA-Zㄱ-힣]', '', title) # replace words by using regular expressions
    urlretrieve(img_src, './images/'+title+'.jpg') # address, directory + file name + extension 