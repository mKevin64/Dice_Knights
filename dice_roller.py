import random
from playerclass import PlayerObject
from enemyclass import EnemyObject
from termcolor import cprint

def roll_the_dice(PlayerObject, EnemyObject):
    
    ### ROLLING PLAYER DICE ###
        ### ROLLING PLAYER ATK DICE
    player_atk_rolls = [random.randint(PlayerObject.atk_dice_min, PlayerObject.atk_dice_max) for _ in range(PlayerObject.atk_dice)]
    player_atk_rolls = player_atk_rolls[:PlayerObject.atk_dice_keep]
    #cprint(f"This is the player atk rolls before they explode: {player_atk_rolls}", "light_yellow")
    
    exploded_player_rolls = []
    explode_counter = 0
    for roll in player_atk_rolls:
        while roll in PlayerObject.atk_explode_value and explode_counter < PlayerObject.player_max_explode:
            roll = random.randint(PlayerObject.atk_dice_min, PlayerObject.atk_dice_max)
            exploded_player_rolls.append(roll)
            explode_counter += 1
    player_atk_rolls.extend(exploded_player_rolls)
    #cprint(f"This is the player atk rolls after they explode {player_atk_rolls}", "light_yellow")
    
    
    player_atk_rolls.sort(reverse=True)
    PlayerObject.player_atk_rolls = player_atk_rolls
    PlayerObject.player_atk_rolls_total = sum(player_atk_rolls)
    PlayerObject.Debug = "I have rolled the player atk dice!"
    
        ### ROLLING PLAYER DEF DICE  ###
    player_def_rolls = [random.randint(PlayerObject.def_dice_min, PlayerObject.def_dice_max) for _ in range(PlayerObject.def_dice)]
    player_def_rolls = player_def_rolls[:PlayerObject.def_dice_keep]
    #cprint(f"This is the player def rolls before they explode: {player_def_rolls}", "light_yellow")
    
    exploded_player_rolls = []
    explode_counter = 0
    for roll in player_def_rolls:
        while roll in PlayerObject.def_explode_value and explode_counter < PlayerObject.player_max_explode:
            roll = random.randint(PlayerObject.def_dice_min, PlayerObject.def_dice_max)
            exploded_player_rolls.append(roll)
            explode_counter += 1
    player_def_rolls.extend(exploded_player_rolls)
    #cprint(f"This is the player def rolls after they explode {player_def_rolls}", "light_yellow")
    
    player_def_rolls.sort(reverse=True)
    PlayerObject.player_def_rolls = player_def_rolls
    PlayerObject.player_def_rolls_total = sum(player_def_rolls)
    PlayerObject.Debug = "I have rolled the dice!"
    
    ### ROLLING ENEMY DICE ###
        ### ROLLING ENEMY ATK DICE ###
    enemy_atk_rolls = [random.randint(EnemyObject.enemy_atk_dice_min, EnemyObject.enemy_atk_dice_max) for _ in range(EnemyObject.enemy_atk_dice)]
    enemy_atk_rolls = enemy_atk_rolls[:EnemyObject.enemy_atk_dice_keep]
    #cprint(f"This is the enemy atk rolls before they explode: {enemy_atk_rolls}", "red")
    
    exploded_enemy_rolls = []
    explode_counter = 0
    for roll in enemy_atk_rolls:
        while roll in EnemyObject.enemy_atk_explode_value and explode_counter < EnemyObject.enemy_explode_max:
            roll = random.randint(EnemyObject.enemy_atk_dice_min, EnemyObject.enemy_atk_dice_max)
            exploded_enemy_rolls.append(roll)
            explode_counter += 1
    enemy_atk_rolls.extend(exploded_enemy_rolls)
    
    enemy_atk_rolls.sort(reverse=True)
    EnemyObject.enemy_atk_rolls = enemy_atk_rolls
    EnemyObject.enemy_atk_rolls_total =sum(enemy_atk_rolls)
    EnemyObject.Debug = "I have rolled the enemy atk dice!"
    
    
        ### ROLLING ENEMY DEF DICE ###
    enemy_def_rolls = [random.randint(EnemyObject.enemy_def_dice_min, EnemyObject.enemy_def_dice_max) for _ in range(EnemyObject.enemy_def_dice)]
    enemy_def_rolls = enemy_def_rolls[:EnemyObject.enemy_def_dice_keep]
    
    exploded_enemy_rolls = []
    explode_counter = 0
    for roll in enemy_def_rolls:
        while roll in EnemyObject.enemy_def_explode_value and explode_counter < EnemyObject.enemy_explode_max:
            roll = random.randint(EnemyObject.enemy_def_dice_min, EnemyObject.enemy_def_dice_max)
            exploded_enemy_rolls.append(roll)
            explode_counter +=1
    enemy_def_rolls.extend(exploded_enemy_rolls)
    
    enemy_def_rolls.sort(reverse=True)
    EnemyObject.enemy_def_rolls = enemy_def_rolls
    EnemyObject.enemy_def_rolls_total = sum(enemy_def_rolls)
    EnemyObject.Debug = "I have rolled the enemy def dice!"
    
    return PlayerObject.player_atk_rolls, PlayerObject.player_atk_rolls_total, PlayerObject.player_def_rolls, PlayerObject.player_def_rolls_total, EnemyObject.enemy_atk_rolls, EnemyObject.enemy_atk_rolls_total, EnemyObject.enemy_def_rolls, EnemyObject.enemy_def_rolls_total