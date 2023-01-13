import test

number_one = int(input())
number_two = int(input())
number_three = int(input())


def sum_numbers(one, two):
    result = one + two
    return result


def subtract(three):
    result = sum_numbers(number_one, number_two) - three
    return result


def add_an_subtract(one, two, three):
    result = subtract(number_three)
    return result


print(
    f'The substraction of the third number out of the sum of first two:\n'
    f'{add_an_subtract(number_one, number_two, number_three)}')
print(f'The smallest out of three is:\n'
      f'{test.smallest_out_of_three(number_three, number_two, number_one)}')
