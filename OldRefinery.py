import os
import pandas as pd
import glob
import csv
import matplotlib.pyplot as plt
import scipy.stats

path = os.getcwd()
files=glob.glob(path + '/StockData'+'/*.csv')

AnalTGT=[]
Price1=[]
Price2=[]
AnalTGT2=[]
Price12=[]
Price22=[]
PriceCHG=[]
AnalTGT3=[]
AnalTGT4=[]
PriceCHG2=[]
for filename in files:
    df= pd.read_csv(filename, index_col=None, header=0)
    with open(filename, newline='') as infh:
        reader = csv.reader(infh)
        for i, row in enumerate(reader):
            if len(row)>=1:
                if i>=1:
                    if int(row[1])>=10:
                        if row[6]=='2021-07-12':
                            AnalTGT.append(row[3])
                            Price1.append(row[5])
                        if row[6]=='2021-08-06':
                            Price2.append(row[5])


        if (len(Price2) and len(Price1) and len(AnalTGT)) == 1:
            if (Price1[0] != 'Error') and (Price2[0] != 'Error'):
                Price12.append(Price1[0])
                Price22.append(Price2[0])
                AnalTGT2.append(AnalTGT[0])
                Price1.clear()
                Price2.clear()
                AnalTGT.clear()
            else:
                continue

        else:
            Price1.clear()
            Price2.clear()
            AnalTGT.clear()

for i in range(len(Price22)):
    Price12[i]=Price12[i].replace(',','')

for x in range(len(Price22)):
    Price22[x]=Price22[x].replace(',','')

for l in range(int(len(Price22))):
    if (float(Price12[l]) != 0):
        PriceCHG.append(float(Price22[l])/float(Price12[l]))
        AnalTGT3.append(AnalTGT2[l])

for n in range(int(len(PriceCHG))):
    if PriceCHG[n] < 2:
         PriceCHG2.append(PriceCHG[n])
         AnalTGT4.append(AnalTGT3[n])

print(len(Price12))
print(len(Price22))
print(AnalTGT2)
print(Price12)
print(Price22)


print(PriceCHG)


plt.scatter(AnalTGT4, PriceCHG2)
print(scipy.stats.spearmanr(AnalTGT4,PriceCHG2))
plt.show()



