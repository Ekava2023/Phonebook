import sqlite3 as sq
from easygui import *

from print_all import print_all, find_contact
from add_contact import add_contact
from save import save_to_file
from delete_contact import delete_contact
from import_from_file import import_file_to_db
from change_contact import change_contact

with sq.connect('phonebook.db') as con:
    cur = con.cursor()
 
    cur.execute("""
            CREATE TABLE IF NOT EXISTS phones
             (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT,
                phone TEXT NOT NULL,
                email TEXT,
                birthdate TEXT
             );
    """)
    cur.execute ("SELECT * FROM phones")
    rows = cur.fetchall ()
    if len(rows)==0: 
        pass
#         contacts_default = [(1, 'Нина', 'Иванова', '123456', 'nina@mail.ru', '07.09.2002'),
#           (2, 'Василий', 'Петров', '789456', '-'','01.05.1995')
#           ]
#         cur.executemany("INSERT INTO phones VALUES (?,?,?,?,?,?)", contacts_default)
# con.close()




image = "phone_img.png"
msgbox("Вас приветствует ТС-2024!", "Телефонный справочник",ok_button="СТАРТ",image=image)


def start_menu():
    command = None
    msg ="Выберите действие и нажмите OK"
    title = "ТС-2024"
    choices = ["Показать все контакты","Найти контакт","Добавить контакт",
                "Удалить контакт", "Редактировать контакт", "Сохранить в файл",
               "Импорт контактов из файла","Выход"]
    
    while command != "Выход":
        command = choicebox(msg, title, choices)
        if command == "Импорт контактов из файла":
            import_file_to_db()
        elif command == "Добавить контакт":
            add_contact()
        elif command == "Удалить контакт":
            delete_contact()
        elif command == "Редактировать контакт":
            change_contact()
        elif command == "Показать все контакты":
            print_all()
        elif command == "Сохранить в файл":
            save_to_file()
        elif command == "Найти контакт":
            find_contact()

start_menu()   
msgbox("Хорошего дня!","Телефонный справочник",ok_button="Закрыть",image=image)
