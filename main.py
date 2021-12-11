from connect_commands import ConnectCreate
from ExecutionСommands import ExecDb


# !!!! РАЗДЕЛИТЬ ПОТОМ НА КЛАССЫ
# 1.Коннект
# 2.Содать табл
# 3. Insert data
# -open.file
# 4. Select
# 5. upload result

class InterfaceDb:

    def __init__(self, db_name="task_3"):
        self.connector = ConnectCreate.connection_db()
        self._cursor = self.connector.cursor()
        self.db_name=db_name

    def create_db(self):
        self._cursor.execute(ExecDb.create_db(self.db_name))

    def drop_db(self):
        self._cursor.execute(ExecDb.drop_db(self.db_name))

    def create_table(self):
        for item_table in ExecDb.create_tables(self.db_name):
            self._cursor.execute(item_table)

    def insert_data(self):
        pass

    #     # self._cursor.execute(ExecDb.drop_db(db_name))
    #     with self._cursor:
    #         self._cursor.

    # def __init__(self, name_data_base=None):
    #     # self.name_data_base =name_data_base
    #     self.connect = self.create_connection_mysql_db(name_data_base)
    #     # self.cursor = self.connect.cursor()
    #
    # def create_connection_mysql_db(self, db):
    #     connection_db = None
    #     try:
    #         connection_db = mysql.connector.connect(
    #             host=db_config['mysql']['host'],
    #             user=db_config['mysql']['user'],
    #             password=db_config['mysql']['pass'],
    #             database=db,
    #             # auth_plugin=db_config['auth_plugin']
    #         )
    #         if connection_db.is_connected():
    #             print('Connected to MySQl database')
    #     except Error as db_connection_error:
    #         print('Attention! An error occured', db_connection_error)
    #     return connection_db

    # def get_data_table_db(self):
    #     select_room_query = '''SELECT * FROM room'''
    #     # print(self.cursor.__dict__)
    #     # w = self.cursor.execute(select_room_query)
    #     # print(w)
    #     # result = w.fetchall()
    #     with self.connect:
    #         cur = self.connect.cursor()
    #         cur.execute(select_room_query)
    #         rows = cur.fetchall()
    #
    #         for row in rows:
    #             print(row)
    #     result = w.fetchall()
    #     for row in result:
    #         print(row)

    # SELECT * FROM test.room


if __name__ == '__main__':
    a = InterfaceDb()
    a.create_db()
    a.create_table()
    # a.drop_db()
    # d=a.create_connection_mysql_db('test1').cursor()
    # d.execute("SELECT * FROM room")

    # cursor = a.create_connection_mysql_db('test1').cursor()
    # a.get_data_table_db()
