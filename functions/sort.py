sequence_of_numbers = input().split()
number = (int(x) for x in sequence_of_numbers)


def sorting_numbers(number):
    sorted_numbers = sorted(number)
    return sorted_numbers


print(sorting_numbers(number))