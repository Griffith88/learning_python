import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """возвращает разность двух векторов"""
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """возвращает произведение вектора на число"""
        return Vec2d(self.x * other, self.y * other)

    def __len__(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        """возвращает пару координат, определяющих вектор"""
        return int(self.x), int(self.y)


class Polyline:
    def __init__(self):
        self.game_display = pygame.display.set_mode(SCREEN_DIM)
        self.speeds = list()
        self.points = list()

    def add_point(self, vec2d):
        self.points.append(vec2d)
        self.speeds.append(Vec2d(random.random() * 2, random.random() * 2))

    def reset(self):
        self.speeds = list()
        self.points = list()

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = (self.points[p] + self.speeds[p])
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(- self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(self.game_display, color,
                                 (int(self.points[p_n].x), int(self.points[p_n].y)),
                                 (int(self.points[p_n + 1].x),
                                  int(self.points[p_n + 1].y)), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(self.game_display, color,
                                   (int(p.x), int(p.y)), width)


class Knot(Polyline):
    def __init__(self, steps):
        self.steps = steps
        super().__init__()

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            points = self.get_knot()
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(self.game_display, color,
                                 (int(points[p_n].x), int(points[p_n].y)),
                                 (int(points[p_n + 1].x),
                                  int(points[p_n + 1].y)), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(self.game_display, color,
                                   (int(p.x), int(p.y)), width)

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = list()
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(self.get_points(ptn))
        return res

    def get_points(self, base_points):
        alpha = 1 / self.steps
        res = []
        for i in range(self.steps):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return (points[deg] * alpha) + \
               (self.get_point(points, alpha, deg - 1) * (1 - alpha))

    def delete(self):
        if self.points and self.speeds:
            self.points.pop()
            self.speeds.pop()


def draw_help(game_display):
    """функция отрисовки экрана справки программы"""
    game_display.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = list()
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["D", "Delete point"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(poly.steps), "Current points"])

    pygame.draw.lines(game_display, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        game_display.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        game_display.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    poly = Knot(steps)
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    poly.reset()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    poly.steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    poly.steps -= 1 if poly.steps > 1 else 0
                if event.key == pygame.K_d:
                    poly.delete()

            if event.type == pygame.MOUSEBUTTONDOWN:
                poly.add_point(Vec2d(event.pos[0], event.pos[1]))

        poly.game_display.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        poly.draw_points()
        poly.draw_points("line", 3, color)

        if not pause:
            poly.set_points()
        if show_help:
            draw_help(poly.game_display)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
