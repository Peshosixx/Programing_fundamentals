number = int(input())


def perfect_number(number):
    total_number = 0
    for num in range(1, number):
        if number % num == 0:
            total_number += num
        else:
            continue
    if total_number == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


perfect_number(number)