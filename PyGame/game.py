import os
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('Cubes Game')

x = 50
y = 425

widht = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

run = True

clock = pygame.time.Clock()
left = False
right = False
animCount = 0
heroMoveDir = 'D:\\GitHub\\PyGame\\texture\\hero'
bgDir = 'D:\\GitHub\\PyGame\\texture\\background'
walkRight = [pygame.image.load(os.path.join(heroMoveDir, 'right_1.png')),
             pygame.image.load(os.path.join(heroMoveDir, 'right_2.png')),
             pygame.image.load(os.path.join(heroMoveDir, 'right_3.png')),
             pygame.image.load(os.path.join(heroMoveDir, 'right_4.png')),
             pygame.image.load(os.path.join(heroMoveDir, 'right_5.png')),
             pygame.image.load(os.path.join(heroMoveDir, 'right_6.png'))
             ]

walkLeft = [pygame.image.load(os.path.join(heroMoveDir, 'left_1.png')),
            pygame.image.load(os.path.join(heroMoveDir, 'left_2.png')),
            pygame.image.load(os.path.join(heroMoveDir, 'left_3.png')),
            pygame.image.load(os.path.join(heroMoveDir, 'left_4.png')),
            pygame.image.load(os.path.join(heroMoveDir, 'left_5.png')),
            pygame.image.load(os.path.join(heroMoveDir, 'left_6.png'))
            ]

bg = pygame.image.load(os.path.join(bgDir, 'bg.jpg'))
playerStand = pygame.image.load(os.path.join(heroMoveDir, 'idle.png'))


def drawWindow():
    win.blit(bg, (0, 0))
    global animCount

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    pygame.display.update()


while run:

    clock.tick(30)
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - widht - speed:
        x += speed
        left = False
        right = True
    else:
        right = False
        left = False
        animCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()
