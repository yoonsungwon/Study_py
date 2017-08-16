# -*- encoding:utf8 -*-
from lib2to3.pgen2 import driver

import BeautifulSoup
import requests
from selenium import webdriver
import time
from HTMLParser import HTMLParser

url = 'https://onoffmix.com/event/'


driver = webdriver.Chrome('/webdriver/chromedriver')

driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("setMorePrint()")
time.sleep(10)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(10)
req = driver.page_source

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
#req = requests.get(url, headers=headers)
soup = BeautifulSoup.BeautifulSoup(req)

h = HTMLParser()
soup2 = soup.find('div', attrs={'class': 'contentBox todayEventArea'})
with open('result.html','w') as f:
        f.write("""<!-- C\Code\mysite\elections\templates\elections\index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <title>강의 목록</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
    <table class="table table-striped">
        <thead>
        <tr>
            <td><B>이미지</B></td>
            <td><B>제목</B></td>
        </tr>
        </thead>""")

for article in soup2.findAll('ul', attrs={'class': 'todayEvent   '}):
    print (article.li.a.img['src'] +  article.li.a.img['alt'])
    with open('result.html','a') as f:
        f.write("""
        <tbody>
        <tr>
            <td><img src=\"""")
        f.write(article.li.a.img['src'])
        f.write(""" width=220px></td>
            <td>""")
        try:
            f.write(h.unescape(article.li.a.img['alt']))
        except:
            f.write(h.unescape(article.li.a.img['alt'].encode('utf8')))
        f.write('</td>')
with open('result.html','a') as f:
    f.write("""</tr>
            <tbody>
        </table>
    </body>""")


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
