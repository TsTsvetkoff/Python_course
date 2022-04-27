import random

standard_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
my_cards = {"Hearts": standard_cards, "Diamonds" : standard_cards, "Clubs": standard_cards, "Spades" : standard_cards}
keys =  list(my_cards.keys())
values =  list(my_cards.values())
a1 = list(my_cards.items())

picked_cards = []


for card in range(3):

    # User shuffle cards
    #random.shuffle(my_cards)
    # RCA - You can't reshuffle a dictionary.
    # What you can do is create a list of the dictionary's keys and shuffle that in order to achieve a new arbitrary order in which to access the dictionary's contents
    random.shuffle(a1)
    a = dict(a1)

    # User choose a card
    chosen_card_color = random.choice(keys)
    print(chosen_card_color)
    chosen_card = random.choice(values[0])
    print(chosen_card)

    # User removes card from the stack
#    my_cards.remove(chosen_card)

    # User took a card
    picked_cards.append(str(chosen_card) +" "+ str(chosen_card_color))

print("User took these 3 cards:\r\n",picked_cards)