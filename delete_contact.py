import sqlite3 as sq
from easygui import *

def lower_string(_str):
    return _str.lower()

def delete_contact():
    msg ="Введите имя для поиска записи на удаление и нажмите OK"
    title = "ТС-2024 Удаление"

    name_del = str(enterbox(msg,title)).lower()
    with sq.connect('phonebook.db') as con:
        cur = con.cursor()
        con.create_function("mylower", 1, lower_string)
        cur.execute ("SELECT * FROM phones WHERE mylower(name) LIKE ?",("%"+name_del+"%",))
        rows = cur.fetchall ()
        if len(rows)==0:
            msgbox(f"Записи с таким именем не найдены!")
            return 0
        if len(rows)>1:
               row = choicebox("Какой контакт удалить?","Выбор контакта",rows)
               id = int(str(row[1:]).split(",")[0])
        else:
             row = rows[0]
             id=row[0]
        image = "attention.png"
        answer = ynbox(f"Удалить контакт {row}?","Подтверждение удаления",("Да", "Нет"),image=image)
       # print(id, type(id), row[1], type(row))
        if answer:
            cur.execute (f"DELETE FROM phones WHERE id = {id}")
            image = "ok.png"
            msgbox("Контакт удален!", "Удаление", image=image)
    con.close()
    