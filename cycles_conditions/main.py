def if_triangle(a: int, b: int, c: int) -> bool:
    return True if a + b > c and a + c > b and b + c > a else False


def even(number: int | float) -> bool:
    return True if number % 2 == 0 else False


def a_b_c(aa: int, bb: int, cc: int) -> bool:
    return True if aa + bb > cc else False


def first_bigger_or_not(aaa: int, bbb: int) -> bool:
    return True if aaa > bbb else False


