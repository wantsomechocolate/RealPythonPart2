import sqlite3

with sqlite3.connect('new.db') as connection:
	
	c = connection.cursor()

	#c.execute("""INSERT INTO regions VALUES(?,?)""", ('East Brunswick',
	#			'East'))

	c.execute("""SELECT DISTINCT population.city, population.population, 
				regions.region FROM population, regions WHERE 
			population.city = regions.city ORDER by
			population.city ASC""")

	rows = c.fetchall()

	for r in rows:
		for i in range(len(r)):
			print(r[i], end=" ")

		print(" ")

