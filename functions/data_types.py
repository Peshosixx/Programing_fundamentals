type_string = input()
expression = input()


def int_(str_type, random_str):
    if str_type == 'int':
        result = int(random_str) * 2
        return result
    elif str_type == 'real':
        result = float(random_str) * 1.5
        return f'{result:.2f}'
    elif str_type == 'string':
        return f'${random_str}$'


print(int_(type_string, expression))