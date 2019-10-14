from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50/')
driver.implicitly_wait(300)

# 전역변수
# 가장 먼저 찾아야 할 숫자
num = 1

# 클릭 함수 정의
def clickBtn():
    global num  # 전역변수 선언
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
    
    for btn in btns:
        # print(btn.text, end='\t')   # btns 안에 있는 데이터를 출력
        if btn.text == str(num):
            btn.click()
            # print(True)   # if문의 조건과 같은 값이 나왔을 때 'True' 출력
            num += 1
            return

while num <= 50:
    clickBtn()

