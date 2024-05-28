import random
class Hero(object):
    def __init__(self, name, health, attack_power, armor_points):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.armor_points = armor_points
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, other):
        print(f"Игрок {self.name} атаковал игрока { other.name}" )
        miss = random.randint(1, 100)
        if miss <= 20:
            print(f"Игрок {self.name} промахнулся")
            return
        other.damage(self.attack_power)

    def damage(self, damage):
        if self.armor_points > damage:
            self.armor_points = self.armor_points - damage
            print("Нанесен урон броне персонажу " + self.name)
        else:
            damage = damage - self.armor_points
            self.armor_points = 0
            self.health = self.health - damage
            if self.health < 0:
                self.health = 0
        print(f"Нанесен урон: {damage} для игрока {self.name} . Текущий уровень здоровья: {self.health}")
class Game(object):
    def __init__(self, computer, player):
        self.computer = Hero(computer, 100, 14, 20)
        self.player = Hero(player, 150, 17, 30)
    def start(self):
        while self.computer.is_alive() and self.player.is_alive():
            self.computer.attack(self.player)
            self.player.attack(self.computer)
        if self.computer.is_alive():
            print("Вы проиграли игру")
        else:
            print("Вы выиграли игру !")
        print("Спасибо за игру !")

game = Game("computer", "player")
game.start()