"""
Напишете опростена версия на играта Бесенка. Нека потребителят разполага с 10 опита да
познае всички букви в дадена дума
"""
import time
from termcolor import colored

lucky_word = "bira"

hint_word = []
sub = "*"
for i in lucky_word:
    hint_word.extend(sub)

len_of_hint_word = len(lucky_word)

intro_game = f"""
Hello human. Lets play a game. 
You have 10 attempts to guess the lucky_word. """
print(intro_game)
time.sleep(3)
print(colored('!If you fail to do so you will be hanged ! o===];;;::::> [^_^] <::::;;;]===o ', 'red'))
time.sleep(4)
print(colored(f'Here is a hint for you - this is the length of the lucky_word {hint_word}', "green"))

time.sleep(2)
intro_counter = 3
while intro_counter >= 1:
    print(f"The game starts in {intro_counter} seconds")
    intro_counter -= 1
    time.sleep(1)

letters_from_lucky_word = []
for letter in lucky_word:
    letters_from_lucky_word.append(letter)

already_guessed_letters = []
attempts = 0
while attempts < 10:
    user_guess_letter = input("Please guess one letter from the 'Lucky word': ").lower()
    if user_guess_letter in letters_from_lucky_word:
        already_guessed_letters.append(user_guess_letter)
        get_index_of_guessed_word = letters_from_lucky_word.index(user_guess_letter, 0, len_of_hint_word)
        hint_word.insert(get_index_of_guessed_word, user_guess_letter)
        hint_word.pop(get_index_of_guessed_word + 1)
        try:
            assert len(user_guess_letter) == 1
        except AssertionError:
            print(colored("Don`t cheat HUMAN! You have to guess only 1 letter at a time.", 'yellow'))
            break

        attempts += 1
        print(colored(f"GOOD you found a letter!{hint_word}", 'green'))
        if "*" not in hint_word:
            print(colored(f"YOU WON HUMAN! You have guessed the lucky_word: '{lucky_word}'", 'green'))
            break
    else:
        attempts += 1
        print(colored(f"WRONG! Try again you have {10-attempts} attempts left", "magenta"))
        try:
            assert len(user_guess_letter) == 1
        except AssertionError:
            print(colored("Don`t cheat HUMAN! You have to guess only 1 letter at a time.", 'yellow'))
            break

    if attempts == 10:
        print(colored("!!!!!!GAME OVER!!!!!! \nYOU HAVE BEEN HANGED\no===];;;::::> [^_^] <::::;;;]===o ", 'red'))



