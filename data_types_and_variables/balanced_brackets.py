number_of_lines = int(input())
opening_counter = 0
closing_counter = 0
previous_character = ''
flag = False
for i in range(number_of_lines):
    character = input()
    if character == '(':
        opening_counter += 1
        if character == previous_character:
            flag = True
        else:
            previous_character = character
    if character == ')':
        closing_counter += 1
        if character == previous_character:
            flag = True
        else:
            previous_character = character
if flag:
    print('UNBALANCED')
else:
    if opening_counter == closing_counter:
        print('BALANCED')
    elif opening_counter != closing_counter:
        print('UNBALANCED')
    else:
        print('BALANCED')