# Web Scrapper
# Nomad Coder practice

import selenium
import requests
from bs4 import BeautifulSoup
from pprint import pprint

THELEC_NEWS_URL = "http://www.thelec.kr/news/articleList.html"
# http://www.thelec.kr/news/articleList.html?page=2&total=5131&box_idxno=


def extThelecNews():
    thelec_results = requests.get(THELEC_NEWS_URL)
    thelec_soup = BeautifulSoup(thelec_results.text, "html.parser")

    total_articles = thelec_soup.find("small", {"class": "text-muted"}).string
    total_articles_number = int(total_articles[1:-2].replace(",", ""))
    print(f"total={total_articles_number}")

    pagination = thelec_soup.find("ul", {"class": "pagination text-center"})
    links = pagination.find_all("a")

    pages = []
    for link in links[1:10]:
        pages.append(int(link.string))

    max_page = max(pages)

    articles = thelec_soup.find_all("div", {"class": "table-row"})
    articles_number = len(articles)

    for n in range(max_page):
        print(f"page={n + 1}")

    pprint(articles_number)


if __name__ == "__main__":
    extThelecNews()
