# хотел модифицтровать этот код но не получилось
a = int(input("Введите первое положительное число: "))
b = int(input("Введите второе положительное число: "))


def get_size(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def pie():
    return (a * b) // get_size(a, b)

print(pie())

# вот модифицированный код(который не работает)
# def min_knife(a, b):
#     if a == 0 or b == 0:
#         return 0
#     def peoples(x, y):
#         while x > 0:
#             x, y = y, x % y
#         return x
#     return (a * b) // peoples(a, b)
#
# people = int(input())
# pie = int(input())
# print(min_knife(people, pie))
