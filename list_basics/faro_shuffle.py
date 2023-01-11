deck = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck) // 2
    left_part = deck[0:middle_of_the_deck]
    right_part = deck[middle_of_the_deck::]
    for faro in range(len(left_part)):
        final_deck.append(left_part[faro])
        final_deck.append(right_part[faro])
    deck = final_deck
print(deck)