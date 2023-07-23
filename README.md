##KIDX 4회차까지 C반 내용 정리

<aside>
🙌 해당 자료는 기존 파이썬 기초 문법의 복습을 위한 자료입니다!
이전 교안의 자료의 내용을 토대로 단순히 복습을 위한 !!**참고자료!!** 이니,
복습을 위한 자료로만 사용하여 주시면 감사하겠습니다 😃

</aside>

- 파이썬이란!
  파이썬은 귀도 반 로섬이 발표한 프로그래밍 언어입니다.
  파이썬이라는 이름은 귀도 반 로섬이 BBC의 코미디 시리즈인 "Monty Python's Flying Circus”에서 출판된 대본을 읽고 여기에서 이름을 가져왔다고 하네요!(https://docs.python.org/3/faq/general.html#why-is-it-called-python)
  파이썬은 문법이 간단해서 배우기 쉽고, 다양한 분야에서 활용할 수 있어 초보자가 처음 배우는 언어로도 인기가 많습니다.
  여기에서! 우리는 파이썬이 프로그래밍 ‘언어’라는 것을 알고 있습니다!
  한국어, 영어, 중국어 … 언어에는 우위가 없습니다.
  프로그래밍 언어도 비슷합니다! 특화된 분야는 있지만, 각 언어에는 우위가 없다는 것만 짚고 넘어가겠습니다!

## 키워드

키워드는 특별한 의미가 부여된 단어로 파이썬이 만들어질 때 이미 사용하겠다고 예약해 놓은 것입니다!

그럼 이 키워드를 왜 구분해야할까요?🧐

바로 우리가 코딩을 할 때, 변수명이나 함수명 등을 정할 때 키워드를 사용하면 안되기 때문입니다!

파이썬의 키워드는 아래와 같습니다!

```python
['False', 'None', 'True', 'and', 'as',
'assert', 'async', 'await', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except',
'finally', 'for', 'from', 'global', 'if', 'import',
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
'raise', 'return', 'try', 'while', 'with', 'yield']
```

그리고 파이썬은 대소문자를 구분합니다!!

예를 들어 `True` 는 키워드지만 `true` 는 키워드가 아닙니다!

그럼 우리는 이 키워드를 전부 외워야 할까요?

<aside>
🔥 **절대 아닙니다!**

</aside>

이 키워드는 코드를 작성하다 보면 저절로 익혀집니다.
절대 외우지 마세요!

그래도 내가 사용하고 싶은 단어가 키워드인지 알고싶다면 아래의 코드를 사용해 보세요!

```python
import keyword
print(keyword.kwlist)
```

아래처럼 출력되는 걸 확인하실 수 있답니다!

![Screenshot 2023-06-14 at 8.46.16 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/38de47df-ee22-48f7-8646-f8e5ddcc8057/Screenshot_2023-06-14_at_8.46.16_PM.png)

---

## 출력

우리가 코딩을 하다보면, 지금 내가 잘 하고 있는 건지 확인하고 싶으실 때가 있죠?

이럴때 사용하는 것이 바로 출력! 파이썬의 가장 기본적인 출력 방법은 print() 함수를 사용하는 것입니다.

이미 우리가 많이 사용해봐서 사용법은 익숙하시죠?

조금 더 알아보자면, print() 함수에서는 출력하고 싶은 내용을 쉼표로 연결해서 여러개를 적을 수도 있답니다!

![Screenshot 2023-06-14 at 8.52.57 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bea956f2-7939-45a7-b957-f2c831c645ba/Screenshot_2023-06-14_at_8.52.57_PM.png)

그렇다면 print() 함수의 인자 값으로 아무것도 전달하지 않으면 어떻게 될까요?

이런 경우에는 줄바꿈을 해 줍니다!

![Screenshot 2023-06-14 at 8.54.54 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/701bffb8-1ff3-408e-9707-a491f18f3772/Screenshot_2023-06-14_at_8.54.54_PM.png)

