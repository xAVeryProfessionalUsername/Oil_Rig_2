import pyodbc
from datetime import datetime

conn = pyodbc.connect(
   'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-84EULDP;DATABASE=StockData;Trusted_Connection=yes;')

cursor = conn.cursor()

tablelist = []

class toolz():

    @classmethod
    def deleterow(self):
        cursor.execute('''
        DELETE FROM Steve WHERE PersonId in (1)''')

    @classmethod
    def showtables(self):
        for x in cursor.tables(schema='dbo', tableType='TABLE'):
            tablelist.append(x[2])
        return(tablelist)

    @classmethod
    def cleartables(self):
        for x in tablelist:
            cursor.execute('''
            DROP TABLE %s;
            ''' % (x))
        conn.commit()

    @classmethod
    def maketables(self, ticker):
        if not cursor.tables(table= ticker, tableType='TABLE').fetchone():
            cursor.execute('''
            CREATE TABLE %s(
            stockID INTEGER IDENTITY(1,1),
            analrate varchar(15) NULL,
            analcnt varchar(15) NULL,
            priceTGT varchar(15) NULL,
            price varchar(15) NULL,
            day varchar(15) NULL,
            split varchar(15) NULL);
            ''' % (ticker, ))
            conn.commit()


    @classmethod
    def addrow(self, ticker, analrate, analcnt, priceTGT2, price, day, split2):
        if cursor.tables(table= ticker, tableType='TABLE').fetchone():
            cursor.execute('''
            SET IDENTITY_INSERT %s ON;
            INSERT INTO %s(
            stockID, analrate, analcnt, priceTGT, price, day, split)
            VALUES(1, '%s', '%s', '%s', '%s', '%s', '%s');
            SET IDENTITY_INSERT %s OFF;
            ''' % (ticker, ticker, analrate, analcnt, priceTGT2, price, day, split2, ticker))
            conn.commit()

    @classmethod
    def formayt(self, split):
        if split != '-':
            m = {
                'jan': 1,
                'feb': 2,
                'mar': 3,
                'apr': 4,
                'may': 5,
                'jun': 6,
                'jul': 7,
                'aug': 8,
                'sep': 9,
                'oct': 10,
                'nov': 11,
                'dec': 12
            }
            s = split[:3].lower()

            date = ''
            month = m[s]
            if len(split) == 12:
                date = split[4:6]
            if len(split) == 11:
                date = split[4]
            year = split[-4:]
            return(str(date) + '/' + str(month) + '/' + str(year))
        if split == '-':
            return('Niks')

    @classmethod
    def datecheck(self, dayte):
        latest = '11/7/2021'
        past = datetime.strptime(latest, "%d/%m/%Y")
        past2 = datetime.strptime(dayte, "%d/%m/%Y")
        if past2.date()<past.date():
            return 1



