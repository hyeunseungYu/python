from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#time.sleep을 사용하지 않았던 문제

# Chrome 실행
driver = webdriver.Chrome()
# dart 페이지로 이동
driver.get("https://dart.fss.or.kr/main.do")

input_box=driver.find_element(By.XPATH,'//*[@id="textCrpNm2"]')


input_box.send_keys('한국투자증권')

search_button=driver.find_element(By.XPATH,'//*[@id="searchForm2"]/div[1]/div[3]/a')
search_button.click()

search_button1=driver.find_element(By.CSS_SELECTOR,'#r_20230515002312')
search_button1.send_keys('\n')

#//*[@id="textCrpNm2"]
#//*[@id="searchForm2"]/div[1]/div[3]/a
#//*[@id="tbody"]/tr[6]/td[3]