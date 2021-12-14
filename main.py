from ExecutionСommands import ExecDb
from conf.connect_commands import ConnectCreate
from argpase_work import Argpase

# !!!! РАЗДЕЛИТЬ ПОТОМ НА КЛАССЫ
# 1.Коннект
# 2.Содать табл
# 3. Insert data
# -open.file
# 4. Select
# 5. upload result
from conf.save_result import SaveResultJsonXml
from task_3_sql import open_file


class InterfaceDb:

    def __init__(self, db_name="task_3"):
        self.connector = ConnectCreate.connection_db()
        self._cursor = self.connector.cursor()
        self.db_name = db_name

    def create_db(self):
        self._cursor.execute(ExecDb.create_db(self.db_name))

    def drop_db(self):
        self._cursor.execute(ExecDb.drop_db(self.db_name))

    def create_table(self):
        for item_table in ExecDb.create_tables(self.db_name):
            self._cursor.execute(item_table)

    def insert_data_rooms(self, rooms):

        self._cursor.executemany(ExecDb.insert_datas_rooms(self.db_name), rooms)
        self.connector.commit()
        print('insert rooms')

    def insert_data_students(self, students):
        for student in students:
            self._cursor.execute(ExecDb.insert_datas_students(self.db_name), (
                student['id'],
                student['birthday'],
                student['name'],
                student['room'],
                student['sex']))
        # self._cursor.executemany(ExecDb.insert_datas_students(self.db_name), students)
        self.connector.commit()
        print('insert students')

    def count_students_in_room(self):
        text_file_res = '1.AmountStudentInRoom'

        self._cursor.execute(ExecDb.count_students_in_room(self.db_name))
        head = self._cursor.description
        result = self._cursor.fetchall()

        SaveResultJsonXml.dictfetchall(head, result, text_file_res)

    def get_min_avg_age_top_5(self):
        #top 5 комнат, где самые маленький средний возраст студентов

        text_file_res = '2.Min_avg_age_top_5'
        self._cursor.execute(ExecDb.get_min_age_avg_top_5(self.db_name))

        head = self._cursor.description
        result = self._cursor.fetchall()
        SaveResultJsonXml.dictfetchall(head, result, text_file_res)

    def get_room_delta_age_top5(self):
        text_file_res = '3.Delta_max_age_top_5'
        self._cursor.execute(ExecDb.get_room_delta_age_top5(self.db_name))
        head = self._cursor.description
        result = self._cursor.fetchall()
        SaveResultJsonXml.dictfetchall(head, result, text_file_res)


    def get_room_dif_sex(self):
        #список комнат где живут разнополые студенты
        text_file_res = '4.RoomSexDif'
        self._cursor.execute(ExecDb.get_room_sex_dif(self.db_name))

        head = self._cursor.description
        result = self._cursor.fetchall()
        SaveResultJsonXml.dictfetchall(head, result, text_file_res)

    def index_sql(self):
        self._cursor.execute(ExecDb.index_sql(self.db_name))


def main():
    arg_parser = Argpase.work_argparse()
    students_file=open_file(arg_parser.r_students)
    rooms_file = open_file(arg_parser.r_rooms)

    a = InterfaceDb()
    a.create_db()
    a.create_table()

    insert_room = [(id,name) for id, name in (item.values() for item in rooms_file)]
    # insert_student=[(id,birth,name,room,sex) for id,birth,name,room,sex in (item.values() for item in students_file)]
    # print(aaa)
    a.insert_data_rooms(insert_room)
    a.insert_data_students(students_file)

    a.count_students_in_room()
    a.get_min_avg_age_top_5()
    a.get_room_delta_age_top5()
    a.get_room_dif_sex()

    a.index_sql()
    

    # a.get_room_dif_sex()


if __name__ == '__main__':
    main()

    # a = InterfaceDb()
    # a.create_db()
    # a.create_table()
    #
    # students_file=open_file('students.json')
    # rooms_file = open_file('rooms.json')
    #
    # insert_room = [(id,name) for id, name in (item.values() for item in rooms_file)]
    # # insert_student=[(id,birth,name,room,sex) for id,birth,name,room,sex in (item.values() for item in students_file)]
    # # print(aaa)
    # a.insert_data_rooms(insert_room)
    # a.insert_data_students(students_file)
    # a.count_students_in_room()
    # a.drop_db()
    # d=a.create_connection_mysql_db('test1').cursor()
    # d.execute("SELECT * FROM room")

    # cursor = a.create_connection_mysql_db('test1').cursor()
    # a.get_data_table_db()



# - Сделать запросы к базе данных чтобы вернуть:
# - список комнат и количество студентов в каждой из них
# - top 5 комнат, где самые маленький средний возраст студентов
# - top 5 комнат с самой большой разницей в возрасте студентов
# - список комнат где живут разнополые студенты
# (Всю "математику" делать стоит на уровне БД)