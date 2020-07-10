import pygame
import os

pygame.init()
bgDir = 'D:\\GitHub\\PyGame\\texture\\background'
bg = pygame.image.load(os.path.join(bgDir, 'bg.jpg'))
win = pygame.display.set_mode((500, 500))

win.blit(bg, (0, 0))

pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    pygame.time.delay(100)
