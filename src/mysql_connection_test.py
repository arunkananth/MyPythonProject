'''
Created on Aug 1, 2017

@author: hdusr
'''
import mysql.connector
import pandas as pd

db = mysql.connector.connect(user='hdusr', password='mercury*88',
                              host='localhost',
                              database='MyDB')
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT min(company_id),company_nm FROM company group by company_nm")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

df_mysql = pd.read_sql('select * from company;', con=db)    
print ('loaded dataframe from MySQL. records:', len(df_mysql))

    

for (company_id, company_nm) in cur:
    print("{} , {}".format(company_id, company_nm))

db.close()
