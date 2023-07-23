import pandas as pd

data = '''차장J
대리
사원S
대리
차장S
차장S
사원S
사원S
사원J
사원S
사원S
대리
대리
사원S
사원S
사원J
차장S
사원S
차장S
차장J
사원S
사원S
차장S
사원S
사원S
차장J
사원S
대리
사원S
사원S
사원S
차장S
대리
대리
사원S
사원J
사원S
사원J
대리
대리
차장S
사원S
대리
차장S
대리
대리
차장J
사원S
대리
차장J
사원S
사원S
대리
사원S
사원S
사원J
대리
사원J
사원S
대리'''

# 개행 문자를 기준으로 데이터를 분할하여 리스트로 변환
data_list = data.split('\n')


df = pd.DataFrame({'변환전':data_list})

def 카테고리_직급(이름):
    if '사원' in 이름:
        return '사원'
    elif '대리' in 이름:
        return '대리'
    elif '차장' in 이름:
        return '차장'
    elif '부장' in 이름:
        return '부장'
    else:
        return '기타'
    

df['직급'] = df['변환전'].apply(카테고리_직급)
직급별_사람_수 = df.groupby('직급').size()

print(직급별_사람_수)



