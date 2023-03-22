def happy_or_not(nums: str) -> str:
    return "happy" if sum(map(int, nums[:3])) == sum(map(int, nums[-3:])) else "normal"


num = input()
print(happy_or_not(num))
