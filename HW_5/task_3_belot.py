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


def give_cards():
    deck = create_deck()
    for index in range(1, 5):
        for _ in range(8):
            all_given_cards.append(deck.pop())


def players_cards():
    print(all_given_cards)
    player_4.append(all_given_cards[0:8])
    player_3.append(all_given_cards[8:16])
    player_2.append(all_given_cards[16:24])
    player_1.append(all_given_cards[24:32])
    for index in range(1, 5):
        print(f"\nplayer {index}:")
        for _ in range(8):
            print(all_given_cards.pop())

give_cards()
players_cards()
print(f"Player 1 cards are {player_1}")
print(f"Player 2 cards are {player_2}")
print(f"Player 3 cards are {player_3}")
print(f"Player 4 cards are {player_4}")



