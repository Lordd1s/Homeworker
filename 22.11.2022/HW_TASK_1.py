import requests

s = input("Введите ссылку: ")
prefix = input("Название картинки: ")
num = int(input("Колиество картинок: "))


for i in range(1, num+1):
    result = requests.get(url=s)
    with open(f"img/{prefix}{i}.jpg", "wb") as downloaded:
        downloaded.write(result.content)

# url = input("Введите ссылку")  # "https://picsum.photos/320/240/"
# prefix = input()  # apple
# count = int(input())  # 10
# for i in range(1, count+1):
#     response = requests.get(url=url, headers=headers)
#     with open(f"img/{prefix}{i}.jpg", "wb") as opened_file:  # f"img/apple1.jpg"
#         opened_file.write(response.content)