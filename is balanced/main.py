# def is_balanced(chr_string):
#     stack = []
#     opening_brackets = '({['
#     closing_brackets = ')}]'
#     for char in chr_string:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if not stack:
#                 return False
#             pop_meth = stack.pop()
#             if (pop_meth == '(' and char != ')') or \
#                     (pop_meth == '{' and char != '}') or \
#                     (pop_meth == '[' and char != ']'):
#                 return False
#     return len(stack) == 0
#
#
# user_input = input("Enter a string of parentheses: ")
# if is_balanced(user_input):
#     print("The parentheses are balanced!")
# else:
#     print("The parentheses are 'NOT' balanced!")
#
# print("\n\n\n")


# not interesting
def find_big_and_small_int(list1: list[int]):
    print("Your list number: ", list1)
    sorted_list = sorted(list1)
    big_int = sorted_list[-1]
    small_int = sorted_list[0]
    print("big int is: ", big_int, "\n" "small int is: ", small_int)
    diff = big_int - small_int
    return "The difference is: ", diff


print(find_big_and_small_int([4, 6, 8, 7, 13, 5]))

print("\n\n\n")


def sum_of_pos_nums(list1: list[int]):
    print("Your list number: ", list1)
    total = 0
    for i in list1:
        if i > 0:
            total += i
        else:
            print("Numbers not positive")
    return total


print("Sum of list num: ", sum_of_pos_nums([4, 2, 8, 7, 6, 1]))

print("\n\n\n")


def big_even_num(list1: list[int]):
    print("your num list: ", list1)
    stack = []
    sorted_nums = sorted(list1)
    for i in sorted_nums:
        if i % 2 == 0:
            stack.append(i)
        if i % 2 == 0 not in sorted_nums:
            return 0
    return stack[-1]


print("big even num: ", big_even_num([7, 8, 6, 7, 9, 4, 22, 4, 0]))
