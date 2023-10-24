# Задание 1. Ревизор диска
# Разработать программу, работающую по принципу «ревизора диска» и контролирующую целостность данных в заданном каталоге.

# Программа должна уметь:

# 1. подсчитать ХЭШ-сумму файлов (для каждого файла отдельно) в заданном каталоге с обходом всех подкаталогов. 
# Сохранить эти сведения для дальнейшей проверки целостности.

# 2. проверить целостность каталога с указанием на изменившиеся файлы.

# Алгоритм подсчета ХЭШ-суммы. 
# Файл читается как бинарный поток. Поток разбивается на 16-битные отрезки, которые складываются по XOR. 
# Если в последнем отрезке не хватает бит до 16, недостающее дополняется нулями.
# Хэш-сумма д.б. сохранена в файле, находящемся в контролируемом каталоге, при этом сам файл не является объектом контроля.


import os, os.path, pickle

ignore_list = ('main.py', 'Zadania_magistram.txt', '.venv', os.path.split(os.getcwd())[1] + '.pickle')

def xor_for_bytes(b_1:bytes, b_2:bytes):
    return bytes(x ^ y for x, y in zip(b_1, b_2))

def get_hash_sum(tmp_dict:dict(), wd:str=os.getcwd()):
    for item in os.listdir(wd):
        if item not in ignore_list:
            tmp_item = os.path.join(wd, item)
            if os.path.isfile(tmp_item):
                file_length = os.path.getsize(tmp_item)
                with open(tmp_item, 'rb') as f:
                    hash_sum = f.read(2)
                    for _ in range(f.tell(), file_length // 2):
                        hash_sum = xor_for_bytes(hash_sum, f.read(2))
                    if f.tell() < file_length:
                        d = b'0'*(file_length - f.tell())
                        hash_sum = xor_for_bytes(hash_sum, f.read() + d)
                tmp_dict[tmp_item] = hash_sum
            else: 
                get_hash_sum(tmp_dict, tmp_item)

def check_hash_sum(wd:str=os.getcwd()):
    with open(os.path.split(os.getcwd())[1] + '.pickle', 'rb') as f:
        hash_table_old = pickle.load(f)
    hash_table_new = dict()
    get_hash_sum(hash_table_new, wd)

    flag = True
    new_keys = set(hash_table_new.keys())
    old_keys = set(hash_table_old.keys())

    for key in new_keys.difference(old_keys):
        print(f'{key} was created')
        flag = False
    
    for key in old_keys.difference(new_keys):
        print(f'{key} was deleted')
        flag = False

    for key in new_keys.intersection(old_keys):
        if hash_table_old[key] != hash_table_new[key]:
            print(f'{key} was edited')
            flag = False
            
    if flag: print(f'Nothing happened')

    with open(os.path.split(os.getcwd())[1] + '.pickle', 'wb') as f:
        pickle.dump(hash_table_new, f)

def init(wd:str=os.getcwd()):
    hash_table = dict()
    get_hash_sum(hash_table, wd)
    with open(os.path.split(os.getcwd())[1] + '.pickle', 'wb') as f:
        pickle.dump(hash_table, f)


# при первом запуске использовать только init()
# init()

# при последующих -- только check_hash_sum()
# check_hash_sum()
