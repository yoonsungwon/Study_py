# -*- encoding:utf8 -*-
# http://www.pythonchallenge.com/pc/def/peak.html
# http://www.pythonchallenge.com/pc/def/peak.php
# http://wiki.pythonchallenge.com/index.php?title=Level4:Main_Page
from email.mime import audio

import requests
import sys

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
html = requests.get(url)

for line in str.split(html.content, '\n'):
    print(line)