import re
budget = 0
list_with_prices = []
profit = 0
clothes_and_prices_split = input()
starting_budget = float(input())
clothes, prices = [], []
clothes_and_prices_split = re.split('->|[|]', clothes_and_prices_split)
for separation in range(len(clothes_and_prices_split)):
    if separation % 2 == 0:
        clothes.append(clothes_and_prices_split[separation])
    else:
        prices.append(float(clothes_and_prices_split[separation]))
for buying in range(len(prices)):
    if clothes[buying] == 'Clothes' and prices[buying] <= 50.00 and prices[buying] <= starting_budget:
        list_with_prices.append(float(prices[buying] * 1.4))
        starting_budget -= prices[buying]
        profit += 0.4 * prices[buying]
        budget += 1.4 * prices[buying]
    elif clothes[buying] == 'Shoes' and prices[buying] <= 35.00 and prices[buying] <= starting_budget:
        list_with_prices.append(float(prices[buying] * 1.4))
        starting_budget -= prices[buying]
        profit += 0.4 * prices[buying]
        budget += 1.4 * prices[buying]
    elif clothes[buying] == 'Accessories' and prices[buying] <= 20.50 and prices[buying] <= starting_budget:
        list_with_prices.append(float(prices[buying] * 1.4))
        starting_budget -= prices[buying]
        profit += 0.4 * prices[buying]
        budget += 1.4 * prices[buying]
print(*[f'{price:.2f}' for price in list_with_prices], end=' ')
print()
print(f'Profit: {profit:.2f}')
if budget+starting_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
