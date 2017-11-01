import requests
from bs4 import BeautifulSoup

def crawl():
    html = requests.get('http://210.98.42.54/domian5/domian5.asp').text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('td font[color*=blue]')

    data=[]
    for tag in tag_list:
        data.append(tag.text)

print(data[1],data[4],data[7])

def get():
    return data[1],data[2],data[7]
