# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# search_url = 'https://finance.yahoo.com/trending-tickers'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(search_url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')

# ticker_list = soup.select('#list-res-table > div.Ovx\(a\).Ovx\(h\)--print.Ovy\(h\).W\(100\%\) > table > tbody > tr')
# trending_tickers = []
# for ticker in ticker_list:
#     symbol = ticker.select_one('td:nth-child(1) > a').text
#     name = ticker.select_one('td:nth-child(2)').text
#     price = ticker.select_one('td:nth-child(3)').text
#     per_change = ticker.select_one('td:nth-child(6)').text + "%"
#     volume = ticker.select_one('td:nth-child(7)').text
#     marketcap = ticker.select_one('td:nth-child(8)').text
#     day_chart = f"https://finance.yahoo.com{ticker.select_one('td:nth-child(11) > a')['href']}"
    
#     doc = {
#         'Name': name,
#         'Last Price': price,
#         '%Change': per_change,
#         'Volume': volume,
#         'Market Cap': marketcap,
#         'Chart Url': day_chart
#     }
#     trending_tickers.append(doc)

# print(trending_tickers)




import requests
from bs4 import BeautifulSoup
import pandas as pd

search_url = 'https://movie.daum.net/ranking/reservation'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


movies = soup.select('#mainContent > div > div.box_ranking > ol > li')
rank = soup.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(2) > div > div.thumb_cont > span.txt_append > span:nth-child(1)')
print(rank.text)

#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span
#mainContent > div > div.box_ranking > ol > li:nth-child(3) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span

print(rank)
titles = []
for movie in movies:
    a_tag = movie.select_one('div > div.thumb_cont > span.txt_append > span:nth-child(1) > span').text
    print(a_tag)

