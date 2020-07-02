from abc import ABC, abstractmethod


class AbstractEffect(ABC):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class Hero(AbstractEffect):

    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractPositive(AbstractEffect):

    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        self.base.get_positive_effects()

    def get_negative_effects(self):
        pass

    def get_stats(self):
        pass


class AbstractNegative(AbstractEffect):

    def __init__(self, base):
        self.base = base

    def get_negative_effects(self):
        self.base.get_negative_effects()

    def get_positive_effects(self):
        pass

    def get_stats(self):
        pass


class Berserk(AbstractPositive):

    def get_positive_effects(self):
        self.base.stats['Strength'] += 7
        self.base.stats['Endurance'] += 7
        self.base.stats['Agility'] += 7
        self.base.stats['Charisma'] -= 3
        self.base.stats['Intelligence'] -= 3
        self.base.stats['Perception'] -= 3
        self.base.stats['HP'] += 50
        return self.base.stats


mage = Hero()
mage.get_stats()
print(mage.stats)
mage.get_negative_effects()
mage.get_positive_effects()
brs1 = Berserk(mage)
brs1.get_stats()
brs1.get_negative_effects()
brs1.get_positive_effects()
print(mage.stats)
brs2 = Berserk(brs1)
brs2.get_stats()
print(mage.stats)
brs3 = Berserk(brs2)
brs3.get_stats()
print(mage.stats)
print(brs3)
print(brs2)
print(brs1)
print(mage)
