import sqlite3 as sq
from easygui import *

def lower_string(_str):
    return _str.lower()

def print_all():
    with sq.connect('phonebook.db') as con:
        cur = con.cursor()
        cur.execute ("SELECT * FROM phones ORDER BY name ASC")
        rows = cur.fetchall()
        result_list = []
        for row in rows:
             record_str = "%s %s %s %s %s %s\n" % (row[0], row[1], row[2], row[3], row[4],row[5])
             result_list.append (record_str)
        textbox ("Найдены контакты:", "ТС-2024", result_list)
    con.close()

def find_contact():
    msg ="Введите имя для поиска записи и нажмите OK"
    title = "ТС-2024 Поиск"

    name_f = str(enterbox(msg,title)).lower()
    with sq.connect('phonebook.db') as con:
        cur = con.cursor()
        con.create_function("mylower", 1, lower_string)
        cur.execute ("SELECT * FROM phones WHERE mylower(name) LIKE ?",("%"+name_f+"%",))
        rows = cur.fetchall ()
        if len(rows)==0:
            msgbox(f"Записи с таким именем не найдены!")
            return 0
        else:
             result_list = []
        for row in rows:
             record_str = "%s %s %s %s %s %s\n" % (row[0], row[1], row[2], row[3], row[4],row[5])
             result_list.append (record_str)
        textbox ("Найдены контакты:", "Поиск", result_list)
    con.close()
    