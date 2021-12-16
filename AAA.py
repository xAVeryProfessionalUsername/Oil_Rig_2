import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP;DATABASE=StockData;Trusted_Connection=yes;')

cursor = conn.cursor()

tablelist = []

class toolz():

    @classmethod
    def tablemake(self):
        if cursor.tables(table='Steve', tableType='TABLE').fetchone():
            print("Steve")
        else:
            cursor.execute('''
                CREATE TABLE Steve(
                    PersonId INTEGER PRIMARY KEY,
                    FirstName TEXT NOT NULL,
                    LastName TEXT NOT NULL,
                    Age INTEGER NULL);
                    ''')

    @classmethod
    def addrow(self):
        cursor.execute('''
            INSERT INTO Steve(
            PersonId, FirstName, LastName, Age)
            VALUES(1, 'steve' , 'sbeve', 69)''')

    @classmethod
    def deleterow(self):
        cursor.execute('''
        DELETE FROM Steve WHERE PersonId in (1)''')

    @classmethod
    def showtables(self):
        for x in cursor.tables(schema='dbo', tableType='TABLE'):
            tablelist.append(x[2])

    @classmethod
    def cleartables(self):
        showtables()
        for x in tablelist:
            cursor.execute('''
            DROP TABLE %s;
            ''' % (x))
        tablelist.clear()
        conn.commit()

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

    @classmethod
    def preent(self):
        print('steve')
