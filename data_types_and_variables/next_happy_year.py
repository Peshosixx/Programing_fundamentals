year = int(input())
flag = False
while not flag:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])
    flag = len(set_year) == len(str(year))
print(year)