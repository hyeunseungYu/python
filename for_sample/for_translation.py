from pdf2docx import Converter
from docx import Document
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from tqdm import tqdm
import pyautogui


# pdf에서 docx로 변환
def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    total_pages = len(cv.pages)
    with tqdm(total=total_pages, desc="Converting PDF to DOCX") as pbar:
        for i in range(total_pages):
            cv.convert(docx_path, start=i, end=i+1)
            pbar.update(1)
    cv.close()

#docx에서 한 문단 단위로 추출
def extract_paragraphs_from_docx(docx_path):
    doc = Document(docx_path)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    return paragraphs



# pdf_path = input("pdf 파일 경로를 입력해 주세요: ")
# docx_path = pdf_path + '.docx'


# # 입력 받은 경로를 사용하여 함수 호출
# convert_pdf_to_docx(pdf_path, docx_path)


# # docx 파일에서 문단 추출
# paragraphs = extract_paragraphs_from_docx(docx_path)


# Chrome 드라이버 서비스 설정
chrome_service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()

# Chrome 실행
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("https://papago.naver.com/")

# time.sleep(3)

# result_list = []

# # 추출된 문단을 출력 또는 다른 용도로 활용
# for paragraph in paragraphs:
#     # print(paragraph)
#     print(result_list)
#     time.sleep(2)

#     source_text = driver.find_element(By.XPATH,'//*[@id="txtSource"]')
#     source_text.send_keys(paragraph)
#     time.sleep(2)

#     result_text = driver.find_element(By.XPATH,'//*[@id="targetEditArea"]')
#     if result_text == None:
#         continue
#     else:
#         result = result_text.get_attribute('innerText')
#         first_sentence = result.split('\n')[0]
#         result_list.append(first_sentence)

#         source_text.clear()
#         time.sleep(2)
    

driver.get("https://kirinman.tistory.com/")

button = driver.find_element(By.XPATH, '//*[@id="dkHead"]/div/div/button/span')
button.click()

write_button = driver.find_element(By.XPATH, '//*[@id="dkHead"]/div/div/ul/li[1]/a')
write_button.click()

login_button = driver.find_element(By.XPATH, '//*[@id="cMain"]/div/div/div/a[2]')
login_button.click()

id_field = driver.find_element(By.XPATH, '#loginKey--1')


time.sleep(60)