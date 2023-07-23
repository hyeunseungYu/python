from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

#프레임 전환을 하지 않았던 문제

# 검색어 설정
query = '달콤다정'
#query = input("음식점 이름을 입력해 주세요 : ")

# Chrome 드라이버 서비스 설정
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()

# 크롬 드라이버 경로 설정
# chrome_driver_path = '/Users/yuhyeonseung/Downloads/chromedriver_mac_arm64'


# 크롬 드라이버 실행
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# 네이버지도 검색 페이지 열기
driver.get('https://map.naver.com/v5/search/' + query)

# 2초간 대기
time.sleep(4)

driver.switch_to.frame('entryIframe')


# em 요소를 찾아서 텍스트 가져오기
em_element = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div.place_section.OP4V8 > div.zD5Nm.f7aZ0 > div.dAsGb > span.PXMot.LXIwF > em')
print(em_element.get_attribute("textContent"))


# # 결과 출력
# print(em_text)

# 드라이버 종료
driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# #프레임 전환을 하지 않았던 문제

# # 검색어 설정
# query = '달콤다정'

# # 크롬 드라이버 경로 설정
# chrome_driver_path = '/Users/yuhyeonseung/Downloads/chromedriver_mac_arm64'

# # 크롬 드라이버 실행
# driver = webdriver.Chrome(chrome_driver_path)

# # 네이버지도 검색 페이지 열기
# driver.get('https://map.naver.com/v5/search/' + query)

# # 2초간 대기
# time.sleep(4)

# driver.switch_to.frame('entryIframe')


# # em 요소를 찾아서 텍스트 가져오기
# em_element = driver.find_element(By.CSS_SELECTOR, '#app-root > div > div > div > div.place_section.OP4V8 > div.zD5Nm.f7aZ0 > div.dAsGb > span.PXMot.LXIwF > em')
# print(em_element.get_attribute("textContent"))


# # # 결과 출력
# # print(em_text)

# # 드라이버 종료
# driver.quit()
