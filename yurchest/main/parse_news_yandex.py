import requests
from bs4 import BeautifulSoup as bs
from .models import News


def parse(url):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    news_content = soup.find_all('')
    news_content = soup.find_all('div', class_='list-item__content')

    news_content = soup.find_all('a', class_='list-item__title color-font-hover-only')

    for news in news_content:
    	href = news.get('href')
    	content  = news.text
    	if not News.objects.filter(link=href):
    		News.objects.create(content =news.text, link=news.get('href'))
    	# result_list['href'].append(news.get('href'))
    	# result_list['content'].append(news.text)

parse(url='https://ria.ru/lenta/')