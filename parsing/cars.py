import requests
from bs4 import BeautifulSoup as BS
from db.base import pop_cars


URL = 'https://www.mashina.kg/search/all/'


def get_cars():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BS(response.text, 'html.parsing')
        cars = soup.find_all('div', class_='list-item list-label')

        data1 = []
        for car in cars:
            slovar = {
                'name': car.find('h2', class_='name').string.replace('\n', '').strip(),
                'price': car.find('p').find('strong').string.replace('\n', '').strip(),
                'descr': car.find('div', class_='block info-wrapper item-info-wrapper'). \
                    find('p', class_='body-type').string.replace('\n', '').strip(),
                'link': 'https://www.mashina.kg' + car.find('a').get('href')
            }
            data1.append(slovar)
        pop_cars(data1)