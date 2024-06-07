
from playerclass import PlayerObject
import sys
from termcolor import cprint

def class_info():
    while True:
        cprint("Select a class to learn more about it")
        cprint("""
[K]night
[B]arbarian
[W]izard
[Q]uit""")
        user_input = input()
        if user_input.lower() == 'k':
            cprint("""
The Knight excels in martial combat with Sword and Shield to slay foes that dare to oppose him.
For attacking you roll 4d6 and keep the highest 3
For defending you roll 5d6 and keep the highest 4
You have a maximum hitpoint total of 30
Your attack and defence dice explode on 5 and 6
Your dice can explode only once.
Would you like to play as the Knight? [Y]es / [N]o
""")
            user_input = input()
            if user_input.lower() == 'y':
                player_class = 'knight'
                return player_class
            elif user_input.lower() == 'n':
                pass
            else:
                cprint("Please enter a valid selection")
        
        elif user_input.lower() == 'b':
            cprint("""
The Barbarian excels in pressing the attack, at the expense of defense.
For attacking you roll 5d6 and keep the highest 4
For defending you roll 3d6 and keep the highest 2
You have a maximum hitpoint total of 35
Your attack dice explode on 5 and 6
Your defence dice only explode on 6
Would you like to play as the Barbarian? [Y]es / [N]o
""")
            user_input = input()
            if user_input.lower() == 'y':
                player_class = 'barbarian'
                return player_class
            elif user_input.lower() == 'n':
                pass
            else:
                cprint("Please enter a valid selection")
                
        elif user_input.lower() == 'w':
            cprint("""
The Wizard is a potent spell caster who has mastered the art of magic, and also really loves explosions.
For attacking you roll 4d6 and keep the highest 3
For defending you roll 4d6 and keep the highest 3
You have a maximum hitpoint total of 25
Your attack dice explode on 4, 5, and 6
Your defence dice explode on 1, 2, and 3
Would you like to play as the Wizard? [Y]es / [N]o
""")
            user_input = input()
            if user_input.lower() == 'y':
                player_class = 'wizard'
                return player_class
            elif user_input.lower() == 'n':
                pass
            else:
                cprint("Please enter a valid selection")
            



