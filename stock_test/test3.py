# -*- encoding:utf8 -*-
import os, sys, time, csv, pprint, sqlite3
import numpy as np
import matplotlib.pyplot as plt

con = sqlite3.connect('002000.db')
cur = con.cursor()
FROM = '1984-01-01'
TO = '2017-01-31'

FROM_unixtime = time.mktime(time.strptime(FROM, "%Y-%m-%d"))
TO_unixtime = time.mktime(time.strptime(TO, "%Y-%m-%d"))

cur.execute("select date, open, high, low, close, volume from ohlc where date >= ? and date <= ? order by date;", (FROM_unixtime, TO_unixtime,))
DataSet = np.array(cur.fetchall(), dtype=np.float32)

con.close()

Close = DataSet[:,4]
short_period = 20
short_values = []
for index in range(len(DataSet[:,4])):
    if index < short_period:
        short_values.append(None)
    else:
        sv = np.mean(Close[index - short_period:index])
        short_values.append(sv)
# print short_values

mid_period = 60
mid_values = []
for index in range(len(DataSet[:,4])):
    if index < mid_period:
        mid_values.append(None)
    else:
        sv = np.mean(Close[index - mid_period:index])
        mid_values.append(sv)
# print mid_values

long_period = 120
long_values = []
for index in range(len(DataSet[:,4])):
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


#open1 , high2 , low3, close4, volume5
position=[] # None , 1:buy, 2:Sell, 3: Buy&Sell
for index, item in enumerate(DataSet):
    if index < 10:
        position.append(None)
        continue
    if item[2] > np.max(DataSet[index-9:index,2]):
        print("First")
        if item[5] >= 100000:
            if abs(item[4]/DataSet[index-1,4]) >= 0.01:
                if item[4] > item[1]:
                    if abs(short_values[index]/mid_values[index]) < 0.035:
                        if abs(mid_values[index] / long_values[index]) < 0.03:
                            position.append(1)
                            print(index)

print(position)

# golden_cross=[]
# dead_cross=[]
# for index, item in enumerate(zip(short_values, long_values)):
#     current_short, current_long = item
#     if index < 1:
#         pass
#     else:
#         previous_short = short_values[index-1]
#         previous_long = long_values[index-1]
#         if current_short > current_long and previous_short < previous_long:
#             golden_cross.append(current_short)
#         else:
#             golden_cross.append(None)
#         if current_short < current_long and previous_short > previous_long:
#             dead_cross.append(current_short)
#         else:
#             dead_cross.append(None)
#
# plt.plot(short_values, 'r-')
# plt.plot(long_values, 'g-')
# plt.plot(golden_cross, 'bo')
#
# #plt.plot(DataSet[:,1])
# plt.show()
