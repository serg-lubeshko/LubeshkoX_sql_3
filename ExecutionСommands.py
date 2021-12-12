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
        table_1 = f'''CREATE TABLE IF NOT EXISTS {db_name}.rooms (
        `id` INT  PRIMARY KEY,
        `name` VARCHAR(123)
         )'''

        table_2 = f'''CREATE TABLE IF NOT EXISTS {db_name}.students (
        `id` INT UNSIGNED PRIMARY KEY,
        `birthday` DATETIME,
        `name` VARCHAR(123),
        `room` INT, `sex` VARCHAR(2),
        FOREIGN KEY (room) REFERENCES rooms(id)
        )'''
        return (table_1, table_2)

    @staticmethod
    def insert_datas_rooms(db_name):
        return f"INSERT IGNORE INTO {db_name}.rooms(`id`, `name`) VALUES(%s, %s)"

    @staticmethod
    def insert_datas_students(db_name):
        return f"INSERT IGNORE INTO {db_name}.students(`id`, `birthday`, `name`, `room`, `sex`) VALUES(%s, %s, %s, %s, %s)"

    @staticmethod
    def count_students_in_room(db_name):
        return f''' SELECT r.id, r.name, COUNT(s.id) count
                    FROM {db_name}.rooms r
                        left JOIN {db_name}.students s ON r.id = s.room
                        group by  r.id
        '''
