while True:
    def get_sum():
        print("Сумма всех чисел")
        val1 = int(input("Введите первое число: "))
        val2 = int(input("Введите второе число: "))
        vals = int((val2 * (val2 + 1)) / 2 - ((val1-1) * ((val1-1) + 1)) / 2)

        if val1 == val2:
            print(val1)
        elif val1 > val2:
            print("Введите первое значение МЕНЬШЕ чем второй!")
            get_sum()
        else:
            print(f"Результат: {vals}")

    get_sum()

    break

exit = input("Введите чего нибудь чтобы выйти: ")


