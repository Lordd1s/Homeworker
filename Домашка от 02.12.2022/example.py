def get_sum(a, b):
    if a == b:
        return a
    if a < b:
        list_value = list(range(a, b + 1, 1))
        return sum(list_value)
    if a > b:
        list_value = list(range(b, a + 1, 1))
        return sum(list_value)


print(get_sum(13, 15))
