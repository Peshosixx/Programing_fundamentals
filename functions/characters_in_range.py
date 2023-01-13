character_one = input()
character_two = input()


def chars_in_between(one, two):
    for chars in range(ord(one)+1, ord(two)):
        print(chr(chars), end=' ')


chars_in_between(character_one, character_two)
