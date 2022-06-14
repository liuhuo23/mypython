import random

from pymysql import *
class MySQL(object):
    def __init__(self,user:str,
                 password:str,
                 host:str,
                 database,
                 port=3306,
                 charset='utf-8'):
        if user is NULL or password is NULL or database is NULL:
            raise "user or password or database can't null"
        self.conn = connect(host=host, user=user, password=password, database=database, port=port, charset=charset)
        self.cursor = self.conn.cursor()
    def selectAll(self):
        sql = "select * from"


if __name__ == '__main__':
    pass
