budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4
loaf_price = flour_price + eggs_price + milk_price
colored_eggs = 0
counter = 0
loaves = 0
while True:
    if budget - loaf_price > 0:
        counter += 1
        budget -= loaf_price
        loaves += 1
        colored_eggs += 3
        if counter % 3 == 0:
            colored_eggs -= (loaves - 2)
    else:
        print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        break
