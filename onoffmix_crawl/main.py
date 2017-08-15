# -*- encoding:utf8 -*-
from lib2to3.pgen2 import driver

import BeautifulSoup
import requests
from selenium import webdriver


url = 'https://onoffmix.com/event/'


driver = webdriver.Chrome('/webdriver/chromedriver')
driver.implicitly_wait(3)
driver.get(url)
driver.execute_script("window.scrollBy(0,0)", "");
driver.implicitly_wait(3)
driver.execute_script("window.scrollBy(0,0)", "");
driver.implicitly_wait(3)

req = driver.page_source

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
#req = requests.get(url, headers=headers)
soup = BeautifulSoup.BeautifulSoup(req)
req.close()

soup2 = soup.find('div', attrs={'class': 'contentBox todayEventArea'})
for article in soup2.findAll('ul', attrs={'class': 'todayEvent   '}):
    print (article.li.a.img['src'] +  article.li.a.img['alt'])

#    img = article.find('li', attrs={'class': 'eventThumbnail'}).a.img['src']
#    title = article.find('li', attrs={'class': 'eventTitle'}).a['title']

# def get_Article(url):
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'lxml')
#     tr_data = soup.find_all('div', class_="tt mrg_b")
#     #tr_data = soup.find_all(href=re.compile('index.php'),class_='title pjax fw_l')
#     for one in tr_data:
#         url = 'http://totolove.cf'+(one.find_all(href=re.compile('index.php'))[0].attrs['href'])
#         text = (one.find_all(href=re.compile('index.php'))[0].text)
#         get_imgFile(url, text)
#
#
# def get_imgFile(url, series):
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'lxml')
#     tr_data = soup.find_all('article')
#     img_data = tr_data[0].find_all('img')
#     for num, imgUrl in enumerate(img_data):
#         print(imgUrl['src'])
#         try:
#             if 'http://totolove.cf' in imgUrl['src']:
#                 imgData = requests.get(imgUrl['src'])
#             else:
#                 imgData = requests.get('http://totolove.cf'+imgUrl['src'])
#             fileName = "../"+series+'-'+str(num+1)+'.'+str(basename(imgUrl['src']).split('.')[-1])
#             output = open(fileName, 'wb')
#             output.write(imgData.content)
#             output.close()
#         except Exception as e:
#             print (e)
#             pass
