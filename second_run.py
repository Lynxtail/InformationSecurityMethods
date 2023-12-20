import os, pickle

WD = '/home/lynxtail/Scripts/InformationSecurityMethods/'
SCRIPT = 'second_task.py'
FILE = 'second_task'
HASH_KEEPER = 'second_task.pickle'

## сборка экзешника
# os.system(f"pyinstaller --onefile --noconfirm {WD + SCRIPT}")
# os.system(f"mv {WD}dist/second_task {WD}/")

# os.system(f"rm -r {WD}dist")
# os.system(f"rm -r {WD}build")
# os.system(f"rm {WD + FILE}.spec")

# os.system(f"rm {WD + FILE}")
# os.system(f"rm {WD + FILE}.pickle")

## запуск
# os.system(WD + FILE)

# # создание хранителя хэша
# with open(HASH_KEEPER, 'wb') as f:
#     pickle.dump({WD + FILE:"000000"}, f)

# # содержимое хранителя хэша
# with open(HASH_KEEPER, 'rb') as f:
#     ans = pickle.load(f)
#     print(f'\tHash sum:\n\t\t{ans}')
