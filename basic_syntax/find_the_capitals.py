word = input()
list1 = []
counter = 0
for i in word:
    if i.isupper():
        list1.append(counter)
    counter += 1
print(list1)
