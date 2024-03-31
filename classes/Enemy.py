class Enemy:
    def __init__(self, name, health, damage, reward):
        self.name = name
        self.health = health
        self.damage = damage
        self.reward = reward

    def attack(self, player): # player is an instance of the Player class
        print("The enemy attacked you!")
        player.health -= self.damage
        print(f"Your health: {player.health}")

    def is_alive(self): # returns True if the enemy's health is greater than 0
        return self.health > 0

    def spawn(self): # prints the enemy's name and health
        print(f"A {self.name} has appeared!")
        print(f"Health: {self.health}")