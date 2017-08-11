# -*- encoding:utf8 -*-
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/peak.html
# http://wiki.pythonchallenge.com/index.php?title=Level4:Main_Page

import requests
import BeautifulSoup
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
value = '66831'

while True:
    keyword = {'nothing': value}
    html = requests.get(url, params=keyword)
    value = ''.join(re.findall('[0-9]+',html.content))
    if value == '':
        print html.content
        break
    else:
        print value