<aside>
❓ 엥? 근데 주피터 노트북에서 대충 print 안써도 값이 나오던데, 왜 print()를 써야돼요?

</aside>

<aside>
❗ 주피터 노트북에서 단순히 1+1이라고만 입력하고 실행을 해도 아래처럼 값이 나오기는 합니다!

![Screenshot 2023-06-14 at 8.58.31 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04a3fa3e-c3dd-4515-84e0-a759d393b309/Screenshot_2023-06-14_at_8.58.31_PM.png)

그리고 pandas를 사용하실 때에도 확인하셨을텐데요,
마지막에 print(df)를 썼을때에는 텍스트 형태로,
df를 사용했을때에는 더 이쁘게 나오는 것을 보셨을겁니다.

**하지만!** 이 기능은 주피터 노트북의 특성이므로
다른 파이썬 실행 환경에서는 동일한 방식으로 작동하지 않습니다!!
(주피터 노트북에서는 셀의 마지막 표현식이 반환하는 값을 자동으로 출력합니다)

</aside>

---

## int / float?

숫자에는 두 종류가 있습니다

소수점이 있는 숫자와 소수점이 없는 숫자입니다!

이미 이전에 확인해 보셔서 아시겠지만,

아래와 같이 int(integer)는 소수점이 없는 정수! float(floating point)는 소수점이 있는 실수! 입니다.

![Screenshot 2023-06-14 at 9.11.51 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6db7dede-60cf-474c-a2ec-110dc66d0b73/Screenshot_2023-06-14_at_9.11.51_PM.png)

마찬가지로 **0은 int!** **0.0은 float 입니다!**
실제 엑셀을 다루실때 가끔 실수하기도 하는 부분이니 참고해 주세요!

![Screenshot 2023-06-14 at 9.13.46 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cf0ca210-4508-4a72-a5e8-1f522da46059/Screenshot_2023-06-14_at_9.13.46_PM.png)

<aside>
❓ 어디에선가 값을 가져왔는데 0.1234e2 이런 값이 나와요.
이게 뭔가요?

</aside>

<aside>
❗ 파이썬에서 e는 10의 거듭제곱을 뜻합니다!
위의 경우에는 e2는 10의 2승을 나타냅니다. 
따라서 0.1234e2는 12.34와 동일한 값을 가지게 되겠네요!

</aside>

---

## 들여쓰기 indent

for문이나 if문 등을 사용할 때에 들여쓰기가 있다는 것은 모두 알고 계시죠?

파이썬 개발에서는 들여쓰기를 띄어쓰기 4번을 많이 사용합니다!

그런데 들여쓰기 하겠다고 스페이스바를 네번이나 누르는 건 내 정신건강과 손가락 건강에 좋지 않겠죠?

그래서 우리는 들여쓰기를 `tab` 을 이용해서 사용합니다!

그리고 여러 줄의 들여쓰기를 제거할 때에는 `shift + tab` 을 누르면 됩니다!

