from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyodbc
import Def_Functions
from datetime import date


tool = AAA.toolz



#------------------------------------------------------------------------------------------------------------------------------------------

path = "C:\chromedriver.exe"

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://stockanalysis.com/stock-screener/")
print(driver.title)

#-------------------------------------------------------------------------------------------------------------------------------------------



#Up to 200
WebDriverWait(driver, 1).until(
   EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/nav/div/div'))).click()
WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/nav/div/div/ul/li[4]/span[1]'))).click()

#Select all the data
#Click cats
WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[3]/div[2]/div[3]/div/div[1]'))).click()
#select cats
#Target %
WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[21]/input'))).click()
#Anal rating
WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[18]/input'))).click()
#Anal cnt
WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[19]/input'))).click()
#Split
WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[98]/input'))).click()

#---------------------------------------------------------------------------------------------------------------------------------------------

#Drill
for y in range(1, 31):
    for x in range(1, 201):
        try:
            #ticker
            ticker = str(driver.find_element_by_xpath('/html/body/div/div/main/div/div[4]/table/tbody/tr[%s]/td[1]/a' % (x)).text)
            #Anal rate
            analrate = str(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[4]/table/tbody/tr[%s]/td[5]/div' % (x,)).text)
            #Anal Cnt
            analcnt = str(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[4]/table/tbody/tr[%s]/td[6]/div' % (x,)).text)
            #Price TGT
            priceTGT = str(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[4]/table/tbody/tr[%s]/td[11]/div' % (x,)).text)
            priceTGT2=priceTGT[0:-1]
            #Price
            price = str(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[4]/table/tbody/tr[%s]/td[7]/div' % (x,)).text)
            #day
            today = date.today()
            day = str(today.strftime('%m-%d-%Y'))
            #split
            split=str(driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[4]/table/tbody/tr[%s]/td[12]/div' % (x,)).text)
            split2 = str(tool.format(split))

            #Storage
            print(ticker +' ' + analrate + ' ' + analcnt + ' ' + priceTGT2 + ' ' + price + ' ' + day + ' ' + split2)
            tool.maketables(ticker)
            tool.addrow(ticker, analrate, analcnt, priceTGT2, price, day, split)

            # tool.cleartables()
        except Exception as e:
            print(e)
            continue

    #Next Page
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/main/div/nav/button[2]'))).click()






