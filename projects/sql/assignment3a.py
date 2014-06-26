import random
import sqlite3

##max_int=100
##
##num_list=[]
##
##for i in range(max_int):
##    rand=round(random.random()*max_int)
##    num_list.append((i,rand))
##
##with sqlite3.connect('newnum.db') as connection:
##
##    c = connection.cursor()
##
##    c.execute("DROP TABLE IF EXISTS randnums")
##
##    c.execute("""CREATE TABLE randnums (counter
##    INTEGER AUTO INCREMENT PRIMARY KEY, num INTEGER)""")
##
##    c.executemany(""" INSERT INTO randnums VALUES(?,?)""",num_list)

def refresh_db(max_int):

    num_list=[]

    for i in range(max_int):
        rand=round(random.random()*max_int)
        num_list.append((i,rand))

    with sqlite3.connect('newnum.db') as connection:

        c = connection.cursor()

        c.execute("DROP TABLE IF EXISTS randnums")

        c.execute("""CREATE TABLE randnums (counter
        INTEGER AUTO INCREMENT PRIMARY KEY, num INTEGER)""")

        c.executemany(""" INSERT INTO randnums VALUES(?,?)""",num_list)
