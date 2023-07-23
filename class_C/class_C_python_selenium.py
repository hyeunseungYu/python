'''
정적 웹페이지? 동적 웹페이지?

정적 웹페이지란 서버에 미리 저장된 파일이 그대로 전달되는 웹 페이지를 말합니다.
동적 웹페이지와의 가장 큰 차이점은 url 주소 외에는 아무 것도 필요없다는 점입니다.
만약, 마우스 휠을 스크롤 다운 했는데, url에 변화는 없고 페이지에 내용이 추가된다면 그 페이지는 동적 웹 페이지입니다.

동적 웹페이지란 url만으로는 들어갈 수 없는 웹페이지나 
url의 변화가 없는데도 실시간으로 내용이 추가되거나 수정되는 웹페이지를 말합니다.
다만, 무언가를 클릭해서 페이지가 변경되는 것은 다릅니다.

- xpath 사용 이유 -> css selector에서 id속성이 중복되는 경우 제대로 복사되지 않는 경우가 있음
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
scrap_list = []
def get_scrap(keyword,index):
    print(f"{keyword} is start")
    # Chrome 실행
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    time.sleep(2)
    # AAPL 주식의 Yahoo Finance 페이지로 이동
    driver.get(f"https://finance.yahoo.com/quote/{keyword}/")
    name = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1')
    tables = driver.find_elements(By.TAG_NAME, "table")

    name = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').text
    scrap_dict = {"name" : name}

    scrap_list.append(scrap_dict)

    for table in tables:
        trs = table.find_elements(By.TAG_NAME, 'tr')
        for tr in trs:
            if tr is None:
                continue
            td = tr.find_elements(By.TAG_NAME, 'td')
            if len(td) < 2:
                print("error")
                continue

            print(td[1].get_attribute("textContent"))

            col_key = td[0].get_attribute("textContent")
            col_val = td[1].get_attribute("textContent")
            
            scrap_list[index][col_key] = col_val
            
    driver.quit()
    print(f"{keyword} is done")
    return scrap_list

stock_list = ['AMZN', 'TSLA']
for index, stock in enumerate(stock_list):
    get_scrap(stock, index)

print(scrap_list)
#######################


# # Chrome 드라이버 서비스 설정
# # ChromeDriverManager().install()를 통해서 크롬 드라이버 설치와 관련된 작업을 자동화해줌
# chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# # Chrome 옵션 설정
# # 이 chrome_options라는 변수를 통해 브라우저를 헤드리스 모드(화면에 표시하지 않고 백그라운드에서 실행)도 가능
# chrome_options = webdriver.ChromeOptions()

# #아래 코드를 활성화 시키면 헤드리스 모드로 실행
# # chrome_options.add_argument('--headless')

# # Chrome 실행
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# # AAPL 주식의 Yahoo Finance 페이지로 이동
# driver.get("https://finance.yahoo.com/quote/AAPL/")



# # print(type(name))
# # print(name.text)

# tables = driver.find_elements(By.TAG_NAME, "table")


# # print(tables)
# scrap_list = []
# name = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').text
# scrap_dict = {"name" : name}
# scrap_list.append(scrap_dict)

# print(scrap_list)

# print(len(tables))

# for i in range(2):
#     table = tables[i]
#     trs = table.find_elements(By.TAG_NAME, 'tr')

#     for tr in trs:
#         if tr is None:
#             continue
        
#         td = tr.find_elements(By.TAG_NAME, 'td')

#         if len(td) == 0:
#             continue

#         col_key = td[0].get_attribute("textContent")
#         col_val = td[1].get_attribute("textContent")

#         scrap_list[0][col_key] = col_val 

#         # print(col_key, col_val)
        

# driver.quit()

# df = pd.DataFrame(scrap_list)


####################################################


       
        
       
        