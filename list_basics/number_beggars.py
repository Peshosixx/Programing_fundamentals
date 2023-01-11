money = input().split(', ')
beggars = int(input())
money_as_digits = []
for money_index in money:
    money_as_digits.append(int(money_index))
starting_point = 0
lst_with_calculated_sums = []
while starting_point < beggars:
    collected_sum = 0
    for beggar in range(starting_point, len(money_as_digits), beggars):
        collected_sum += money_as_digits[beggar]
    lst_with_calculated_sums.append(collected_sum)
    starting_point += 1
print(lst_with_calculated_sums)
