import utils

# class Automobile:
#     model_name = "GT Black Series"
#     year_of_issue = 2020
#     manufacturer = 'Mercedes-Benz'
#     engine_capacity = '6.3L'
#     color = 'Yellow'
#     price = '300.000$'
#
#     def car(self):
#         self.manufacturer = input(str())
#         if self.manufacturer == "Mers" or "Mercedes" or "Mercedes-benz" or "mers":
#             print("Car name: Mercedes-Benz")
#
#
# mers_gt = Automobile()
# print("Input car name: ")
# mers_gt.car()
# print("Model name: ", mers_gt.model_name)
# print("Year: ", mers_gt.year_of_issue)
# print("Engine: ", mers_gt.engine_capacity)
# print("Color: ", mers_gt.color)
# print("Price: ", mers_gt.price)
#
# print("\n\n\n")


# class Book:
#     print("Input book name: ")
#     name = input()
#     autor = "Luis Carrol"
#     year = 1865
#     genre = "Fantasy"
#     price = "1275p."
#
#     def b(self):
#         if self.name == "Alice in Wonderland":
#             print("Name: ", self.name.title(), )
#             print("Year: ", self.year)
#             print("Autor: ", self.autor)
#             print("Genre: ", self.genre)
#             print("Price: ", self.price)
#         elif self.name == "Alice" or "alice":
#             print("Name: ", self.name.title(), "In Wonderland")
#             print("Year: ", self.year)
#             print("Autor: ", self.autor)
#             print("Genre: ", self.genre)
#             print("Price: ", self.price)
#         else:
#             print("In my datebase there is only 'Alice'")
#
#
# book = Book()
# book.b()
# print("\n\n\n")
#
#
# class Stadium:
#     print("Stadium name: ")
#     name = input()
#     opening_date = "01/05/1989"
#     country = "KNDR"
#     city = "Pkhenyan"
#     capacity = 114000
#
#     def stadia(self):
#         if self.name == "nynnado":
#             print("Stadium name: ", nynnado.name.title())
#             print("Where is located: ", nynnado.country, nynnado.city)
#             print("When did it open: ", nynnado.opening_date)
#             print("Capacity: ", nynnado.capacity)
#         else:
#             print("In my datebase there is only 'Nynnado'")
#
#
# nynnado = Stadium()
# nynnado.stadia()


n = input("Type 'One' or 'Many' for get 'JSON' file: ")


def jsons():
    if n == str("one"):
        utils.get_json_one()
        print("Done")
    elif n == str("Many"):
        utils.get_json_many()
        print("done")


jsons()
