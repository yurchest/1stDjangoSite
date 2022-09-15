import requests
from bs4 import BeautifulSoup as bs
from .models import News
import time
import threading
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def get_source_html(url):
    driver = webdriver.Chrome(
        executable_path="/home/yuriy/ProgrammingProjects/1stDjangoSite/yurchest/main/chromedriver_linux64/chromedriver"
    )
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)
        clicked = False
        actions = ActionChains(driver)
        while True:
            down_to = driver.find_element(By.CLASS_NAME, "footer__copyright-col")
            actions.move_to_element(down_to).perform()
            if not clicked:
                button_more = driver.find_element(By.CLASS_NAME, "list-more")
                time.sleep(3)
                actions.click(button_more).perform()
                clicked = True

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()



def main():
    get_source_html(url="https://ria.ru/20220101/")

def parse(url):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    # news_content = soup.find_all('div', class_='list-item__content')
    news_content = soup.find_all('a', class_='list-item__title color-font-hover-only')
    print("News have been Downloaded")
    # print(news_content)
    for news in news_content:
        href = news.get('href')
        content  = news.text
        if not News.objects.filter(link=href):
            News.objects.create(content =news.text, link=news.get('href'))
        # result_list['href'].append(news.get('href'))
        # result_list['content'].append(news.text)


def thread_func():
        parse(url='https://ria.ru/lenta/')
        threading.Timer(30, thread_func).start()

thread_func()
# main()