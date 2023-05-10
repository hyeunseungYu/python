import dart_fss as dart_fss
import pandas as pd

'''
venv 실행
source venv/bin/activate

venv 종료
deactivate

'''
api_key = '	b81bd814632ef49454b88b483de0b65a89cd7c4f'
dart_fss.set_api_key(api_key=api_key)

# https://dart-fss.readthedocs.io/en/latest/dart_corp.html

# DART API를 사용하여 회사 리스트를 조회
corp_list = dart_fss.get_corp_list()

# 검색할 회사명 입력
# corp_name = '삼성전자'

# 회사명으로 검색하여 해당 회사의 종목코드 출력
# for corp in corp_list:
#     if corp_name in corp.name:
#         print(f'{corp_name}: {corp.stock_code}')

        

all = dart_fss.api.filings.get_corp_code()

df = pd.DataFrame(all)

# 비상장
df_non_listed = df[df['stock_code'].isnull()]

# 상장
df_listed = df[df['stock_code'].notnull()]

# iloc 
corp_code = df_listed[df_listed['corp_name'] == '카카오'].iloc[0,0]
# loc를 쓴다면
# corp_code = df_listed[df_listed['corp_name'] == '카카오'].loc[81667,'corp_code']


corp_code = df_non_listed[df_non_listed['corp_name'] == '야놀자'].iloc[0,0]
data = dart_fss.api.info.alot_matter(corp_code, '2021', '11011')

df = pd.DataFrame(data['list'])

#thstrm 당기 frmtrm 전기 lwfr 전전기
#참고 : https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS002&apiId=2019005
df = df[df['se'] == '(연결)당기순이익(백만원)'][['corp_name','thstrm','frmtrm','lwfr']]
df.columns = ['기업명','2021','2020','2019']

#
# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS002&apiId=2019011
data = dart_fss.api.info.emp_sttus(corp_code, '2021', '11011')

df = pd.DataFrame(data['list'])
df = df[['corp_name','sexdstn','jan_salary_am']]
print(df)



corp_codes = list(df_listed.sample(10)['corp_code'])


def get_salary(corp_code):
  data = dart_fss.api.info.emp_sttus(corp_code, '2021', '11011')

  df = pd.DataFrame(data['list'])
  df = df[['corp_name','sexdstn','jan_salary_am']]

  df_result = pd.DataFrame()
  doc = {
      '기업명':df.iloc[0,0],
      '연봉(남)':df[df['sexdstn'] == '남'].iloc[0,2],
      '연봉(여)':df[df['sexdstn'] == '여'].iloc[0,2]
  }
  df_doc = pd.DataFrame([doc])
  df_result = pd.concat([df_result, df_doc], ignore_index=True)

  df_result['연봉(남)'] = pd.to_numeric(df_result['연봉(남)'].str.replace(',',''))
  df_result['연봉(여)'] = pd.to_numeric(df_result['연봉(여)'].str.replace(',',''))

  return df_result



dfs = []
for corp_code in corp_codes:
  try:
    df = get_salary(corp_code)
    dfs.append(df)
    
  except:
    print(f'error - {corp_code}')

df_result = pd.concat(dfs)

print(df_result)

df_result['차이(남-여)'] = df_result['연봉(남)'] - df_result['연봉(여)']
df_result['평균'] = (df_result['연봉(남)']+df_result['연봉(여)'])/2

# print(df_result.sort_values(by="차이(남-여)",ascending=True))