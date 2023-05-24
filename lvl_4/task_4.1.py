# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

# Cоздание таблицы School

def create_tbl_School():
    connection = sqlite3.connect('teachers.db')
    cursor = connection.cursor()
    sqlquery = """CREATE TABLE School (
    School_Id INTEGER NOT NULL PRIMARY KEY,
    School_Name TEXT NOT NULL,
    Place_Count INTEGER NOT NULL
    );"""
    cursor.execute(sqlquery)
    connection.commit()
    connection.close()

# При необходимости (Удаление таблицы Schools):
def delete_tbl_Schools():
    connection = sqlite3.connect('teachers.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS Schools')
    connection.commit()
    connection.close()

# Вставка значений в таблицу School
def add_Schools():
    connection = sqlite3.connect('teachers.db')
    cursor = connection.cursor()
    sqlquery = """INSERT INTO School (School_Id , School_Name , Place_Count )
    VALUES
    ('1', 'Протон', 200),
    ('2', 'Преспектива', 300),
    ('3', 'Спектр', 400),
    ('4', 'Содружество', 500);"""
    cursor.execute(sqlquery)
    connection.commit()
    connection.close()

# При необходимости (Удаление таблицы Students):
def delete_tbl_Students():
    connection = sqlite3.connect('teachers.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS Students')
    connection.commit()
    connection.close()

# Cоздание таблицы Students
def create_tbl_Students():
    connection = sqlite3.connect('teachers.db')
    cursor = connection.cursor()
    sqlquery = """CREATE TABLE Students (
    Student_Id INTEGER NOT NULL,
    Student_Name TEXT NOT NULL,
    School_Id INTEGER NOT NULL PRIMARY KEY
    );"""
    cursor.execute(sqlquery)
    connection.commit()
    connection.close()

def add_Students():
    connection = sqlite3.connect('teachers.db')
    cursor = connection.cursor()
    sqlquery = """INSERT INTO Students (Student_Id , Student_Name , School_Id)
    VALUES
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4);"""
    cursor.execute(sqlquery)
    connection.commit()
    connection.close()

def get_student(student_id):
  connection = sqlite3.connect("teachers.db")
  cursor = connection.cursor()
  # Чтобы соответствовать заданию, запрос нужно сделать так (но почему-то не работает):
  #query = "SELECT Students.Student_id, Students.Student_Name, Students.School_Id, chools.School_Name FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Students.Student_id = ?"
  #Работает так
  query = "SELECT Students.Student_id, Students.Student_Name, Students.School_Id FROM Students JOIN School ON School.School_Id = Students.School_Id WHERE Students.Student_id = ?"
  # Или так
  #query = "SELECT * FROM Students JOIN School ON School.School_Id = Students.School_Id WHERE Students.Student_id = ?"
  cursor.execute(query,(student_id,))
  records = cursor.fetchall()
  print(records)
  for row in records:
    print()

#create_tbl_School()
#delete_tbl_Schools()
#add_Schools()
#create_tbl_Students()
#delete_tbl_Students()
#add_Students()
get_student(202)