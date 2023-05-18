
import random

input_string = '''강민우
강상훈
권서연
김대건
김소연
김수현
김영미
김현진
노도희
박한진
신지원
윤나연
이범필
이용인
이윤선
이재희
이하정
장애리
조성구
조원규
채연아
최영철
홍노영
홍윤정'''

temp = input_string.split('\n')


def get_random_groups(lst, group_size):
    
    random.shuffle(lst)  # 리스트를 섞음

    random_groups = []  # 빈 리스트를 생성하여 랜덤하게 조 편성
    num_groups = len(lst) // group_size  # 그룹의 개수 계산

    # 그룹 개수만큼 반복
    for i in range(num_groups):
        start_idx = i * group_size  # 현재 그룹의 시작 인덱스 계산
        # print("start_idx >",start_idx)
        end_idx = start_idx + group_size  # 현재 그룹의 끝 인덱스 계산
        # print("end_idx >",end_idx)
        group = lst[start_idx:end_idx]  # 현재 그룹을 리스트 슬라이싱을 통해 추출
        # print(group)
        # print("################################")
        random_groups.append(group)  # 추출한 그룹을 random_groups 리스트에 추가

    return random_groups  # 랜덤 그룹의 리스트 반환

def line_change(lis):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 그룹에 부여할 알파벳 리스트

    num_alphabets = len(alphabet)  # 사용 가능한 알파벳 개수
    num_groups = len(lis)  # 그룹의 개수

    #enumerate로 인덱스와 값 리턴
    for i, group in enumerate(lis):
        group_name = 'Group '
        quotient = i // num_alphabets  # 몫을 계산하여 알파벳 조합을 구성
        remainder = i % num_alphabets  # 나머지를 계산하여 알파벳 인덱스를 얻음

        if quotient > 0:
            group_name += alphabet[quotient - 1]  # 알파벳 조합의 첫 글자를 추가. 1바퀴 돌면 A, 2바퀴 돌면 B 이런 식으로

        group_name += alphabet[remainder]  # 나머지에 해당하는 알파벳을 추가
        print('########################################')
        print(group_name)
        print('\n'.join(group))
        


random_group = get_random_groups(temp, 8)


line_change(random_group)

# print(random_elements)
