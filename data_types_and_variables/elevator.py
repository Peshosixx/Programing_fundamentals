people = int(input())
capacity = int(input())
if people <= capacity:
    print(1)
else:
    full_courses = people // capacity
    leftovers = people % capacity
    if leftovers == 0:
        print(f'{full_courses}')
    else:
        print(f'{full_courses+1}')
