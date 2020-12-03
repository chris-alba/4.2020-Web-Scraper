from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re


page=requests.get('https://www.tradewindsfruit.com/hot-peppers/?sort=alphaasc&page=2')

bs=BeautifulSoup(page.content, 'html.parser')

theID=bs.find(id='Wrapper')

theclass=theID.find_all(class_='ProductDetails')

x = theclass[0].find('strong').get_text()
y= theclass[0].find('br').next_sibling

strongs=[aclass.find('strong').get_text() for aclass in theclass]
brs=[aclass.find('br').next_sibling for aclass in theclass]

print(col)
print(m)

pepperlist=pd.DataFrame(
    {
        'Name': col,
        'Price':m,
    })

print(pepperlist)

pepperlist.to_csv('pepperprice.csv')
