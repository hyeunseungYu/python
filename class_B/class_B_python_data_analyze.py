import pandas as pd
import datetime

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

#read_csv의 기본 구분자는 ,임
#read_table의 기본 구분자는 탭임
sparta_data = pd.read_csv('/Users/yuhyeonseung/Downloads/access_detail.csv')

print(type(sparta_data['access_date'][0]))
# sparta_data.head(40)

#######################################

now = datetime.datetime.now()
print(now)
print(type(now))

print()

dt_str = '2022-12-31 23:59:59'
print(dt_str)
print(type(dt_str))

print()

dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

#dt가 어떤 함수를 지원하는 지 볼 수 있음
print(dir(dt))
print(dt)
print(type(dt))

new = now.strftime('%y%m%d')


'''
%d : 0을 채운 10진수 표기로 날짜를 표시
%m : 0을 채운 10진수 표기로 월을 표시
%y : 0을 채운 10진수 표기로 2자리 년도
%Y : 0을 채운 10진수 표기로 4자리 년도
%H : 0을 채운 10진수 표기로 시간 (24시간 표기)
%I : 0을 채운 10진수 표기로 시간 (12시간 표기)
%M : 0을 채운 10진수 표기로 분
%S : 0을 채운 10진수 표기로 초
%f : 0을 채운 10진수 표기로 마이크로 초 (6자리)
%A : locale 요일
%a : locale 요일 (단축 표기)
%B : locale 월
%b : locale 월 (단축 표기)
%j : 0을 채운 10진수 표기로 년중 몇 번째 일인지 표시 
%U : 0을 채운 10진수 표기로 년중 몇 번째 주인지 표시 (일요일 시작 기준)
%W : 0을 채운 10진수 표기로 년중 몇 번째 주인지 표시 (월요일 시작 기준)
'''

###############################################################

format='%Y-%m-%d %H:%M:%S'
# sparta_data['access_date_time'] = pd.to_datetime(sparta_data['access_date'], format=format,errors='coerce')
sparta_data['access_date_time'] = pd.to_datetime(sparta_data['access_date'], format='mixed')

###############################################################


#axis가 0이면 행, 1이면 열. 기본값은 0이어서 행인경우 생략해도 됨.
sparta_data = sparta_data.drop('access_date', axis=1)
# sparta_data.drop(0, axis=0)

###############################################################

#weekday_name은 구버전!
sparta_data['access_date_time_weekday'] = sparta_data['access_date_time'].dt.day_name()
sparta_data.tail(5)

###############################################################

weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdata = sparta_data.groupby('access_date_time_weekday')['user_id'].count()
# print(weekdata.get_group("Monday"))

weekdata = weekdata.reindex(weeks)

###############################################################

sales_data = pd.DataFrame({
    'store_id': ['A', 'A', 'B', 'B', 'B', 'C', 'C'],
    'product_id': ['X', 'Y', 'X', 'Y', 'Z', 'X', 'Z'],
    'sales': [10, 20, 30, 15, 25, 12, 18]
})

grouped_sales = sales_data.groupby('store_id')

#groupedsales의 요소를 하나 가져와서, 그 안에 있는 것들을 순서대로
for name, group in grouped_sales:
    print(name)
    print(group)

#sales라는 열에 대해서 sum과 mean을 실행한 것을 보여주겠다
agg_sales = grouped_sales.agg({'sales': ['sum', 'mean']})

print(agg_sales)


#########################################################

# [날짜 컬럼].dt.hour 을 사용하면 해당 날짜의 시간 값을 가져 올수 있어요! 

sparta_data['access_date_time_hour'] = sparta_data['access_date_time'].dt.hour

hourdata = sparta_data.groupby('access_date_time_hour')['user_id'].count()

# sparta_data
hourdata.sort_index()
# hourdata

##########################################################



rcParams['font.family'] = 'AppleGothic'

#그래프 사이즈
plt.figure(figsize=(10,5))

#그래프 x축 y축
plt.bar(weekdata.index, weekdata)

#그래프 명
plt.title('요일별 수강 완료 수강생 수')

#그래프 x축 레이블
plt.xlabel('요일')

#그래프 y축 레이블
plt.ylabel('수강생(명)')

#x축 레이블을 90도로 변환 
plt.xticks(rotation=90)

#그래프 출력
plt.show()

##################################################################

#그래프 사이즈 변경
plt.figure(figsize=(10,5))

#그래프 x축 y축
plt.plot(hourdata.index, hourdata)

#그래프 명
plt.title('시간별 수강 완료 사용자 수')

#그래프 x축 레이블
plt.xlabel('시간')

#그래프 y축 레이블
plt.ylabel('사용자(명)')

#x축 눈금 표시 하기
plt.xticks(np.arange(24))

#그래프 출력
plt.show()


#####################################################################

#피벗테이블 만들기

#values : 피벗 테이블의 데이터로 사용할 열. 여기서는 user_id 열을 사용하여 테이블을 구성합니다. -> user_id 갯수를 센다는 이야기
#index : 행에 들어가는 부분
#aggfunc : 데이터 축약시 사용할 함수
weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sparta_data_pivot_table = pd.pivot_table(sparta_data, values='user_id', 
                       index=['access_date_time_weekday'],
                       columns=['access_date_time_hour'], 
                       aggfunc="count").agg(weeks)
