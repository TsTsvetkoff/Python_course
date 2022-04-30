import numpy as np
from itertools import zip_longest
card_points =['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_signs =['Пика', 'Купа', 'Каро', 'Спатия']


all_given_cards = []
given_players_cards = []
player_1 = []
player_2 = []
player_3 = []
player_4 = []


def create_deck():
    deck = set()
    for suite in card_signs:
        suite_cards = {f'{rank} {suite}' for rank in card_points}
        deck.update(suite_cards)
    return deck


def play():
    deck = create_deck()
    for index in range(1, 5):
        for _ in range(8):
            all_given_cards.append(deck.pop())


def players_cards():
    print(all_given_cards)
    for index in range(1, 5):
        print(f"\nplayer {index}:")
        for _ in range(8):
            if index == 1:
                player_1.append(all_given_cards.pop())



play()
players_cards()
print(player_1)


