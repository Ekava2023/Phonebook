import sqlite3 as sq
from easygui import *
import os
import csv

def save_to_file():
    with sq.connect('phonebook.db') as con:
        cur = con.cursor()
        cur.execute ("SELECT * FROM phones ORDER BY id ASC")
        rows = cur.fetchall ()
        filename = filesavebox()
        if os.path.exists(filename):
            os.remove(filename)
        
        # with open('phonebook.csv', 'w', newline='') as f:
        #         writer = csv.writer(f, lineterminator='\n') 
        for row in rows:
             file = open(filename, 'a', encoding='utf-8')
             file.write("%s %s %s %s %s %s\n" % (row[0], row[1], row[2], row[3], row[4],row[5]))
             file.close()
    image = "ok.png"
    msgbox (f"Все данные сохранены в файл {filename}.", "Телефонный справочник", ok_button="Закрыть",image=image)
