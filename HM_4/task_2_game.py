from termcolor import colored


available_chars = ["Barbarian", "Sorceress", "Paladin"]
game_is_running = True
intro_msg = """
Welcome to PYTHON DIABLO GAME
Your journey begins at ACT 1 "Rogue Encampment".
If you want to win the game ... with your hero you have to defeat the final boss 'Andariel'.
In order to do so you have to be at minimum level 4.
You have to clear out the dungeon outside ACT 1 in order to level up.
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

level = 0
new_hero = Hero(name=char_name, char_type=char_type_updated, level=level)
print(f"Lets build your character...."
      f"Hello player '{char_name}' you have picked character class '{char_type_updated}' and you begin your journey "
      f"on level '{level}'")

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
while first_action_in_progress:
    try:
        first_action = input(colored(act_1_welcome_msg, 'magenta'))
        assert first_action in valid_reply
        if first_action == "help":
            print(intro_msg)
            first_action_in_progress = False
        if first_action == "east":
            print("You leveled up")
            first_action_in_progress = False
    except:
        print("Enter a valid option")
        first_action_in_progress = True
        continue

