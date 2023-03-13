# def do_vasya(s: int, p: int, m: int) -> int:
#     if s + p < m:
#         return True
#     else:
#         return False


# s = int(input())
# p = int(input())
# m = int(input())
# print(do_vasya(s, p, m))

# не понял вопрос! на занятий буду спрашивать)

def is_queen_move(start, end):
    x1, y1 = start
    x2, y2 = end
    if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
        return True
    else:
        return False


def is_knight_move(start, end):
    x1, y1 = start
    x2, y2 = end
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        return True
    else:
        return False
