# TODO Incapsulation
# class MainClass:
#     def __init__(self, text):
#         self.text_field = text
#
#     def set_text_field(self, text=None):
#         if text:
#             self.text_field = text
#         else:
#             self.text_field = ""
#
#
# class ChildClass(MainClass):
#     def __init__(self, text, number):
#         super().__init__(text)
#         self.number_field = number
#
#     def set_number_field(self, number):
#         self.number_field = number
#
#
# main_obj = MainClass("Hello")
# print(main_obj.text_field)  # "Hello"
#
# main_obj.set_text_field("World")
# print(main_obj.text_field)  # "World"
#
# child_obj = ChildClass("Hi", 42)
# print(child_obj.text_field)  # "Hi"
# print(child_obj.number_field)  # 42
#
# child_obj.set_text_field("Hello")
# child_obj.set_number_field(123)
# print(child_obj.text_field)  # "Hello"
# print(child_obj.number_field)  # 123
# TODO Incapsulation

# TODO Polymorphism
# class MainClass:
#     def __init__(self, text):
#         self._text_field = text
#
#     def set_text_field(self, text=None):
#         if text:
#             self._text_field = text
#         else:
#             self._text_field = ""
#
#     def get_info(self):
#         return f"MainClass: {self._text_field}"
#
#     def calculate(self):
#         return 0
#
#
# class ChildClass(MainClass):
#     def __init__(self, text, number):
#         super().__init__(text)
#         self._number_field = number
#
#     def set_number_field(self, number):
#         self._number_field = number
#
#     def get_info(self):
#         return f"ChildClass: {self._text_field}, {self._number_field}"
#
#     def calculate(self):
#         return self._number_field * 2
#
#
# def main():
#     main_obj = MainClass("Hello")
#     child_obj = ChildClass("Hi", 42)
#
#     obj_list = [main_obj, child_obj]
#
#     for obj in obj_list:
#         print(obj.get_info())
#         print(obj.calculate())
#
#
# if __name__ == "__main__":
#     main()
# TODO Polymorphism


# TODO Staticmethods
class Roman:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.int_value = self.roman_to_int(roman_numeral)

    def __str__(self):
        return self.roman_numeral

    def __add__(self, other):
        return Roman.int_to_roman(self.int_value + other.int_value)

    def __sub__(self, other):
        return Roman.int_to_roman(self.int_value - other.int_value)

    def __mul__(self, other):
        return Roman.int_to_roman(self.int_value * other.int_value)

    def __truediv__(self, other):
        return Roman.int_to_roman(self.int_value // other.int_value)

    @staticmethod
    def roman_to_int(roman_numeral):
        result = 0
        for i in range(len(roman_numeral)):
            if i > 0 and Roman.roman_dict[roman_numeral[i]] > Roman.roman_dict[roman_numeral[i-1]]:
                result += Roman.roman_dict[roman_numeral[i]] - 2 * Roman.roman_dict[roman_numeral[i-1]]
            else:
                result += Roman.roman_dict[roman_numeral[i]]
        return result

    @staticmethod
    def int_to_roman(int_value):
        result = ""
        for numeral, value in Roman.roman_dict.items():
            while int_value >= value:
                result += numeral
                int_value -= value
        return result
# TODO Staticmethods
