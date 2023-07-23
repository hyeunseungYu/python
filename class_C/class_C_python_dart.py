# dart_fss 모듈을 import합니다.
import dart_fss
# pandas 모듈을 import합니다.
import pandas as pd

# DART API 키를 입력합니다.
api_key = 'b81bd814632ef49454b88b483de0b65a89cd7c4f'
# 입력한 API 키를 dart_fss 모듈의 set_api_key() 함수를 사용하여 설정합니다.
dart_fss.set_api_key(api_key=api_key)

# dart_fss 모듈의 get_corp_list() 함수를 사용하여 기업 리스트를 조회합니다.
corp_list = dart_fss.get_corp_list()

# 조회된 기업 리스트 중 기업 정보를 담고 있는 Corporation 객체들의 리스트입니다.
# 이 리스트를 통해 기업 정보를 추출할 수 있습니다.

all = dart_fss.api.filings.get_corp_code()

df = pd.DataFrame(all)

df_listed = df[df['stock_code'].notnull()]

corp_code = df_listed[df_listed['corp_name'] == '카카오'].iloc[0,0]


new_df = df_listed[df_listed['corp_name'].str.contains('한국')]

companies = ['카카오', '삼성전자', '한국금융지주']
data_list = []

corp_code = df_listed[df_listed['corp_name'] == '카카오'].iloc[0,0]
data = dart_fss.api.info.hyslr_sttus(corp_code, '2021', '11011')
print(pd.DataFrame(data['list']))


