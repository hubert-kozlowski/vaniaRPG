import random

from classes.Player import Player


def startScreen():
    from functions.screens.menuScreen import menuScreen
    print("Welcome to the game!")
    print(''' 
    1. Start  
    2. Exit
    ''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        nameInput = input("Enter your name: ")
        starterCash = 100
        damage = random.randint(5,10)

        global user # make user a global variable
        user = Player(nameInput, 100, damage, starterCash, [])
                    # name, health, damage, coins, inventory

        print(f"Welcome {nameInput}!")
        print(f"Your stats: \nHealth: {user.health}\nDamage: {user.damage}\nCoins: {user.coins}\nInventory: {user.inventory}")

        menuScreen()

    elif choice == 2:
        print("game exit!!11!!")
    else:
        print("choose valid number\n\n")
        startScreen()


def get_user():
    global user
    return user