# test.py

import os
import unittest

#from views import app, db
from app import app, db
from app.models import User
from app.models import FTasks
from config import basedir
import datetime

TEST_DB = 'test.db'

class Users(unittest.TestCase):

    # this is a special method that is executed prior to each test

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+\
                os.path.join(basedir, TEST_DB)

        self.app = app.test_client()
        db.create_all()

    # this is a special method that is executed after each test

    def tearDown(self):
        db.drop_all()

    # each test should start with 'test'

    def test_new_user_can_register(self):
        new_user = User('mherman', 'micheal@mherman.org', 'michealhearm')
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            #t.name
            assert t.name == 'mherman'

    def test_existing_user_can_login(self):
        new_user=User('mherman', 'micheal@mherman.org', 'michealhearm')
        db.session.add(new_user)
        db.session.commit()
        u=User.query.filter_by(name='mherman', password='michealhearm').first()
        assert u.name=='mherman'

    def test_add_new_task(self):
        new_task = FTasks(
                    'Task Name',
                    datetime.date(2012,6,5),
                    8,
                    datetime.date(2012,6,5),
                    '1',
                    'mherman'
                    )
        db.session.add(new_task)
        db.session.commit()
        
        

    
    

if __name__== "__main__":
    unittest.main()
