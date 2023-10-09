"""
Реализовать консольное приложение заметки, с сохранением,
чтением, добавлением,редактированием и удалением заметок.
Заметка должна содержать идентификатор,заголовок,
тело заметки и дату/время создания или последнего изменения заметки.
Сохранение заметок необходимо сделать в формате json или csv формат
(разделение полей рекомендуется делать через точку с запятой).
Реализацию пользовательского интерфейса студент может делать как ему удобнее,
можно делать как параметры запуска программы (команда,данные),
можно делать как запрос команды с консолии последующим вводом данных,
как-то ещё,наусмотрение студента.Например:

pythonnotes.pyadd--title"новаязаметка"– msg"телоновой заметки" 

Или так: pythonnote.py 
Введитекоманду:add 
Введитезаголовокзаметки:новаязаметка 
Введитетелозаметки:телоновойзаметки 
Заметкауспешносохранена 
Введитекоманду: При чтении списка заметок
реализовать фильтрацию подате. 

"""

import csv
from datetime import datetime

fileBase = "Base.csv"
x = []


def writer():
    readOfFile()
    print("Заметка")
    a = input("Title \n")
    b = input("Text \n")
    c = datetime.today().strftime("%d/%m/%y %H:%M")
    x.append( {"ID": len(x), "DATE" : c, "TITLE" : a, "TEXT" : b} )
    writeOfFile()



def writeOfFile():

    with open(fileBase , "w", newline="") as file:

        # readOfFile()
        columns = ["ID","DATE","TITLE","TEXT"]
        write = csv.DictWriter(file, fieldnames=columns)
        write.writeheader()

        write.writerows(x)

def readOfFile():

    with open(fileBase , "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            x.append(row)