
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Chrome 드라이버 서비스 설정
# ChromeDriverManager().install()를 통해서 크롬 드라이버 설치와 관련된 작업을 자동화해줌
# chrome_service = webdriver.Chrome()
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Chrome 옵션 설정
# 이 chrome_options라는 변수를 통해 브라우저를 헤드리스 모드(화면에 표시하지 않고 백그라운드에서 실행)도 가능
chrome_options = webdriver.ChromeOptions()

#아래 코드를 활성화 시키면 헤드리스 모드로 실행
# chrome_options.add_argument('--headless')

# Chrome 실행
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# AAPL 주식의 Yahoo Finance 페이지로 이동
driver.get("https://datacenter.hankyung.com/economic-calendar")
# 프레임 전환하는 코드
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)

# 기본 프레임으로 돌아가기 (필요한 경우)
# driver.switch_to.default_content()

tables = driver.find_elements(By.TAG_NAME, 'table')
print(type(tables))
print(tables[0].get_attribute('innerText'))