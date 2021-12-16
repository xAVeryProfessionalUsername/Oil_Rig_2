from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyodbc
from SQLtoolpackage.SQLtoolsmodule import SQLtools
import time



conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-84EULDP;DATABASE=StockData;Trusted_Connection=yes;')

cursor=conn.cursor()


class tool():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-84EULDP;DATABASE=StockData;Trusted_Connection=yes;')

    cursor = conn.cursor()


    @classmethod
    def maketables(self):
        cursor.execute('''
            CREATE TABLE %s(
                PersonId INTEGER PRIMARY KEY,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                Age INTEGER NULL);
                ''' % (ticker,))
        conn.commit()

# def maketables():
#     cursor.execute('''
#         CREATE TABLE %s(
#             PersonId INTEGER PRIMARY KEY,
#             FirstName TEXT NOT NULL,
#             LastName TEXT NOT NULL,
#             Age INTEGER NULL);
#             ''' % (ticker,))
#     conn.commit()


#------------------------------------------------------------------------------------------------------------------------------------------

path = "C:\chromedriver.exe"

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://stockanalysis.com/stock-screener/")
print(driver.title)

#-------------------------------------------------------------------------------------------------------------------------------------------

try:

#Up to 200
    WebDriverWait(driver, 1).until(
       EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/nav/div/div'))).click()
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/main/div/nav/div/div/ul/li[4]'))).click()

#Select all the fucking data
    #Click cats
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[3]/div[2]/div[3]/div/div[1]'))).click()
    #select cats
    #Target %
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[21]/input'))).click()
    #Anal rating
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[2]/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[18]/input'))).click()
    #Anal cnt
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[2]/main/div/div[3]/div[2]/div[3]/div/div[2]/div/div[2]/div[19]/input'))).click()

#---------------------------------------------------------------------------------------------------------------------------------------------
    for y in range(2):
        for x in range(1, 2):
            #ticker
            ticker = str(driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[4]/table/tbody/tr[%s]/td[1]/a' % (x,)).text)
            #Anal rate
            analdata = driver.find_element_by_xpath('/html/body/div/div[2]/main/div/div[4]/table/tbody/tr[%s]/td[5]/div' % (x,)).text
            #Anal Cnt
            analcnt = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div[4]/table/tbody/tr[%s]/td[6]/div' % (x,)).text
            #Price TGT
            priceTGT = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div[4]/table/tbody/tr[%s]/td[11]/div' % (x,)).text
            #Price
            price = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div[4]/table/tbody/tr[%s]/td[7]/div' % (x,)).text

            print(ticker +' ' + analdata + ' ' + analcnt + ' ' + priceTGT + ' ' + price)
            tool.maketables()

        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div[2]/main/div/nav/button[2]'))).click()
except:
    print("steve")




