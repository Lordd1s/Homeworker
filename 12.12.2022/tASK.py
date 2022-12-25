import random
import math

# TODO 1
# a = int(input("Введите первое положительное число: "))
# b = int(input("Введите второе положительное число: "))
#
#
# def get_size():
#     global b
#     global a
#     while b > 0:
#         a, b = b, a % b
#     return a
#
#
# def pie():
#     return (a * b) // get_size()
#
# print(pie())

# TODO 2

# n = int(input("Введите число: "))
# sum_of_factorials = 1
# current_factorial = 1
# for i in range(2, n + 1):
#     current_factorial = current_factorial * i
#     sum_of_factorials = sum_of_factorials + current_factorial
# print(sum_of_factorials)

# TODO 3

# n = int(input("Введите число: "))
#
# for i in range(1, n + 1):
#     for x in range(1, i + 1):
#         print(x, end='')
#     print("\n")

# TODO 4
#
# n = int(input("Число карт: "))
# sum2 = 0
# for i in range(1, n+1):
#     sum2+= i
# for i in range(n - 1):
#     sum2 -= int(input("Введите чиcло: "))
# print(sum2)

# TODO 5


# n = int(input("Число: "))
# sum1 = 1
# for i in range(1, n+1):
#     if n > sum1:
#         sum1 = i ** 2
#         i += 1
#         print(sum1)
#

# TODO 6

# n = int(input("""Введите "n" число: """))
# list1 = [random.randint(1, 100) for i in range(n)]
# print(list1)
# list2 = [i % 2 == 0 for i in list1]
# list3 = [i % 2 != 0 for i in list1]
# if list2 > list3:
#     print("Четные больше ")
# else:
#     print("Нечетные больше")

# TODO 7
# n = int(input("Введите число ряд ФИБОНАЧЧИ: "))
#
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(n):
#     print(f"FIbonacci number: {i + 1} = ", fibonacci(i))

# TODO 8

# n = int(input('Введите n число: '))
#
#
# def count(int: n) -> bool:
#     return n % 2 == 0:

# print(count(n))

# TODO 9

# def cv():
#     name = input("Your name: ")
#     surname = input("Your surname: ")
#     pos = input("Your position: ")
#     edc = input("Your education: ")
#     xp = input("Your experience: ")
#     print(name, surname)
#     print("POSITION")
#     print(pos)
#     print('EDUCATION')
#     print(edc)
#     print('EXPERIENCE')
#     print(xp)
#
#
# cv()

# TODO 10

# print("Hello there!")
#
# num = int(input("Input 'First' value: "))
# action = input("Choose the action: +, -, *, /, root, degree, Fibonnacci, ! : ")
# factorial = 1
# if action == "+":
#     d = float(input("Input 'Second' value: "))
#     print("Equal: ", num + d)
# elif action == '-':
#     d = float(input("Input 'Second' value: "))
#     print("Equal: ", num - d)
# elif action == "*":
#     d = float(input("Input 'Second' value: "))
#     print("Equal: ", num * d)
# elif action == "/":
#     d = float(input("Input 'Second' value: "))
#     print("Equal: ", num / d)
# elif action == "root":
#     print('Equal: ', math.sqrt(num))
# elif action == "degree":
#     print("Equal: ", num ** 2)
# elif action == "Fibonnacci":
#     print("\n")
#
#
#     def fib(c):
#         if c <= 1:
#             return c
#         else:
#             return fib(c - 1) + fib(c - 2)
#
#
#     for i in range(num):
#         print(f"Fibonacci number {i} = ", fib(i))
# elif action == "!":
#     factorial = 1
#
#     for i in range(2, num + 1):
#         factorial *= i
#
#     print("Factorial equal: ", factorial)

# TODO 11

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def play():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])
    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])
    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


def steps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


def result():
    win_1 = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win_1 = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win_1 = "O"

    return win_1


game_over = False
player1 = True

while not game_over:
    play()
    if player1:
        symbol = "X"
        step = int(input("PLAYER_1, Your turn: "))
    else:
        symbol = "O"
        step = int(input("PLAYER_2, Your turn: "))

    steps(step, symbol)
    win = result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not player1

play()
print("You win", win)
