# -*- encoding:utf8 -*-
# http://www.pythonchallenge.com/pc/def/ocr.html
# http://www.pythonchallenge.com/pc/def/equality.html
# http://wiki.pythonchallenge.com/index.php?title=Level2:Main_Page

import requests
import BeautifulSoup

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
html = requests.get(url)
soup = BeautifulSoup.BeautifulSoup(html.content)
book = soup.findAll(text=lambda text:isinstance(text, BeautifulSoup.Comment))

#print([c for c in book[1] if c.isalnum()])

output = []
for charac in book[1]:
    if charac.isalpha():
        output.append(charac)

print(''.join(output))
