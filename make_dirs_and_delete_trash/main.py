import os
import json
import random

# chars = "CHeiy"
# rand_char = random.choice(chars)
# dir_path = f"e://Homeworker/make_dirs_and_delete_trash/temp_{rand_char}/"
# for i in rand_char:
#     print(i)
#     dict1 = {f"key_{i}": f"value_{i}"}
#     os.makedirs(dir_path, exist_ok=True)
#     with open(os.path.join(dir_path, "my_cop.json"), "w") as file:
#         json.dump(dict1, file)
#     with open(os.path.join(dir_path, "not_my_cop.json"), "w") as trash_file:
#         json.dump(dict1, trash_file)

top = 'parent_dir'
keep_file = 'my_cop.json'

for root, dirs, files, in os.walk(top, topdown=True):
    for name in files:
        if name != keep_file:
            os.remove(os.path.join(root, name))
            print('done')
