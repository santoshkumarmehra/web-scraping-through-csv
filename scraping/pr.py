from bs4 import BeautifulSoup
import requests

import pdb;pdb.set_trace()
page = requests.get("https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.text)
