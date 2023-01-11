numbers = input()+ ' '
message = input()
char_list = []
numbers_list = []
sum_numbers = 0

for i in range(len(message)):
    char_list.append(message[i])
for u in range(len(numbers)):
    if numbers[u] != ' ':
        sum_numbers += int(numbers[u])
    else:
        print(char_list[sum_numbers%len(char_list)], end='')
        char_list.pop(sum_numbers%len(char_list))
        sum_numbers = 0
