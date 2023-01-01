dict1 = {"Kazakhstan": "Astana", "Ukraine": "Kiev", "Germany": "Berlin"}
dict1["England"] = "London"
print(dict1)
dict1.pop("Germany")
print(dict1)
print(dict1["Kazakhstan"])
with open("dict1.txt", 'w') as file:
    file.write(str(dict1))
with open("dict1.txt", "r") as file_read:
    x = file_read.read()
print(x)

dict2 = {'Oliver Tree': 'Miss you', 'The Weeknd': 'The Highlights'}
dict2['Linkin Park'] = 'In The End'
print(dict2)
dict2.pop('The Weeknd')
print(dict2)
print(dict2['Linkin Park'])
with open("dict2.txt", "w") as file_2:
    file_2.write(str(dict2))
with open("dict2.txt", "r") as file_2_read:
    r = file_2_read.read()
print(r)