# -*- coding:utf8 -*-
import os, sys, time, csv, pprint, sqlite3
import numpy as np
import matplotlib.pyplot as plt
import datetime
import MySQLdb
import talib
import pandas_datareader


def insert_stock_data(CODE):
    DataFrame = pandas_datareader.data.DataReader(CODE, "yahoo", '1970-01-01', '2017-08-19')
    print DataFrame

insert_stock_data('000020')

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
    cur.execute("select distinct(symbol) from ohlc where date >= ? and date <= ? order by date;",
                (FROM_unixtime, TO_unixtime,))
elif DB == 'mysql':
    cur.execute("select distinct(종목코드) from opt10081 where 일자 >= %s and 일자 <= %s order by 일자;",
                (FROM_unixtime, TO_unixtime,))
symbol_list = cur.fetchall()

if DB == 'sqlite':
    cur.execute(
        "select date, open, high, low, close, volume, symbol from ohlc where date >= ? and date <= ? order by date;",
        (FROM_unixtime, TO_unixtime,))
elif DB == 'mysql':
    cur.execute(
        "select 일자, 시가, 고가, 저가, 종가, 거래량, 종목코드 from opt10081 where 일자 >= %s and 일자 <= %s order by 일자;",
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

short_term = dict()
mid_term = dict()
long_term = dict()

Result = []
Earning = []

for key in dataSet.keys():
    short_term[key] = talib.DEMA(close, timeperiod=20)
    mid_term[key] = talib.DEMA(close, timeperiod=60)
    long_term[key] = talib.DEMA(close, timeperiod=120)

    # print long_values
    # 신고가:[일]0봉전 고가가 10봉중 신고가
    # [일]거래량:100000이상 999999999이하
    # 주가등락률:[일]1봉전(중) 종가대비 0봉전 종가등락률 1%이상
    # 캔들연속발생:[일]0봉전 1봉 연속 양봉발생
    # 이평이격도:[일]0봉전(종가 20, 종가 60) 3.5%이내 근접 1회이상
    # 이평이격도:[일]0봉전(종가 60, 종가 120) 3%이내 근접 1회이상
    # n일 이격도 = (현재 주가 / n일 이동평균) x 100

    # date0, open1 , high2 , low3, close4, volume5
    position = []  # None , 1:buy, 2:Sell, 3: Buy&Sell
    profit = []
    for index, item in enumerate(dataSet[keys]):
        if index < 120:
            position.append(None)
            profit.append(None)
            continue
        if (item[2] > np.max(dataSet[keys][index - 10:index, 2])) and \
                (item[5] >= 100000) and \
                (abs(item[4] / dataSet[keys][index - 1, 4]) >= 1.01) and \
                (item[4] > item[1]) and \
                (0.965 <= abs(short_values[index] / mid_values[index]) < 1.035) and \
                (0.97 <= abs(mid_values[index] / long_values[index]) < 1.03):
            if (position[index - 1] == 1) or (position[index - 1] == 3):
                position.append(3)
                profit.append(dataSet[keys][index, 1] - dataSet[keys][index - 1, 4])
                Earning.append(
                    (Symbol, dataSet[keys][index, 0], dataSet[keys][index - 1, 4], dataSet[keys][index, 1], profit[-1]))
            else:
                position.append(1)
                profit.append(None)
        else:
            if (position[index - 1] == 1) or (position[index - 1] == 3):
                position.append(2)
                profit.append(dataSet[keys][index, 1] - dataSet[keys][index - 1, 4])
                Earning.append(
                    (keys, dataSet[keys][index, 0], dataSet[keys][index - 1, 4], dataSet[keys][index, 1], profit[-1]))
            else:
                position.append(None)
                profit.append(None)
    Result.append((keys, dataSet[keys], position, profit))
else:
    con.close()
