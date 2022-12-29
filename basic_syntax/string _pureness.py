number = int(input())
for i in range(number):
    word = input()
    if ',' in word:
        print(f"{word} is not pure!")
    elif '.' in word:
        print(f"{word} is not pure!")
    elif '_' in word:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")