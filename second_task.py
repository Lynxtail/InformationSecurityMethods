import os, os.path, pickle

WD = '/home/lynxtail/Scripts/InformationSecurityMethods/'
SCRIPT = 'second_task.py'
HASH_KEEPER = 'second_task.pickle'
FILE = 'second_task'


def xor_for_bytes(b_1:bytes, b_2:bytes):
    return bytes(x ^ y for x, y in zip(b_1, b_2))

def get_hash_sum(item:str=WD + FILE):
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

def check(item:str=WD + FILE):
    # hash_keeper = item.split('/')[-1][-11:] + '.pickle'
    hash_keeper = HASH_KEEPER
    if hash_keeper in os.listdir():
        with open(hash_keeper, 'rb') as f:
            hash_table = pickle.load(f)
        if hash_table == {item : "000000"}:
            print("\tIt's a first run")
            with open(hash_keeper, 'wb') as f:
                hash_table = get_hash_sum()
                pickle.dump(hash_table, f)
            print("\tHash-sum was calculated after first run")
        else:
            hash_table_new = get_hash_sum()
            if hash_table_new == hash_table:
                print("\tNothing changed")
            else:
                with open(hash_keeper, 'wb') as f:
                    pickle.dump(hash_table_new, f)
                print("\tFile has been changed")
    else:
        print("\tHash-sum keeper file was not found:")
        print(f'\tExpected {hash_keeper} not in {os.listdir()}')
        
if __name__ == "__main__":
    check()
    pass