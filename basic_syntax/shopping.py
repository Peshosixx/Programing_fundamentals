budget = int(input())
while True:
    price = input()
    if price != 'End':
        price = int(price)
        budget -= price
        if budget < 0:
            print("You went in overdraft!")
            break
    else:
        print("You bought everything needed.")
        break
