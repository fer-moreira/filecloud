import sqlite3
from sqlite3 import Error

from django.conf import settings
import random


class SqliteStorageHandler (object):
    def __init__ (self):
        self.dbpath = settings.USER_DB_PATH
        self.finaldbpath = ""
        self.iserror = False

    def create_file (self):
        """ create a database connection to a SQLite database """
        conn = None
        fulldbpath = ""
        dbhash = 0

        try:
            dbhash = self.random_hash()
            fulldbpath = "{path}/{hash}.db".format(path=settings.USER_DB_PATH,hash=dbhash)
            print(fulldbpath)

            conn = sqlite3.connect(fulldbpath)

        except Error as e:
            self.iserror = True
            raise
        
        finally:
            if conn:
                self.iserror = False
                self.finaldbpath = fulldbpath
                conn.close()

    def random_hash (self, size=32):
        return random.getrandbits(size)
