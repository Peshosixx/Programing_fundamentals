word = input()
counter = 0
for 'SAND' in word.upper():
    counter += 1
    for 'WATER' in word.upper():
        counter += 1
        for 'FISH' in word.upper():
            counter += 1
            for 'SUN' in word.upper():
                counter += 1
print(counter)