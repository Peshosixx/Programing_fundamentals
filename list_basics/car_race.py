times = input().split()
left_car = []
right_car = []
left_time, right_time = 0, 0
for i in range(len(times)//2):
    left_car.append(int(times[i]))
    right_car.append(int(times[-1-i]))
for u in range(len(left_car)):
    if left_car[u] == 0:
        left_time *= 0.8
    else:
        left_time += left_car[u]
    if right_car[u] == 0:
        right_time *= 0.8
    else:
        right_time += right_car[u]
if left_time < right_time:
    print(f'The winner is left with total time: {left_time:.1f}')
else:
    print(f'The winner is right with total time: {right_time:.1f}')