from Model import *

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

    

    while True:
        num = int(input("Выберите операцию "))
        if num == 0:
            break
        if num == 1:
           user = input_user()
           phone_dir, key_count = create_user(phone_dir,get_last_key(phone_dir),user)
        if num == 2:
            print_dict (phone_dir)
        if num == 3:
            file_name = input("Выберите имя файла ")
            export_phone_dir(phone_dir, file_name)
        if num == 4:
            searching = input("Введите имя пользователя которого хотите найти ")
            search_user(phone_dir, searching)
        if num == 5:
            searching = input("Введите имя пользователя которого хотите обновить ")
            user_id = search_user(phone_dir, searching)
            print(f"Вы изменяете пользователя {get_printable_user_by_id(phone_dir, user_id)}")
            update_user(phone_dir, user_id)
        if num == 6:
            searching = input("Введите имя пользователя которого хотите удалить ")
            user_id = search_user(phone_dir, searching)
            delete_user(phone_dir, user_id)
        if num == 7:
            file_name = input("Выберите имя файла ")
            key_count = import_phone_dir(phone_dir, file_name, get_last_key(phone_dir))

def print_dict(phone_dir: dict):
    for idc, user in phone_dir.items():
        print(f"{idc}: {user[0]} {user[3]} {user[2]} {user[3]}")
        
def get_printable_user_by_id(phone_dir: dict, user_id: int):
    return " ".join(phone_dir[user_id])