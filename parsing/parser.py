from aiogram import types
import requests
from bs4 import BeautifulSoup as BS

URL='https://akipress.org/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

response = requests.get(URL, headers={'User-Agen' : user_agent})
def get_news():
    if response.status_code == 200:
        soup = BS(response.text, 'html.parser')
        news = soup.find('div', class_ = 'nowread_list')
        news_list = []
        for nw in news.find_all('a'):
            new = {}
            new['link'] = nw.get('href')
            new['title'] = nw.text
            news_list.append(new)
        return news_list
news = get_news()

async def send_news(message: types.Message):
    for i in news:
        await message.answer(f"{i['link']}")
        await message.answer(f"{i['title']}")