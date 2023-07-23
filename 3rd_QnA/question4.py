from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
scrap_dic = {}
scrap_list = []

def get_scrap(ticker):
    print(f"{ticker} is start")
    print()
    
    
    # Chrome 실행
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    time.sleep(2)
    
    # AAPL 주식의 Yahoo Finance 페이지로 이동
    driver.get(f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}")

    target_ul = driver.find_elements(By.CSS_SELECTOR, ".js-content-viewer")
    
    for i in range(3):
        scrap_list.append(target_ul[i].text)

    scrap_dic[ticker] = scrap_list

    driver.quit()
    
    return print(f"{ticker} done!")



print(scrap_dic)
