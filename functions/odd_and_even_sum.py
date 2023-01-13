def sum_of_odd(odd):
    return sum(odd)


def sum_of_even(even):
    return sum(even)


number = input()
odd_numbers, even_numbers = [], []

for i in number:
    if int(i) % 2 == 0:
        even_numbers. append(int(i))
    else:
        odd_numbers.append(int(i))

print(f'Odd sum = {sum_of_odd(odd_numbers)}, Even sum = {sum_of_even(even_numbers)}')



