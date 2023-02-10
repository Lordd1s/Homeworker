text = "Hello world"
text_ascii = [ord(c) for c in text]
text_ascii_sorted = sorted(text_ascii)
sorted_text = ''.join(chr(c) for c in text_ascii_sorted)
print(sorted_text)

text = "Hello world"
text_list = list(text)


def bubble_sort(txt_list):
    n = len(txt_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if txt_list[j] > txt_list[j + 1]:
                txt_list[j], txt_list[j + 1] = txt_list[j + 1], txt_list[j]


bubble_sort(text_list)
sorted_text = ''.join(text_list)
print(sorted_text)
