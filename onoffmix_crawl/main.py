# -*- encoding:utf8 -*-
import BeautifulSoup
import requests

url = 'https://onoffmix.com/event'
req = requests.get(url)
soup = BeautifulSoup.BeautifulSoup(r.content)
req.close()

soup2 = soup.find('div', attrs={'class': 'contentBox todayEventArea'})
for article in soup2.findAll('ul', attrs={'class': 'todayEvent   '}):
    print article.li[0]


    print


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
