class EnemyObject:
    def __init__(self, enemy_type, enemy_name, enemy_max_health, enemy_explode_max, enemy_hitpoints, xp_value, enemy_dmg, enemy_atk_dice_min, enemy_atk_dice_max, enemy_atk_dice, enemy_atk_dice_keep, enemy_atk_explode_value, enemy_atk_rolls, enemy_exploded_atk_dice, enemy_atk_rolls_total, enemy_def_dice_min, enemy_def_dice_max, enemy_def_dice, enemy_def_dice_keep, enemy_def_explode_value, enemy_def_rolls, enemy_exploded_def_dice, enemy_def_rolls_total, enemy_Debug):
        
        self.enemy_type = enemy_type
        self.enemy_name = enemy_name
        self.enemy_max_health = enemy_max_health
        self.enemy_hitpoints = enemy_hitpoints
        self.enemy_dmg = enemy_dmg
        self.enemy_atk_dice_min = enemy_atk_dice_min
        self.enemy_atk_dice_max = enemy_atk_dice_max
        self.enemy_atk_dice = enemy_atk_dice
        self.enemy_atk_dice_keep = enemy_atk_dice_keep
        self.enemy_atk_explode_value = enemy_atk_explode_value
        self.enemy_atk_rolls = enemy_atk_rolls
        self.enemy_exploded_atk_dice = enemy_exploded_atk_dice
        self.enemy_atk_rolls_total = enemy_atk_rolls_total
        self.enemy_explode_max = enemy_explode_max
        
        self.enemy_def_dice_min = enemy_def_dice_min
        self.enemy_def_dice_max = enemy_def_dice_max
        self.enemy_def_dice = enemy_def_dice
        self.enemy_def_dice_keep = enemy_def_dice_keep
        self.enemy_def_explode_value = enemy_def_explode_value
        self.enemy_def_rolls = enemy_def_rolls
        self.enemy_exploded_def_dice = enemy_exploded_def_dice
        self.enemy_def_rolls_total = enemy_def_rolls_total
        
        self.xp_value = xp_value
        self.enemy_Debug = enemy_Debug
        
        #def enemy_take_damage(self, enemy_dmg):
            # self.enemy_hitpoints -= enemy_dmg