- 변수 & 기본 연산
  ## 변수
  변수는 값을 저장하는 상자입니다!
  그리고 이 상자에는 여러 가지 물건을 넣을 수 있습니다.
  예를 들어 `apple` 이라는 이름의 상자가 있고 여기에 사과를 넣었다고 해 보겠습니다!
  그런 다음에 `apple` 이라는 이름의 상자를 열어보면 사과가 들어있는 걸 확인할 수 있겠죠?
  변수도 마찬가지 입니다!
  변수도 이름을 가지고 있고, 그 이름을 호출하면 그 안에 저장된 값을 볼 수 있습니다.
  ```python
  apple = '사과'
  print(apple)
  ```
  ***
  ## 기본 연산
  우리가 생각하는 기본 사칙연산을 파이썬에서도 사용할 수 있습니다!
  `+` 는 덧셈 연산자!
  `-` 는 뺄셈 연산자!
  `*` 는 곱셈 연산자!
  `/` 는 나눗셈 연산자!
  이전에 배우기도 했고, 너무 쉽죠?
  몇가지 더 추가해보죠!
  정수 나누기 연산자 `//` !
  이건 나누기를 하고 소숫점 이하 자릿수를 없애고 정수만 반환하는 연산자 입니다!
  아래 예시를 보면 이해가 쉬우실 겁니다
  ![Screenshot 2023-06-14 at 9.32.36 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2bfd3509-9e36-459b-a6f2-2986890922e0/Screenshot_2023-06-14_at_9.32.36_PM.png)
  그리고 나머지 연산자 `%` !
  이것은 나머지를 구하는 연산자입니다.
  보통 사용하실 기회가 많지 않으실텐데, 이런 게 있구나! 하는 정도로 알고 넘어가 주세요!
  ![Screenshot 2023-06-14 at 9.34.46 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc71d6af-7f63-423d-ac25-22f13433c5c8/Screenshot_2023-06-14_at_9.34.46_PM.png)
  ***
  ## f-string?
  f-string은 다들 한 번씩 써 보셨을 겁니다!
  이젠 어느정도 익숙하시겠지만, 다시 한 번 짚고 넘어가시죠!
  사실 이 f-string은 파이썬 3.6버전부터 등장했습니다!
  그래서 python 2.7이나 이전 버전을 사용하면 syntax error를 마주하게 됩니다🥲
  원래는 format 함수를 이용해서 아래와 같이 사용했었는데요, f-string이 등장하고 나서는 이게 더 직관적이고 알아보기 쉬워서 거의 f-string만 사용하는 편입니다!
  ![Screenshot 2023-06-14 at 9.57.24 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7507d34-59a4-4d19-b753-49614a72cbdb/Screenshot_2023-06-14_at_9.57.24_PM.png)
  f-string은 아래와 같은 형식을 가집니다.
  ```python
  f’~~~{표현식}~~~~’
  ```
  여기에서 표현식이란 값, 변수, 연산자를 말합니다! 머리가 더 어지러워지기 전에 그냥 변수가 들어간다! 라고 생각하셔도 좋을 것 같습니다.
    <aside>
    🔥 QUIZ
    
    </aside>
    
    ```python
    '''
    Q1
    다음 코드의 실행 결과를 예측해 보세요
    '''
    
    print(15, "+", 4, "=", 15+4)
    ```
    
    ```python
    '''
    Q2
    다음 코드에서 ~~부분을 채워주세요
    '''
    
    print("4783을 7로 나누면?")
    print("몫은 -> ", ~~~~~)
    print("나머지는 -> ", ~~~~~)
    ```
    
    - 답안
        
        ```python
        Q1. 15 + 4 = 19
        Q2. 4783 // 7, 4783 % 7
        ```

