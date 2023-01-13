password = input()


def password_checker(password):
    counter = 0
    validation_flag = True
    if 6 <= len(password) <= 10:
        pass
    else:
        print("Password must be between 6 and 10 characters")
        validation_flag = False

    for chars in password:
        if 48 <= ord(chars) <= 57:
            counter += 1
        elif 65 <= ord(chars) <= 90:
            continue
        elif 97 <= ord(chars) <= 122:
            continue
        else:
            print("Password must consist only of letters and digits")
            validation_flag = False
            break
    if counter < 2:
        print("Password must have at least 2 digits")
        validation_flag = False
    if validation_flag:
        print("Password is valid")


password_checker(password)