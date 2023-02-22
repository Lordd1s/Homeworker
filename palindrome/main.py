def is_palindrome(words: str) -> bool:  # ordinary
    res = words.replace(" ", "").replace("?", "").lower()
    print(res)
    if res[0] == res[::-1]:
        return True
    return True if res else False


print(is_palindrome('Do geese see God?'), '\n')


def is_palindrome_2(words: str) -> bool:  # O(n)
    res = words.replace(" ", "").replace("?", "").lower()
    print(res)
    start, end = 0, len(res) - 1
    while start < end:
        if res[start] != res[end]:
            return False
        start += 1
        end -= 1
    return True if res else False


print(is_palindrome_2('А роза упала на лапу Азора'), '\n')


def is_palindrome_3(word: str) -> bool:  # recursion
    res = word.replace(" ", "").replace("?", "").replace("'", "").replace(",", "").lower()
    print(res)
    if len(res) <= 1:
        return True
    if res[0] == res[-1]:
        return is_palindrome_3(res[1:-1:])
    else:
        return False


print(is_palindrome_3("Madam I'm Adam"), '\n')

print('\n\n')


def num_range(numbers: list[int]):    # вот это я не понял ВОООБЩЕ
    res = sorted(set(numbers))
    ranges = []
    print(res)
    for num in res:
        if not ranges or num != ranges[-1][-1] + 1:
            ranges.append([num])
        else:
            ranges[-1].append(num)
    return ', '.join(f"{r[0]}-{r[-1]}" if len(r) > 1 else str(r[0]) for r in ranges)


print(num_range([1, 4, 5, 2, 3, 9, 8, 11, 0]))
