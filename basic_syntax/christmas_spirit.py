quantity = int(input())
days = int(input())
total_cost = 0
spirit = 0
counter = 0
flag = False
if days % 10 == 0:
    flag = True
for shopping in range(1, days+1):
    counter += 1
    if counter % 11 == 0:
        quantity += 2
    if shopping % 2 == 0:
        spirit += 5
        total_cost += 2 * quantity
    if shopping % 3 == 0:
        spirit += 13
        total_cost += (quantity * 5) + (quantity * 3)
    if shopping % 5 == 0:
        spirit += 17
        total_cost += quantity * 15
    if counter % 10 == 0:
        spirit -= 20
        total_cost += 23
    if shopping % 3 == 0 and shopping % 5 == 0:
        spirit += 30

if flag:
    print(f"Total cost: {total_cost}")
    print(f"Total spirit: {spirit-30}")
else:
    print(f"Total cost: {total_cost}")
    print(f"Total spirit: {spirit}")
