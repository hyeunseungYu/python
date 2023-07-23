# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import os
# import requests
# import pandas as pd


# # Chrome 드라이버 서비스 설정
# chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# # Chrome 옵션 설정
# chrome_options = webdriver.ChromeOptions()

# # Chrome 실행
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# # dart 페이지로 이동
# driver.get("https://dart.fss.or.kr/dsab007/main.do")

# my_button = driver.find_element(By.XPATH, '//*[@id="option"]/option[3]')
# my_button.click()

# time.sleep(1)

# my_input = driver.find_element(By.XPATH, '//*[@id="reportName"]')
# my_input.send_keys("증권신고서(지분증권)")

# time.sleep(1)

# from datetime import datetime, timedelta

# today=datetime.now()
# start_date=today-timedelta(days=7)
# start_date_str = start_date.strftime("%Y%m%d")

# time.sleep(1)

# start_date_input = driver.find_element(By.XPATH, '//*[@id="startDate"]')
# start_date_input.clear()
# start_date_input.send_keys(start_date_str)

# time.sleep(1)

# my_button = driver.find_element(By.XPATH, '//*[@id="maxResultsCb"]')
# my_button.click()
# option_100 = driver.find_element(By.XPATH, '//*[@id="maxResultsCb"]/option[text()="100"]')
# option_100.click()

# time.sleep(1)

# my_button = driver.find_element(By.XPATH, '//*[@id="searchForm"]/div[1]/div/ul/li/div[3]/a')
# my_button.click()

# time.sleep(1)

# my_button = driver.find_element(By.XPATH, '//*[@id="btnPlus"]')
# my_button.click()

# time.sleep(1)

# my_button = driver.find_element(By.XPATH, '//*[@id="corporationType"]')
# my_button.click()
# option_유가증권시장 = driver.find_element(By.XPATH, '//*[@id="corporationType"]/option[2]')
# option_유가증권시장.click()

# time.sleep(1)

# my_button = driver.find_element(By.XPATH, '//*[@id="searchForm"]/div[2]/div[2]/a[1]')
# my_button.click()

# time.sleep(3)

# tables = driver.find_elements(By.TAG_NAME,'table')
# print(type(tables))
# print(tables)
# print('#######################')

# tbodies = []
# trs =  []

# for table in tables:
#     tbody = table.find_element(By.TAG_NAME, 'tbody')
#     tr = tbody.find_elements(By.TAG_NAME, 'tr')

#     trs.append(tr)


# # 첫 번째 요소를 클릭
# first_element = trs[0][0]  # 첫 번째 요소 선택
# first_element.click()     # 클릭


# for tr_list in trs:
#     for tr in tr_list:
#         text = tr.text
#         print(text)




 # dart_fss 모듈을 import합니다.
import dart_fss
# pandas 모듈을 import합니다.
import pandas as pd

# DART API 키를 입력합니다.
api_key = 'b81bd814632ef49454b88b483de0b65a89cd7c4f'
# 입력한 API 키를 dart_fss 모듈의 set_api
# _key() 함수를 사용하여 설정합니다.
dart_fss.set_api_key(api_key=api_key)


reports = dart_fss.filings.search(bgn_de='20190501', end_de='20190701', pblntf_detail_ty='c001')
print(reports)

all = dart_fss.api.filings.get_corp_code()

df = pd.DataFrame(all)

# df_listed = df[df['corp_code'] == f'{}']
