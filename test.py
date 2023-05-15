# students = [
# {"class": "A"}, 
# {"all_data": 
# 	[{"name" : "Alice", "english": 80, "science": 62},
#   {"name" : "Bob", "english": 73, "science": 70},
#   {"name" : "Charlie", "english": 60, "science": 83},
#   {"name" : "David", "english": 50, "science": 79},
#   {"name" : "Eve", "english": 75, "science": 58}]
# }
# ]

# print(students[1]['all_data'][0]['name'])

#
'''
구의 반지름을 r이라고 할 때
부피는 4/3 * pi ^3
겉넓이는 4*pi ^2
'''

#딕셔너리 만들기
key_list = ["name","hp","mp","level"]
value_list = ['전사',200,30,5]

dic = {key_list[0]:value_list[0]}
print(dic)

#for문 연습문제
numbers= [1,2,3,4,5,2,3,2,15,6,8,12,3,4,5,9]

counter = {}

for num in numbers:
    if num in counter:
        counter['num'] = counter['num'] + 1
    else:
        counter['num'] = 1

# 함수
def call():
    print('hello')
    print('hello')
    print('hello')

def call_by_num(n,text):
    for i in range(n):
        print(f'{text}')

call_by_num(5, "안녕하세요")

# f-string
a = 1
b = 2

c = "{} 더하기 {}은 {}입니다".format(a,b,a+b)



#append , concat
aList = [1, 2]
bList = [3, 4]

# append() 메서드를 사용하여 aList에 bList를 추가합니다.
aList.append(bList)
print(aList)

# concatenate() 메서드를 사용하여 aList와 bList를 연결합니다.
concatenatedList = aList + bList
print(concatenatedList)

