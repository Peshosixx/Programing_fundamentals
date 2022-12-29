import math

group_size = int(input())
days = int(input())
counter = 0
coins = 0
for i in range(days):
    counter += 1
    coins += 50
    if counter % 15 == 0:
        group_size += 5
    if counter % 10 == 0:
        group_size -= 2
    coins -= group_size * 2
    if counter % 3 == 0:
        coins -= 3 * group_size
    if counter % 5 == 0:
        if counter % 3 == 0:
            coins -= 2 * group_size
            coins += 20 * group_size
        else:
            coins += 20 * group_size

print(f"{group_size} companions received {math.floor(coins/group_size)} coins each.")
