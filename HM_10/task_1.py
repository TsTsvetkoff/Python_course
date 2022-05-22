import sqlite3 as sq
import pandas as pd
from termcolor import colored

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

curs.execute(
    "SELECT * FROM inflationInfo WHERE inflation >=3 AND date_to >= '1999-01';"
)
inflation_high = curs.fetchall()
print(f"Here is when (after 1999 year) the MONTHLY inflation % is greater or equal to 3 :\n{inflation_high}")
print(colored("FYI 1999-2000 : Dot-com bubble burst\n"
              "FYI 2006-2007 : Financial crisis triggered by Lehman Brothers collapse\n", 'green'))

curs.execute(
    "SELECT * FROM inflationInfo WHERE date_to >= '2022-01';"
)
apocalypse_now = curs.fetchall()

print(colored(f"Where are we in 2022 in terms of crisis prediction (3% critical point)\n{apocalypse_now}", "red"))

connection.close()
