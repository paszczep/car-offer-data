def get_particular_data(offer_item):

    offer_title = offer_item.find('a', {'class': 'offer-title__link'})

#     vehicle = {'title': offer_title.string[29:-44],
#                'link': offer_title['href'],
#                # 'sub_title': offer_item.find('h3', {'data-type': "complement"}).string,
#                'year': offer_item.find('li', {'data-code': "year"}).text[1:-2],
#                # 'mileage': offer_item.find('li', {'data-code': "mileage"}).text[1:-1],
#                # 'engine_capacity': offer_item.find('li', {'data-code': "engine_capacity"}).text[1:-1],
#                'fuel_type': offer_item.find('li', {'data-code': "fuel_type"}).text[1:-1],
#                'price': offer_item.find('span', {'class': "offer-price__number ds-price-number"}).text[1:-5],
#                'price_currency': offer_item.find('span', {'class': "offer-price__currency ds-price-currency"}).text,
#                }
    
    try:
        vehicle = {'title': offer_title.string[29:-44],
                   'link': offer_title['href'],
                   # 'sub_title': offer_item.find('h3', {'data-type': "complement"}).string,
                   'year': offer_item.find('li', {'data-code': "year"}).text[1:-1],
                   'mileage': offer_item.find('li', {'data-code': "mileage"}).text[1:-1],
                   'engine_capacity': offer_item.find('li', {'data-code': "engine_capacity"}).text[1:-1],
                   'fuel_type': offer_item.find('li', {'data-code': "fuel_type"}).text[1:-1],
                   'price': offer_item.find('span', {'class': "offer-price__number ds-price-number"}).text[1:-5],
                   'price_currency': offer_item.find('span', {'class': "offer-price__currency ds-price-currency"}).text,
                   }
    
    except AttributeError:
        vehicle = {'title': offer_title.string[29:-44],
                   'link': offer_title['href'],
                   # 'sub_title': offer_item.find('h3', {'data-type': "complement"}).string,
                   'year': offer_item.find('li', {'data-code': "year"}).text[1:-2],
                   'mileage': offer_item.find('li', {'data-code': "mileage"}).text[1:-1],
                   'engine_capacity': None,
                   'fuel_type': offer_item.find('li', {'data-code': "fuel_type"}).text[1:-1],
                   'price': offer_item.find('span', {'class': "offer-price__number ds-price-number"}).text[1:-5],
                   'price_currency': offer_item.find('span', {'class': "offer-price__currency ds-price-currency"}).text,
    #                }

    return vehicle
