class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def spawn(self):
        print(f"A {self.name} has appeared!")
        print(f"Health: {self.health}")


