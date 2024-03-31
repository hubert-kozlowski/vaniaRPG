class Player:
    def __init__(self, name, health, damage, coins, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.coins = coins
        self.inventory = inventory

    def attack(self, enemy): # enemy is an instance of the Enemy class
        print("You attacked the enemy!")
        enemy.health -= self.damage
        print(f"Enemy health: {enemy.health}")

    def is_alive(self): # returns True if the player's health is greater than 0
        return self.health > 0