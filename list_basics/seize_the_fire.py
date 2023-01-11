list_of_high = []
list_of_medium = []
list_of_low = []
total_effort = 0
total_fire = 0
splited_word = ''
list_of_cells = []
for i in range(1, 126):
    if i < 51:
        list_of_low.append('Low = ' + str(i))
    elif i < 81:
        list_of_medium.append('Medium = ' + str(i))
    else:
        list_of_high.append('High = ' + str(i))
type_of_fire_cells = input().split('#')
water_level = int(input())
for cells in range(len(type_of_fire_cells)):
    if type_of_fire_cells[cells] in list_of_low:
        splited_word = type_of_fire_cells[cells].split()
        if int(splited_word[2]) <= water_level:
            water_level -= int(splited_word[2])
            total_fire += int(splited_word[2])
            total_effort += 0.25 * int(splited_word[2])
            list_of_cells.append(splited_word[2])
    elif type_of_fire_cells[cells] in list_of_medium:
        splited_word = type_of_fire_cells[cells].split()
        if int(splited_word[2]) <= water_level:
            water_level -= int(splited_word[2])
            total_fire += int(splited_word[2])
            total_effort += 0.25 * int(splited_word[2])
            list_of_cells.append(splited_word[2])
    elif type_of_fire_cells[cells] in list_of_high:
        splited_word = type_of_fire_cells[cells].split()
        if int(splited_word[2]) <= water_level:
            water_level -= int(splited_word[2])
            total_fire += int(splited_word[2])
            total_effort += 0.25 * int(splited_word[2])
            list_of_cells.append(splited_word[2])
print('Cells:')
for final in range(len(list_of_cells)):
    print(f' - {list_of_cells[final]}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {int(total_fire)}')
