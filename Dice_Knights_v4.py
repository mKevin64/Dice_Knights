
### TO DO LIST ###
### PRIORITIZE ITEMS HIGHER UP ###
    #Finish making character classes
    #Make Character Class Selector better (info about classes, make sure of player choice, etc.)
    #Add intro screen that has how to play, general info, etc.
    #Make Leveling System
    #Add more enemies
    #Add more items
    #Make items in shop randomly generated
    #Add inventory system for player
    #Make Random Dungeon Map Generator
    #Make Random Encounter Generator
    
    
    
    
import sys
from termcolor import cprint
from time import sleep
from playerclass import *
from enemyclass import *
from player_class_selection import *
from enemy_select import *
from dice_roller import *
from calcs import *
from item_shop import *
from printer import *


def main():
    
    print("Please Select Your Class")
    player_class = input()
    class_selection(player_class)
    #cprint(PlayerObject.Debug, "light_magenta")
    EnemySelect(enemy_type="TestGoblin")
    
    while True:
        while PlayerObject.player_hitpoints > 0:
            
            if PlayerObject.player_hitpoints > 0:
                
                roll_the_dice(PlayerObject, EnemyObject)
                print_text(PlayerObject, EnemyObject)
                calc_player_damage(PlayerObject, EnemyObject)
                calc_enemy_damage(PlayerObject, EnemyObject)
                calc_hitpoints(PlayerObject, EnemyObject)
                
                if EnemyObject.enemy_hitpoints <= 0:
                    calc_rewards(PlayerObject, EnemyObject)
                    cprint(f"You have won the fight against {EnemyObject.enemy_name}", "light_green")
                    cprint(f"Current HP: {PlayerObject.player_hitpoints}", "blue")
                    cprint(f"Current XP: {PlayerObject.player_xp}", "blue")
                    cprint(f"Current Gold: {PlayerObject.player_gold}", "light_yellow")
                    ShopKeeper.open_shop(Potion, Weapon, Armor)
                
                elif PlayerObject.player_hitpoints <= 0:
                    cprint(f"You have died! Would you like to play again? [Y]es / [N]o")
                    user_input = input()
                    if user_input.lower() == 'y':
                        break
                    elif user_input.lower() == 'n':
                            sys.exit()
                    
                
                
                




main()