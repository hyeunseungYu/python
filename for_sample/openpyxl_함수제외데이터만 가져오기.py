from openpyxl import load_workbook

# 엑셀 파일 열기
workbook = load_workbook('/Users/yuhyeonseung/Desktop/운용지시파일_23년2Q_230530.xlsx',data_only=True)

# 시트 선택
sheet = workbook['거래내역']

# 셀 값 가져오기
value = sheet['I303'].value  # A1 셀의 값 가져오기
print(value)

#pandas를 이용하는 것도 방법일 수도 있습니다!!

