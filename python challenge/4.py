# -*- encoding:utf8 -*-
# http://www.pythonchallenge.com/pc/def/linkedlist.php
#
# http://wiki.pythonchallenge.com/index.php?title=Level4:Main_Page

import requests
import BeautifulSoup
import re
65776
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
value = '12345'
keyword = {'nothing': value}
html = requests.get(url, params=keyword)

while html.status_code == 200:
    value = ''.join(re.findall('[0-9]+',html.content))
    keyword = {'nothing': value}
    html = requests.get(url, params=keyword)
    print value
