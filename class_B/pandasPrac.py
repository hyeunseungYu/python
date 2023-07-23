import pandas as pd
import numpy as np

#pandas에서는 데이터프레임을 만들때 데이터를 딕셔너리로 전달해야 합니다.
# 또한 그 딕셔너리의 값(value)을 리스트로 묶어주어야 합니다.  
data = {"name": ["영수", "철수", "영희", "소희"], "age": [20, 15, 38, 8]}

df = pd.DataFrame(data)

doc = {
    "name": "세종",
    "age": 14,
}



# # append : 리스트에 값을 추가하는 함수
# df = df.append(doc,ignore_index=True)


# or pandas 최신버전에서는 append가 deprecated
# ignore_index는 왜?
# 만약에 A라는 회사와 B라는 회사가 있다. -> 사번 체계가 같았다! -> 그대로 합치면 문제 발생!
# 그것과 비슷하게 우리가 df를 사용할 때에도 문제가 발생할 수 있으니 ignore_index를 사용하는 것

test_df = pd.DataFrame([doc])
new_df = pd.DataFrame({"name": ["세종"], "age": [14]})
df = pd.concat([df, new_df], ignore_index=True)


df["city"] = ["서울", "부산", "서울", "대구", "서울"]

###########################################################################


# concat예시
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

df_concat = pd.concat([df1, df2])

print(df.iloc[0, 1])
print(df.loc[0, "city"])

print()


# df.sort_values(by='age',ascending=False)

# dtype='<U3'는 NumPy 배열의 데이터 타입을 나타내는 것. <U3는 유니코드 문자열을 의미하며, 문자열의 길이가 3이라는 것을 의미
is_adult= np.where(df["age"] > 18, "성인", "청소년")

df["is_adult"] = is_adult

# 최대값의 인덱스 뽑을떄
idx = df[df["city"] == "서울"]["age"].idxmax()

# 중간값
median_age = df["age"].median()

# df[df['city'] == '서울' & df['age'] >18] 이런 식으로 하면 연산자의 우선순위가 달라 에러가 발생함
df[(df["city"] == "서울") & (df["age"] > 18)]


# dataFrame크기 반환
print(df.shape)

# (df['city'] == '서울') & (df['age'] >18) 이 부분을
# cond = (df['city'] == '서울') & (df['age'] >18) 이렇게 밖으로 빼줄 수도 있음
print(len(df[(df["city"] == "서울") & (df["age"] > 18)]))


# marketcap = all_data['TSLA']['price']['marketCap']
# formatted_marketcap = '{:,.0f}'.format(marketcap)
#{:,}로 쓰면 됨
# print(formatted_marketcap)


string = 'f가 뭘까?'
c = "{} 나도 잘 모르겠어".format(string)