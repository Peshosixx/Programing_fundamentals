key = int(input())
characters = int(input())
decrypt_list = []
for i in range(characters):
    letter = input()
    letter_to_number = ord(letter) + key
    decrypt_list.append(letter_to_number)
for u in decrypt_list:
    print(chr(u), end='')