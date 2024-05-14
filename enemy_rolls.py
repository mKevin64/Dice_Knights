from enemyclass import EnemyObject
import random
from termcolor import cprint

def roll_enemy_atk(EnemyObject):
    
    enemy_atk_dice_min = EnemyObject.enemy_atk_dice_min
    enemy_atk_dice_max = EnemyObject.enemy_atk_dice_max
    enemy_atk_dice = EnemyObject.enemy_atk_dice
    enemy_atk_dice_keep = EnemyObject.enemy_atk_dice_keep
    enemy_atk_explode_value = EnemyObject.enemy_atk_explode_value
    
    enemy_atk_rolls = [random.randint(enemy_atk_dice_min, enemy_atk_dice_max) for _ in range(enemy_atk_dice)]
    enemy_atk_rolls.sort(reverse=True)
    enemy_atk_rolls = enemy_atk_rolls[:enemy_atk_dice_keep]
    
    cprint(f"This is the enemy atk rolls before they explode: {enemy_atk_rolls}", "light_magenta")
    
    new_rolls = []
    for roll in enemy_atk_rolls:
        while roll in enemy_atk_explode_value:
            roll = random.randint(enemy_atk_dice_min, enemy_atk_dice_max)
            new_rolls.append(roll)
            if roll not in enemy_atk_explode_value:
                break
    
    enemy_atk_rolls.extend(new_rolls)
    
    cprint(f"This is the enemy atk rolls after they explode: {enemy_atk_rolls}", "light_magenta")
    
    if enemy_atk_dice_min is not None:
        enemy_atk_rolls = [max(roll, enemy_atk_dice_min) for roll in enemy_atk_rolls]
    if enemy_atk_dice_max is not None:
        enemy_atk_rolls = [min(roll, enemy_atk_dice_max) for roll in enemy_atk_rolls]
        
    cprint(f"This is the final enemy atk rolls: {enemy_atk_rolls}", "light_magenta")
    
    enemy_atk_rolls.sort(reverse=True)
    EnemyObject.enemy_atk_rolls = enemy_atk_rolls
    EnemyObject.enemy_atk_rolls_total = sum(enemy_atk_rolls)
    EnemyObject.Debug = "I have rolled the enemy atk dice!"
    
    return EnemyObject.enemy_atk_rolls, EnemyObject.Debug, EnemyObject.enemy_atk_rolls_total


def roll_enemy_def(EnemyObject):
    
    enemy_def_dice_min = EnemyObject.enemy_def_dice_min
    enemy_def_dice_max = EnemyObject.enemy_def_dice_max
    enemy_def_dice = EnemyObject.enemy_def_dice
    enemy_def_dice_keep = EnemyObject.enemy_def_dice_keep
    enemy_def_explode_value = EnemyObject.enemy_def_explode_value
    
    enemy_def_rolls = [random.randint(enemy_def_dice_min, enemy_def_dice_max) for _ in range(enemy_def_dice)]
    #enemy_def_rolls.sort(reverse=True)
    enemy_def_rolls = enemy_def_rolls[:enemy_def_dice_keep]
    
    cprint(f"This is the enemy def rolls before they explode: {enemy_def_rolls}", 'light_magenta')
    
    new_rolls = []
    for roll in enemy_def_rolls:
        while roll in enemy_def_explode_value:
            roll = random.randint(enemy_def_dice_min, enemy_def_dice_max)
            new_rolls.append(roll)
            if roll not in enemy_def_explode_value:
                break
    
    enemy_def_rolls.extend(new_rolls)
    
    cprint(f"This is the enemy def rolls after they explode: {enemy_def_rolls}", 'light_magenta')
    
    if enemy_def_dice_min is not None:
        enemy_def_rolls = [max(roll, enemy_def_dice_min) for roll in enemy_def_rolls]
    if enemy_def_dice_max is not None:
        enemy_def_rolls = [min(roll, enemy_def_dice_max) for roll in enemy_def_rolls]
    
    enemy_def_rolls.sort(reverse=True)
    EnemyObject.enemy_def_rolls = enemy_def_rolls
    EnemyObject.enemy_def_rolls_total = sum(enemy_def_rolls)
    EnemyObject.Debug = 'I have rolled the enemy def dice!'
    
    return EnemyObject.enemy_def_rolls, EnemyObject.enemy_def_rolls_total, EnemyObject.Debug