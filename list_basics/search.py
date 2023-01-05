number_of_lines = int(input())
key_word = input()
words = []
for sentence in range(number_of_lines):
    words.append(input())
words_including_key = []
for i in words:
    if key_word in i:
        words_including_key.append(i)
print(words)
print(words_including_key)