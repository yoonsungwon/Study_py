# -*- encoding:utf8 -*-
# http://www.pythonchallenge.com/pc/def/equality.html
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://wiki.pythonchallenge.com/index.php?title=Level3:Main_Page

import re


import requests
import BeautifulSoup

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
html = requests.get(url)
soup = BeautifulSoup.BeautifulSoup(html.content)
book = soup.findAll(text=lambda text:isinstance(text, BeautifulSoup.Comment))
result = ",".join(re.findall("[a-z]+[A-Z]{3}[a-z][A-Z]{3}[a-z]+", book[0]))

print(result)