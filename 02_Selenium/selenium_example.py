from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('02_Selenium/chromedriver')
driver.get("https://www.youtube.com/")

time.sleep(3)

# 검색어 창을 찾아 'search' 변수에 저장
search = driver.find_element_by_xpath('//*[@id="search"]')

search.send_keys('반원 코딩')
time.sleep(1)

search.send_keys(Keys.ENTER)
time.sleep(5)