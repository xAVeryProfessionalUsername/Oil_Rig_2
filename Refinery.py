import AAA
import pyodbc
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import scipy.stats
import seaborn as sb

tool= AAA.toolz
conn = pyodbc.connect(
   'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-84EULDP;DATABASE=StockData;Trusted_Connection=yes;')

cursor = conn.cursor()


tickers = []
ticker1 = []
ticker2 =[]
price1 = []
price2 =[]
priceTGT =[]


tablelist=tool.showtables()

#Refining
for x in tablelist:

    ticker1 = []
    ticker2 = []
    cursor.execute('''
    SELECT * FROM %s
    ''' % (x))

    for y in cursor:

        #Before

        print(y)
        if y[5]=='2021-07-12' and (y[4] != 'Error') and (y[3] != 'Error') and(y[3]!='>-0.01') and (int(y[2])>10):
            print(x,' ',y[4], ' ', y[3])
            ticker1.append(x)
            ticker1.append(y[4])
            ticker1.append(y[3])

        #After

        if y[5]=='12-20-2021':
            #No stock splits between dates
            if y[6] != '-':
                dayte = tool.formayt(y[6])
                if tool.datecheck(dayte) == 1:
                    print(x, ' ', y[4], ' ', y[3])
                    ticker2.append(x)
                    ticker2.append(y[4])
            if y[6] == '-':
                print(x, ' ', y[4], ' ', y[3])
                ticker2.append(x)
                ticker2.append(y[4])
    if (len(ticker1)==3) and (len(ticker2)==2):
        tickers.append([ticker1, ticker2])

#Setup for visulization

pctarr=[]
ptgt=[]
for x,y in enumerate(tickers):
        print(x, ' ', y)
        p1 = float(tickers[x][1][1].replace(',',''))
        p2 = float(tickers[x][0][1].replace(',',''))
        pct=(p1/p2)
        pctarr.append(pct)
        ptgt.append(float(tickers[x][0][2]))
        print(pct)


print(pctarr)
print(ptgt)

data = np.array([ptgt, pctarr])
newdata=data.transpose()


df=pd.DataFrame(data=newdata, columns=['priceTGT', 'percent'])

#Scatterplot


sb.regplot(x=ptgt, y=pctarr, ci=None, data=df)
print(scipy.stats.spearmanr(ptgt,pctarr))
plt.show()



