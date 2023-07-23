import dart_fss as dart_fss
import pandas as pd

api_key = 'b81bd814632ef49454b88b483de0b65a89cd7c4f'
dart_fss.set_api_key(api_key=api_key)

all = dart_fss.api.filings.get_corp_code()

df = pd.DataFrame(all)

df_non_listed = df[df['stock_code'].isnull()]

corp_code = df_non_listed[df_non_listed['corp_name'] == '아워홈'].iloc[0,0]

company = dart_fss.api.filings.get_corp_info(corp_code=corp_code)  # 감사보고서를 찾고자 하는 회사의 코드

print(company)
