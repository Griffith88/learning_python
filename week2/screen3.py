#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    """Vector Class"""
    def __init__(self, *params):
        if len(params) == 1:
            self.x = params[0][0]
            self.y = params[0][1]
        elif len(params) == 2:
            self.x = params[0]
            self.y = params[1]
        else:
            raise ValueError

    def __add__(self, other):
        """returns the sum of two vectors"""
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """returns the difference of two vectors"""
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """returns the product of a vector by a number"""
        return Vec2d(self.x * other, self.y * other)

    def __len__(self):
        """returns the vector length"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def int_pair(self):
        """returns a pair of coordinates defining the vector (the vector end point coordinates),
            the vector starting point coordinates coincide with the coordinate system origin (0, 0)"""
        return int(self.x), int(self.y)


class Polyline:
    """Base Polyline Class"""
    def __init__(self, width=3):
        self.points = []
        self.speeds = []
        self.width = width

    def add_point(self, point, speed=None):
        _speed = speed or (random.random() * 2, random.random() * 2)
        self.points.append(Vec2d(point))
        self.speeds.append(Vec2d(_speed))

    def drop_point(self):
        if len(self.points) > 0:
            self.points.pop()
            self.speeds.pop()

    def set_points(self):
        """function of recalculation of coordinates of control points"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(- self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def speed_up(self):
        """function of increasing line moving"""
        for p in range(len(self.speeds)):
            if len(self.speeds) > 0:
                self.speeds[p] += self.speeds[p] * 0.1

    def speed_down(self):
        """function of decreasing line moving"""
        for p in range(len(self.speeds)):
            if len(self.speeds) > 0:
                self.speeds[p] -= self.speeds[p] * 0.1

    def draw_points(self, gameDisplay):
        """function of drawing points on the screen"""
        for p in self.points:
            pygame.draw.circle(gameDisplay, (255, 255, 255),
                               p.int_pair(), self.width)

    def draw_help(self, gameDisplay, steps=None):
        """function of program help screen rendering"""
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Z", "Undo"])
        data.append(["N", "New Polyline"])
        data.append(["W", "Points Speed Up"])
        data.append(["S", "Points Speed Down"])
        if not steps is None:
            data.append(["Num+", "More points"])
            data.append(["Num-", "Less points"])
            data.append(["", ""])
            data.append([str(steps), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


class Knot(Polyline):
    def __init__(self, hue=0, color=pygame.Color(0), width=3, steps=35):
        super().__init__(width)
        self.smooth_points = []
        self.hue = hue
        self.color = color
        self._steps = steps

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        if value > 0:
            self._steps = value

    def __get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.__get_point(points, alpha, deg - 1) * (1 - alpha)

    def __get_points(self, base_points):
        alpha = 1 / self.steps
        res = []
        for i in range(self.steps):
            res.append(self.__get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        self.smooth_points = []

        if len(self.points) >= 3:
            for i in range(-2, len(self.points) - 2):
                ptn = []
                ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
                ptn.append(self.points[i + 1])
                ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

                self.smooth_points.extend(self.__get_points(ptn))

    def add_point(self, point, speed=None):
        super().add_point(point, speed)
        self.get_knot()

    def drop_point(self):
        super().drop_point()
        self.get_knot()

    def set_points(self):
        """function of recalculation of coordinates of control points"""
        super().set_points()
        self.get_knot()

    def draw_points(self, gameDisplay):
        """function of drawing line on the screen"""
        super().draw_points(gameDisplay)

        self.hue = (self.hue + 1) % 360
        self.color.hsla = (self.hue, 100, 50, 100)

        for p_n in range(-1, len(self.smooth_points) - 1):
            pygame.draw.line(gameDisplay, self.color,
                             self.smooth_points[p_n].int_pair(),
                             self.smooth_points[p_n + 1].int_pair(), self.width)

    def draw_help(self, gameDisplay, steps=None):
        """function of program help screen rendering"""
        super().draw_help(gameDisplay, self.steps)


class Polylines:
    """Polyline Array Class"""
    def __init__(self):
        self.polylines = []

    def append(self, value):
        if isinstance(value, Polyline):
            self.polylines.append(value)

    def undo(self):
        if len(self.last().points) > 1:
            self.last().drop_point()
        elif len(self.polylines) > 1:
            self.polylines.pop()

    def last(self):
        if len(self.polylines) > 0:
            return self.polylines[-1]

    def draw_points(self, gameDisplay):
        for polyline in self.polylines:
            polyline.draw_points(gameDisplay)

    def set_points(self):
        for polyline in self.polylines:
            polyline.set_points()


# =======================================================================================
# Main program
# =======================================================================================
def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True
    pause = True
    show_help = False

    polylines = Polylines()
    polylines.append(Knot())

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    polylines = Polylines()
                    polylines.append(Knot())
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_z:
                    polylines.undo()
                if event.key == pygame.K_n:
                    polylines.append(Knot())
                if event.key == pygame.K_w:
                    polylines.last().speed_up()
                if event.key == pygame.K_s:
                    polylines.last().speed_down()
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_PLUS:
                    polylines.last().steps += 1
                if event.key == pygame.K_KP_MINUS:
                    polylines.last().steps -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                polylines.last().add_point(event.pos)

        gameDisplay.fill((0, 0, 0))
        polylines.draw_points(gameDisplay)
        if not pause:
            polylines.set_points()
        if show_help:
            polylines.last().draw_help(gameDisplay)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)


if __name__ == "__main__":
    main()
