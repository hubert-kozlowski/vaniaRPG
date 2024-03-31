from screens import Battle

from functions.LeaveGame import leaveGame


def menuScreen():
    from functions.screens import Inventory, Shop, Stats, startScreen
    print("Menu Screen")
    choices = {
        1 : ["Fight", "Fight the ugly birds", Battle],
        2 : ["Shop", "Buy weapons and potions", Shop],
        3 : ["Inventory", "Check your inventory", Inventory],
        4 : ["Stats", "Check your stats", Stats],
        5 : ["Exit", "Exit the game", leaveGame],
    }
    for choice, value in choices.items():
        print(f'{choice}. {value[0]} - "{value[1]}"')
    selection = int(input("\nEnter your choice: ")) 
    
    if selection in choices:
        action = choices[selection]
        print(f'You selected {action[0]}. {action[1]}')
        action[2]()
    else:
        print("Invalid choice. Please try again.")
        menuScreen()



