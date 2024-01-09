import os, os.path, json, sys

WD = '/home/lynxtail/Scripts/InformationSecurityMethods/'
HASH_KEEPER = 'second_task.json'
FILE = sys.argv[0]


def xor_for_bytes(b_1:bytes, b_2:bytes):
    return bytes(x ^ y for x, y in zip(b_1, b_2))

def get_hash_sum(item:str=FILE):
    tmp_dict = dict()
    file_length = os.path.getsize(item)
    with open(item, 'rb') as f:
        hash_sum = f.read(2)
        for _ in range(f.tell(), file_length // 2):
            hash_sum = xor_for_bytes(hash_sum, f.read(2).ljust(2, b'\x00'))
    hash_sum = ''.join(f'{item:02x}' for item in hash_sum)
    tmp_dict[item] = hash_sum
    return hash_sum

def check(item:str=FILE):
    hash_keeper = HASH_KEEPER
    if hash_keeper in os.listdir():
        with open(hash_keeper, 'r') as f:
            hash_sum = list(json.load(f).values())[-1]
        if hash_sum == '000000':
            print("\tIt's a first run")
            with open(hash_keeper, 'w') as f:
                hash_sum = get_hash_sum()
                f.write(json.dumps({item : hash_sum}, indent=4, ensure_ascii=False))
            print("\tHash-sum was calculated after first run")
        else:
            hash_sum_new = get_hash_sum()
            if hash_sum_new == hash_sum:
                print("\tNothing changed")
            else:
                with open(hash_keeper, 'w') as f:
                    f.write(json.dumps({item : hash_sum_new}, indent=4, ensure_ascii=False))
                print("\tFile has been changed")
    else:
        print("\tHash-sum keeper file was not found:")
        print(f'\tExpected {hash_keeper} not in {os.listdir()}')
        
if __name__ == "__main__":
    print('_'*50)
    check()
    print()