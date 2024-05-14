from termcolor import cprint
import random
from playerclass import PlayerObject




def roll_player_atk(PlayerObject):
    # Assuming the player object has these attributes set already
    atk_dice_min = PlayerObject.atk_dice_min
    atk_dice_max = PlayerObject.atk_dice_max
    atk_dice = PlayerObject.atk_dice
    atk_dice_keep = PlayerObject.atk_dice_keep
    atk_explode_value = PlayerObject.atk_explode_value
    
    player_atk_rolls = [random.randint(atk_dice_min, atk_dice_max) for _ in range(atk_dice)]
    player_atk_rolls = player_atk_rolls[:atk_dice_keep]

    cprint(f"This is the player atk rolls before they explode: {player_atk_rolls}", 'light_magenta')

    new_rolls = []
    for roll in player_atk_rolls:
        while roll in atk_explode_value:
            roll = random.randint(atk_dice_min, atk_dice_max)  # New roll for each explosion
            new_rolls.append(roll)
            if roll not in atk_explode_value:
                break

    player_atk_rolls.extend(new_rolls)

    cprint(f"This is the player atk rolls after they explode: {player_atk_rolls}", "light_magenta")

    # Assuming there are limits to respect after explosions
    if atk_dice_min is not None:
        player_atk_rolls = [max(roll, atk_dice_min) for roll in player_atk_rolls]
    if atk_dice_max is not None:
        player_atk_rolls = [min(roll, atk_dice_max) for roll in player_atk_rolls]

    cprint(f"This is the final player atk rolls: {player_atk_rolls}", "light_magenta")
    
    player_atk_rolls.sort(reverse=True)
    PlayerObject.player_atk_rolls = player_atk_rolls
    PlayerObject.player_atk_rolls_total = sum(player_atk_rolls)
    PlayerObject.Debug = "I have rolled the player atk dice!"

    return PlayerObject.player_atk_rolls, PlayerObject.Debug, PlayerObject.player_atk_rolls_total



def roll_player_def(PlayerObject):
    # Assuming the player object has these attributes set already
    def_dice_min = PlayerObject.def_dice_min
    def_dice_max = PlayerObject.def_dice_max
    def_dice = PlayerObject.def_dice
    def_dice_keep = PlayerObject.def_dice_keep
    def_explode_value = PlayerObject.def_explode_value
    
    player_def_rolls = [random.randint(def_dice_min, def_dice_max) for _ in range(def_dice)]
    #player_def_rolls.sort(reverse=True)
    player_def_rolls = player_def_rolls[:def_dice_keep]

    cprint(f"This is the player def rolls before they explode: {player_def_rolls}", 'light_magenta')

    new_rolls = []
    for roll in player_def_rolls:
        while roll in def_explode_value:
            roll = random.randint(def_dice_min, def_dice_max)  # New roll for each explosion
            new_rolls.append(roll)
            if roll not in def_explode_value:
                break

    player_def_rolls.extend(new_rolls)

    cprint(f"This is the player def rolls after they explode: {player_def_rolls}", "light_magenta")

    # Assuming there are limits to respect after explosions
    if def_dice_min is not None:
        player_def_rolls = [max(roll, def_dice_min) for roll in player_def_rolls]
    if def_dice_max is not None:
        player_def_rolls = [min(roll, def_dice_max) for roll in player_def_rolls]

    cprint(f"This is the final player def rolls: {player_def_rolls}", "light_magenta")

    player_def_rolls.sort(reverse=True)
    PlayerObject.player_def_rolls = player_def_rolls
    PlayerObject.player_def_rolls_total = sum(player_def_rolls)
    PlayerObject.Debug = "I have rolled the player def dice!"

    return PlayerObject.player_def_rolls, PlayerObject.Debug, PlayerObject.player_def_rolls_total
