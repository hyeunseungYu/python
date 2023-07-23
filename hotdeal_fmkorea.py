import requests
import json
import time
import copy
import re
from bs4 import BeautifulSoup
from datetime import datetime

import kakao_test


site_url = 'https://m.fmkorea.com/hotdeal'
board_list = []  # 크롤링 결과 저장 리스트
p_board_list = []  # 이전 크롤링 결과 저장 리스트


def f_get_list():
    result_search = requests.get(site_url)
    html = result_search.text
    soup = BeautifulSoup(html, 'html.parser')
    times = soup.select('.regdate') #글 작성시간 크롤링
    titles = soup.find_all('a', re.compile('hotdeal_var8*'))    #딜 종료 게시글까지 가져오기 위해 정규식을 사용함, select 함수는 정규식 미지원 (딜 진행중 게시글은 hotdeal_var8, 딜 종료 게시글은 hotdeal_var8Y 클래스)
    #titles = soup.select('h3.title > a')    #핫딜과 핫딜종료 게시글의 제목을 가지고 있는 클래스명이 상이하여 부모노드를 명시하여 크롤링을 함
    prices = soup.select('.hotdeal_info > span:nth-child(2) > a.strong') #가격 크롤링

    for idx in range(0, len(titles), 1):
        t = titles[idx].text.replace('\t', '') #제목 앞에 탭 제거
        loc = t.rfind('[') #댓글 수가 제목에 포함되어 댓글 수는 날려버리기 위해서 '[' 문자의 위치 값 찾음
        board_list.append('제목: ' +t[0:loc] +'\n작성시간: '+times[idx].text.replace('\t','') +'\n가격: ' +prices[idx].text +'\n링크: ' +site_url +titles[idx]['href'])


# kakao_test.f_get_refresh_token() #최초 refresh token 추출시에만 수행

while True:
    print("작동합니다")
    f_get_list()  #게시글 크롤링
    access_token = kakao_test.f_reissue_token()  # 새로운 액세스 토큰을 발급 받음
    sms_list = list(set(board_list) - set(p_board_list))  # 이전 리스트와 비교하여 다른 값만 문자 보낼 리스트로 저장
    p_board_list = copy.deepcopy(board_list)  # 현재 게시글을 이전 게시글로 저장

    kakao_test.f_send_msg(access_token, 'FM 핫딜 결과\n'  +'현재 시간 {} 최신글은 총 {}개입니다.'.format(datetime.now().strftime('%H:%M:%S'),len(sms_list)))

    for i in range(0, len(sms_list), 1):
        kakao_test.f_send_msg(access_token, sms_list[i])

    board_list.clear()
    sms_list.clear()
    time.sleep(1800)  # 반복 주기