- 리스트 & 딕셔너리
  ## 리스트
  리스트는 파이썬에서 여러가지 자료를 모아둔 형태라고도 할 수 있습니다.
  리스트는 대괄호[]에 자료를 **쉼표**로 구분해서 입력하여 사용합니다.
  대괄호[] 내부에 들어가는 것들을 요소, element라고 부릅니다!
  아래와 같은 리스트가 있다고 해 보겠습니다.
  ```python
  list_prac = ['히히', '깔깔', '익스큐즈미']
  ```
  그리고 이 리스트의 요소들은 아래와 같이 숫자로 접근할 수 있습니다!
  그리고 컴퓨터는 숫자를 0부터 센다는 것 기억하시죠?
  | ‘히히’ | '깔깔’ | '익스큐즈미’ |
  | ------ | ------ | ------------ |
  | [0]    | [1]    | [2]          |
  리스트에 요소를 추가하고 싶다면! `append` 를 사용합니다!
  ```python
  리스트명.append(요소)
  ```
  혹시 리스트 중간에 추가하고 싶다면? `insert` 를 사용합니다!
  ```python
  리스트명.insert(위치,요소)
  ```
  ![Screenshot 2023-06-14 at 10.21.01 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/00769cd5-d501-4203-a885-f0528d13cc11/Screenshot_2023-06-14_at_10.21.01_PM.png)
  위의 경우에는 아래와 같았다가
  | 1   | 2   | 3   | 4   | 5   |
  | --- | --- | --- | --- | --- |
  | [0] | [1] | [2] | [3] | [4] |
  insert로 이렇게 바뀐 셈이죠!
  | 1   | 2   | 6   | 3   | 4   | 5   |
  | --- | --- | --- | --- | --- | --- |
  | [0] | [1] | [2] | [3] | [4] | [5] |
  - (알아두면 좋은) 파괴적 ? 비파괴적?
    append는 파괴적이라고 표현하고 list_a + list_b는 비파괴적이라고 표현한다는 내용 정리하기
  리스트에서 요소를 제거하고 싶다면? `pop` !
  ```python
  리스트명.pop(인덱스)
  ```
    <aside>
    🔥 QUIZ
    
    </aside>
    
    ```python
    students = [
    {"class": "A"}, 
    {"all_data": 
    	[{"name" : "Alice", "english": 80, "science": 62},
      {"name" : "Bob", "english": 73, "science": 70},
      {"name" : "Charlie", "english": 60, "science": 83},
      {"name" : "David", "english": 50, "science": 79},
      {"name" : "Eve", "english": 75, "science": 58}]
    }
    ]
    ```
    
    ```python
    #딕셔너리 만들기
    key_list = ["name","hp","mp","level"]
    value_list = ['전사',200,30,5]
    charactor = {}
    
    #charactor = {"name" : '전사', 'hp':200, 'mp':30, 'level':5}
    ```
    
    ```jsx
    enack = [
    {'식품유형' : '과자/유탕처리제품'},
    {'원재료명' : ['밀가루','타피오카전분',['설탕','마늘분말','향미증진제']]},
    {'영양정보' : {'나트륨' : 10,'탄수화물':12, '지방' : {'트랜스지방' : 0, '포화지방' : 36}}}
    ]
    ```
    
    ```python
    {
      "id":  "http://some.site.somewhere/entry-schema#",
      "$schema":  "http://json-schema-org/draft-06/schema#",
      "type":  "object",
      "required":  [ "options" ],
      "properties":  {
        "options":  {
          "type":  "array",
          "description": "Interesting details: Fresh New Awesome",
          "minItems":  1,
          "items":  { "type":  "string" },
          "uniqueItems":  rue,
        },
        "readonly":  { "type":  "boolean" }
      }
    }
    ```
    
    - 답안
        
        ```python
        for i in range(len(key_list)):
            charactor[key_list[i]] = value_list[i]
        ```

