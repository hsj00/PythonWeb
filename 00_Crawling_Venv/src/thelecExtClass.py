# Web Scrapper
# Nomad Coder practice

import selenium
import requests
from bs4 import BeautifulSoup

# from pprint import pprint

# http://www.thelec.kr/news/articleList.html?page=2&total=5131&box_idxno=


class thelecScrap:
    def __init__(self):
        # thelec.kr 전체 기사 목록을 읽어서 `html.parser`로 파싱
        THELEC_NEWS_URL = "http://www.thelec.kr/news/articleList.html"
        self.thelec_results = requests.get(THELEC_NEWS_URL)
        self.thelec_soup = BeautifulSoup(thelec_results.text, "html.parser")

        # 파싱된 데이터에서 전체 기사수 항목에서 값을 불러와 정수로 변환해서 출력
        self.total_articles = thelec_soup.find("small", {"class": "text-muted"}).string
        self.total_articles_number = int(total_articles[1:-2].replace(",", ""))
        print(f"total={total_articles_number}")

        # 파싱된 데이터에서 `class`가 `pagination text-center`인 `ul` 태그? 항목을 찾아서 `a` 태그 항목 전체 검색
        self.pagination = thelec_soup.find("ul", {"class": "pagination text-center"})
        self.links = pagination.find_all("a")

        # 빈 리스트를 `pages` 변수에 선언하고 `links` 변수에 선언된 데이터에서 `string` 항목들을 정수로 변환하여 추가
        self.pages = []
        for link in self.links[1:10]:
            self.pages.append(int(link.string))

        # `pages` 리스트에서 정수로 변환된 페이지중 가장 큰 값을 반환하여 선언
        self.max_page = max(pages)

        # 전체 페이지만큼의 값을 갖는 범위를 선언하여 `for` 루프로 "page=" 값을 출력하는 내용
        # "page=" 값을 `page_url_list`에 선언된 리스트로 반환
        self.page_url_list = []
        for n in range(self.max_page):
            page_url_str = f"page={n + 1}"
            self.page_url_list.append(page_url_str)
            # print(f"page={n + 1}")
            print(page_url_list)

        # 한 페이지에 뜨는 기사의 수를 알기 위해서 `class`가 `table-row`인 `div` 태그? 항목을 찾고 그 값의 길이를 반환하여 선언
        self.articles = thelec_soup.find_all("div", {"class": "table-row"})
        self.articles_number = len(self.articles)

        # print(articles_number)

    def thelecPageURL():
        pass

    if __name__ == "__main__":
        thelec = thelecScrap()
