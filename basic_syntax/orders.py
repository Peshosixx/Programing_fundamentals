number_of_orders = int(input())
total_price = 0
for orders in range(number_of_orders):
    price_per_capsule = float(input())
    day = int(input())
    daily_capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if day < 1 or day > 31:
        continue
    if daily_capsules < 1 or daily_capsules > 2000:
        continue
    price = price_per_capsule * day * daily_capsules
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
else:
    print(f"Total: ${total_price:.2f}")
