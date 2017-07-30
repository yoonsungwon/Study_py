import pandas as pd
import os, sys, time, csv, pprint, sqlite3

with open('opt10081.csv') as f:
    csv_reader = csv.reader(f)
    dataSet=dict()
    for index, row in enumerate(csv_reader):
        Symbol, Close, Volume, _, Date, Open, High, Low, _, _, _, _, _, _, _ = row
        try:
            dataSet[Symbol]
        except KeyError:
            dataSet[Symbol] = list()
        dataSet[Symbol].append([Date, Open, High, Low, Close, Volume, Symbol])
con = sqlite3.connect('opt10081.db')
cur = con.cursor()
cur.execute('''
    CREATE TABLE ohlc(
                date INT,
                open FLOAT,
                high FLOAT,
                low FLOAT,
                close FLOAT,
                volume FLOAT,
                symbol TEXT);
''')

for key in dataSet.keys():
    for row in dataSet[key]:
        Date, Open, High, Low, Close, Volume, Symbol = row
        Date_unixtime = time.mktime(time.strptime(Date, "%Y-%m-%d %H:%M:%S"))
        cur.execute('''
            INSERT INTO ohlc(date, open, high, low, close, volume, symbol)
            VALUES(?, ?, ?, ?, ?, ?, ?);
        ''', (Date_unixtime, Open, High, Low, Close, Volume, Symbol))
con.commit()
# con.execute("""
#     select * from ohlc;
# """)

con.close()
exit()



# with open('opt10081.csv') as f:
#     csv_reader = csv.reader(f)
#     dataSet=[]
#     for index, row in enumerate(csv_reader):
#         dataSet.append(row)
#         if index > 100:
#             break
# for row in dataSet:
#     Symbol, Close, _, _, Date, Open, High, Low, _, _, _, _, _, _, _ = row
