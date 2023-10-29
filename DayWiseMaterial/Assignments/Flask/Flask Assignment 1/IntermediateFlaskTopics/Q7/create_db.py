import sqlite3

conn = sqlite3.connect('items.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE items (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

conn.commit()
conn.close()