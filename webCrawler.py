import requests
from bs4 import BeautifulSoup

def trade_spider():

    url = 'https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,features="html.parser")


    for link in soup.find_all('a'):
        href = 'https://www.tutorialspoint.com'+link.get('href')
        title = link.string
        print(title)
        print(href)

trade_spider()