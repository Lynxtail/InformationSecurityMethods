import os, json, sys

WD = '/home/lynxtail/Scripts/InformationSecurityMethods/'
SCRIPT = 'second_task.py'
FILE = SCRIPT[:-3] + '.exe'
HASH_KEEPER = 'second_task.json'

# os.system(f"rm {FILE}")
# os.system(f"rm {FILE[:-4]}.json")

# сборка экзешника
os.system(f"pyinstaller --onefile --distpath . --noconfirm -n {SCRIPT[:-3]}'.exe' {WD + SCRIPT}")
os.system(f"rm -r {WD}build")
os.system(f"rm {FILE}.spec")


## создание хранителя хэша
# with open(HASH_KEEPER, 'w') as f:
#     f.write(json.dumps({f'./{FILE}' : '000000'}, indent=4, ensure_ascii=False))


## содержимое хранителя хэша
# with open(HASH_KEEPER, 'r') as f:
#     ans = json.load(f)
#     print(f'\tHash sum:\n\t\t{ans}')
