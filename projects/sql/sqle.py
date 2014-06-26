import sqlite3

conn = sqlite3.connect('new.db')

cursor = conn.cursor()

try:
	cursor.execute("INSERT INTO populations \
				VALUES('New York City','NY',8200000)")
	cursor.execute("INSERT INTO populations \
				VALUES('San Francicso','CA', 800000)")

	conn.commit()

except sqlite3.OperationalError:
	print("Oops! something went wrong. Try again...")

conn.close()

