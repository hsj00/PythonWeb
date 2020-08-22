# Web Scrapper
# Nomad Coder practice
# thelec.kr news page crawling
## 현재 구현한 수준
## 1. 전체 기사의 수 확인
## 2. 화면에서 전체 페이지 수를 확인
## 3. 한 화면에 나오는 전체 기사 수 확인
## 4. 구한 값을 조합해서 전체 기사 메뉴에서 각 페이지별 주소 반환

## 목표하는 구현 수준
## - 분야별로 기사 스크랩 (ex 반도체, 배터리, 디스플레이별 기사 스크랩)
## - 특정 날짜 이후 기사 스크랩
## - 특정 키워드 포함 기사만 스크랩
## - 메뉴별 주소 규칙을 확인하여 스크랩할 분야를 미리 선택을 할 수 있는 방법 구현 (전체 메뉴 주소를 확인해서 리스트로 만든 후 그중에서 선택하는 방식?)
## - 스크랩한 기사를 분야/헤드라인/날짜/링크 정보로 스프레드시트에 저장해서 파일로 만들기

import selenium
import requests
from bs4 import BeautifulSoup
from pprint import pprint

# http://www.thelec.kr/news/articleList.html?page=2&total=5131&box_idxno=

URL = f"http://www.thelec.kr/news/articleList.html"

# thelec.kr 전체 기사 목록을 읽어서 `html.parser`로 파싱
thelec_results = requests.get(URL)
thelec_soup = BeautifulSoup(thelec_results.text, "html.parser")

# 전체 기사 수
def thelecTotalArticle():
    # 파싱된 데이터에서 전체 기사수 항목에서 값을 불러와 정수로 변환해서 출력
    total_articles = thelec_soup.find("small", {"class": "text-muted"}).string
    total_articles_number = int(total_articles[1:-2].replace(",", ""))
    total_articles_url = f"total={total_articles_number}"
    # print(f"total={total_articles_number}")

    return total_articles_url


# 전체 페이지 수
def thelecPages():
    # 파싱된 데이터에서 `class`가 `pagination text-center`인 `ul` 태그? 항목을 찾아서 `a` 태그 항목 전체 검색
    pagination = thelec_soup.find("ul", {"class": "pagination text-center"})
    links = pagination.find_all("a")

    # 빈 리스트를 `pages` 변수에 선언하고 `links` 변수에 선언된 데이터에서 `string` 항목들을 정수로 변환하여 추가
    pages = []
    for link in links[1:10]:
        pages.append(int(link.string))

    # `pages` 리스트에서 정수로 변환된 페이지중 가장 큰 값을 반환하여 선언
    max_page = max(pages)

    return max_page
    # 한 페이지에 뜨는 기사의 수를 알기 위해서 `class`가 `table-row`인 `div` 태그? 항목을 찾고 그 값의 길이를 반환하여 선언


# 한 페이지에 보이는 기사 수
def thelecPageArticles():
    articles = thelec_soup.find_all("div", {"class": "table-row"})
    articles_number = len(articles)
    return articles_number

    # print(articles_number)


# 각 페이지별 섹션/타이틀/날짜를 리스트로 반환
def InfoExt(last_pages):
    # 전체 페이지만큼의 값을 갖는 범위를 선언하여 `for` 루프로 "page=" 값을 출력하는 내용
    # "page=n"에서 확인할 수 있는 섹션/타이틀/기자 이름/날짜/주소 정보 총 5가지 리스트 각각의 요소로 갖는 하나의 결과값 리스트로 반환

    # 추출한 정보를 `append`하기 위한 list들
    sect_list = []
    title_list = []
    author_list = []
    date_list = []
    add_list = []
    # box_id = "box_idxno="

    # 마지막 페이지 번호 `last_pages`를 `range` 함수의 인자로 받는 `for`루프
    for n in range(last_pages):
        # 주소와 페이지 번호가 결합된 구조로 바인딩된 주소에서 `requests`를 이용해 정보를 가져오고, `html.parser`로 파싱한 후, 각 기사에 해당하는 "table-row" 클래스를 모두 찾아서 `table_row`에 반환
        # comb_URL = f"{URL}?page={n + 1}&{TOTAL}&{box_id}"
        comb_URL = f"{URL}?page={n + 1}"
        URL_requests = requests.get(comb_URL)
        URL_soup = BeautifulSoup(URL_requests.text, "html.parser")
        table_row = URL_soup.find_all("div", {"class": "table-row"})

        # `table_row`로부터 반복되는 `for`문
        for table in table_row:
            # 기사의 타이틀 추출 후 반환
            title_text = table.find("a").string
            title_list.append(title_text)

            # 기사의 섹션 내용 추출 후 반환
            sect_find = table.find("small", {"class": "list-section"})
            sect_text = sect_find.string
            sect_list.append(sect_text)

            # "list-dated table-cell"로부터 가져온 문자를 `.split(" | ")`을 이용해 분리하여 각각 저자 리스트와 날짜 리스트로 반환
            date_find = table.find("div", {"class": "list-dated table-cell"})
            date_text = date_find.string
            author_list.append(date_text.split(" | ")[0])
            date_list.append(date_text.split(" | ")[1])

            # 기사 링크 주소를 추출해서 조합하여 반환
            add_link = table.find("a")["href"]
            add_text = URL[:20] + add_link
            add_list.append(add_text)

    # 함수의 결과를 리스트 자료형으로 반환
    return [sect_list, title_list, author_list, date_list, add_list]


# 다섯가지 기사 정보를 하나의 문자열로 합친 후 리스트의 인자로 반환
def infoComb():
    news = []
    total_page = thelecPages()
    articles_on_page = thelecPageArticles()
    page_ext = InfoExt(total_page)
    for n in range(total_page * articles_on_page):
        text_comb = f"{page_ext[0][n]} | {page_ext[1][n]} | {page_ext[2][n]} | {page_ext[3][n]} | {page_ext[4][n]}"
        news.append(text_comb)
    return news


"""
        처음 구현한 `for`문, 중복되는 부분을 제거하여 하나로 통합
        for link in table_row:
            title_text = link.find("a").string
            title_list.append(title_text)
        for sect in table_row:
            sect_find = sect.find("small", {"class": "list-section"})
            sect_text = sect_find.string
            sect_list.append(sect_text)
        for date in table_row:
            date_find = date.find("div", {"class": "list-dated table-cell"})
            date_text = date_find.string
            date_list.append(date_text)
        for address in table_row:
            add_link = address.find("a")["href"]
            add_text = URL[:20] + add_link
            add_list.append(add_text)
"""

if __name__ == "__main__":
    total_articles = thelecTotalArticle()
    total_page = thelecPages()
    articles_on_page = thelecPageArticles()
    page_ext = InfoExt(total_page)
    print(total_articles, total_page, articles_on_page)
    print(len(page_ext))
    pprint(page_ext[0][0])
    pprint(infoComb())
