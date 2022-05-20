import sqlite3 as sq
import pandas as pd
connection = sq.connect('information.db')
curs = connection.cursor()
curs.execute("create table if not exists inflationInfo" +
             " (date_from text, date_to text, inflation integer)")


inf_rate = pd.read_csv('inflation.csv')

curs.execute(
        "INSERT INTO inflationInfo (date_from,date_to,inflation) VALUES ('{}','{}','{}')")
connection.commit()

inf_rate.to_sql('inflationInfo', connection, if_exists='replace')

curs.execute('select * from inflationInfo')
records = curs.fetchall()
for row in records:
    print(row)

connection.close()