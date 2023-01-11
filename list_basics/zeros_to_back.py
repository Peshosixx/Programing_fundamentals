numbers = input().split(', ')
sorted_numbers = []
counter = 0
for i in range(len(numbers)):
    sorted_numbers.append(int(numbers[i]))
for j in range(len(sorted_numbers)):
    if sorted_numbers[j] == 0:
        sorted_numbers.remove(0)
        sorted_numbers.append(0)
print(sorted_numbers)