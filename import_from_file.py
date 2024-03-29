import csv
import sqlite3 as sq
from easygui import *

def import_file_to_db():
    with open('phonebook.txt','r', encoding = 'utf-8') as f: #psevdomin failu
        data = f.readlines()
        #print(data)
        with sq.connect('phonebook.db') as con:
                cur = con.cursor()
                id_list = list(cur.execute("SELECT id from phones;"))
                id_list = [int(x[0]) for x in id_list]
                print(id_list, type(id_list))
                for line in data:
                    line = line.split()
                    line[0] = int(line[0])
                    count=0
                    if line[0] not in id_list:
                        count+=1
                        cur.execute("INSERT INTO phones (id, name, surname, phone,email, birthdate) VALUES (?, ?, ?, ?, ?, ?);", line)
        msgbox(f"{count} записей загружено")    
    con.close()    
        
 