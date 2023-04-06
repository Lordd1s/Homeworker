# def prices(arr: list[int]) -> int:
#     sorted_list = sorted(arr, reverse=True)
#     mid = len(sorted_list) // 2
#     return (sorted_list[:mid][0] + sorted_list[:mid][1]) + (sorted_list[mid:][0] + sorted_list[mid:][1])
from typing import Tuple


# arrayy = [1, 3, 4, 5, 5, 7]
# print(prices(arrayy))


def find_closest_pair(lst: list[int]) -> tuple[int, int]:
    sorted_lst = sorted(lst)
    min_diff = sorted_lst[1] - sorted_lst[0]
    min_pair = (sorted_lst[0], sorted_lst[1])

    for i in range(1, len(sorted_lst) - 1):
        diff = sorted_lst[i+1] - sorted_lst[i]
        if diff < min_diff:
            min_diff = diff
            min_pair = (sorted_lst[i], sorted_lst[i+1])

    return min_pair


def strings(lst: list[str]) -> str:
    sorted_l = sorted(lst, key=len)
    for i in sorted_l:
        res = len(sorted_l[-1]) - len(i)
        return "*" * res + i


# l = ['da', 'net', 'poka']
# strings(l)


def absolute(array: list[int], num: int) -> list[int]:
    plus = sum(x for x in array if x > 0)
    negative = sum(x for x in array if x < 0)
    res = abs(plus - negative)
    if res == num:
        return array
    elif res < num:
        array.append(num - res)
        return array
    elif res > num:
        print("""sum of elements with positive values and the modulus of the sum of elements with negative values is unequal""")
        result = (res - num) - sum(array)
        array.pop(result)
        return array


# print(absolute([-3,-2,1,2,3,4], 9))


def encrypt_caesar(text, shift):
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                result += chr((ord(text[i]) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(text[i]) + shift - 97) % 26 + 97)
        else:
            result += text[i]
    return result


# print(encrypt_caesar("hello world", 5))


fruits_1 = ("apple", "banana", "orange", "grape", "pineapple")

fruit = input("Введите название фрукта: ")

count = fruits_1.count(fruit)

print(f"Количество вхождений фрукта {fruit}: {count}")


fruits_2 = ('apple', 'banana', 'mango', 'strawberry', 'kiwi', 'pineapple', 'banana-mango', 'strawberry-banana')

name = input("Введите название фрукта: ")

count_exact = fruits_2.count(name)
count_part = 0

for fruit in fruits_2:
    if name in fruit:
        count_part += 1

print("Количество точных вхождений: ", count_exact)
print("Количество вхождений как часть слова: ", count_part)


car_brands = ("Toyota", "Ford", "Chevrolet", "Honda", "Ford", "Tesla")
brand_to_replace = input("Введите название производителя: ")
replacement_word = input("Введите слово для замены: ")
new_car_brands = tuple(replacement_word if brand == brand_to_replace else brand for brand in car_brands)

print("Новый кортеж с замененными элементами:")
print(new_car_brands)
