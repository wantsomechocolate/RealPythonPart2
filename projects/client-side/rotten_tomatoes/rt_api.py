
import json
import requests
import sqlite3

YOUR_OWN_KEY = 'uz7wfv82dhxwdwg7h3bme45u'
url = requests.get("http://api.rottentomatoes.com/api/public/v1.0/" +
                   "lists/movies/in_theaters.json?apikey=%s" % (YOUR_OWN_KEY,))

binary = url.content

output = json.loads(binary)

movies = output['movies']

with sqlite3.connect('movies.db') as connection:

    c = connection.cursor()

    for movie in movies:

        c.execute("""INSERT INTO new_movies VALUES(?,?,?,?,?,?,?)""",
                  (movie['title'], movie['year'], movie['mpaa_rating'],
                   movie['release_dates']['theater'], movie['runtime'],
                   movie['ratings']['critics_score'],
                   movie['ratings']['audience_score']))

        c.execute("SELECT * FROM new_movies ORDER BY title ASC")

        rows = c.fetchall()

        for r in rows:
            for i in range(len(r)):
                print r[i],
            print ""
