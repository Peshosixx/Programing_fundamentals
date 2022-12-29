coffee_counter = 0
while True:
    event = input()
    if event == 'END':
        if coffee_counter > 5:
            print("You need extra sleep")
        else:
            print(f'{coffee_counter}')
        break
    else:
        if event.lower() == 'coding' or event.lower() == 'dog' or event.lower() == 'cat' or event.lower() == 'movie':
            if event.isupper():
                coffee_counter += 2
            elif event.islower():
                coffee_counter += 1

