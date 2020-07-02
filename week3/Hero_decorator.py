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



