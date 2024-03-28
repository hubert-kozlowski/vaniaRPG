from functions.screens.startScreen import get_user


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



