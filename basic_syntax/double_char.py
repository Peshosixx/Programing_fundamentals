while True:
    word = input()
    if word == 'End':
        break
    elif word == 'SoftUni':
        continue
    else:
        for i in word:
            print(i+i, end='')
        print()