import sqlite3 
carData =[
    (1, 'Audi', 54678),
    (2, 'Tata', 54678),
    (3, 'Skoda', 54678),
    (4, 'volvo', 54678),
    (5, 'bently', 54678),
    (6, 'hummer', 54678)]

con = sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute("CREATE TABLE cars(Id INT,Name TEXT,price INT)")
cur.executemany("INSERT INTO cars VALUES(?,?,?)",carData)
con.commit()
con.close()
print("values inserted.")
