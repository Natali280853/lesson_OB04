from abc import ABC, abstractmethod

# Шаг 1: Создание абстрактного класса для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Атака мечом!"

class Bow(Weapon):
    def attack(self):
        return "Атака из лука!"

# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "Боец без оружия не может атаковать!"

class Monster():
    def __init__(self, name):
        self.name = name
        self.weapon = None


# Шаг 4: Реализация боя
fighter = Fighter("Боец")
monster = Monster("Монстр")

sword = Sword()
bow = Bow()

fighter.change_weapon(sword)
print(f"{fighter.name} выбирает меч.")
print(fighter.attack())
print(f"{monster.name} побежден!\n")

fighter.change_weapon(bow)
print(f"{fighter.name} выбирает лук.")
print(fighter.attack())
print(f"{monster.name} побежден!")
