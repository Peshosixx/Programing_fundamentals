import sys

n = int(input())
list1 = []
for i in range(2, n+1):

    flag = False
    for u in range(2, n+1):
        if i % u == 0 and i % 2 != 0:
            flag = True
        elif i == 2:
            flag = True
        for j in list1:
            if i % j == 0:
                flag = False
    if flag:
        list1.append(i)
if n in list1:
    print(True)
else:
    print(False)