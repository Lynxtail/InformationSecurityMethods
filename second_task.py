import os, os.path, pickle

ignore_list = ('main.py', 'Zadania_magistram.txt', '.venv', os.path.split(os.getcwd())[1] + '.pickle')

def xor_for_bytes(b_1:bytes, b_2:bytes):
    return bytes(x ^ y for x, y in zip(b_1, b_2))

def get_hash_sum(item:str=__file__):
    tmp_dict = dict()
    file_length = os.path.getsize(item)
    with open(item, 'rb') as f:
        hash_sum = f.read(2)
        for _ in range(f.tell(), file_length // 2):
            hash_sum = xor_for_bytes(hash_sum, f.read(2))
        if f.tell() < file_length:
            d = b'0'*(file_length - f.tell())
            hash_sum = xor_for_bytes(hash_sum, f.read() + d)
    tmp_dict[item] = hash_sum
    return tmp_dict

def check(item:str=__file__):
    hash_keeper = item.split('/')[-1][:-3] + '.pickle'
    if hash_keeper in os.listdir():
        with open(hash_keeper, 'rb') as f:
            hash_table = pickle.load(f)
        if hash_table == {item : "000000"}:
            with open(hash_keeper, 'wb') as f:
                hash_table = get_hash_sum()
                pickle.dump(hash_table, f)
            print("Hash-sum was calculated after first run")
        else:
            hash_table_new = get_hash_sum()
            if hash_table_new == hash_table:
                print("Nothing changed")
            else:
                with open(hash_keeper, 'wb') as f:
                    pickle.dump(hash_table_new, f)
                print("File has been changed")
    else:
        print("Hash-sum keeper file was not found")
        print(hash_keeper)
        print(os.listdir())
        
if __name__ == "__main__":
    # with open(__file__[:-3] + ".pickle", 'wb') as f:
    #     pickle.dump({__file__:"000000"}, f)
    check()