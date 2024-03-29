import sqlite3 as sq
from easygui import *

def lower_string(_str):
    return _str.lower()

def change_contact():
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
        if len(rows)>1:
               row = choicebox("Какой контакт изменить?","Выбор контакта",rows)
               id = int(str(row[1:]).split(",")[0])
        else:
             row = rows[0]
             id=row[0] #номер записи в БД
        
        choices = ["Имя","Фамилия","Телефон","Email","Дата рождения"]
        msg=f"Выберите поле, чтобы изменить \n {row}"
        field = choicebox(msg,"Поле редактирования",choices)
        
        if field == "Имя":
            new_value = enterbox("Ведите новое имя:")
            query = f"UPDATE phones SET name = '{new_value}' where id = {id}"
            cur.execute (query) 
        elif field == "Фамилия":
            new_value = enterbox("Ведите новую фамилию:")
            query = f"UPDATE phones SET surname = '{new_value}' where id = {id}"
            cur.execute (query)
        elif field == "Телефон":
            new_value = enterbox("Ведите новый телефон:")
            query = f"UPDATE phones SET phone = '{new_value}' where id = {id}"
            cur.execute (query)
        elif field == "Email":
            new_value = enterbox("Ведите новый email:")
            query = f"UPDATE phones SET email= '{new_value}' where id = {id}"
            cur.execute (query)
        elif field == "Дата рождения":
            new_value = enterbox("Ведите новую дату рождения:")
            query = f"UPDATE phones SET birthdate = '{new_value}' where id = {id}"
            cur.execute (query)
        image = "ok.jpg"
        msgbox("Контакт изменен!", "Редактирование",image=image)
    con.close()