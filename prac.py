import requests
from bs4 import BeautifulSoup
import pandas as pd

test = '삼성전자'

def hello(text):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={text}')
    soup = BeautifulSoup(data.text, 'html.parser')
    a = soup.select_one('#sp_nws1 > div.news_wrap.api_ani_send > div > a')
    return print(a.text)


search = '한국투자증권'
data = requests.get(f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={search}')
soup = BeautifulSoup(data.text, 'html.parser')
a = soup.select_one('#sp_nws1 > div.news_wrap.api_ani_send > div > a')
lis = soup.select('#main_pack > section > div > div.group_news > ul > li',limit=20)

b = len(lis)

num = 1000000
print(f'숫자: {num:,}')

test = {
    "temp1" : [],
    "temp2" : [2]
}

df = pd.DataFrame(test)
print(df)

# temp = []
# for li in lis:
#     temp.append(li.select_one('a.news_tit').text)

# print(temp)






