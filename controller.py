import db, gui 
from datetime import datetime 

def button_click():
    a = gui.Choice()
    if (a == 1):

        id = gui.id_input()
        name = gui.Name_input()
        print("Выберите какой формат Вы хотите использовать: txt (1), csv (2), gson (3):")
        flag = int(input())
        while ((flag < 1) & (flag > 3)):
            flag = int(input())
            print("Вы ввели некоректные данные, пожалуйста, попробуйте снова: ")
        current_datetime = str(datetime.now())
        if flag == 1:
            print("В данной версии приложения данный формат не доступен")
            #db.Saving_json(id, name, description, current_datetime)
        elif flag == 2:
            print 
            #db.Saving_csv(id, name, description, current_datetime)
        else: 
            db.Saving_json(id, name, description, current_datetime) 
    elif (a == 2):
        print("Выберите какой формат Вы хотите использовать: txt (1), csv (2), gson (3):")
        flag = int(input())
        while ((flag < 1) & (flag > 3)):
            flag= int(input())
            print("Вы ввели некоректные данные, пожалуйста, попробуйте снова: ")
            if flag == 1:
                print("В данной версии приложения данный формат не доступен")
                #print(db.get_base())
            elif flag == 2: 
                print("В данной версии приожения данный формат не доступен")
                #db.get_base_csv()
            elif flag == 3:
                db.get_base_json_names()
            else:
                print("Вы ввели некорекктные данные")
    elif(a == 3):
        print("Введите id заметки, которую Вы хотите прочитать")
        id_found = int(input())
        db.get_base_json_descriptions(id_found)
    elif(a == 4):
        print("Введите id заметки, котррую Вы хотите редактировать")
        id_found = int(input())
        db.editing_json(id_found)
    elif(a == 5):
        print("Введите id заметки, которую хотите удалить")
        id_found = int(input())
        db.deleting_json(id_found)