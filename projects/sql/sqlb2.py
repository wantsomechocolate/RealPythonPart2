import sqlite3
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO population VALUES('East Brunswick', 'NJ', 82000)")
	c.execute("INSERT INTO population VALUES('Richmond', 'CA', 80000)")