- 반복문(for문)
  ## 반복문
  우리가 1이라는 숫자를 100번 반복해서 쓴다고 생각해 보겠습니다.
  벌써 엄청 피곤하게 느껴지죠?
  그렇다면 컴퓨터는 어떨까요?
  컴퓨터는 아무리 반복해도 컴퓨터는 지루해 하지도, 능률이 떨어지지도 않습니다.
  이게 바로 컴퓨터의 장점이죠!
    <aside>
    ❓ 그렇다면 컴퓨터에게 반복 작업은 어떻게 시키면 될까요?
    
    </aside>
    
    - 첫번째 방법은 반복할 작업을 복사하고, 원하는 만큼 붙여넣기를 하는 것입니다!
    하지만 이러면 반복할 작업이 무수히 많을때에는 너무나 힘들겠죠?
        
        ![안돼요..](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/86bdde01-3cb0-43b3-8c8f-17bc6b0e905a/%E1%84%82%E1%85%AE%E1%86%AB%E1%84%86%E1%85%AE%E1%86%AF.png)
        
        안돼요..
        
    - 두번째 방법은 for문! 반복문을 사용하는 것입니다.
    예를 들어 아래와 같이 코드를 쓸 수 있겠죠?
    
    ```python
    for i in range(100):
    	print(i)
    ```
    
    for문의 형태는 아래와 같습니다.
    
    ```python
    for 변수 in 반복할 수 있는 것:
    	코드블럭
    ```
    
    <aside>
    🔥 QUIZ
    
    </aside>
    
    ```python
    '''
    Q1
    아래와 같이 fruits라는 리스트가 주어졌을 때, 
    for문을 활용해서 fruits의 요소들을 print하도록 코드를 작성해 주세요
    '''
    fruits = ["사과", "바나나", "딸기"]
    ```
    
    ```python
    '''
    Q2
    range() 함수를 사용해서 1부터 5까지를 print하는 코드를 작성해 주세요
    '''
    
    ```
    
    ```python
    '''
    Q3
    다음과 같이 scores라는 리스트가 주어졌을때,
    "1번째 학생의 점수는 90" 과 같이 print되도록 작성해 주세요
    '''
    
    scores = [80, 90, 70, 85, 60]
    
    ```
    
    ```python
    '''
    Q4
    다음과 같이 numbers라는 리스트가 주어졌을때,
    짝수라면 (~는 짝수입니다)
    홀수라면 (~는 홀수입니다)라고 출력되도록 코드를 작성해 주세요
    '''
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    ```
    
    ```python
    '''
    Q5
    아래의 nested_list는 리스트 안의 요소들이 리스트로 이루어진 리스트 입니다.
    flattened_list라는 빈 리스트를 생성하고, [1,2,3,4,5,6,7,8,9]와 같이 되도록 해 주세요
    '''
    
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    
    flattened_list = []
    
    ```
    
    ```python
    '''
    Q6
    for문을 사용하여 1부터 10까지의 숫자 중에서 홀수만 출력되도록 해주세요
    '''
    
    ```
    
    ```python
    '''
    Q7
    제시된 코드를 사용하여 아래와 같은 결과물을 얻고자 합니다. 어떻게 하면 될까요?
    {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '15': 1, '6': 1, '8': 1, '12': 1, '9': 1}
    '''
    numbers= [1,2,3,4,5,2,3,2,15,6,8,12,3,4,5,9]
    
    counter = {}
    
    ```
    
    - 답안
        
        ```python
        Q1.
        for fruit in fruits:
        	print(fruit)
        
        Q2.
        for num in range(1, 6):
        	print(num)
        
        Q3.
        for i in range(len(scores)):
        	print(i+1,"번째 학생의 점수는", scores[i])
        
        ##########################
        
        count = 0
        for score in scores:
        	count += 1
        	print(count, "번째 학생의 점수는", score)
        
        Q4.
        for num in numbers:
        	if num % 2 == 0:
        		print(num, "은(는) 짝수입니다.")
        	else:
        		print(num, "은(는) 홀수입니다.")
        
        Q5.
        for sublist in nested_list:
        	for item in sublist:
        		flattened_list.append(item)
        
        print(flattened_list)
        
        Q6.
        
        for num in range(1, 11):
        	if num % 2 != 0:
        		print(num)
        			
        Q7.
        for num in numbers:
            if num in counter:
                counter[str(num)] = counter[str(num)] + 1
            else:
                counter[str(num)] = 1
        
        print(counter)
        ```