def class_selection(player_class):
    if player_class.lower() == 'knight':
        print("You have selected: Knight")
        PlayerObject.player_class = 'knight'
        PlayerObject.player_hitpoints = 30
        PlayerObject.player_dmg = 0
        PlayerObject.player_xp = 0
        PlayerObject.player_gold = 0
        PlayerObject.player_max_health = 30
        PlayerObject.player_max_explode = 1
        
        PlayerObject.atk_dice_min = 1
        PlayerObject.atk_dice_max = 6
        PlayerObject.atk_dice = 4
        PlayerObject.atk_dice_keep = 3
        PlayerObject.atk_explode_value = [5, 6]
        PlayerObject.player_atk_rolls = []
        PlayerObject.player_exploded_atk_dice = []
        PlayerObject.player_atk_rolls_total= 0
        
        PlayerObject.def_dice_min = 1
        PlayerObject.def_dice_max = 6
        PlayerObject.def_dice = 5
        PlayerObject.def_dice_keep = 4
        PlayerObject.def_explode_value = [5, 6]
        PlayerObject.player_def_rolls = []
        PlayerObject.player_exploded_def_dice = []
        PlayerObject.player_def_rolls_total = 0
        
        PlayerObject.Debug = "Player Class has been selected"
        
        return PlayerObject.player_gold, PlayerObject.player_max_health, PlayerObject.player_max_explode, PlayerObject.player_xp, PlayerObject.player_class, PlayerObject.player_hitpoints, PlayerObject.atk_dice_min, PlayerObject.atk_dice_max, PlayerObject.atk_dice, PlayerObject.atk_dice_keep, PlayerObject.atk_explode_value, PlayerObject.Debug, PlayerObject.player_atk_rolls, PlayerObject.player_exploded_atk_dice, PlayerObject.def_dice_min, PlayerObject.def_dice_max, PlayerObject.def_dice, PlayerObject.def_dice_keep, PlayerObject.player_def_rolls, PlayerObject.player_exploded_def_dice, PlayerObject.player_def_rolls_total
        
    elif player_class.lower() == "barbarian":
        print("You have selected: Barbarian")
        PlayerObject.player_class = 'barbarian'
        PlayerObject.player_hitpoints = 35
        PlayerObject.player_dmg = 0
        PlayerObject.player_xp = 0
        PlayerObject.player_gold = 0
        PlayerObject.player_max_health = 35
        PlayerObject.player_max_explode = 2
        
        PlayerObject.atk_dice_min = 1
        PlayerObject.atk_dice_max = 6
        PlayerObject.atk_dice = 5
        PlayerObject.atk_dice_keep = 4
        PlayerObject.atk_explode_value = [5, 6]
        PlayerObject.player_atk_rolls = []
        PlayerObject.player_exploded_atk_dice = []
        PlayerObject.player_atk_rolls_total= 0
        
        PlayerObject.def_dice_min = 1
        PlayerObject.def_dice_max = 6
        PlayerObject.def_dice = 3
        PlayerObject.def_dice_keep = 2
        PlayerObject.def_explode_value = [6]
        PlayerObject.player_def_rolls = []
        PlayerObject.player_exploded_def_dice = []
        PlayerObject.player_def_rolls_total = 0

        PlayerObject.Debug = "Player Class has been selected"

        return PlayerObject.player_gold, PlayerObject.player_max_health, PlayerObject.player_max_explode, PlayerObject.player_xp, PlayerObject.player_class, PlayerObject.player_hitpoints, PlayerObject.atk_dice_min, PlayerObject.atk_dice_max, PlayerObject.atk_dice, PlayerObject.atk_dice_keep, PlayerObject.atk_explode_value, PlayerObject.Debug, PlayerObject.player_atk_rolls, PlayerObject.player_exploded_atk_dice, PlayerObject.def_dice_min, PlayerObject.def_dice_max, PlayerObject.def_dice, PlayerObject.def_dice_keep, PlayerObject.player_def_rolls, PlayerObject.player_exploded_def_dice, PlayerObject.player_def_rolls_total
    
    ### WIZARD STATBLOCK GOES HERE
    if player_class.lower() == 'wizard':
        print("You have selected: Wizard")
        PlayerObject.player_class = 'wizard'    
        PlayerObject.player_hitpoints = 25
        PlayerObject.player_dmg = 0
        PlayerObject.player_xp = 0
        PlayerObject.player_gold = 0
        PlayerObject.player_max_health = 25
        PlayerObject.player_max_explode = 4
        
        PlayerObject.atk_dice = 4
        PlayerObject.atk_dice_min = 1
        PlayerObject.atk_dice_max = 6
        PlayerObject.atk_dice_keep = 3
        PlayerObject.atk_explode_value = [4, 5, 6]
        PlayerObject.player_atk_rolls = []
        PlayerObject.player_exploded_atk_dice = []
        PlayerObject.player_atk_rolls_total = 0
        
        PlayerObject.def_dice_min = 1
        PlayerObject.def_dice_max = 6
        PlayerObject.def_dice = 4
        PlayerObject.def_dice_keep = 3
        PlayerObject.def_explode_value = [1, 2, 3]
        PlayerObject.player_def_rolls = []
        PlayerObject.player_exploded_def_dice = []
        PlayerObject.player_def_rolls_total = []
        
        PlayerObject.Debug = "Player class has been selected"
        
        return PlayerObject.player_gold, PlayerObject.player_max_health, PlayerObject.player_max_explode, PlayerObject.player_xp, PlayerObject.player_class, PlayerObject.player_hitpoints, PlayerObject.atk_dice_min, PlayerObject.atk_dice_max, PlayerObject.atk_dice, PlayerObject.atk_dice_keep, PlayerObject.atk_explode_value, PlayerObject.Debug, PlayerObject.player_atk_rolls, PlayerObject.player_exploded_atk_dice, PlayerObject.def_dice_min, PlayerObject.def_dice_max, PlayerObject.def_dice, PlayerObject.def_dice_keep, PlayerObject.player_def_rolls, PlayerObject.player_exploded_def_dice, PlayerObject.player_def_rolls_total

    else:
        sys.exit()