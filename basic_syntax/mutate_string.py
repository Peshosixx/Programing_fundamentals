first_word = input()
second_word = input()
remaining_word = ''
previous_word = first_word
for mutation in range(len(first_word)):
    mutated_word = second_word[0:mutation + 1]
    remaining_word = first_word[mutation + 1:len(first_word)]
    if previous_word != mutated_word+remaining_word:
        print(f'{mutated_word}{remaining_word}')
        previous_word = mutated_word+remaining_word
