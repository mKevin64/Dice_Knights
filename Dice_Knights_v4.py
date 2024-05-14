### NOTES ###
    #Make player as a class with stats (hp, attack dice, def dice, etc.)
        #Make Player Classes (Knight, Warrior, Wizard, etc.)
            #MAKE THE PLAYER CLASSES AS SUBCLASSES OF Player_Object
                #make the warrior class and test that with the dice roller before trying to fix the dice roller, since the values will change between the warrior and the knight
                    #ok so the dice roller can work with the different classes, now to make the defence dice roller.
    #Make Dice Roller
        #Start with just player attack dice then work on defence dice
            # Ok so the dice roller *is* working, but it's not perfect yet. will fix it later. need to make it add exploded dice to the list properly *and* not go into an infinite loop
                #fix the dice exploding issue later


### TO DO LIST ###
    #Make the other character classes (Wizard, Monk, Rogue)
        #Add their defence stats as well
            #Added def stats for Knight and Warrior, should finish up by adding the other classes later
    #Refactor and split i up so each like thing is in it's own .py file
        #keep player dice rolls in one file, enemy dice rolls in another, player classes in one, enemy classes in another etc.
    #Make and XP and Leveling system
        #enemy xp should be static while the rewards should be dynamic
            #scale stuff based off player level?
    #Make Item shop to spend gold at
        #start with a health potion, an attack enhancement item, and a defence enhancement item

### THIS IS A TEST COMMENT SO I CAN FIGURE OUT HOW GITHUB AND GITKRAKEN WORK

import sys
from termcolor import cprint
from time import sleep
from playerclass import PlayerObject
from enemyclass import EnemyObject
from player_class_selection import class_selection
from enemy_select import EnemySelect
from player_rolls import roll_player_atk, roll_player_def
from enemy_rolls import roll_enemy_atk, roll_enemy_def
from calcs import calc_enemy_damage, calc_player_damage, calc_hitpoints, calc_rewards
from item_shop import ItemObject, Potion, Weapon, Armor, ShopKeeper



def main():
    
    print("Please Select Your Class")
    player_class = input()
    class_selection(player_class)
    cprint(PlayerObject.Debug, "light_magenta")
    EnemySelect(enemy_type="TestGoblin")
    ShopKeeper.open_shop([], Potion, Weapon, Armor)
    while True:
        while PlayerObject.player_hitpoints > 0:
            if PlayerObject.player_hitpoints > 0:
                roll_player_atk(PlayerObject)
                cprint(PlayerObject.Debug, "light_magenta")
                cprint(PlayerObject.player_atk_rolls, "green")
                cprint(PlayerObject.player_atk_rolls_total, 'green')
                sleep(2)
    
                roll_player_def(PlayerObject)
                cprint(PlayerObject.Debug, "light_magenta")
                cprint(PlayerObject.player_def_rolls, "blue")
                cprint(PlayerObject.player_def_rolls_total, "blue")
                sleep(2)
    
            
                roll_enemy_atk(EnemyObject)
                cprint(EnemyObject.Debug, "light_magenta")
                cprint(EnemyObject.enemy_atk_rolls, "red")
                cprint(EnemyObject.enemy_atk_rolls_total, "red")
                sleep(2)
    
                roll_enemy_def(EnemyObject)
                cprint(EnemyObject.Debug, 'light_magenta')
                cprint(EnemyObject.enemy_def_rolls, "yellow")
                cprint(EnemyObject.enemy_def_rolls_total, 'yellow')
                sleep(2)
    
                calc_enemy_damage(PlayerObject, EnemyObject)
                calc_player_damage(PlayerObject, EnemyObject)
                calc_hitpoints(PlayerObject, EnemyObject)
                cprint(f"Player hitpoints: {PlayerObject.player_hitpoints}", "green")
                cprint(f"Enemy hitpoints: {EnemyObject.enemy_hitpoints}", "yellow")
                sleep(2)

            
                if EnemyObject.enemy_hitpoints <=0 :
                    cprint("You have won!", "green")
                    calc_rewards(PlayerObject, EnemyObject)
                    cprint(f"Experience: {PlayerObject.player_xp}")
                    cprint(f"Gold: {PlayerObject.player_gold}")
                    ShopKeeper.open_shop([], Potion, Weapon, Armor)
                    break
        
                elif PlayerObject.player_hitpoints <= 0:
                    cprint("You have died!", "red")
                    sys.exit()

            
                user_choice = input("Shall you fight on or run away? ")
                if user_choice.lower() == 'fight':
                    continue
                elif user_choice.lower() == 'run':
                    cprint("You have run away from the fight!")
                    sys.exit()








main()