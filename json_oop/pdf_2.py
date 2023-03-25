n = int(input("Give number: "))
for i in range(1, n+1):
    if i * i >= n:
        break
    print(i*i)


N = int(input("Enter the value of N: "))
given_numbers = list(map(int, input("Enter the remaining card numbers separated by spaces: ").split()))
sum_of_given_numbers = sum(given_numbers)
sum_of_all_cards = (N * (N + 1)) // 2
sum_remaining = sum_of_all_cards - sum_of_given_numbers

print("The lost card is:", sum_remaining)
