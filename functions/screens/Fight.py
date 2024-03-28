import random

from classes.Enemy import Enemy
from functions.screens import startScreen
from functions.screens.startScreen import get_user


def fight():
    print('Welcome to the fight!')

    name = "Moth"
    health = random.randrange(30,60,5)
    damage = random.randrange(5,15,5)
    reward = random.randrange(5,15,5)
    currentEnemy = Enemy(name, health, damage)
    currentEnemy.spawn()
    
    while currentEnemy.health > 0 and get_user().health > 0:
        input("\n\nPress enter to attack!")

        print("You attacked the enemy!")
        currentEnemy.health -= get_user().damage
        print(f"Enemy health: {currentEnemy.health}")

        print("The enemy attacked you!")
        get_user().health -= currentEnemy.damage
        print(f"Your health: {get_user().health}")

    if currentEnemy.health <= 0:
        print("You defeated the enemy!")
        get_user().coins += reward
        print(f"Coins: {get_user().coins}")

    elif get_user().health <= 0:
        print("You lost!")
        print("Game over!")
        startScreen()