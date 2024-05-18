


from enemyclass import EnemyObject
from playerclass import PlayerObject
from termcolor import cprint

def calc_enemy_damage(PlayerObject, EnemyObject):
    
    player_atk_rolls_total = PlayerObject.player_atk_rolls_total
    enemy_def_rolls_total = EnemyObject.enemy_def_rolls_total
    
    if player_atk_rolls_total > enemy_def_rolls_total:
        EnemyObject.enemy_dmg = player_atk_rolls_total - enemy_def_rolls_total
        cprint(f"The enemy has taken {EnemyObject.enemy_dmg} points of damage!", "light_red")
        return EnemyObject.enemy_dmg
    elif player_atk_rolls_total <= enemy_def_rolls_total:
        EnemyObject.enemy_dmg = 0
        cprint(f"The enemy has taken no damage!", "light_magenta")
        return EnemyObject.enemy_dmg

def calc_player_damage(PlayerObject, EnemyObject):
    
    enemy_atk_rolls_total = EnemyObject.enemy_atk_rolls_total
    player_def_rolls_total = PlayerObject.player_def_rolls_total
    
    if enemy_atk_rolls_total > player_def_rolls_total:
        PlayerObject.player_dmg = enemy_atk_rolls_total - player_def_rolls_total
        cprint(f"The player has taken {PlayerObject.player_dmg} points of damage!", "light_red")
        return PlayerObject.player_dmg
    elif enemy_atk_rolls_total <= player_def_rolls_total:
        PlayerObject.player_dmg = 0
        #cprint(f"The player has taken no damage!", 'light_magenta')
        return PlayerObject.player_dmg
    

def calc_hitpoints(PlayerObject, EnemyObject):
    
    
    PlayerObject.player_hitpoints -= max(0, PlayerObject.player_dmg)
    EnemyObject.enemy_hitpoints -= max(0, EnemyObject.enemy_dmg)
    
    cprint(f"The Player and the Enemy have taken damage!", "light_magenta")
    
    return PlayerObject.player_hitpoints, EnemyObject.enemy_hitpoints

def calc_rewards(PlayerObject, EnemyObject):
    
    PlayerObject.player_xp += EnemyObject.xp_value
    PlayerObject.player_gold += EnemyObject.gold_value
    return PlayerObject.player_xp, PlayerObject.player_gold