login = str(input("Enter login: "))
password = str(input("Enter password: "))

if login == 'user' and password == 'qwerty':
    print("Authentication completed")
else:
    print("Invalid Login or Password")


tg = float(input("Enter value KZT: "))
print("Choose currency:")
translate = input("[1] USD \n[2] EUR \n[3] RUB\n")

if translate == "[1]" or translate == "USD" or translate == "[1] USD":
    print(f"{round(tg / 446, 2)} USD")
elif translate == "[2]" or translate == "EUR" or translate == "[2] EUR":
    print(f"{round(tg / 470, 2)} EUR")
elif translate == "[3]" or translate == "RUB" or translate == "[3] RUB":
    print(f"{round(tg / 5.78, 2)} RUB")
