import sqlite3
carData=[
    (lite.connect('mtica.db')

cur=con.cursor()
cur.execute("SELECT * FROM cars")
rows=cur.fetchall()
for row in rows:
    print(row)

