
from playerclass import PlayerObject
import sys


def class_selection(player_class):
    if player_class.lower() == 'knight':
        print("You have selected: Knight")
        PlayerObject.player_class = 'knight'
        PlayerObject.player_hitpoints = 30
        PlayerObject.player_dmg = 0
        PlayerObject.player_xp = 0
        PlayerObject.player_gold = 50
        PlayerObject.player_max_health = 30
        
        PlayerObject.atk_dice_min = 1
        PlayerObject.atk_dice_max = 6
        PlayerObject.atk_dice = 4
        PlayerObject.atk_dice_keep = 3
        PlayerObject.atk_explode_value = (5, 6)
        PlayerObject.player_atk_rolls = []
        PlayerObject.player_exploded_atk_dice = []
        PlayerObject.player_atk_rolls_total= 0
        
        PlayerObject.def_dice_min = 1
        PlayerObject.def_dice_max = 6
        PlayerObject.def_dice = 4
        PlayerObject.def_dice_keep = 3
        PlayerObject.def_explode_value = (5, 6)
        PlayerObject.player_def_rolls = []
        PlayerObject.player_exploded_def_dice = []
        PlayerObject.player_def_rolls_total = 0
        
        PlayerObject.Debug = "Player Class has successfully selected"
        
        return PlayerObject.player_gold, PlayerObject.player_max_health, PlayerObject.player_xp, PlayerObject.player_class, PlayerObject.player_hitpoints, PlayerObject.atk_dice_min, PlayerObject.atk_dice_max, PlayerObject.atk_dice, PlayerObject.atk_dice_keep, PlayerObject.atk_explode_value, PlayerObject.Debug, PlayerObject.player_atk_rolls, PlayerObject.player_exploded_atk_dice, PlayerObject.def_dice_min, PlayerObject.def_dice_max, PlayerObject.def_dice, PlayerObject.def_dice_keep, PlayerObject.player_def_rolls, PlayerObject.player_exploded_def_dice, PlayerObject.player_def_rolls_total
        
    elif player_class.lower() == "warrior":
        print("You have selected: Warrior")
        PlayerObject.player_class = 'warrior'
        PlayerObject.player_hitpoints = 35
        PlayerObject.player_dmg = 0
        PlayerObject.player_xp = 0
        PlayerObject.player_gold = 0
        PlayerObject.player_max_health = 35
        
        PlayerObject.atk_dice_min = 1
        PlayerObject.atk_dice_max = 6
        PlayerObject.atk_dice = 5
        PlayerObject.atk_dice_keep = 4
        PlayerObject.atk_explode_value = (5, 6)
        PlayerObject.player_atk_rolls = []
        PlayerObject.player_exploded_atk_dice = []
        PlayerObject.player_atk_rolls_total= 0
        
        PlayerObject.def_dice_min = 1
        PlayerObject.def_dice_max = 6
        PlayerObject.def_dice = 3
        PlayerObject.def_dice_keep = 2
        PlayerObject.def_explode_value = (0, 6)
        PlayerObject.player_def_rolls = []
        PlayerObject.player_exploded_def_dice = []
        PlayerObject.player_def_rolls_total = 0
        
        
        
        PlayerObject.Debug = "Player Class has successfully selected"
    
    
        return PlayerObject.player_gold, PlayerObject.player_max_health, PlayerObject.player_xp, PlayerObject.player_class, PlayerObject.player_hitpoints, PlayerObject.atk_dice_min, PlayerObject.atk_dice_max, PlayerObject.atk_dice, PlayerObject.atk_dice_keep, PlayerObject.atk_explode_value, PlayerObject.Debug, PlayerObject.player_atk_rolls, PlayerObject.player_exploded_atk_dice, PlayerObject.def_dice_min, PlayerObject.def_dice_max, PlayerObject.def_dice, PlayerObject.def_dice_keep, PlayerObject.player_def_rolls, PlayerObject.player_exploded_def_dice, PlayerObject.player_def_rolls_total
    else:
        sys.exit()