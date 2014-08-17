import sqlite3

conn = sqlite3.connect('project2.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS data 
	(text TEXT, url TEXT, views TEXT)""")

conn.commit()
conn.close()