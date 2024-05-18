
from enemyclass import EnemyObject
import random

def EnemySelect(enemy_type):
    if enemy_type == 'TestGoblin':
        EnemyObject.enemy_type = 'TestGoblin'
        EnemyObject.enemy_name = 'Test Goblin'
        EnemyObject.enemy_hitpoints = 20
        EnemyObject.enemy_dmg = 0
        EnemyObject.enemy_explode_max = 2
        
        EnemyObject.enemy_atk_dice_min = 1
        EnemyObject.enemy_atk_dice_max = 6
        EnemyObject.enemy_atk_dice = 3
        EnemyObject.enemy_atk_dice_keep = 2
        EnemyObject.enemy_atk_explode_value = (0, 6)
        EnemyObject.enemy_atk_rolls = []
        EnemyObject.enemy_exploded_atk_dice = []
        EnemyObject.enemy_atk_rolls_total = 0
        
        EnemyObject.enemy_def_dice_min = 1
        EnemyObject.enemy_def_dice_max = 6
        EnemyObject.enemy_def_dice = 3
        EnemyObject.enemy_def_dice_keep = 2
        EnemyObject.enemy_def_explode_value = (0, 6)
        EnemyObject.enemy_def_rolls = []
        EnemyObject.enemy_exploded_def_dice = []
        EnemyObject.enemy_def_rolls_total = 0
        EnemyObject.xp_value = 25
        EnemyObject.gold_value = random.randint(5, 15)
        return EnemyObject.enemy_type, EnemyObject.enemy_name, EnemyObject.enemy_hitpoints, EnemyObject.enemy_explode_max, EnemyObject.enemy_atk_dice_min, EnemyObject.enemy_atk_dice_max, EnemyObject.enemy_atk_dice, EnemyObject.enemy_atk_dice_keep, EnemyObject.enemy_atk_explode_value, EnemyObject.enemy_atk_rolls, EnemyObject.enemy_exploded_atk_dice, EnemyObject.enemy_atk_rolls_total, EnemyObject.enemy_def_dice_min, EnemyObject.enemy_def_dice_max, EnemyObject.enemy_def_dice, EnemyObject.enemy_def_dice_keep, EnemyObject.enemy_def_explode_value, EnemyObject.enemy_def_rolls, EnemyObject.enemy_exploded_def_dice, EnemyObject.enemy_def_rolls_total
