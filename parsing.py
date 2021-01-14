from bs4 import BeautifulSoup
import csv
import lxml
import requests

URL = 'https://valuta.kg/'

def get_html(url):
    r = requests.get(url)
    return r.text

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser') 
    items = soup.find('div', class_='rate-list active').find('table', class_='vl-list').find_all('td', class_='td-rate')
    rate_sales = []
    rate =[]

    
    for item in items:
        div_= item.find('div', class_='td-rate__wrp').text
        rate_sales.append(div_.replace('\n', '').replace(' ', '').replace('-', ''))
    
    for item in rate_sales[:8]:
        rate.append(item)

    return rate

html = get_html(URL)
valuta = get_content(html)
