# 8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
#   Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
#   Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
#   Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
#   Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
#   Берем первое совпадение по фамилии.
#   Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
#   Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

from os.path import join, abspath, dirname

def menu ():
    print("Введите 1 для ввода пользователя")
    print("Введите 2 для распечатки вашего справочника")
    print("Введите 3 для экспорта")
    print("Введите 4 для поиска")
    print("Введите 5 для изменения данных")
    print("Введите 6 для удаления пользователя")
    print("Введите 7 для импорта")

    phone_dir = {1: ['Иванов',   'Иван',  '+7(xxx)xxx-xx-xx', 'desription_Иванов'], 
                2: ['Петров',   'Петр',  '+7(---)xxx-xx-xx', 'desription_Петров'], 
                3: ['Соколов',  'Илья',  '+7(---)---------', 'desription_Соколов'], 
                4: ['Павельев', 'Андрей','+7(***)***-**-**', 'desription_Павельев'], 
                5: ['Пешехов',  'Антон', '+7++++++++++',     'desription_Пешехов'], 
                6: ['Сааков',   'Илья',  '+7(+++)+++-++-++', 'desription_Сааков'], 
    }

    key_count = len(phone_dir)
    

    while True:
        num = int(input("Выберите операцию "))
        if num == 0:
            break
        if num == 1:
           user = input_user()
           phone_dir, key_count = create_user(phone_dir,key_count,user)
        if num == 2:
            print (phone_dir)
        if num == 3:
            file_name = input("Выберите имя файла ")
            export_phone_dir(phone_dir, file_name)
        if num == 4:
            searching = input("Введите имя пользователя которого хотите найти ")
            search_user(phone_dir, searching)
        if num == 5:
            searching = input("Введите имя пользователя которого хотите обновить ")
            update_user(phone_dir, searching)
        if num == 6:
            searching = input("Введите имя пользователя которого хотите удалить ")
            delete_user(phone_dir, searching)
        if num == 7:
            file_name = input("Выберите имя файла ")
            key_count = import_phone_dir(phone_dir, file_name, key_count)

def input_user()->list:
    user=[]
    user.append(input("Input ferst name "))
    user.append(input("Input second name "))
    user.append(input("Input phone "))
    user.append(input("Input discription "))
    return user

def create_user (phone_dir_local: dict, idc: int,  user:list)->dict:
    idc += 1
    phone_dir_local[idc] = user
    return phone_dir_local, idc

def search_user(phone_dir: dict, searching: str) -> int:
    for idc, user in phone_dir.items():
        if user[0].startswith(searching):
            return idc
    print("Пользователь не найден")

def delete_user(phone_dir: dict, searching: str):
    user_id = search_user(phone_dir, searching)
    confirmation = input(f"Вы уверены что хотит удалить пользователя? {get_printable_user_by_id(phone_dir, user_id)}\nНапишите yes если необходимо выполнить удаление ")
    if user_id and confirmation == 'yes': del phone_dir[user_id]

def update_user(phone_dir: dict, searching: str):
    user_id = search_user(phone_dir, searching)
    print(f"Вы изменяете пользователя {get_printable_user_by_id(phone_dir, user_id)}")
    if user_id:
        user = input_user()
        phone_dir[user_id] = user
        print("Пользователь изменен!")

def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name+'.txt')
    with open(full_name, mode='w', encoding='utf-8') as file:
        for idc, user in phone_dir.items():
            file.write(f"{idc}#{user[0]}#{user[1]}#{user[2]}#{user[3]}\n")

def import_phone_dir(phone_dir: dict, file_name: str, idc: int):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name+'.txt')
    with open(full_name, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            idc += 1
            phone_dir[idc] = line.strip().split("#")[1:]
    return idc

def print_dict(phone_dir: dict):
    for idc, user in phone_dir.items():
        print(f"{idc}: {user[0]} {user[3]} {user[2]} {user[3]}")
        
def get_printable_user_by_id(phone_dir: dict, user_id: int):
    return " ".join(phone_dir[user_id])


menu ()