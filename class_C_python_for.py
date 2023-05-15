'''
for문 기초예제
'''

'''
Q1
아래와 같이 fruits라는 리스트가 주어졌을 때, 
for문을 활용해서 fruits의 요소들을 print하도록 코드를 작성해 주세요
'''
fruits = ["사과", "바나나", "딸기"]

# for fruit in fruits:
#     print(fruit)

'''
Q2
range() 함수를 사용해서 1부터 5까지를 print하는 함수를 작성해 주세요
'''
# for num in range(1, 6):
#     print(num)


'''
Q3
다음과 같이 scores라는 리스트가 주어졌을때,
"1번째 학생의 점수는 90" 과 같이 print되도록 작성해 주세요
'''

scores = [80, 90, 70, 85, 60]

# for i in range(len(scores)):
#     print(i+1,"번째 학생의 점수는", scores[i])

##########################

# count = 0

# for score in scores:
#     count += 1
#     print(count, "번째 학생의 점수는", score)


'''
Q4
다음과 같이 numbers라는 리스트가 주어졌을때,
짝수라면 (~는 짝수입니다)
홀수라면 (~는 홀수입니다)라고 출력되도록 코드를 작성해 주세요
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num % 2 == 0:
#         print(num, "은(는) 짝수입니다.")
#     else:
#         print(num, "은(는) 홀수입니다.")

'''
Q5
아래의 nested_list는 리스트 안의 요소들이 리스트로 이루어진 리스트 입니다.
flattened_list라는 빈 리스트를 생성하고, [1,2,3,4,5,6,7,8,9]와 같이 되도록 해 주세요
'''

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flattened_list = []

# for sublist in nested_list:
#     for item in sublist:
#         flattened_list.append(item)

# print(flattened_list)