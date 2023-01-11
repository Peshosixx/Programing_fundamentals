list_of_string = input().split()
numbers_to_remove = int(input())
list_of_integers = []
single_string = ''
for i in list_of_string:
    list_of_integers.append(int(i))
working_list_of_integers = list_of_integers.copy()
working_list_of_integers.sort()
for u in range(numbers_to_remove):
    list_of_integers.remove(working_list_of_integers.pop(0))
for j in list_of_integers:
    single_string += str(j) + ', '
print(single_string[0:-2])
