# TODO FUNCTIONS #######################################
# def even_bigger_or_not(array: list[int]) -> str:
#     even = [x for x in array if x % 2 == 0]
#     odd = [x for x in array if x % 2 != 0]
#     if len(even) > len(odd):
#         return "YES"
#     else:
#         return "NO"
#
#
# print(even_bigger_or_not([4, 16, 19, 31, 2]))


# def sum_of_dg(arr: list[list[int]]) -> int:
#     first_dg = 0
#     for i in range(len(arr)):
#         first_dg += arr[i][i]
#     return first_dg
#
#
# print(sum_of_dg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# def get_info():
#     name = input("Your name: ")
#     age = int(input("Your age: "))
#     study = input("The place where you studied: ")
#     work = input("The place where you work(-ed): ")
#     exp = input("How many did you work: ")
#     return name, age, study, work, exp
#
#
# def show_info(name, age, study, work, exp):
#     print(name)
#     print(age)
#     print(study)
#     print(work)
#     print(exp)
#
#
# if __name__ == "__main__":
#     name, age, study, work, exp = get_info()
#     show_info(name=name, age=age, study=study, work=work, exp=exp)


# n = int(input("Enter the number to Fibbonacci number: "))
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(n):
#     print(f"FIbonacci number: {i + 1} = ", fibonacci(i + 1))


# def two_two(n: int) -> bool:
#     if n <= 0:
#         return False
#     while n > 1:
#         if n % 2 != 0:
#             return False
#         n = n // 2
#     return True
#
# print(two_two(n))


# import math
#
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# num = input("Input 'First' value: ")
# while not num.isdigit():
#     num = input("Please input a valid number: ")
# num = int(num)
#
# actions = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x - y,
#     '*': lambda x, y: x * y,
#     '/': lambda x, y: x / y if y != 0 else None,
#     'root': lambda x, y: math.sqrt(x),
#     'degree': lambda x, y: x ** 2,
#     'Fibonacci': lambda x, y: [fibonacci(i) for i in range(x)],
#     '!': lambda x, y: math.factorial(x)
# }
#
# action = input("Choose the action: +, -, *, /, root, degree, Fibonacci, ! : ")
# while action not in actions:
#     action = input("Please choose a valid action: ")
#
# if action != 'Fibonacci':
#     num2 = input("Input 'Second' value: ")
#     while not num2.isdigit():
#         num2 = input("Please input a valid number: ")
#     num2 = float(num2)
#     result = actions[action](num, num2)
# else:
#     result = actions[action](num, None)
#
# if result is None:
#     print("Error: Division by zero")
# else:
#     print("Result: ", result)


# maps = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 9]
#
# victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
#              [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#
# def play():
#     for i in range(0, 9, 3):
#         print(maps[i:i+3])
#
#
# def steps(step, symbol):
#     maps[maps.index(step)] = symbol
#
#
# def check_win(symbol):
#     for victory in victories:
#         if all(maps[i] == symbol for i in victory):
#             return True
#     return False
#
#
# game_over = False
# player1 = True
#
# while not game_over:
#     play()
#     if player1:
#         symbol = "X"
#         step = int(input("PLAYER_1, Your turn: "))
#     else:
#         symbol = "O"
#         step = int(input("PLAYER_2, Your turn: "))
#
#     steps(step, symbol)
#     if check_win(symbol):
#         game_over = True
#         print(f"{symbol} wins!")
#     elif all(isinstance(i, str) for i in maps):
#         game_over = True
#         print("It's a tie!")
#     else:
#         player1 = not player1
#
# play()
