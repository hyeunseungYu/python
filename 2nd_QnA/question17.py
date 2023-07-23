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
print(len(tbody))
tbody = driver.find_element(By.XPATH, '//*[@id="viewHeightDiv"]/table/tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

title_list= []
title_raw_list = []
for i in range(1, len(trs)+1):
    test = driver.find_element(By.XPATH,f'//*[@id="viewHeightDiv"]/table/tbody/tr[{i}]/td[2]/a')
    title_list.append(test.text)
    title_raw_list.append(test)
    print(test.get_attribute("innerText"))

input_value1 = input("첫번째 키워드를 입력해 주세요 : ")
input_value2 = input("두번째 키워드를 입력해 주세요 : ")

index_list = [i for i, title in enumerate(title_list) if f'{input_value1}' in title or f'{input_value2}' in title]
print(index_list)


for index in index_list:
    title_raw_list[index].click()
    time.sleep(2)
    download = driver.find_element(By.XPATH, '//*[@id="bdySaveBtn"]')
    download.click()
    time.sleep(2)
    
    download2 = driver.find_element(By.XPATH,'//*[@id="aBtnOutPutSave"]')
    time.sleep(2)
    
    draw = driver.find_element(By.XPATH,'//*[@id="west-toggler"]/span[1]/div[2]')
    draw.click()
    time.sleep(2)
