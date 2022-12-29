capacity = 255
total_water = 0
pours = int(input())
for i in range(pours):
    litters = int(input())
    if litters > capacity:
        print('Insufficient capacity!')
    else:
        capacity -= litters
        total_water += litters
print(f'{total_water}')