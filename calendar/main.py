
def list():#1
    return dict# возрашает список всех записей в БД
def add():#2
    pass # добовляет запись в БД
def create():#3
    pass # редактирует запись в БД
def statusTRUE():#4
    pass #изменят сатус задачи TRUE FALSE
def statusFALSE():#5
    pass#изменят сатус задачи FALSE TRUE


#_____________________________________________________________________________________________________

def whatchdog(in_data):
    if in_data == "1":
        return list()
    elif in_data == "3":
        return add()
    elif in_data == "4":
        # print("ОК")
        return create()
    elif in_data == "5":
        # print("ОК")
        return statusTRUE()
    elif in_data == "6":
        return statusFALSE()
    else:
        print ("Повтори")
        return True

#___________________________________________________________________________

def main():

    print(""" 
    Ежедневник выбирити задачу:
    1. Вывесте список задач
    2. Добавить Задачу
    3. Отредеактировать задачу
    4.Завершить задачу
    5.Начать задачу сначала
    6.Выход   
    """)
    while True:
        s= whatchdog(input("Введиет число:"))
        if s == False:
           break
        else:
           print(s)



if(__name__=="__main__"):
    main()