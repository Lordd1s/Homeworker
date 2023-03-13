# a = int(input("Цена тарифа: "))
# b = int(input("Размер тарифа: "))
# c = int(input("Цена за МБ: "))
# d = int(input("Трата в след. месяце: "))
#
#
# while 1 <= a and b and c and d <= 100:
#     if d <= b:
#         cost = a
#         print(cost)
#         break
#     else:
#         cost = a + (d - b) * c
#         print(cost)
#         break


n = int(input())

if n == 1:
    ans = 0
elif n <= 5:
    ans = 2
else:
    ans = n // 5

print(ans)
