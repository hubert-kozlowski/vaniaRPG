import random

from classes.Enemy import Enemy
from classes.Player import Player
from functions.LeaveGame import leaveGame
from functions.screens import Battle
from functions.screens.Battle import Battle  # Import the Battle class
from functions.screens.startScreen import get_user  # Import get_user function


def menuScreen():
    from functions.screens import Inventory, Shop, Stats, startScreen
    print("Menu Screen")
    choices = {
        1: ["Fight", "Fight the ugly birds", Battle],  # Pass the Battle class itself
        2: ["Shop", "Buy weapons and potions", Shop],
        3: ["Inventory", "Check your inventory", Inventory],
        4: ["Stats", "Check your stats", Stats],
        5: ["Exit", "Exit the game", leaveGame],
    }
    for choice, value in choices.items():
        print(f'{choice}. {value[0]} - "{value[1]}"')
    selection = int(input("\nEnter your choice: ")) 

    if selection == 1:  # If the user chooses to fight
        user = get_user()  # Get the user object
        player = user
        enemies = [
            Enemy("Moth", random.randrange(30, 60, 5), random.randrange(5, 15, 5), random.randrange(5, 15, 5)),
            Enemy("Spider", random.randrange(40, 70, 5), random.randrange(5, 15, 5), random.randrange(5, 15, 5)),
            # Add more enemies as needed
        ]
        battle = value[2](player, enemies)  # Create a Battle object using the Battle class
        battle.start()
    elif selection in choices:
        action = choices[selection]
        print(f'You selected {action[0]}. {action[1]}')
        if len(action) == 3:
            action[2]()
    else:
        print("Invalid choice. Please try again.")
        menuScreen()