- 반복문(while)
  while 반복문은 아래와 같은 형태를 가집니다!
  ```python
  while 참 혹은 거짓이 오는 것:
  	코드블럭
  ```
  while문에서는 <참 혹은 거짓이 오는 것>에서 참인 경우, 코드블럭을 계속 반복합니다!
  예시로 아래와 같이도 쓸 수 있겠네요!
  ```python
  i = 0
  while i < 10:
  	print(f"{i}번째 반복입니다요")
  	i += 1
  ```
    <aside>
    ❓ 그럼 for문과 while문 중 뭘 써야하나요?
    
    </aside>
    
    <aside>
    ❗ 더 편하다고 생각되거나 더 적합하다고 판단되는 걸 사용하시면 됩니다!
    다만 지금은 while문 보다 for문을 더 익숙하다고 생각하실테고, 실제로도 거의 for문을 사용하시게 될 겁니다!
    
    </aside>
    
    ---
    
    ## break? continue?
    
    break는 반복문 완전 종료!! continue는 지금 실행 중인 반복만 종료!!
    
    아래 예시를 통해 확인하시면 이해가 더 쉬우실 겁니다!
    
    ```jsx
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```
    
    ```jsx
    for i in range(10):
        if i == 5:
            continue
        print(i)
    ```

- 조건문
  ## if 조건문
  조건문은 조건에 따라 코드를 실행하거나, 실행하지 않게 만들고 싶을 때 사용합니다!
  아래 예시로 확인해 보겠습니다!
  ```python
  if True:
  	print("True 입니다")
  	print("아 True 맞다구요")
  ```
  그렇다면 아래의 코드의 결과물은 어떻게 나올까요?
  ```python
  if False:
  	print("False 인데요?")
  ```
  요렇게 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰는 것이 바로 if문이라고 합니다!
  그런데!
  우리가 홀수와 짝수를 판별해야 하는 상황이라고 가정해 보겠습니다.
  ```python
  number = 2

  if number % 2 == 0:
  	print("짝수지롱")

  if number % 2 == 1:
  	print("홀수지롱")
  ```
  물론! 이렇게 해도 답은 나옵니다!
  다만 홀수가 아니면 반드시 짝수이고 , 홀수라면 반드시 짝수가 아니죠?
  이렇게 정반대되는 상황에서 두 번이나 조건을 비교하는 것은 굳이라는 생각이 들지 않나요?
  ![컴퓨터는 이것을 기억할 것입니다 (무조건 나쁘다는 뜻 아님)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6cf5cc70-5066-4c96-bf8e-69651dc114de/%E1%84%90%E1%85%B3%E1%86%A8%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%A5%E1%86%B7.png)
  컴퓨터는 이것을 기억할 것입니다 (무조건 나쁘다는 뜻 아님)
  그럴때 사용하는 것이 바로 else! 위 코드를 이렇게 바꿀 수 있겠네요!
  ```python
  number = 2

  if number % 2 == 0:
  #조건이 참이면 이거 해라!
  	print("짝수지롱")

  else:
  #조건이 거짓이면 이거 해라!
  	print("홀수지롱")
  ```
  추가로 elif도 있었죠! 우리가 보통 사용할 때에는 아래와 같은 형태로 사용하게 됩니다
  ```python
  if 조건A:
  	조건A가 참일 때
  elif 조건B:
  	조건B가 참일 때
  elif 조건C:
  	조건C가 참일 때
  else:
  	모든 조건이 거짓일 때
  ```
    <aside>
    🔥 QUIZ
    
    </aside>
    
    ```python
    '''
    input으로 사용자로부터 값을 입력받아 0보다 크면 '양수입니다'를,
    0보다 작으면 '음수입니다',
    0이라면 '0입니다' 를 출력하는 코드를 작성해 주세요
    '''
    ```
    
    ```python
    '''
    한 때 대학생 커뮤니티에서 아래와 같은 유머가 있었습니다.
    학점이 4.5면 신
    4.2 ~ 4.5면 교수님의 사랑
    3.5 ~ 4.2면 현 체제의 수호자
    2.8 ~ 3.5면 일반인
    2.3 ~ 2.8면 일탈을 꿈꾸는 소시민 
    1.0 ~2.3면 불가촉 천민
    0 ~ 1.0은 플랑크톤
    0은 시대를 앞서가는 혁명의 씨앗
    
    이것을 조건문으로 구현해 보세요!
    
    '''
    ```
    
    - 답안
        
        ```python
        Q1.
        num = int(input("숫자를 입력하세요: ")) 
        
        if num > 0:
            print("양수입니다.")
        elif num < 0:
            print("음수입니다.")
        else:
            print("0입니다.")
        
        Q2.
        
        grade = float(input()) 
        
        # 학점에 따른 메시지 출력
        if grade == 4.5:
            print("신")
        elif 4.2 <= grade < 4.5:
            print("교수님의 사랑")
        elif 3.5 <= grade < 4.2:
            print("현 체제의 수호자")
        elif 2.8 <= grade < 3.5:
            print("일반인")
        elif 2.3 <= grade < 2.8:
            print("일탈을 꿈꾸는 소시민")
        elif 1.0 <= grade < 2.3:
            print("불가촉 천민")
        elif 0 < grade < 1.0:
            print("플랑크톤")
        elif grade == 0:
            print("시대를 앞서가는 혁명의 씨앗")
        ```

