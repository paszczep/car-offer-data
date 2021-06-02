import requests
from bs4 import BeautifulSoup
import csv
from get_pages import get_pages
from get_particular_data import get_particular_data


BODIES = ['mini', 'city-car', 'compact', 'sedan', 'combi', 'minivan', 'suv', 'cabrio', 'coupe']
YEARS = [(1990, 2010), (2011, 2015), (2016, 2018), (2019, 2021)]
DOUBLE_NAMES = ['Alfa Romeo', 'Aston Martin', 'Land Rover', 'De Lorean', 'DS Automobiles']
DROP = ['Samochód osobowy']

with open('otomoto_offer_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['make',
                  'model',
                  'body',
                  'fuel_type',
                  # 'engine_capacity',
                  # 'milage',
                  'year',
                  'price',
                  'currency',
                  'link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for body in BODIES[-4:]:
        for prod_from, prod_until in YEARS:
            format_url = f'https://www.otomoto.pl/osobowe/seg-{body}/od-{prod_from}/' \
                         f'?search[filter_float_year%3Ato]={prod_until}' \
                         f'&search[filter_enum_damaged]=0'

            print(body, prod_from, prod_until, get_pages(format_url))

            page = 1
            for page in range(1, get_pages(format_url)):
                format_page_url = format_url + f'&page={page}'

                source = requests.get(format_page_url).text
                soup = BeautifulSoup(source, 'lxml')

                offer_items = soup.find_all("div", {"class": "offer-item__wrapper"})

                for offer_item in offer_items:
                    vehicle = get_particular_data(offer_item)

                    if ' '.join(vehicle['title'].split()[:2]) in DOUBLE_NAMES:
                        # print('DOUBLE NAME', vehicle['title'])
                        try:
                            writer.writerow({'make': ' '.join(vehicle['title'].split()[:2]),
                                             'model': ' '.join(vehicle['title'].split()[2:]),
                                             'body': body,
                                             'fuel_type': vehicle['fuel_type'],
                                             # 'engine_capacity': vehicle['engine_capacity'],
                                             # 'mileage': vehicle['mileage'],
                                             'year': vehicle['year'],
                                             'price': vehicle['price'],
                                             'currency': vehicle['price_currency'],
                                             'link': vehicle['link']})
                        except IndexError:
                            print(vehicle['link'])

                    else:
                        try:
                            writer.writerow({'make': vehicle['title'].split()[0],
                                             'model': ' '.join(vehicle['title'].split()[1:]),
                                             'body': body,
                                             'fuel_type': vehicle['fuel_type'],
                                             # 'engine_capacity': vehicle['engine_capacity'],
                                             # 'mileage': vehicle['mileage'],
                                             'year': vehicle['year'],
                                             'price': vehicle['price'],
                                             'currency': vehicle['price_currency'],
                                             'link': vehicle['link']})
                        except IndexError:
                            print(vehicle['link'])
