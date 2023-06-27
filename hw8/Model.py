from os.path import join, abspath, dirname


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

def delete_user(phone_dir: dict, user_id: str):
    del phone_dir[user_id]

def update_user(phone_dir: dict, user_id: str):
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

def get_last_key(phone_dir: dict):
    return list(phone_dir.keys())[-1]