
from time import sleep
from enemyclass import EnemyObject
from playerclass import PlayerObject
import calcs
from termcolor import cprint


def print_text(PlayerObject, EnemyObject):

    cprint(f"Your attack rolls: {PlayerObject.player_atk_rolls}", "green")
    cprint(F"Your attack roll total: {PlayerObject.player_atk_rolls_total}", "green")
    sleep(1)
    cprint(f"The {EnemyObject.enemy_name}'s attack rolled: {EnemyObject.enemy_atk_rolls}", "light_red")
    cprint(f"The {EnemyObject.enemy_name} rolled a total of: {EnemyObject.enemy_atk_rolls_total}", "light_red")
    sleep(1)
    cprint(f"Your defense rolls: {PlayerObject.player_def_rolls}", "blue")
    cprint(f"Your defense roll total: {PlayerObject.player_def_rolls_total}")
    sleep(1)
    cprint(f"The {EnemyObject.enemy_name}'s defense rolled: {EnemyObject.enemy_def_rolls}", "yellow")
    cprint(f"The {EnemyObject.enemy_name} rolled a total of: {EnemyObject.enemy_def_rolls_total}", "yellow")
    sleep(1)