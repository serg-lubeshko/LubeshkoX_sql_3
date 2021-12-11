class ExecDb:
    @staticmethod
    def create_db(db_name):
        print('DataBase Create')
        return f"CREATE DATABASE IF NOT EXISTS {db_name}"

    @staticmethod
    def drop_db(db_name):
        print('DataBase Delete')
        return f"DROP DATABASE IF EXISTS{db_name}"

    @staticmethod
    def create_tables(db_name):
        print('Table Create')
        table_1 = f"CREATE TABLE IF NOT EXISTS {db_name}.rooms (`id` INT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(123))"
        table_2 = f'''CREATE TABLE IF NOT EXISTS {db_name}.students (`id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
         `birthday` DATETIME, `name` VARCHAR(123), `room` INT, `sex` VARCHAR(2), FOREIGN KEY (room) REFERENCES rooms(id) ON DELETE CASCADE )'''
        return (table_1, table_2)
