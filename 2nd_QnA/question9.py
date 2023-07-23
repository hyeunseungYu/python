import numpy as np
import pandas as pd

# xls 읽기 vs xlsx 읽기
df = pd.read_excel('/Users/yuhyeonseung/Downloads/temp.xls', engine='xlrd')  
# 확장자:.xlsx이면 engine='openpyxl' #df = pd.read_excel('a.xlsx', engine='openpyxl')
x = df.loc[0, :] # 0번 레코드의 모든 값
print(df)
