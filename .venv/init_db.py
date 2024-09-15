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

cur.execute("INSERT INTO girls (title, members, lvl) VALUES (?, ?, ?)",
            ('SUNMI - You Cant Sit With US', '1', 'easy')
            )

cur.execute("INSERT INTO girls (title, members, lvl) VALUES (?, ?, ?)",
            ('XG - GRLGVNG', '7', 'pro')
            )

cur.execute("INSERT INTO girls (title, members, lvl) VALUES (?, ?, ?)",
            ('XG -Tippy Toes', '7', 'pro')
            )

cur.execute("INSERT INTO boys (title, members, lvl) VALUES (?, ?, ?)",
            ('Taemin - Guilty', '1', 'hard')
            )

cur.execute("INSERT INTO boys (title, members, lvl) VALUES (?, ?, ?)",
            ('TXT - Devil by the window', '5', 'medium')
            )

connection.commit()
connection.close()