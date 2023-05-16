import requests
from bs4 import BeautifulSoup
import pandas as pd

search_url = 'https://movie.daum.net/ranking/reservation'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
movie_list = soup.select('#mainContent > div > div.box_ranking > ol > li')


for movie in movie_list:
    test = soup.select_one('div > div.thumb_cont > span.txt_append > span:nth-child(1) > span')

  
    #mainContent > div > div.box_ranking > ol > li:nth-child(2) > div > div.thumb_cont > strong > a
    #mainContent > div > div.box_ranking > ol > li:nth-child(3) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span
    
#     movie_point=soup.select_one('div > div.thumb_cont > span.txt_append > span:nth-child(1) > span').text
#     print(movie_point)

#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span
#mainContent > div > div.box_ranking > ol > li:nth-child(2) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span