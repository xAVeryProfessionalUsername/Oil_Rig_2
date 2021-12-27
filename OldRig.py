import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import path
import csv
from datetime import date
import datetime
import time

dfs = []
dfr = []
dfp = []
dfc = []
dfpt = []
dfpr = []
dr = []

zackerror = 0
istime = 0
while True:
    now = datetime.datetime.now()
    minute = now.minute
    hour = now.hour

    if (hour == 23):
        istime = 1

    if istime == 1:
        stonks = []
        header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
        url = "https://stockanalysis.com/stocks/"

        r = requests.get(url, headers=header, verify=True)
        soup = BeautifulSoup(r.text, 'html.parser')

        for node in soup.find_all('td'):
            print(node)
            stonks.append(node)

        deef = pd.DataFrame(stonks, columns=['Ticker'])

        deef.to_csv('1Tickerz')

        stock_list = pd.read_csv('1Tickerz')
        stocks = stock_list['Ticker']
        fields = ['Stock', 'Analyst Count', 'Consensus', 'Price Target', 'Zacks', 'Price', 'Date']

        for x in range(0, int(len(stocks))):
            try:
                today = str(date.today())
                zackerror = 0

                if not len(dfr) == len(dfs) == len(dfp) == len(dfc) == len(dfpt) == len(dfpr):
                    print("Error", ticker)
                    print(dr)
                    break
                ticker = str(stocks.values[x])

                # -------------------------------------------------------------------------------------------------------#

                header = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
                url = "https://www.tipranks.com/stocks/" + ticker + "/forecast"
                r = requests.get(url, headers=header, verify=True)
                soup = BeautifulSoup(r.text, 'html.parser')

                ratingfind = soup.find('div', {'class': "flexccc displayflex grow1"}).find_all('span')[0]
                analystcount = soup.find('text', {'class': "override fontWeightbold fontSize6"})
                pricetrend = soup.find('div', {'class': "displayflex fontSize10"})
                count = (str(analystcount.text))

                rating = (str(ratingfind.text))

                upside1 = (str(pricetrend.text))
                upside1 = upside1.split()
                upside2 = upside1[0]
                upside3 = upside2.lstrip(upside2[0:2])
                upside4 = upside3.rstrip(upside3[-1])
                print(ticker)
                dfs.append(ticker)
                dr.append(ticker)
                dfc.append(count)
                dfp.append(rating)
                dfpt.append(upside4)
                dr.append(count)
                dr.append(rating)
                dr.append(upside4)

                # ------------------------------------------------------------------------------------------------------#

                '''
                header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
                url4 = "https://www.tipranks.com/stocks/" + ticker + "/stock-news"
                r4 = requests.get(url4, headers=header, verify=True)
                soup = BeautifulSoup(r4.text, 'html.parser')

                sentiment = soup.find('div', {'class': 'flexc__ w6 displayflex'}).find_all('div')[0]
                print(sentiment.text)
                '''
                # -------------------------------------------------------------------#

                try:

                    url2 = "https://www.zacks.com/stock/quote/" + ticker + "?q=" + ticker
                    r2 = requests.get(url2, headers=header, verify=True)

                    soup = BeautifulSoup(r2.text, 'html.parser')
                    num = soup.find('p', {'class': "rank_view"})  # .find('span',{'class': "rank_chip rankrect_2"})

                    numstring = str(num.text)
                    list = numstring.split()
                    if len(list) > 1:
                        for i in list:

                            if i == '1-Strong':
                                dfr.append(str(i[0]))
                                dr.append(str(i[0]))

                                break
                            if i == '2-Buy':
                                dfr.append(str(i[0]))
                                dr.append(str(i[0]))
                                break
                            if i == '3-Hold':
                                dfr.append(str(i[0]))
                                dr.append(str(i[0]))

                                break
                            if i == '4-Sell':
                                dfr.append(str(i[0]))
                                dr.append(str(i[0]))

                                break
                            if i == '5-Strong':

                                dfr.append(str(i[0]))
                                dr.append(str(i[0]))

                                break
                            else:
                                dfr.append("Error")
                                dr.append('Error')
                except:
                    zackerror = 1

                if len(list) == 0:
                    zackerror = 1
                if len(dr) == 4:
                    zackerror = 1

                # ----------------------------------------------------------------------------------#

                if zackerror == 0:
                    try:
                        url3 = 'https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker + '&.tsrc=fin-srch'
                        r3 = requests.get(url3, headers=header, verify=True)

                        soup = BeautifulSoup(r3.text, 'html.parser')
                        price = soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})

                        price = price.text
                        price.split
                        if (len(price)) == 0:
                            dfpr.append('Error')
                            dr.append('Error')
                            dr.append(today)

                            break
                        if (len(price)) >= 1:
                            dfpr.append(price)
                            dr.append(price)
                            dr.append(today)

                        if (len(dr) == 5):
                            dr.append("Error")
                            dfpr.append("Error")
                            dr.append(today)
                    except:
                        dr.append("Error")
                        dfpr.append("Error")
                        dr.append(today)
                if zackerror == 1:
                    dfr.append("Error")
                    dr.append('Error')
                    dfpr.append("Error")
                    dr.append("Error")
                    dr.append(today)
                print(dr)
                # ----------------------------------------------------------------------------------------------#

                if path.exists(stocks[x] + '.csv') == True:
                    filename = str(stocks[x]) + ".csv"
                    with open(filename, 'a') as w:
                        writer = csv.writer(w)
                        writer.writerow(dr)

                if path.exists(str(stocks[x] + '.csv')) == False:
                    filename = str(stocks[x]) + ".csv"
                    with open(filename, 'w') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow(fields)
                        csvwriter.writerow(dr)
                dr = []

                if x == int(len(stocks)):
                    break
                istime = 0
            except:
                continue
        time.sleep(60)
    istime = 0
    time.sleep(10)



