import subprocess
from openpyxl import load_workbook


#################################
#맥에서 사용할 때                   #
#################################

wb = load_workbook('/Users/yuhyeonseung/Desktop/filtered_data_by_ticker_20230516.xlsx')

# 모든 워크시트에 대해 반복
for ws in wb.worksheets:
    # 해당 시트의 각 열에 대해서 반복
    for column in ws.columns:
        max_length = 0 #셀 너비 자동화에 사용할 변수
        column = [cell for cell in column] #각 열의 셀들을 리스트에 집어넣겠다 *list comprehension *https://wikidocs.net/22805
        for cell in column:
            try:
                # 현재 셀의 값의 길이가 max_length보다 큰지 확인. 만약 그렇다면, max_length를 현재 셀의 값의 길이로 업데이트
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) # 열 너비를 조정하기 위한 값. 셀의 가장 긴 내용물에 약간의 여유를 두기 위해 2를 더함.
        ws.column_dimensions[column[0].column_letter].width = adjusted_width

# 변경 사항을 저장합니다
wb.save('/Users/yuhyeonseung/Desktop/filtered_data_by_ticker_20230516.xlsx')

# AppleScript를 사용
script = '''
tell application "Microsoft Excel"
    set theWorkbook to open workbook workbook file name "/Users/yuhyeonseung/Desktop/filtered_data_by_ticker_20230516.xlsx"
    set theOutputPath to "/Users/yuhyeonseung/Desktop/filtered_data_by_ticker_20230516.pdf"
    save theWorkbook in theOutputPath as PDF file format
    close theWorkbook
end tell
'''

# AppleScript를 실행
subprocess.run(['osascript', '-e', script])



#################################
#윈도우에서 사용할 때                #
#################################
'''
import win32com.client

# Excel 켜기
excel = win32com.client.Dispatch("Excel.Application")

# 워크북 열기
doc = excel.Workbooks.Open('path_to_your_file.xlsx')

# 워크북의 모든 워크시트에 대해 for문 돌기
for ws in doc.Worksheets:
    # 열 너비를 자동으로 조정
    ws.Columns.AutoFit()

# 워크북을 PDF로 저장
doc.ExportAsFixedFormat(0, 'output.pdf')

# 워크북을 닫기
doc.Close(SaveChanges=False)

# Excel을 종료(종료해줘야됨!)
excel.Quit()


'''