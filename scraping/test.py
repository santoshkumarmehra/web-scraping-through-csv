from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import html
import requests


url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

d=soup.body.find_all('div',attrs={'class': 's-item__info clearfix'})

import csv
with open('scrap.csv','a+') as f1:
    w = csv.writer(f1)
    l=[]
    for i in d:
        k=i.find_all('h3',attrs={'class': 's-item__title'})
        k2=i.find_all('span',attrs={'class': 's-item__price'})
        k3=i.find_all('span',attrs={'class': 's-item__shipping s-item__logisticsCost'})
        l1=[]
        for a in k:
            l1.append(a.text)
            break
        for s in k2:
            l1.append(s.text)
            break
        for v in k3:
            l1.append(v.text)
            break
        w.writerow(l1)