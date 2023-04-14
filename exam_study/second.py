def plus_two(number):
    try:
        result = 2 + int(number)
        print(result)
    except ValueError:
        print("Ожидаемый тип данных — число!")


my_list = [1, 2, 3]

try:
    index = int(input("Введите индекс элемента: "))
    value = my_list[index]
    print("Значение элемента:", value)
except IndexError:
    print("Ошибка: выход за границы массива!")
except ValueError:
    print("Ошибка: введенное значение не является целым числом!")
