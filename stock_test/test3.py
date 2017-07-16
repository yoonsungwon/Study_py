# -*- encoding:utf8 -*-
import os, sys, time, csv, pprint, sqlite3
import numpy as np
import matplotlib.pyplot as plt

con = sqlite3.connect('002000.db')
cur = con.cursor()
FROM = '2016-01-01'
TO = '2017-01-31'

FROM_unixtime = time.mktime(time.strptime(FROM, "%Y-%m-%d"))
TO_unixtime = time.mktime(time.strptime(TO, "%Y-%m-%d"))

cur.execute("select * from ohlc where date >= ? and date <= ? order by date;", (FROM_unixtime, TO_unixtime,))
DataSet = np.array(cur.fetchall(), dtype=np.float32)

con.close()

Opens = DataSet[:,1]

short_period = 1
short_values = []
for index in range(len(Opens)):
    if index < short_period:
        short_values.append(None)
    else:
        sv = np.mean(Opens[index - short_period:index])
        short_values.append(sv)
print short_values
long_period = 60
long_values = []
for index in range(len(Opens)):
    if index < long_period:
        long_values.append(None)
    else:
        sv = np.mean(Opens[index - long_period:index])
        long_values.append(sv)
print long_values

golden_cross=[]
dead_cross=[]
for index, item in enumerate(zip(short_values, long_values)):
    current_short, current_long = item
    if index < 1:
        pass
    else:
        previous_short = short_values[index-1]
        previous_long = long_values[index-1]
        if current_short > current_long and previous_short < previous_long:
            golden_cross.append(current_short)
        else:
            golden_cross.append(None)
        if current_short < current_long and previous_short > previous_long:
            dead_cross.append(current_short)
        else:
            dead_cross.append(None)

plt.plot(short_values, 'r-')
plt.plot(long_values, 'g-')
plt.plot(golden_cross, 'bo')

#plt.plot(DataSet[:,1])
plt.show()
