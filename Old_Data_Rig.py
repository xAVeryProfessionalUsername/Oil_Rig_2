import os
import pandas as pd
import glob
import csv
import Def_Functions

tool = AAA.toolz
path = os.getcwd()
files=glob.glob(path + '/StockData'+'/*.csv')

for filename in files:
    try:
        df= pd.read_csv(filename, index_col=None, header=0)
        with open(filename, newline='') as infh:
            reader = csv.reader(infh)
            for i, row in enumerate(reader):
                if len(row)>=1:
                    if row[6] == '2021-07-12':
                        ticker=row[0]
                        analcnt=row[1]
                        analrate = row[2]
                        priceTGT2 = row[3]
                        price=row[5]
                        day=row[6]
                        split2 = '1-1-2000'
                        tool.maketables(ticker)
                        tool.addrow(ticker, analrate, analcnt, priceTGT2, price, day, split2)

                        print(row)
    except:
        continue


