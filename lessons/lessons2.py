# Наследование

class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} base action"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp: int = 10):
        super().__init__(name, lvl, hp)
        self.mp = mp




