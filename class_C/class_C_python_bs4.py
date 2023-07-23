'''
html에서는 누가 누구 안에 있는지를 이해하는 것이 가장 중요합니다!
나를 감싼 태그가 무엇인지에 따라 그 안의 내용물들이 영향을 받기 때문입니다!
'''


'''
야후쿼리
'''
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# search_url = 'https://finance.yahoo.com/trending-tickers'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(search_url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')

# trending_tickers = []

# ticker_list = soup.select('#list-res-table > div.Ovx\(a\).Ovx\(h\)--print.Ovy\(h\).W\(100\%\) > table > tbody > tr')

# for ticker in ticker_list:
#     symbol_element = ticker.select_one('td:nth-child(1) > a')
#     name_element = ticker.select_one('td:nth-child(2)')
#     price_element = ticker.select_one('td:nth-child(3)')
#     per_change_element = ticker.select_one('td:nth-child(6)')
#     volume_element = ticker.select_one('td:nth-child(7)')
#     marketcap_element = ticker.select_one('td:nth-child(8)')
#     day_chart_element = ticker.select_one('td:nth-child(11) > a')

#     if (
#         symbol_element is None or
#         name_element is None or
#         price_element is None or
#         per_change_element is None or
#         volume_element is None or
#         marketcap_element is None or
#         day_chart_element is None
#     ):
#         print("오류: 요소가 없습니다.")
#         continue

#     symbol = symbol_element.text
#     name = name_element.text
#     price = price_element.text
#     per_change = per_change_element.text + "%"
#     volume = volume_element.text
#     marketcap = marketcap_element.text
#     day_chart = f"https://finance.yahoo.com{day_chart_element['href']}"

#     doc = {
#         'Symbol': symbol,
#         'Name': name,
#         'Price': price,
#         'Percentage Change': per_change,
#         'Volume': volume,
#         'Market Cap': marketcap,
#         'Day Chart': day_chart
#     }
#     trending_tickers.append(doc)

# print(trending_tickers)


"""
네이버뉴스
"""
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# search_url = r'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(search_url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')

# article_list = soup.select('#main_pack > section > div > div.group_news > ul > li')
# article_data = []

# for article in article_list:
#         title = article.select_one(".news_tit").text
#         image = article.select_one(".dsc_thumb")["href"]
#         desc = article.select_one(".dsc_wrap > a").text
#         doc = {"title": title, "image": image, "desc": desc}
#         article_data.append(doc)

# df = pd.DataFrame(article_data)

# print(df)
"""
다음영화
"""
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# search_url = 'https://movie.daum.net/ranking/reservation'
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(search_url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')


# movies = soup.select('#mainContent > div > div.box_ranking > ol > li')
# name_temp = soup.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong > a')


# titles = []
# ranks= []

# for movie in movies:
#     name = movie.select_one('div > div.thumb_cont > strong > a').text
#     score = movie.select_one(' div > div.thumb_cont > span.txt_append > span:nth-child(1) > span').text
#     titles.append(name)
#     ranks.append(score)

# print(titles)
# print(ranks)
    



