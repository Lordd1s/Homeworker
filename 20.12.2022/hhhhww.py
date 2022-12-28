with open("hw\Data0.txt", "r", encoding='utf-8') as text_file:
    re = text_file.read().split(sep='\n')
idx1 = [0]
idx2 = [2]
idx3 = [3]

first = [re[x] for x in idx1]
sec = [re[y] for y in idx2]
third = [re[z] for z in idx3]

with open('hw\e1.txt', "w") as file_1:
    print(first, file=file_1)
with open('hw\s2.txt', "w") as file_2:
    print(sec, file=file_2)
with open('hw\h3.txt', "w") as file_3:
    print(third, file=file_3)
