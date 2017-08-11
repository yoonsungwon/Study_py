# -*- encoding:utf8 -*-
import os, sys, time, csv, pprint, sqlite3
import numpy as np
import matplotlib.pyplot as plt
import datetime
import MySQLdb

DB = 'mysql'

if DB == 'sqlite':
    con = sqlite3.connect('opt10081.db')
elif DB == 'mysql':
    con = MySQLdb.connect(host='localhost', user='pyadmin', password='password', db='pystock', charset='utf8')
cur = con.cursor()

FROM = '1984-01-01'
TO = '2017-07-31'

FROM_unixtime = time.mktime(time.strptime(FROM, "%Y-%m-%d"))
TO_unixtime = time.mktime(time.strptime(TO, "%Y-%m-%d"))

if DB == 'sqlite':
    cur.execute("select distinct(symbol) from ohlc where date >= ? and date <= ? order by date;", (FROM_unixtime, TO_unixtime,))
elif DB == 'mysql':
    cur.execute("select distinct(종목코드) from opt10081 where 일자 >= %s and 일자 <= %s order by 일자;", (FROM_unixtime, TO_unixtime,))
symbol_list = cur.fetchall()

Result=[]
Earning=[]

if DB == 'sqlite':
    cur.execute(
        "select date, open, high, low, close, volume, symbol from ohlc where date >= ? and date <= ? order by date;",
        (FROM_unixtime, TO_unixtime,))
elif DB == 'mysql':
    cur.execute(
        "select 일자, 시가, 고가, 저가, 종가, 거래량 from opt10081 where 일자 >= %s and 일자 <= %s order by 일자;",
        (FROM_unixtime, TO_unixtime,))
resultSet = cur.fetchall()

dataSet = {}
for date, open, high, low, close, volume, symbol in resultSet:
    try:
        dataSet[symbol]
    except KeyError:
        dataSet[symbol] = list()
    dataSet[symbol].append([date, open, high, low, close, volume])

for keys in dataSet:
    dataSet[keys] = np.array(dataSet[keys], dtype=np.float32)

for key in dataSet.keys():
    #한글 처리??

    Close = dataSet[keys][:,4]
    short_period = 20
    short_values = []
    for index in range(len(dataSet[keys][:,4])):
        if index < short_period:
            short_values.append(None)
        else:
            sv = np.mean(Close[index - short_period:index])
            short_values.append(sv)
    # print short_values

    mid_period = 60
    mid_values = []
    for index in range(len(dataSet[keys][:,4])):
        if index < mid_period:
            mid_values.append(None)
        else:
            sv = np.mean(Close[index - mid_period:index])
            mid_values.append(sv)
    # print mid_values

    long_period = 120
    long_values = []
    for index in range(len(dataSet[keys][:,4])):
        if index < long_period:
            long_values.append(None)
        else:
            sv = np.mean(Close[index - long_period:index])
            long_values.append(sv)
    # print long_values

    # 신고가:[일]0봉전 고가가 10봉중 신고가
    # [일]거래량:100000이상 999999999이하
    # 주가등락률:[일]1봉전(중) 종가대비 0봉전 종가등락률 1%이상
    # 캔들연속발생:[일]0봉전 1봉 연속 양봉발생
    # 이평이격도:[일]0봉전(종가 20, 종가 60) 3.5%이내 근접 1회이상
    # 이평이격도:[일]0봉전(종가 60, 종가 120) 3%이내 근접 1회이상
    #n일 이격도 = (현재 주가 / n일 이동평균) x 100

    #date0, open1 , high2 , low3, close4, volume5
    position=[] # None , 1:buy, 2:Sell, 3: Buy&Sell
    profit=[]
    for index, item in enumerate(dataSet[keys]):
        if index < 120:
            position.append(None)
            profit.append(None)
            continue
        if (item[2] > np.max(dataSet[keys][index-10:index,2])) and \
                (item[5] >= 100000) and \
                (abs(item[4]/dataSet[keys][index-1,4]) >= 1.01) and \
                (item[4] > item[1]) and \
                (0.965 <= abs(short_values[index] / mid_values[index]) < 1.035) and \
                (0.97 <= abs(mid_values[index] / long_values[index]) < 1.03):
            if (position[index-1] == 1) or (position[index-1] == 3):
                position.append(3)
                profit.append(dataSet[keys][index, 1] - dataSet[keys][index-1, 4])
                Earning.append((Symbol, dataSet[keys][index,0], dataSet[keys][index-1,4], dataSet[keys][index,1], profit[-1]))
            else:
                position.append(1)
                profit.append(None)
        else:
            if (position[index-1] == 1) or (position[index-1] == 3):
                position.append(2)
                profit.append(dataSet[keys][index, 1] - dataSet[keys][index-1, 4])
                Earning.append((keys, dataSet[keys][index,0], dataSet[keys][index-1,4], dataSet[keys][index,1], profit[-1]))
            else:
                position.append(None)
                profit.append(None)
    Result.append((keys, dataSet[keys], position, profit))
else:
    con.close()




# for index, item in enumerate(DataSet):
#     if position[index] == 1 or position[index] == 3:
#
#         tot_sum += sum
#         print(index, datetime.datetime.utcfromtimestamp(item[0]).strftime('%Y-%m-%dT%H:%M:%SZ'),\
#           sum, position[index], DataSet[index+1,1] / DataSet[index,4] - 1, DataSet[index+1,1], DataSet[index,4])
#
# print tot_sum