number = input().split()
numbers = (int(x) for x in number)


def check_even(number):
    if number % 2 == 0:
        return True


even_numbers_iterator = filter(check_even, numbers)

print(list(even_numbers_iterator))
