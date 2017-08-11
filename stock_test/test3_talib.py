# -*- encoding:utf8 -*-
import talib
import numpy

close = numpy.random.random(100)
output = talib.SMA(close)

print output
upper, middle, lower = talib.BBANDS(close, matype=talib.MA_Type.T3)
output = talib.MOM(close, timeperiod=5)
print output
