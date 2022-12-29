number = int(input())
for i in range(number):
    for u in range(number):
        for j in range(number):
            print(f'{chr(97+i)}{chr(97+u)}{chr(97+j)}')