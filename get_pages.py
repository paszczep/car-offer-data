import requests
from bs4 import BeautifulSoup


def get_pages(url):

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    spans = soup.find_all('span')
    class_spans = []
    for span in spans:
        try:
            span['class']
            class_spans.append(span)
        except KeyError:
            pass

    pages = []
    for el in class_spans:
        if 'page' in el['class']:
            pages.append(el)
    pages_number = int(pages[-1].text)

    return pages_number
