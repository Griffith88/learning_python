from abc import ABC, abstractmethod


class AbstractEffect(ABC, Hero):

    def __init__(self, base):
        self.base = base

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

    def get_negative_effects(self):
        return self.base.get_negative_effects().copy()


class AbstractNegative(AbstractEffect):

    def get_positive_effects(self):
        return self.base.get_positive_effects().copy()


class Berserk(AbstractPositive):

    def get_positive_effects(self):
        positive = self.base.get_positive_effects()
        positive.append('Berserk')
        return positive.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        for k in stats:
            if k in ('Strength', 'Endurance', 'Agility', 'Luck'):
                stats[k] += 7
            elif k in ('Perception', 'Intelligence', 'Charisma'):
                stats[k] -= 3
            elif k == 'HP':
                stats[k] += 50
        return stats.copy()


class Blessing(AbstractPositive):

    def get_positive_effects(self):
        positive = self.base.get_positive_effects()
        positive.append('Blessing')
        return positive.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        for k in stats:
            if k in ('Strength', 'Endurance', 'Agility', 'Charisma', 'Perception', 'Intelligence', 'Luck'):
                stats[k] += 2
        return stats.copy()


class Weakness(AbstractNegative):

    def get_negative_effects(self):
        negative = self.base.get_negative_effects()
        negative.append('Weakness')
        return negative.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        for k in stats:
            if k in ('Strength', 'Endurance', 'Agility'):
                stats[k] -= 4
        return stats.copy()


class EvilEye(AbstractNegative):

    def get_negative_effects(self):
        negative = self.base.get_negative_effects()
        negative.append('EvilEye')
        return negative.copy()

    def get_stats(self):
        state = self.base.get_stats()
        state['Luck'] -= 10
        return state.copy()

class Curse(AbstractNegative):

    def get_negative_effects(self):
        negative = self.base.get_negative_effects()
        negative.append('Curse')
        return negative.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        for k in stats:
            if k in ('Strength', 'Endurance', 'Agility', 'Charisma', 'Perception', 'Intelligence', 'Luck'):
                stats[k] -= 2
        return stats.copy()
