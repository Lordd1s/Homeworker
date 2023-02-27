import os
import json
import random

# for i in range(5):
#     dict1 = {f"key_{i}": f"value_{i}"}
#     dict2 = {f"key_{i}": f"value_{i}"}
#     dir_path = f"e://Homeworker/make_dirs_and_delete_trash/temp_{i}/"
#     os.makedirs(dir_path, exist_ok=True)
#     with open(os.path.join(dir_path, "my_cop.json"), "w") as file:
#         json.dump(dict1, file)
#     with open(os.path.join(dir_path, "not_my_cop.json"), "w") as trash_file:
#         json.dump(dict2, trash_file)


for i in range(5):
    os.remove(f"e://Homeworker/make_dirs_and_delete_trash/temp_{i}/not_my_cop.json")
    print("done")
