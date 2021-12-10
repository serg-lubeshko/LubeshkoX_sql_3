import mysql.connector
from mysql.connector import Error

from config import db_config
#!!!! РАЗДЕЛИТЬ ПОТОМ НА КЛАССЫ
#1.Коннект
#2.Содать табл
#3. Insert data
    #-open.file
#4. Select
#5. upload result

class interfaceDb:
    def __init__(self, name_data_base=None):
        # self.name_data_base =name_data_base
        self.connect = self.create_connection_mysql_db(name_data_base)
        # self.cursor = self.connect.cursor()

    def create_connection_mysql_db(self, db):
        connection_db = None
        try:
            connection_db = mysql.connector.connect(
                host=db_config['mysql']['host'],
                user=db_config['mysql']['user'],
                password=db_config['mysql']['pass'],
                database=db
            )
            if connection_db.is_connected():
                print('Connected to MySQl database')
        except Error as db_connection_error:
            print('Attention! An error occured', db_connection_error)
        return connection_db

    def get_data_table_db(self):
        select_room_query = '''SELECT * FROM room'''
        # print(self.cursor.__dict__)
        # w = self.cursor.execute(select_room_query)
        # print(w)
        # result = w.fetchall()
        with self.connect:
            cur = self.connect.cursor()
            cur.execute(select_room_query)
            rows = cur.fetchall()

            for row in rows:
                print(row)
        #     result = w.fetchall()
        #     for row in result:
        #         print(row)

    # SELECT * FROM test.room


if __name__ == '__main__':
    a = interfaceDb(name_data_base='test')
    # d=a.create_connection_mysql_db('test1').cursor()
    # d.execute("SELECT * FROM room")

    # cursor = a.create_connection_mysql_db('test1').cursor()
    a.get_data_table_db()
