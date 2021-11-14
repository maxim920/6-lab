from collections import Counter
import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://ru.wikipedia.org/wiki/Python'
fr = []
wanted = ['python']
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for word in wanted:
    freq = soup.get_text().lower().count(word)
    dic = {'phrase': word, 'frequency': freq}          
    fr.append(dic)  
    print('Частота слова', word, ':', freq)

def get_img_cnt(url):
    response1 = requests.get(url)
    parser = etree.HTMLParser()
    root = etree.fromstring(response1.content, parser=parser)

    return int(root.xpath('count(//img)'))

print('кількість фото на сайті:')
print(get_img_cnt('https://ru.wikipedia.org/wiki/Python'))
