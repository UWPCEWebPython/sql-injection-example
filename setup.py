import sqlite3

conn = sqlite3.connect('my_database.db')

c = conn.cursor()
c.execute("CREATE TABLE messages (ip text, content text)")

c.close()

