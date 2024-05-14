class PlayerObject:
    def __init__(self, player_class, player_max_health, player_gold, player_hitpoints, player_xp, player_dmg, atk_dice_min, atk_dice_max, atk_dice, atk_dice_keep, atk_explode_value, player_atk_rolls, Debug, player_exploded_atk_dice, player_atk_rolls_total, def_dice_min, def_dice_max, def_dice, def_explode_value, def_dice_keep, player_def_rolls, player_exploded_def_dice, player_def_rolls_total):
        
        self.player_class = player_class #player's class
        self.player_hitpoints = player_hitpoints #how many hitpoints they have
        self.player_dmg = player_dmg
        self.player_xp = player_xp
        self.player_gold = player_gold
        self.player_max_health = player_max_health
        #Setting atk dice values
        self.atk_dice_min = atk_dice_min #lowest value of the attack dice
        self.atk_dice_max = atk_dice_max #highest value of the attack dice
        self.atk_dice = atk_dice #how many attack dice they have
        self.atk_dice_keep = atk_dice_keep #how many of the highest dice they will keep after rolling
        self.atk_explode_value = atk_explode_value #the values in which the dice will explode and roll more dice
        self.player_atk_rolls = player_atk_rolls #the list of what the player rolled
        self.player_exploded_atk_dice = player_exploded_atk_dice #the list of the exploded atk rolls
        self.player_atk_rolls_total = player_atk_rolls_total #sum of the list of the atk roll
        
        #setting def dice values
        self.def_dice_min = def_dice_min
        self.def_dice_max = def_dice_max
        self.def_dice = def_dice
        self.def_dice_keep = def_dice_keep
        self.def_explode_value = def_explode_value
        self.player_def_rolls = player_def_rolls
        self.player_exploded_def_dice = player_exploded_def_dice
        self.player_def_rolls_total = player_def_rolls_total
        
        #debug console log
        self.Debug = Debug 
        
        #def player_take_damage(self, player_dmg):
            #self.player_hitpoints -= player_dmg