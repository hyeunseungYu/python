from tkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# GUI 설정
tk = Tk()
tk.geometry("500x500")

chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
scrap_dic = {}
scrap_list = []

# 스크랩핑 함수 정의
def get_scrap():
    ticker = ticker_entry.get()  # 사용자 입력 값을 받아옵니다
    # 스크랩핑 과정
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}")
    target_ul = driver.find_elements(By.CSS_SELECTOR, ".js-content-viewer")
    
    for i in range(3):
        scrap_list.append(target_ul[i].text)
    scrap_dic[ticker] = scrap_list
    driver.quit()
    
    # 결과를 GUI에 표시
    output.delete(1.0, END) # 이전 출력 내용 삭제
    output.insert(END, f"{ticker} done!\n") # ticker 완료 메시지 추가
    output.insert(END, str(scrap_dic)) # 결과 딕셔너리 추가

label = Label(tk, text="Enter ticker value")
label.pack(pady=2)

# 사용자 입력 Entry 생성
ticker_entry = Entry(tk)
ticker_entry.pack(pady=2)

# 버튼 생성
button = Button(tk,text='버튼입니다. 누르면 함수가 실행됩니다.',command=get_scrap)
button.pack(padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 





# 결과 출력 Text Widget 생성
output = Text(tk, wrap=WORD, width=50, height=10)
output.pack(padx=10, pady=10)

tk.mainloop()
