input('Print anything for start program or press "Enter": ')

list1 = []
with open("data.txt", "r") as txt_file:
    data = txt_file.read().split('\n')
for i in data:
    list1.append(int(i))
list1.sort(reverse=True)
list2 = []
for j in list1:
    if j % 2 == 0:
        continue
    list2.append(j)
list3 = set(list1)
print(list1)
print(list3)
print(list2)

with open("new.txt", "w") as file:
    file.write(str(f"{list1}\n{list2}\n{list3}"))

input("Print anything for quit or press 'Enter': ")
print("BYE")
input("")

