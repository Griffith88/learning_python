from abc import ABC, abstractmethod
import pygame
import random


def create_sprite(img, sprite_size):
    icon = pygame.image.load(img).convert_alpha()
    icon = pygame.transform.scale(icon, (sprite_size, sprite_size))
    sprite = pygame.Surface((sprite_size, sprite_size), pygame.HWSURFACE)
    sprite.blit(icon, (0, 0))
    return sprite


class AbstractObject(ABC):

    @abstractmethod
    def draw(self, display):
        pass


class Creature(AbstractObject):

    def __init__(self, icon, stats, position):
        self.sprite = icon
        self.stats = stats
        self.position = position
        self.calc_max_HP()
        self.hp = self.max_hp

    def calc_max_HP(self):
        self.max_hp = 5 + self.stats["endurance"] * 2

    def draw(self, display):
        display.blit(self.sprite, ((self.position[0]) * display.engine.sprite_size,
                                   (self.position[1]) * display.engine.sprite_size))


class Interactive(ABC):

    @abstractmethod
    def interact(self, engine, hero):
        pass


class Ally(AbstractObject, Interactive):

    def __init__(self, icon, action, position):
        self.sprite = icon
        self.action = action
        self.position = position

    def interact(self, engine, hero):
        self.action(engine, hero)

    def draw(self, display):
        pass


class Enemy(Creature, Interactive):

    def __init__(self, icon, stats, xp, position):
        super().__init__(icon, stats, position)
        self.xp = xp

    def interact(self, engine, hero):
        delta = (self.stats["strength"] + self.stats["endurance"]) / \
                (hero.stats["strength"] + hero.stats["endurance"])
        exp = self.xp
        if delta > 1.25:
            for i in range(hero.stats["luck"]):
                if hero.stats["luck"] >= random.randint(1, 150):
                    exp += int(self.xp // 2)
                    break

        exp = int(exp)
        hero.exp += exp
        engine.notify({"info": f"{exp} exp up"})


class Hero(Creature):

    def __init__(self, stats, icon):
        pos = [1, 1]
        self.level = 1
        self.exp = 0
        self.gold = 0
        super().__init__(icon, stats, pos)

    def level_up(self):
        while self.exp >= 100 * (2 ** (self.level - 1)):
            yield "level up!"
            self.level += 1
            self.stats["strength"] += 2
            self.stats["endurance"] += 2
            self.calc_max_HP()
            self.hp = self.max_hp


class Effect(Hero):

    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats.copy()
        self.apply_effect()

    @property
    def position(self):
        return self.base.position

    @position.setter
    def position(self, value):
        self.base.position = value

    @property
    def level(self):
        return self.base.level

    @level.setter
    def level(self, value):
        self.base.level = value

    @property
    def gold(self):
        return self.base.gold

    @gold.setter
    def gold(self, value):
        self.base.gold = value

    @property
    def hp(self):
        return self.base.hp

    @hp.setter
    def hp(self, value):
        self.base.hp = value

    @property
    def max_hp(self):
        return self.base.max_hp

    @max_hp.setter
    def max_hp(self, value):
        self.base.max_hp = value

    @property
    def exp(self):
        return self.base.exp

    @exp.setter
    def exp(self, value):
        self.base.exp = value

    @property
    def sprite(self):
        return self.base.sprite

    @abstractmethod
    def apply_effect(self):
        pass


class Berserk(Effect):
    def apply_effect(self):
        self.stats["Strength"] += 7
        self.stats["Endurance"] += 7
        self.stats["Agility"] += 7
        self.stats["Luck"] += 7
        self.stats["Intelligence"] -= 3
        self.stats["Charisma"] -= 3
        self.stats["Intelligence"] -= 3
        self.stats["HP"] += 50
        super().apply_effect()


class Blessing(Effect):
    def apply_effect(self):
        self.stats["Strength"] += 2
        self.stats["Endurance"] += 2
        self.stats["Agility"] += 2
        self.stats["Charisma"] += 2
        self.stats["Perception"] += 2
        self.stats["Intelligence"] += 2
        self.stats["Luck"] += 2
        super().apply_effect()


class Weakness(Effect):
    def apply_effect(self):
        self.stats["Strength"] -= 4
        self.stats["Endurance"] -= 4
        self.stats["Agility"] -= 4
        super().apply_effect()


class Sunset(Effect):

    def apply_effect(self):
        self.stats["Luck"] -= 2
        super().apply_effect()
