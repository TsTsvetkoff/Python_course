from termcolor import colored
import sys

available_chars = ["Barbarian", "Sorceress", "Paladin"]
game_is_running = True
intro_msg = """
Welcome to PYTHON DIABLO GAME
Your journey begins at ACT 1 "Rogue Encampment".
If you want to win the game ... with your hero you have to defeat the final boss 'Andariel'.
In order to do so you have to be at minimum level 4.
You have to clear out the dungeons outside ACT 1 in order to level up.
"""
print(colored(intro_msg, 'yellow'))

class Hero():
    def __init__(self, name, char_type, level):
        self.name = name
        self.type = char_type
        self.level = level

    @property
    def build_a_char(self):
        self.name = char_name
        self.type = char_type_updated

    def get_name(self):
        return self.name

    def char_type(self):
        return self.char_type

    def level_up(self, new_level):
        self.level = new_level


char_name = input("Please enter a name for your hero: ")
while game_is_running:
    try:
        char_type_updated = input(f"Please pick one character class. "
                                  f"Note at version 1.01 only 3 types are available {available_chars}: ")
        assert char_type_updated in available_chars, "Please pick a correct character type!"
        break
    except:
        print("Please enter a valid character class!")
        game_is_running = True
        continue
current_level = 1

new_hero = Hero(name=char_name, char_type=char_type_updated, level=current_level)
print(f"Lets build your character...."
      f"Hello player '{char_name}' you have picked character class '{char_type_updated}' and you begin your journey "
      f"on level '{current_level}'")

act_1_welcome_msg = f"""
Welcome '{char_name}' to Rogue Encampment.
The Rogue Encampment is the only town in PYTHON Diablo II and the starting point of the game.
It is a makeshift fortress located right next to the Blood Moor dungeon. 
The Rogue Encampment, as its name designates, is the camp set up by the survivors from the Sisterhood of the 
Sightless Eye. The Rogue Monastery, guarding the only pass to the east, was attacked by the forces of Hell after Diablo
had passed by. There he left Andariel, the Maiden of Anguish, in charge to prevent any eventual pursuers 
from following him east.
Now lets clear Blood Moor dungeon.
Note: If you want to see the rules of the game type 'help'
Type 'east' to begin :
"""
valid_reply = ['east', 'help']

first_action_in_progress = True
level_up_counter = 1
while first_action_in_progress:

    try:
        first_action = input(colored(act_1_welcome_msg, 'magenta')).lower()
        assert first_action in valid_reply
        if first_action == "help":
            print(intro_msg)
        if first_action == "east":
            first_action = 0
            print("After multiple health potions and brave fighting, you have managed to clear out all "
                  "minions in the Blood Moor dungeon and you have leveled up!")
            hero_stats_0 = {"Name": new_hero.name, "Character": char_type_updated, "Current Level": new_hero.level}
            print(f"Updated from {hero_stats_0}")
            first_action = 1 # Blood Moor is cleared
            if first_action == 1:
                level_up_counter += 1
                new_hero.level_up(level_up_counter)
                hero_stats_1 = {"Name": new_hero.name, "Character": char_type_updated, "Current Level": new_hero.level}
                print(f"Updated to {hero_stats_1}")



            act_1_second = """
            Now that you have cleared Blood Moor you can go to : 
            1) Den of Evil
            2) Cold Plains
            Please enter 1 or 2 based on your preferably
            """
            secont_action_in_progress = True
            valid_reply_2 = [1,2, "help"]
            counter_1 = 0
            counter_2 = 0

            while secont_action_in_progress:
                try:

                    secont_action_in_progress_input = int(input(colored(act_1_second, 'magenta')))
                    assert secont_action_in_progress in valid_reply_2
                    if secont_action_in_progress_input == 1 and counter_1 == 0:
                        counter_1 += 1


                        print("After multiple health potions and brave fighting, you have managed to clear out all "
                              "minions in the Den of Evil dungeon and you have leveled up!")
                        hero_stats_0 = {"Name": new_hero.name, "Character": char_type_updated,
                                        "Current Level": new_hero.level}
                        print(f"Updated from {hero_stats_0}")
                            #  Den of Evil
                        level_up_counter += 1
                        new_hero.level_up(level_up_counter)
                        hero_stats_1 = {"Name": new_hero.name, "Character": char_type_updated, "Current Level": new_hero.level}
                        print(f"Updated to {hero_stats_1}")
                        print("Now that Den of Evil is cleared you do not have any options to go further. Only option now you have is"
                              " to go back from Den of Evil and go to --> Cold Plants")

                        go_back = True
                        while go_back:
                            try:
                                back_input = input("Type 'Back' in order to continue your journey: ").lower()

                                assert back_input == "back"
                                go_back = False
                                whent_back = True

                            except:
                                print("Enter a valid option")
                                go_back = True
                                continue

                    if secont_action_in_progress_input == 1 and counter_1 > 0:
                        print("You did not gain any experience since the Den of Evil is cleared out of minions "
                              "Please proceed towards 'Cold Plains' ")


                    elif secont_action_in_progress_input == 2:
                        counter_2 += 1
                        final_action_in_progress = True
                        valid_reply_2 = [1, 2]
                        while final_action_in_progress:
                            try:
                                #  Cold Plains
                                if counter_2 == 1:
                                    print(F"Brave {char_type_updated} you have proceed towards 'Cold Plains'. "
                                          F"There you got your first boss fight. The gained experience will help you in your fight with the final boss Andariel"
                                          F"\n\rAs remember  you have to be at least level 4 before you fight her too !!!!")
                                    hero_stats_0 = {"Name": new_hero.name, "Character": char_type_updated,
                                                    "Current Level": new_hero.level}
                                    print(f"Updated from {hero_stats_0}")
                                    level_up_counter += 1
                                    new_hero.level_up(level_up_counter)
                                    hero_stats_1 = {"Name": new_hero.name, "Character": char_type_updated,
                                                    "Current Level": new_hero.level}
                                    print(f"Updated to {hero_stats_1}")

                                else:
                                    print(
                                        "You did not gain any experience since the 'Cold Plains' is cleared out of minions "
                                        "Please proceed towards 'Cold Plains' and be ready for the fight with Andariel!"
                                        "In order to defeat her you MUST BE at least on LEVEL 4")

                                    print(f"You Current status is {hero_stats_1}")

                                cold_plants = int(input("Now you have 2 options: \n\r"
                                                        "1) Go back to Blood Moor \n\r"
                                                        "2) Fight Andariel \n\r"))

                                if cold_plants == 1:
                                    final_action_in_progress = False
                                    print("Going back to Blood Moor ..")
                                if cold_plants == 2:
                                    if new_hero.level < 4 :
                                        print(f"YOU HAVE DIED! Your hero {hero_stats_1} is too weak!")
                                        print(f"In order to defeat Andariel your level current level must be atleast level 4 and yours is {new_hero.level}")
                                        secont_action_in_progress = False
                                        first_action_in_progress = False
                                        break

                                    else:
                                        print(f"You WON Brave {char_type_updated} ! Your hero {hero_stats_1}! defeated the evil")
                                        secont_action_in_progress = False
                                        first_action_in_progress = False
                                        break


                            except:
                                print("Enter a valid option")
                                final_action_in_progress = True
                                continue

                except:
                    print("Enter a valid option")
                    secont_action_in_progress = True
                    continue
            break
    except:
        print("Enter a valid option")
        first_action_in_progress = True
        continue

