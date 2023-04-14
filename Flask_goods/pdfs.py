import json
import datetime


# TODO set #############################################
# def superset(set1: set, set2: set):
#     if set1 == set2:
#         print("Множества равны")
#     elif set1.issuperset(set2):
#         print(f"Объект {set1} является чистым супермножеством")
#     else:
#         print("Супермножество не обнаружено")
#

# dictionary = {}
#
#
# def add_word():
#     word = input("Введите слово на английском языке: ")
#     translation = input("Введите перевод слова на французский язык: ")
#     dictionary[word] = translation
#     print("Слово добавлено в словарь")
#
#
# def remove_word():
#     word = input("Введите слово на английском языке: ")
#     if word in dictionary:
#         del dictionary[word]
#         print("Слово удалено из словаря")
#     else:
#         print("Слово не найдено в словаре")
#
#
# def search_word():
#     word = input("Введите слово на английском языке: ")
#     if word in dictionary:
#         print(f"{word} - {dictionary[word]}")
#     else:
#         print("Слово не найдено в словаре")
#
#
# def replace_word():
#     word = input("Введите слово на английском языке: ")
#     if word in dictionary:
#         translation = input("Введите новый перевод слова на французский язык: ")
#         dictionary[word] = translation
#         print("Перевод слова изменен")
#     else:
#         print("Слово не найдено в словаре")
#
#
# while True:
#     print(
#         "Выберите действие:\n1 - добавить слово в словарь\n2 - удалить слово из словаря\n3 - найти перевод слова\n4 - изменить перевод слова\n5 - выйти из программы")
#     choice = input()
#     if choice == "1":
#         add_word()
#     elif choice == "2":
#         remove_word()
#     elif choice == "3":
#         search_word()
#     elif choice == "4":
#         replace_word()
#     elif choice == "5":
#         break
#     else:
#         print("Неправильный выбор")


# def set_gen(numbers):
#     result_set = set()
#     for number in numbers:
#         count = numbers.count(number)
#         if count > 1:
#             number_string = str(number) * count
#             result_set.add(number_string)
#         else:
#             result_set.add(number)
#     return result_set
# TODO set #############################################


# TODO dict ############################################
# def biggest_dict(**kwargs):
#     my_dict = {'first_one': 'we can do it'}
#     for key, value in kwargs.items():
#         my_dict[key] = value
#     return my_dict


# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
#
# first_key = list(my_dict.keys())[0]
# last_key = list(my_dict.keys())[-1]
# my_dict[last_key], my_dict[first_key] = my_dict[first_key], my_dict[last_key]
#
# my_dict.pop(list(my_dict.keys())[1])
#
# my_dict.update({'new_key': 'new_value'})
#
# print(my_dict)


# countries = {}
#
#
# def add_country(country, capital):
#     countries[country] = capital
#
#
# def delete_country(country):
#     if country in countries:
#         del countries[country]
#     else:
#         print(f"{country} не найдена в словаре")
#
#
# def find_country(country):
#     if country in countries:
#         print(f"{country}: {countries[country]}")
#     else:
#         print(f"{country} не найдена в словаре")
#
#
# def edit_country(country, capital):
#     if country in countries:
#         countries[country] = capital
#     else:
#         print(f"{country} не найдена в словаре")
#
#
# def save_countries(file_path):
#     with open(file_path, 'w') as f:
#         json.dump(countries, f)
#
#
# def load_countries(file_path):
#     global countries
#     with open(file_path, 'r') as f:
#         countries = json.load(f)
#
#
# add_country("Россия", "Москва")
# add_country("США", "Вашингтон")
# add_country("Китай", "Пекин")
# add_country("Франция", "Париж")
# add_country("Германия", "Берлин")
#
# delete_country("Китай")
#
# find_country("Россия")
#
# edit_country("США", "Нью-Йорк")
#
# save_countries("countries.json")
#
# load_countries("countries.json")
#
# print(countries)
# TODO dict ############################################


# TODO time ############################################
# print("date:", datetime.datetime.now().isocalendar()[1])


# year = 2015
# week_number = 50
# start_date = datetime.date(year, 1, 1)
# days_to_go = 7 - start_date.weekday()
# start_date = start_date + datetime.timedelta(days_to_go)
# start_date = start_date + datetime.timedelta(weeks=week_number-1)
#
# print(start_date)


# year = 2023
#
# start_date = datetime.date(year, 1, 1)
#
# end_date = datetime.date(year, 12, 31)
#
# for i in range((end_date - start_date).days + 1):
#     date = start_date + datetime.timedelta(i)
#     if date.weekday() == 6:  # 6 - это воскресенье
#         print(date)


def addYears(d, years):
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        # если исходная дата - 29 февраля и год после добавления не является високосным,
        # то возвращаем 28 февраля вместо 1 марта
        return d.replace(year=d.year + years, day=28)


print(addYears(datetime.date(2015, 1, 1), -1))  # 2014-01-01
print(addYears(datetime.date(2015, 1, 1), 0))   # 2015-01-01s