import random


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





class Weapon:
    def __init__(self, name, damage, range, cost):
        self.name = name
        self.damage = damage
        self.range = range
        self.cost = cost

    def buy(self):
        print(f'You bought {self.name} for {self.cost} coins!')
        user.coins -= self.cost
        user.inventory.append(self)





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
        starterCash = 100

        global user # make user a global variable
        user = Player(nameInput, 100, 10, starterCash, [])

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

    name = "Moth"
    health = random.randrange(30,60,5)
    damage = random.randrange(5,15,5)
    reward = random.randrange(5,15,5)
    currentEnemy = Enemy(name, health, damage)
    currentEnemy.spawn()
    
    while currentEnemy.health > 0 and user.health > 0:
        input("\n\nPress enter to attack!")

        print("You attacked the enemy!")
        currentEnemy.health -= user.damage
        print(f"Enemy health: {currentEnemy.health}")

        print("The enemy attacked you!")
        user.health -= currentEnemy.damage
        print(f"Your health: {user.health}")

    if currentEnemy.health <= 0:
        print("You defeated the enemy!")
        user.coins += reward
        print(f"Coins: {user.coins}")

    elif user.health <= 0:
        print("You lost!")
        print("Game over!")
        startScreen()







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






def inventory():
    print(f'''Inventory - {user.name} - ${user.coins} - [{len(user.inventory)}]
          ''')
    
    for item in user.inventory:
        print(f'{item.name} - {item.damage} - {item.range} - ${item.cost}')
        
    input("Press enter to continue...")
    menuScreen()






def shop():
    items = { # name, damage, range, cost
        1 : ["Sword", 20, 0, 50],
        2 : ["Bow", 15, 0, 40],
        3 : ["Potion", 0, 0, 10],
    }
    print("Welcome to the shop!")
    print("Items for sale:")
    for item, value in items.items():
        print(f'{item}. {value[0]} - {value[1]} damage - {value[2]} range - ${value[3]}')

    choice = int(input("Enter the number of the item you want to buy: "))
    if choice in items:
        item = items[choice]
        if user.coins >= item[3]:
            weapon = Weapon(item[0], item[1], item[2], item[3])
            weapon.buy()
        else:
            print("You don't have enough coins!")
    else:
        print("Invalid choice. Please try again.")
        shop()
    menuScreen()





startScreen() 
