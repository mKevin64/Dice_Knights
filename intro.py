from termcolor import cprint
from time import sleep
import sys

def introduction():
    while True:
        cprint("""
██████  ██  ██████ ███████     ██   ██ ███    ██ ██  ██████  ██   ██ ████████ ███████ 
██   ██ ██ ██      ██          ██  ██  ████   ██ ██ ██       ██   ██    ██    ██      
██   ██ ██ ██      █████       █████   ██ ██  ██ ██ ██   ███ ███████    ██    ███████ 
██   ██ ██ ██      ██          ██  ██  ██  ██ ██ ██ ██    ██ ██   ██    ██         ██ 
██████  ██  ██████ ███████     ██   ██ ██   ████ ██  ██████  ██   ██    ██    ███████ 
                        Welcome to Dice Knights v0.04
        Dice Knights © 2024 by skillkill235 is licensed under CC BY-NC-ND 4.0 
""", "blue")

        cprint("""
Main Menu:
To select an option, type the character within the square brackets []
[I]formation
[H]ow to Play
[P]lay Dice Knights
[Q]uit
""")
        user_input = input()
    
        if user_input.lower() == 'i':
            cprint("""
Dice Knights is a free to play terminal based Roguelite RPG using d6 dice rolls to handle combat, encounters, and more!
Dice Knights is currently under construction with new content added whenever I am able to.""")
            sleep(2)
            cprint("If you have any comments, ideas, or suggestions on how to improve Dice Knights, please leave a comment on my github page.")
            sleep(2)
            cprint("Although Dice Knights is free to play and I highly encourage you to share it, it is under CC BY-NC-ND 4.0")
            sleep(2)
            cprint("Link to github repo: https://github.com/skillkill235/Dice_Knights")
            sleep(2)
            cprint("Link to my github page: https://github.com/skillkill235")
            sleep(2)
            cprint("Thanks for trying out Dice Knights!")
            input("Press Enter to return to main menu.")
    
        elif user_input.lower() == 'h':
            cprint("To play Dice Knights, select a character class to play as from the character selection menu")
            sleep(2)
            cprint("Your character will then fight against enemies by rolling d6 dice for attacking and defending")
            sleep(2)
            cprint("The enemy operates in the same way, attacking and defending by rolling d6 dice")
            sleep(2)
            cprint("If your attacking dice roll total is higher than the enemy defence dice roll total, you will damage the enemy, and vice versa")
            sleep(2)
            cprint("You and the enemy will fight until one of you has perished. If you win you get gold and xp, if you die you get nothing and must start over")
            sleep(2)
            cprint("This game is still a work in progress and some features that are planned may not be functional in game yet, so check the github repo for updates periodically")
            sleep(2)
            cprint("Have fun playing!")
            input("Press Enter to return to main menu.")
            
        elif user_input.lower() == 'p':
            break
        
        elif user_input.lower() == 'q':
            sys.exit()
        else:
            cprint("Please enter the character within [] to make a selection", "red")