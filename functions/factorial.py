n1 = int(input())
n2 = int(input())


def factorial(num1, num2):
    sum_num1 = 1
    sum_num2 = 1
    if num1 != 0:
        for num in range(num1, 1, -1):
            sum_num1 *= num
    else:
        sum_num1 = 1
    if sum_num2 != 0:
        for num in range(num2, 1, -1):
            sum_num2 *= num
    else:
        sum_num2 = 1
    division = sum_num1 / sum_num2
    print(f'{division:.2f}')


factorial(n1, n2)