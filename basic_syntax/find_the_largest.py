number = input()
list1 = []
for i in number:
    list1.append(i)
list1.sort(reverse=True)
for u in list1:
    print(u, end='')