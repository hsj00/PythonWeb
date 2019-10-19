from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://twitter.com/d97844d6-839f-41f7-b1f7-457ead224519")

time.sleep(3)

url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
print(vid_url)
