import pandas as pd
import datetime
import calendar

# 엑셀 파일 읽기
raw_data = pd.read_excel('/Users/yuhyeonseung/Downloads/시장약정 정리.xlsx', header=None, index_col=None)

# 오늘의 년월 구하기
today = datetime.datetime.now()

# 오늘 날짜의 이전 달의 마지막 날짜를 구하기
if today.month == 1:  # 현재 달이 1월인 경우 작년 12월로 설정
    end_date = datetime.datetime(today.year - 1, 12, 1) - datetime.timedelta(days=1)
else:
    end_date = datetime.datetime(today.year, today.month - 1, 1) - datetime.timedelta(days=1)
last_day = calendar.monthrange(end_date.year, end_date.month)[1]
print(last_day)

# 해당 셀까지의 날짜 범위를 생성
date_range = pd.date_range(start='2023-01-01', end=f'2023-{today.month - 1}-30', freq='MS')

# 해당 열에 날짜 데이터 입력
for idx, date in enumerate(date_range):
    # 새 열 추가
    raw_data.insert(idx + 3, date.strftime('%Y/%m'), "")

# 결과 확인
# print(raw_data)

# 수정한 데이터를 엑셀 파일로 저장
raw_data.to_excel('/Users/yuhyeonseung/Downloads/시장약정 정리(수정).xlsx', index=False)
