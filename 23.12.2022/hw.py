import pathlib
from pathlib import Path

text_path = pathlib.Path.cwd()
del_list = ['for_delete.txt']

for file_name in del_list:
    file_path = Path(text_path, 'for_scan', file_name)
    if Path.exists(file_path):
        Path.unlink(file_path)
        print('done' + str(file_path))
    else:
        print('error' + str(file_path))

for file_name_2 in del_list:
    file_path = Path(text_path, 'for_scan', 'for_delete', file_name_2)
    if Path.exists(file_path):
        Path.unlink(file_path)
        print('done' + str(file_path))
    else:
        print('error' + str(file_path))

for file_name_3 in del_list:
    file_path = Path(text_path, 'for_scan', 'for_scan', file_name_3)
    if Path.exists(file_path):
        Path.unlink(file_path)
        print('done' + str(file_path))
    else:
        print('error' + str(file_path))

for file_name_4 in del_list:
    file_path = Path(text_path, 'for_scan', 'for_scan', 'for_delete', file_name_4)
    if Path.exists(file_path):
        Path.unlink(file_path)
        print('done' + str(file_path))
    else:
        print('error' + str(file_path))