from selenium import webdriver
from pprint import pprint
import time
from collections import Counter

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

start = time.time()
while time.time() - start <= 60:
    try:
        btn = driver.find_element_by_class_name("main")  # 정답 버튼의 class 속성이 main이라 main만 찾아냄
        btn.click()
    except:
        pass

# btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')  # xpath에서 버튼 전체의 정보를 찾아 btns에 리스트로 저장
# # print(len(btns))

# def analysis():
#     # print(btns[0].value_of_css_property('background-color'))  # btns에 저장된 리스트 중에 0번 값에서 css 정보중에 'background-color'만 찾는다
#     btns_rgba = [ btn.value_of_css_property('background-color') for btn in btns ]  # for문을 이용하여 btns list의 모든 background-color를 다시 리스트로 저장
#     # pprint(btns_rgba)

#     result = Counter(btns_rgba)  # btns_rgba에서 유형별로 묶어서 개수를 센 후 반화
#     # pprint(result)

#     for key, value in result.items():  # dictionary 형태로 반환된 result에서 key와 value를 순서대로 반환?
#         if value == 1:  # value가 하나인 것 = 유일하게 색이 다른 버튼 이므로
#             answer = key  # answer에 key를 반환
#             break  # for문을 나오고
#     else:  # key, value가 반환되지 않으면
#         answer = None  # answer에 None을 반환
#         print("Can't find the answer.")

#     if answer :  # answer가 참일 경우
#         index = btns_rgba.index(answer)  # btns_rgba에서 answer값을 갖는 순서를 찾아서 index에 반환
#         btns[index].click()  # btns 리스트에서 index에 반환된 순서와 같은 값을 클릭

# start = time.time()

# while time.time() - start <= 60:  # 60초동안 동작하도록 반복문 설정
#     analysis()