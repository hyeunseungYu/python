import requests
import json
import time
import copy
import re
from bs4 import BeautifulSoup
from datetime import datetime

import kakao_test


site_url = 'https://eomisae.co.kr/fs'
board_list = []  # 크롤링 결과 저장 리스트
p_board_list = []  # 이전 크롤링 결과 저장 리스트


def f_get_list():
    result_search = requests.get(site_url)
    html = result_search.text
    soup = BeautifulSoup(html, 'html.parser')
    all_lists = soup.select('.card_el.n_ntc.clear') #전체 게시글 덩어리 크롤링

    times = soup.select('div > div.card_content > p > span:nth-child(2)')
    titles = soup.select('div > div.card_content > h3 > a')
    

    for idx in range(len(titles)):
        title = titles[idx].text #제목 앞에 탭 제거
        if "레벨 미만의 회원은" in title:
            continue
        else:
            board_list.append('제목: ' +title +'\n작성시간: '+times[idx].text  +'\n링크: ' + titles[idx]['href'])



# # kakao_test.f_get_refresh_token() #최초 refresh token 추출시에만 수행

while True:
    print(f"{datetime.now().strftime('%H:%M:%S')} 작동합니다")
    f_get_list()  #게시글 크롤링
    access_token = kakao_test.f_reissue_token()  # 새로운 액세스 토큰을 발급 받음
    sms_list = list(set(board_list) - set(p_board_list))  # 이전 리스트와 비교하여 다른 값만 문자 보낼 리스트로 저장
    p_board_list = copy.deepcopy(board_list)  # 현재 게시글을 이전 게시글로 저장

    kakao_test.f_send_msg(access_token, '어미새 핫딜 결과\n'  +'현재 시간 {} 최신글은 총 {}개입니다.'.format(datetime.now().strftime('%H:%M:%S'),len(sms_list)))

    for i in range(len(sms_list)):
        kakao_test.f_send_msg(access_token, sms_list[i])

    board_list.clear()
    sms_list.clear()
    time.sleep(1800)  # 반복 주기