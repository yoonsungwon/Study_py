import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

initial_account = 100000000
ratio = 0.01

# Get GS Data from Yahoo
gs = web.DataReader("000520.KS", "yahoo", "2016-01-01", "2016-02-27")
new_gs = gs[gs['Volume']!=0]

# Moving average
ma2 = new_gs['Adj Close'].rolling(window=5).mean()
ma3 = new_gs['Adj Close'].rolling(window=20).mean()
price = new_gs['Adj Close'].tolist()


# 양수>음수 일때 데드, 음수>양수일때 골든
diff = ma2 - ma3
status = []
cash = []
stock = []
account = []

for i in range(len(price)):
    if i == 0:
        status.append("HOLD")
        cash.append(initial_account)
        stock.append(0)
        account.append(cash[i])
    elif diff[i] >= 0:
        status.append("BUY")
        #살 수 있는 주식 수
        stock.append(stock[i - 1] + int((cash[i - 1] * ratio) / price[i]))
        cash.append(cash[i - 1] - price[i] * stock[i])
        account.append(cash[i] + stock[i] * price[i])
    elif diff[i] < 0:
        try:
            if status[i-1] == "BUY":
                status.append("SELL")
                stock.append(0)
                cash.append(cash[i-1] + price[i] * stock[i-1])
                account.append(cash[i])
            else:
                status.append("HOLD")
                stock.append(stock[i - 1])
                cash.append(cash[i-1])
                account.append(cash[i] + stock[i] * price[i])
        except Exception as e:
            print("Exception",  e)
    else:
        status.append("HOLD")
        stock.append(stock[i - 1])
        cash.append(cash[i - 1])
        account.append(cash[i] + stock[i] * price[i])


# Insert columns
new_gs.insert(len(new_gs.columns), "MA2", ma2)
new_gs.insert(len(new_gs.columns), "MA3", ma3)
new_gs.insert(len(new_gs.columns), "DIFF", diff)
new_gs.insert(len(new_gs.columns), "STATUS", status)
new_gs.insert(len(new_gs.columns), "STOCK", stock)
new_gs.insert(len(new_gs.columns), "CASH", cash)
new_gs.insert(len(new_gs.columns), "ACCOUNT", account)

print(status)
print(account)

# Plot
#plt.plot(new_gs.index, new_gs['Adj Close'], label='Adj Close')
#plt.plot(new_gs.index, new_gs['MA2'], label='MA2')
fig = plt.figure()
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.plot(new_gs.index, new_gs['MA3'], label='MA3')
# for i in range(len(status)):
#     if status[i] == "BUY":
#         ax1.plot([new_gs.index,new_gs.index], [0, price[i]], color = 'red', linewidth = 2.5, linestyle='--')
#     elif status[i] == "SELL":
#         ax1.plot(new_gs.index, [0,price[i]], color = 'blue', linewidth = 5, linestyle='--')

ax2.plot(new_gs.index, new_gs['DIFF'], label='diff')
#plt.plot(new_gs.index, new_gs['CASH'], label='cash')
ax2.plot(new_gs.index, new_gs['STOCK'], label='stock')
ax3.plot(new_gs.index, new_gs['ACCOUNT'], label='account')

#plt.plot(new_gs.index, str1, label='str1')
# avg = new_gs['Adj Close'].mean()

plt.legend(loc="best")
plt.grid()
plt.show()