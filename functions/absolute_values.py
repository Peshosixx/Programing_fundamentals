


def absolute_numbers(num):
    return abs(num)


numbers = list(map(float, input().split()))
result = map(absolute_numbers, numbers)
print(list(result))

