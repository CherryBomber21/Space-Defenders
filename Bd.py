import sqlite3
# скелет структуры бд
con = sqlite3.connect("rating.db")
cur = con.cursor()

cur.execute('''CREATE TABLE main(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name vachar(50) unique,
    level int)''')

con.commit()
con.close()