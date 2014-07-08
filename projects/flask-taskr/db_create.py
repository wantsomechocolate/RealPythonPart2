#db_create.py

from views import db
from models import FTasks
from datetime import date

# create the database and the bd table
db.create_all()

#insert data
##db.session.add(FTasks('Finish this tutorial', date(2014, 3, 13), 10, 1))
##db.session.add(FTasks('Finish Real Python', date(2014, 3, 13), 10, 1))

# commit the changes
db.session.commit()

#import sqlite3
#from config import DATABASE_PATH

##with sqlite3.connect(DATABASE_PATH) as connection:
##
##    #get a cursor object used to execute SQL commands
##    c = connection.cursor()
##
##    #create the table
##    c.execute("""CREATE TABLE ftasks(task_id INTEGER PRIMARY KEY
##        AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL,
##        priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
##
##    #insert dummy data into the table
##    c.execute("""INSERT INTO ftasks (name, due_date, priority, status)
##              VALUES("Finish this tutorial", "02/03/2014", 10, 1)""")
##    c.execute("""INSERT INTO ftasks (name, due_date, priority, status)
##              VALUES("Finish Real Python Course 2", "02/03/2014", 10, 1)""")
