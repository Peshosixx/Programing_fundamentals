numbers = list(map(int, input().split()))


def min_number(num):
    return min(num)


def max_number(num):
    return max(num)


def sum_numbers(num):
    return sum(num)


print(f'The minimum number is {min_number(numbers)}\n'
      f'The maximum number is {max_number(numbers)}\n'
      f'The sum number is: {sum_numbers(numbers)}')
