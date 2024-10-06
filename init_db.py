import sqlite3

connection = sqlite3.connect('laundry.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO requests (machine_id, issue, email) VALUES (?, ?)",
          ("678-HHJ", "Dryer doesn't work", 'qpmzj@example.com')
          )


connection.commit()
connection.close()