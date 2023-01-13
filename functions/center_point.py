import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def center_point(x1, y1, x2, y2):
    counter_x1 = 0
    counter_x2 = 0
    counter_y1 = 0
    counter_y2 = 0
    for i in range(int(abs(x1)), 0, -1):
        counter_x1 += 1
    for i in range(int(abs(x2)), 0, -1):
        counter_x2 += 1
    for i in range(int(abs(y1)), 0, -1):
        counter_y1 += 1
    for i in range(int(abs(y2)), 0, -1):
        counter_y2 += 1

    if counter_x1 <= counter_x2:
        largest_x = x1
    else:
        largest_x = x2
    if counter_y1 <= counter_y2:
        largest_y = y1
    else:
        largest_y = y2

    print(f"({math.floor(largest_x)}, {math.floor(largest_y)})")


center_point(x1, y1, x2, y2)