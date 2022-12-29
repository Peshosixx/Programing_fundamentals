lst = []
name = input()
name.split(', ')
counter = 0
flag = False
for i in name:
    if i == ',':
        if flag:
            counter += 1
        flag = True
