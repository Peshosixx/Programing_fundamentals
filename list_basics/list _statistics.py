positive_numbers, negative_numbers = [], []
number_of_rows = int(input())
for numbers in range(number_of_rows):
    num = int(input())
    if num >= 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)
print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {len(positive_numbers)}')
print(f'Sum of negatives: {sum(negative_numbers)}')