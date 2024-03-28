import random

from classes.Weapon import Weapon
from functions.screens.menuScreen import menuScreen
from functions.screens.startScreen import get_user


def shop():
    items = {
        1: ["Sword", random.randint(15,20), 0, 50],
        2: ["Bow", random.randint(10,15), 0, 40],
        3: ["Potion", 0, 0, 10],
    }
    print("Welcome to the shop!")
    print("Items for sale:")
    for item, value in items.items():
        print(f'{item}. {value[0]} - {value[1]} damage - {value[2]} range - ${value[3]}')
    print("Press Enter to exit shop")

    try:
        choice = input("Make your selection: ")
        if choice == "":
            menuScreen()
        elif int(choice) in items:
            item = items[int(choice)]
            if get_user().coins >= item[3]:
                weapon = Weapon(item[0], item[1], item[2], item[3])
                weapon.buy()
            else:
                print("You don't have enough coins!")
        else:
            print("Invalid choice. Please try again.")
            shop()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        shop()
    menuScreen()
