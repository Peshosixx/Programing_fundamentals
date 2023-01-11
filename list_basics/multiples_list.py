factor = int(input())
counter = int(input())
list_with_numbers = []
for element in range(1, counter+1):
    current_element = element * factor
    list_with_numbers.append(current_element)
list_with_numbers.sort()
print(list_with_numbers)
