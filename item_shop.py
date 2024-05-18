
import random
from playerclass import PlayerObject
from termcolor import cprint

class ItemObject(): #master item object class
    def __init__(self, item_type, item_cost, item_name, item_description):
        
        self.item_type = item_type
        self.item_cost = item_cost
        self.item_name = item_name
        self.item_description = item_description

class Potion(ItemObject): #potion subclass of item object
    
    def __init__(self, item_type, item_cost, item_name, item_description):
        super().__init__(item_type, item_cost, item_name, item_description)
        
    item_type = 'Potion'
    item_cost = random.randint(3, 7)
    item_name = 'Potion of Healing'
    item_description = 'Restore you to full health'
        
    def potion_effect(PlayerObject):
        PlayerObject.player_hitpoints+= PlayerObject.player_max_health
        if PlayerObject.player_hitpoints > PlayerObject.player_max_health:
            PlayerObject.player_hitpoints = PlayerObject.player_max_health

        return PlayerObject.player_hitpoints

class Weapon(ItemObject):
    def __init__(self, item_type, item_cost, item_name, item_description):
        super().__init__(item_type, item_cost, item_name, item_description)
        
    item_type = 'Weapon'
    item_cost = random.randint(6, 10)
    item_name = 'Sword of Sharpness'
    item_description = 'Increase your attack dice and attack dice keep by 1'
        
    def weapon_effect(PlayerObject):
        PlayerObject.atk_dice += 1
        PlayerObject.atk_dice_keep += 1
        return PlayerObject.atk_dice_keep, PlayerObject.atk_dice


class Armor(ItemObject):
    def __init__(self, item_type, item_cost, item_name, item_description):
        super().__init__(item_type, item_cost, item_name, item_description)
        
    item_type = 'Armor'
    item_cost = random.randint(4,8)
    item_name = 'Shield of Defense'
    item_description = 'Increase your defence dice and defence dice keep by 1'
        
    def armor_effect(PlayerObject):
        PlayerObject.def_dice += 1
        PlayerObject.def_dice_keep += 1
        return PlayerObject.def_dice, PlayerObject.def_dice_keep

    
    
class ShopKeeper():
    def __init__(self, item_list):
        self.item_list = item_list
    def open_shop(Potion, Weapon, Armor):
        item_list = []
        item_list.append(Potion.item_type)
        item_list.append(Weapon.item_type)
        item_list.append(Armor.item_type)
            
        cprint(f"Welcome to my shop, what would you like to buy?\n" + f"{item_list}", 'cyan')
        
        what_to_buy = input()
            
        if what_to_buy.lower() == 'potion':
            cprint(f"Would you like to buy {Potion.item_name} ?")
            cprint(f"The {Potion.item_name} will {Potion.item_description}")
            confirm_purchase = input()
            if confirm_purchase.lower() == 'y' and PlayerObject.player_gold >= Potion.item_cost:
                PlayerObject.player_gold -= Potion.item_cost
                Potion.potion_effect(PlayerObject)
                return PlayerObject.player_gold
            else:
                cprint("Not enough gold", "red")
        if what_to_buy.lower() == 'armor':
            cprint(f"Would you like to buy {Armor.item_name} ?")
            cprint(f"The {Armor.item_name} will {Armor.item_description}")
            confirm_purchase = input()
            if confirm_purchase.lower() == 'y' and PlayerObject.player_gold >= Armor.item_cost:
                PlayerObject.player_gold -= Armor.item_cost
                Armor.armor_effect(PlayerObject)
                return PlayerObject.player_gold
            else:
                cprint("Not enough gold", "red")
        if what_to_buy.lower() == 'weapon':
            cprint(f"Would you like to buy {Weapon.item_name} ?")
            cprint(f"The {Weapon.item_name} will {Weapon.item_description}")
            confirm_purchase = input()
            if confirm_purchase.lower() == 'y' and PlayerObject.player_gold >= Armor.item_cost:
                PlayerObject.player_gold -= Weapon.item_cost
                Weapon.weapon_effect(PlayerObject)
                return PlayerObject.player_gold
            else:
                cprint("Not enough gold", "red")