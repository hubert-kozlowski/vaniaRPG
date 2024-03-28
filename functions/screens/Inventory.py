from functions.screens.menuScreen import menuScreen
from functions.screens.startScreen import get_user


def inventory():
    print(f'''Inventory - {user.name} - ${user.coins} - [{len(user.inventory)}]
          ''')
    
    for item in user.inventory:
        print(f'{item.name} - {item.damage} - {item.range} - ${item.cost}')
        
    input("Press enter to continue...")
    menuScreen()