- 함수
  ## 함수
  함수는 코드의 집합이라고도 할 수 있습니다. 그리고 아래와 같은 형태를 가집니다!
  ```python
  def 함수이름():
  	코드블럭
  ```
  ```python
  def 붕어빵만들기(속재료):
  	print('붕어빵 만들기~~')
  	print(f'{속재료}맛 붕어빵을 만들었어요!')

  	return 붕어빵

  ```
  여기에서 만약! **return**이 없다면?
  ![i13428937115.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/91f41781-b33f-4cb3-8652-b0909b12be33/i13428937115.png)
  그럼 함수를 왜 쓰나요?
  바로 **‘코드의 재사용성’!**
  함수를 한 번 정의하면 어디에서든 필요할 때마다 해당 함수를 호출하여 사용할 수 있습니다.
  이는 동일한 코드를 여러 번 쓰는 것을 방지해 줍니다!
  ![공대생들의 멋있는 패션이 한껏 재사용된 모습.
  함수를 사용한 듯 하다.](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e704c633-03ca-4786-af3c-30ec03c74b24/%E1%84%92%E1%85%A1%E1%86%B7%E1%84%89%E1%85%AE.jpg)
  공대생들의 멋있는 패션이 한껏 재사용된 모습.
  함수를 사용한 듯 하다.
  그렇다면 무조건 함수를 쓰는 게 좋을까요?
  **아닙니다!**
  재사용성이 낮은 코드인데, 굳이 함수로 만드는 건
  딱 한 번 만들 붕어빵을 위해 붕어빵 기계를 만드는 셈입니다!
  ```python
  '''
  Q1
  아래와 같이 정의된 함수가 있을때, 결과값을 예상해 보세요
  '''
  def hello():
      print("안녕하세요!")

  hello()

  ```
  ```python

  '''
  Q2
  위의 greet라는 함수를 활용해서, 함수의 인자 (괄호안에 들어가는 값)에 이름을 넣으면
  "안녕하세요 ~~~ 님!"과 같이 출력되도록 해 주세요
  '''
  def hello(name):
      print("안녕하세요, " , name , "님!")

  hello("영희")
  ```
  ```python
  '''
  Q3
  a,b라는 숫자를 매개변수로 가지는 add_numbers라는 함수를 만들고,
  두 숫자를 더한 결과를 result라는 변수에 담아 return 하도록 해 주세요
  '''

  ```
  - 답안
    ```python
     def add_numbers(a, b):
         result = a + b
         return result

     sum = add_numbers(3, 5)
     print("두 수의 합:", sum)
    ```
  ```python
  a = {
      "history": [
          {
              "date": "2015-03-11",
              "item": "iPhone"
          },
          {
              "date": "2016-02-23",
              "item": "Monitor"
          }
      ],
      "id": 152352,
      "name": "\uac15\uc9c4\uc218"
  }
  ```
