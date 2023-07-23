from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

import time

# Chrome 드라이버 서비스 설정
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()

# Chrome 실행
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 법제처 홈페이지로 이동
url = 'https://www.law.go.kr/'
driver.get(url)

# 검색어 입력 - "개정"
search_keyword_xpath = '//*[@id="query"]'
search_keyword_element = driver.find_element(By.XPATH, search_keyword_xpath)
search_keyword_element.send_keys('개정')

# 검색 버튼 실행
search_button_xpath = '//*[@id="inner"]/a'
search_button_element = driver.find_element(By.XPATH, search_button_xpath)
search_button_element.click()

button = driver.find_element(By.XPATH,'//*[@id="tab1"]')
button.click()
print("버튼클릭")

time.sleep(2)

title_list = []

tbody = driver.find_elements(By.XPATH,'//*[@id="viewHeightDiv"]/table/tbody')

for i in tbody:
    trs = driver.find_elements(By.TAG_NAME,'tr')
    print(len(trs))

for i in range(1, round(len(trs)//2)):
    test = driver.find_element(By.XPATH,f'//*[@id="viewHeightDiv"]/table/tbody/tr[{i}]/td[2]/a')
    print(test.get_attribute("innerText"))


# sample = driver.find_elements(By.TAG_NAME, "ul")

# # 8번째 ul 요소 가져오기
# sample = driver.find_elements(By.TAG_NAME, "ul")[8]

# # ul 요소의 0번째 자식 요소 클릭
# first_child_element = sample.find_elements(By.TAG_NAME, "li")[0]
# first_child_element.click()

# test = driver.find_element(By.XPATH,'//*[@id="viewHeightDiv"]/table/tbody/tr[1]/td[2]/a')
# test.click()

