from config import db_config
import mysql.connector
from mysql.connector import Error

class ConnectCreate:
    # def __init__(self, name_data_base=None):
        # self.name_data_base =name_data_base
        # self.connect = self.create_connection_mysql_db(name_data_base)
        # self.cursor = self.connect.cursor()

    @staticmethod
    def connection_db():
        connection_db = None
        try:
            connection_db = mysql.connector.connect(
                host=db_config['mysql']['host'],
                user=db_config['mysql']['user'],
                password=db_config['mysql']['pass'],
                # database=db,
            )
            if connection_db.is_connected():
                print('Connected to MySQl database')
        except Error as db_connection_error:
            print('Attention! An error occured', db_connection_error)
        return connection_db