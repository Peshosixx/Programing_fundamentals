word = input()
sentence_list = []
reversed_list = []
flag = False
word.split(' ')
for i in word:
    if flag:
        reversed_list.append(i)
        flag = False
    else:
        if i == '-':
            flag = True
        else:
            if i == ' ':
                continue
            else:
                reversed_list.append(-int(i))
print(reversed_list)


