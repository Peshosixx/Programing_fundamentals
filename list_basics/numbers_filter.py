number_of_lines = int(input())
numbers = []
filtered = []
for i in range(number_of_lines):
    numbers.append(int(input()))
special_command = input()
if special_command == 'even':
    for u in numbers:
        if u % 2 == 0:
            filtered.append(u)
elif special_command == 'odd':
    for u in numbers:
        if u % 2 != 0:
            filtered.append(u)
elif special_command == 'positive':
    for u in numbers:
        if u >= 0:
            filtered.append(u)
elif special_command == 'negative':
    for u in numbers:
        if u < 0:
            filtered.append(u)
print(filtered)