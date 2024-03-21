import random


def shop():
    print("Welcome to the shop!")

def inventory():
    print("Welcome to the inventory!")

def stats():
    print("Welcome to the stats!")


#### Player --> Stats (health, damage, speed, etc.) <-- attack = rizz?
#### Enemy (moths) <-- attack = friendzone?
#### Way to fight enemies
#### Weapons (sword, bow, etc.)
#### Shop system (buying weapons, potions, etc.)


class Player:
    def __init__(self, name, health, damage, coins, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.coins = coins
        self.inventory = inventory


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def spawn(self):
        print(f"A {self.name} has appeared!")
        print(f"Health: {self.health}")

def startScreen():
    print("Welcome to the game!")
    print(''' 
    1. Start  
    2. Exit
    ''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        nameInput = input("Enter your name: ")

        user = Player(nameInput, 100, 10, 0, [])

        print(f"Welcome {nameInput}!")
        print(f"Your stats: \nHealth: {user.health}\nDamage: {user.damage}\nCoins: {user.coins}\nInventory: {user.inventory}")

        menuScreen()

    elif choice == 2:
        print("game exit!!11!!")
    else:
        print("choose valid number\n\n")
        startScreen()






def fight():
    print('Welcome to the fight!')
    health = random.randrange(30,60,5)
    currentEnemy = Enemy("Moth", health, 5)
    currentEnemy.spawn()
    
    input("Press enter to attack!")

    print("You attacked the enemy!")
    currentEnemy.health -= user.damage
    print(f"Enemy health: {currentEnemy.health}")

    print("The enemy attacked you!")
    user.health -= currentEnemy.damage
    print(f"Your health: {user.health}")







def menuScreen():
    print("Menu Screen")
    choices = {
        1 : ["Fight", "Fight the ugly birds", fight],
        2 : ["Shop", "Buy weapons and potions", shop],
        3 : ["Inventory", "Check your inventory", inventory],
        4 : ["Stats", "Check your stats", stats],
        5 : ["Exit", "Exit the game" ],
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





startScreen() 
