import sqlite3 as sq
from easygui import *

def add_contact():
    msg = "Введите новый контакт"
    title = "Добавление контакта"
    fieldNames = ["Имя","Фамилия","Телефон","Email","Дата рождения"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)
        
    #проверка на пустые поля
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "" and i in (0,2):
                errmsg = errmsg + (' Пожалуйста заполните поле "%s"!\n\n' % fieldNames[i])
        if errmsg == "": 
            break
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    
    if fieldValues != None: 
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                    fieldValues[i]= '-'
            
        fieldValues=tuple(fieldValues)
            #errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        #data_tuple = (name,surname,phone,email,birthdate)
        contact = ' '.join(fieldValues)
        if boolbox(f"Добавить контакт {contact}?", "ТС-2024: новый контакт", ["ДА", "НЕТ"]):
            with sq.connect('phonebook.db') as con:
                cur = con.cursor()
                cur.execute("""
                            INSERT INTO phones (name, surname, phone, email, birthdate) 
                            VALUES (?,?,?,?,?)""",fieldValues)
            image = "ok.png"
            msgbox("Контакт успешно добавлен!", image=image)
            con.close()

