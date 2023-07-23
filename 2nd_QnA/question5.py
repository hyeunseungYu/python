from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome 실행
driver = webdriver.Chrome()
# dart 페이지로 이동
driver.get("https://dart.fss.or.kr/main.do")

# 1)한국투자증권 입력 2)검색버튼클릭
input_box=driver.find_element(By.XPATH,'//*[@id="textCrpNm2"]')
input_box.send_keys('한국투자증권')

search_button=driver.find_element(By.XPATH,'//*[@id="searchForm2"]/div[1]/div[3]/a')
search_button.click()

# 1)상세조건 열기클릭 2)보고서명에 파생결합사채 입력
search_button=driver.find_element(By.XPATH,'//*[@id="btnPlus"]')
search_button.click()

input_box=driver.find_element(By.XPATH,'//*[@id="reportName2"]')
input_box.send_keys('파생결합사채')

# 1)검색클릭 2)3초 쉬기 3)파생결합사채 보고서 클릭 
search_button=driver.find_element(By.XPATH,'//*[@id="searchForm"]/div[2]/div[2]/a[1]')
search_button.click()

time.sleep(3)

search_button=driver.find_element(By.XPATH,'//*[@id="r_20230511000248"]')
search_button.click()

time.sleep(1)

current_window_handle = driver.current_window_handle
popup_window_handle = None

# 모든 윈도우 핸들을 확인하여 팝업창 핸들을 찾음
for handle in driver.window_handles:
    if handle != current_window_handle:
        popup_window_handle = handle
        break

driver.switch_to.window(popup_window_handle)

# 모집 또는 매출에 관한 사항의 요약 클릭
search_button=driver.find_element(By.XPATH,'//*[@id="3_anchor"]')
search_button.click()

time.sleep(3)
