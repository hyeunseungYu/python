# dart_fss 모듈을 import합니다.
import dart_fss
# pandas 모듈을 import합니다.
import pandas as pd

#api키 설정
api_key = '1fc24509de0487791f00f57c862cfb359b27075f'
# 입력한 API 키를 dart_fss 모듈의 set_api_key() 함수를 사용하여 설정합니다.
dart_fss.set_api_key(api_key=api_key)

#코드검색
corp_code='00160144'
reports = dart_fss.filings.search(corp_code=corp_code, bgn_de='20230505',page_no=1,page_count=60)

file_names = []  # 파일 이름을 저장할 리스트

# 파생결합사채 제목으로 된 항목만 뽑아서 보고서 PDF로 다운
for report in reports.report_list:
    if '일괄신고추가서류(파생결합사채-주가연계파생결합사채)' in report.report_nm:
        print('있음')
        attached_file = report.extract_attached_files()[0]
        file_name = attached_file.to_dict()['filename']
        file_names.append(file_name)  # 파일 이름을 리스트에 추가
        attached_file.download('.')       
        #print(attached_file.to_dict()['filename'])  # 파일 이름 출력
       #attached_file.download('.')
         #report.extract_attached_files()[0].download('.')
    else:
        print('없음')
print(file_names)  # 파일 이름 리스트 출력

import fitz
from pdf2docx import Converter

def extract_pages_from_pdf(pdf_file_path, output_pdf_path, search_term, start_item, end_item):
    output_pdf = fitz.open()  # 새로운 PDF 문서 생성

    # 원본 PDF 파일 열기
    with fitz.open(pdf_file_path) as pdf_file:
        # '모집 또는 매출에 관한 사항의 요약' 페이지 추출
        for page_num in range(1, pdf_file.page_count):  # Skip the first page
            page = pdf_file[page_num]
            page_text = page.get_text()

            # 텍스트에서 특정 단어 찾기
            if search_term in page_text:
                output_pdf.insert_pdf(pdf_file, from_page=page_num, to_page=page_num)
                break  # 첫 번째 출현한 페이지만 추가하고 종료

        found_start = False  # 시작 항목을 찾았는지 여부
        start_count = 0  # 시작 항목이 나타난 횟수
        end_reached = False  # 종료 항목에 도달했는지 여부

        # '2. 권리의 내용'부터 '이 경우 발생하는 손실은 모두 투자자에게 귀속됩니다.' 페이지 추출
        for page in pdf_file:
            page_text = page.get_text()

            if start_item in page_text:
                start_count += 1
                if start_count == 2:
                    found_start = True

            if found_start:
                output_pdf.insert_pdf(pdf_file, from_page=page.number, to_page=page.number)

            if end_item in page_text:
                end_reached = True
                break

    # 새로운 PDF 파일로 저장
    output_pdf.save(output_pdf_path)
    output_pdf.close()

def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()

def extract_and_convert_pdf_pages(pdf_file_path, output_pdf_path, output_docx_path, search_term, start_item, end_item):
    extract_pages_from_pdf(pdf_file_path, output_pdf_path, search_term, start_item, end_item)
    convert_pdf_to_docx(output_pdf_path, output_docx_path)

# 사용 예시
pdf_file_path = '[한국투자증권]일괄신고추가서류(파생결합사채-주가연계파생결합사채)(2023.05.11).pdf'
search_term = '모집 또는 매출에 관한 사항의 요약'
start_item = '2. 권리의 내용'  # 저장할 시작 항목
end_item = '이 경우 발생하는 손실은 모두 투자자에게 귀속됩니다.'  # 저장할 종료 항목

for file_name in file_names:
    output_pdf_path = file_name.replace('.pdf', '_추출된페이지.pdf')
    output_docx_path = file_name.replace('.pdf', '_변환된문서.docx')

    extract_and_convert_pdf_pages(file_name, output_pdf_path, output_docx_path, search_term, start_item, end_item)
    print(f"'{search_term}'를 포함하는 페이지와 '{start_item}'부터 '{end_item}'까지의 페이지를 추출하여 '{output_pdf_path}'로 저장했습니다.")
    print(f"변환된 결과를 '{output_docx_path}'로 저장했습니다.")

import fitz
import os
import shutil

def find_sentence_with_keyword(pdf_file_path, keyword):
    doc = fitz.open(pdf_file_path)
    for page in doc:
        text = page.get_text()
        if keyword in text:
            # 문자열을 줄바꿈 기준으로 분할
            lines = text.split('\n')
            # 각 줄을 순회하면서 키워드를 포함하는 첫 번째 줄을 찾음
            for line in lines:
                if keyword in line:
                    return line  # 키워드를 포함하는 첫 번째 줄 반환
    return None

for file_name in file_names:
    output_pdf_path = file_name.replace('.pdf', '_추출된페이지.pdf')
    output_docx_path = file_name.replace('.pdf', '_변환된문서.docx')
    print(output_docx_path)

    extract_and_convert_pdf_pages(file_name, output_pdf_path, output_docx_path, search_term, start_item, end_item)

    extracted_text = find_sentence_with_keyword(output_pdf_path, "트루")
    print('######################################')
    print(extracted_text)
    print('######################################')

    if extracted_text:
        new_filename = extracted_text + '.docx'
        new_filename = new_filename.replace('\n', '_').replace('\r', '')

        new_docx_dir = "/Users/yuhyeonseung/Downloads"


        if not os.path.exists(new_docx_dir):
            os.makedirs(new_docx_dir)

        new_docx_path = os.path.join(new_docx_dir, new_filename)

        shutil.move(output_docx_path, new_docx_path)

        print(f"'{search_term}'를 포함하는 페이지와 '{start_item}'부터 '{end_item}'까지의 페이지를 추출하여 '{output_pdf_path}'로 저장했습니다.")
        print(f"변환된 결과를 '{new_docx_path}'로 저장했습니다.")
    else:
        print(f"'트루'를 포함하는 문장이 없어 변환된 문서를 그대로 유지합니다.")