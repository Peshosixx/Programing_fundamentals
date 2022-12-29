fights = int(input())
helm_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_price = 0
counter = 0
shield_counter = 0
for i in range(fights):
    counter += 1
    if counter % 2 == 0:
        if counter % 3 == 0:
            shield_counter += 1
            total_price += helm_price + sword_price + shield_price
            if shield_counter % 2 == 0:
                total_price += armor_price
        else:
            total_price += helm_price
    elif counter % 3 == 0:
        total_price += sword_price

print(f'Gladiator expenses: {total_price:.2f} aureus')