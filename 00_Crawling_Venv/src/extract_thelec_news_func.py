# Web Scrapper
# Nomad Coder practice
# thelec.kr news page crawling

import selenium
import requests
from bs4 import BeautifulSoup

# from pprint import pprint

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


# 페이지 수만큼 URL을 조합해서 리스트로 반환
def URLcomb(last_pages, TOTAL):
    # 전체 페이지만큼의 값을 갖는 범위를 선언하여 `for` 루프로 "page=" 값을 출력하는 내용
    # "page=" 값을 `page_url_list`에 선언된 리스트로 반환
    URL_list = []
    box_id = "box_idxno="
    for n in range(last_pages):
        comb_URL = f"{URL}?page={n + 1}&{TOTAL}&{box_id}"
        URL_list.append(comb_URL)
        # page_url_str = f"page={n + 1}"

    return URL_list


if __name__ == "__main__":
    total_articles = thelecTotalArticle()
    total_page = thelecPages()
    articles_on_page = thelecPageArticles()
    URL_combination = URLcomb(total_page, total_articles)
    print(total_articles, total_page, articles_on_page)
    print(URL_combination)
