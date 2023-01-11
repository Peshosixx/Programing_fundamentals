names_of_the_gifts = input().split()
commands = input()
current_gift, required_gift, required_gift_index = '', '', ''
while commands != "No Money":
    if 'OutOfStock ' in commands:
        current_gift = commands.split('OutOfStock ')
        current_gift = current_gift[1]
        for i in range(len(names_of_the_gifts)):
            if names_of_the_gifts[i] == current_gift:
                names_of_the_gifts[i] = 'None'
    elif 'Required ' in commands:
        current_gift = commands.split('Required ')
        gifts = current_gift[1].split()
        required_gift = gifts[0]
        required_gift_index = int(gifts[1])
        if required_gift_index < len(names_of_the_gifts):
            names_of_the_gifts[required_gift_index] = required_gift
    elif 'JustInCase ' in commands:
        current_gift = commands.split('JustInCase ')
        current_gift = current_gift[1]
        names_of_the_gifts[-1] = current_gift
    commands = input()
for gifts in range(len(names_of_the_gifts)):
    if names_of_the_gifts[gifts] == 'None':
        continue
    else:
        print(names_of_the_gifts[gifts], end=' ')