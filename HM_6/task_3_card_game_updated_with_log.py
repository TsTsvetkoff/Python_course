import random, datetime

card_points = ['7', '8', '9', '1', 'J', 'Q', 'K', 'A']
card_signs = ['Пика', 'Купа', 'Каро', 'Спатия']

number_to_points = {
        '7': 7,
        '8': 8,
        '9': 9,
        '1': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
}


all_given_cards = []
given_players_cards = []
player_1 = []
player_2 = []
player_3 = []
player_4 = []
current_hand = {"Player1 card": [], "Player2 card": [], "Player3 card": [], "Player4 card": []}


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
    player_4.extend(all_given_cards[0:8])
    player_3.extend(all_given_cards[8:16])
    player_2.extend(all_given_cards[16:24])
    player_1.extend(all_given_cards[24:32])
    for index in range(1, 5):
        print(f"\nplayer {index}:")
        for _ in range(8):
            print(all_given_cards.pop())
    print(f"Player 1 cards are {player_1}")
    print(f"Player 2 cards are {player_2}")
    print(f"Player 3 cards are {player_3}")
    print(f"Player 4 cards are {player_4}")


def other_players_play():
    player_1_first_card = player_1.pop()
    current_hand["Player1 card"].append(player_1_first_card)

    first_color_player1 = []
    for x in player_1_first_card:
        if ord(x[0]) > 128:
            first_color_player1.append(x)
    updated_list = ("".join(first_color_player1))
    print(f"The color that all must match is: {updated_list}")

    str_match = [s for s in player_2 if s.__contains__(updated_list)]
    if len(str_match) > 0:
        current_hand["Player2 card"].append(str_match[0])
        player_2.remove(str_match[0])
    else:
        player_2_first_card = player_2.pop()
        #current_hand["Player2 card"].append(player_2_first_card)

    str_match_3 = [s for s in player_3 if s.__contains__(updated_list)]
    if len(str_match_3)>0:
        current_hand["Player3 card"].append(str_match_3[0])
        player_3.remove(str_match_3[0])
    else:
        player_3_first_card = player_3.pop()
       # current_hand["Player3 card"].append(player_3_first_card)

    str_match_4 = [s for s in player_4 if s.__contains__(updated_list)]

    if len(str_match_4)> 0:
        current_hand["Player4 card"].append(str_match_4[0])
        player_4.remove(str_match_4[0])
    else:
        player_4_first_card = player_4.pop()
        #current_hand["Player4 card"].append(player_4_first_card)

    print(current_hand)

    all_trown_cards = []
    for v in current_hand.values():
        all_trown_cards.extend(v)

    idz_of_thrownd_cards = []
    for z in all_trown_cards:
        idz_of_thrownd_cards.extend(z[0])

    new_dict = {k: number_to_points[k] for k in idz_of_thrownd_cards if k in number_to_points}
    maxed = (max(new_dict, key=new_dict.get))

    def matchingKeys(dictionary, searchString):
        return print([key for key, val in dictionary.items() if any(searchString in s for s in val)])

    print(f"With card '{maxed} {updated_list}' The Winner is : ")
    matchingKeys(current_hand, maxed)

    card_log = open('cards_given.log', 'a+')
    card_log.write(f"Current Date: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')} Given cards : {current_hand}"
                   f" The winning card is {maxed} and card sign {updated_list}  \n")
    card_log.close()

    #note see https://stackoverflow.com/questions/1082343/unicode-characters-appear-as-question-marks-in-intellij-idea-console
    #for issues with cyrilic in logs

    # print("------------------------------------------------------------------")
    # print(f"Player 1 cards now are {player_1}")
    # print(f"Player 2 cards now are {player_2}")
    # print(f"Player 3 cards now are {player_3}")
    # print(f"Player 4 cards now are {player_4}")
    #


give_cards()
players_cards()
other_players_play()







