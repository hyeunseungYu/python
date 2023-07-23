import dart_fss

# DART API 키를 입력합니다.
api_key = 'b81bd814632ef49454b88b483de0b65a89cd7c4f'
# 입력한 API 키를 dart_fss 모듈의 set_api_key() 함수를 사용하여 설정합니다.
dart_fss.set_api_key(api_key=api_key)

# 회사 리스트를 불러옵니다
corp_list = dart_fss.get_corp_list()

# '삼성전자'라는 이름을 가진 회사를 검색합니다
samsung = corp_list.find_by_corp_name('야놀자', exactly=True)[0]

# 감사보고서를 검색합니다
fs_reports = samsung.search_filings(bgn_de='20210101', pblntf_detail_ty='F001')

print(fs_reports)
# # 각 보고서의 제목과 URL을 출력합니다
# for report in fs_reports:
#     print(f'Title: {report.title}, URL: {report.url}')



#https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20200413001927