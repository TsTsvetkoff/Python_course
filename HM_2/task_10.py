"""
Напишете опростена версия на играта Бесенка. Нека потребителят разполага с 10 опита да
познае всички букви в дадена дума
"""
import time

lucky_word = "car"

hint_word = []
sub = "*"
for i in lucky_word:
    hint_word.extend(sub)

intro_game = f"""
Hello human. Lets play a game. 
You have 10 attempts to guess the lucky_word. 
<::::;;;]===o ! If you fail to do so you will be hanged ! o===];;;::::>
================================================================================
Here is a hint for you - this is the length of the lucky_word {hint_word}
================================================================================
"""
print(intro_game)
time.sleep(3)
intro_counter = -3
while intro_counter < 0:
    print(f"The game starts in {intro_counter} seconds")
    intro_counter += 1
    time.sleep(1)

letters_from_lucky_word = []
for letter in lucky_word:
    letters_from_lucky_word.append(letter)

attempts = 0
while attempts < 10:
    user_guess_letter = input("Please guess a letter from the 'Lucky word': ").lower()
    if user_guess_letter in letters_from_lucky_word :
        for user_guess_letter in letters_from_lucky_word :
            hint_word.append(user_guess_letter)
        print(f"You got 1 letter! Contracts the letter {user_guess_letter} in in the lucky word. Here "
              f"is your hint again {hint_word}")
        #TODO - fix the bug do not show the complete word but search in list by index
    else:
        print("sorry")


