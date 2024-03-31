import random

from classes.Enemy import Enemy
from classes.Player import Player
from functions.screens import startScreen
from functions.screens.startScreen import get_user


class Battle:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def start(self):
        print('Welcome to the fight!')

        for enemy in self.enemies:
            enemy.spawn()

        while self.player.is_alive() and any(enemy.is_alive() for enemy in self.enemies):
            input("\n\nPress enter to attack!")
            for enemy in self.enemies:
                if enemy.is_alive():
                    self.player.attack(enemy)

                    if enemy.is_alive():
                        enemy.attack(self.player)

        if all(not enemy.is_alive() for enemy in self.enemies):
            print("You defeated all enemies!")
            for enemy in self.enemies:
                self.player.coins += enemy.reward
            print(f"Coins: {self.player.coins}")
        else:
            print("You lost!")
            print("Game over!")