import sqlite3

connection = sqlite3.connect('database.db')


with open('.venv\scheme.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO gmedium (title, members) VALUES (?, ?)",
            ('ITZY - Untouchable', '5')
            )

cur.execute("INSERT INTO gmedium (title, members) VALUES (?, ?)",
            ('Everglow - Adios', '6')
            )

connection.commit()
connection.close()