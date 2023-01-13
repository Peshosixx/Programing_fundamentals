#firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
numbers = list(map(str, input().split(', ')))


def palindrome_check_func(num):
    '''Function which checks if a given sequence of numbers are palindrome'''
    for string in num:
        first_part = []
        backwards_part = []
        flag = True
        for chars in range(len(string)//2):
            first_part.append(string[chars])
        if len(string) % 2 == 0:
            for back_chars in range(-1, (-len(string) // 2)-1, -1):
                backwards_part.append(string[back_chars])
        else:
            for back_chars in range(-1, (-len(string)//2), -1):
                backwards_part.append(string[back_chars])
        for compare in range(len(first_part)):
            if first_part[compare] != backwards_part[compare]:
                flag = False
        print(flag)


palindrome_check_func(numbers)
