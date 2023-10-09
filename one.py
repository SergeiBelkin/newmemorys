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
    x.clear

def readOfFile():

    with open(fileBase , "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            x.append(row)
    

def printList ():

    readOfFile()
    for note in x:
        print(note["ID"],note["DATE"])
    x.clear()

def redNote (number):

    readOfFile()
    for note in x:
        if note["ID"] == str(number):
            index = x.index(note)
            # print(index)
            print(note)
            del x[index]
    print(x)
    

def printNote (number):

    readOfFile()
    for note in x:
        if note["ID"] == str(number):

            print(note)
    x.clear()


def main():

    while True:
        print('Выберите действие:')
        print('1. Вывести все заметки')
        print('2. Вывести конкретную заметку')
        print('3. Добавить новую заметку')
        print('4. Редактировать заметку')
        print('5. Удалить заметку')
        print('6. Выход')

        numChoice = input()
        if numChoice == "1":
            printList()
            

        elif numChoice == "2":
            num = input("введите номер заметки: ")
            printNote(num)

        elif numChoice == "3":
            writer()

        elif numChoice == "4":
            num = input("введите номер заметки: ")
            redNote(num)
            writer()

        elif numChoice == "5":
            num = input("введите номер заметки: ")
            redNote(num)
            writeOfFile()

        elif numChoice == "6":
            break

        else: print("не допустимая команда")

main()
# writer()
# redNote(0)