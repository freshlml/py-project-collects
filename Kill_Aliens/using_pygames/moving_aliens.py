import sys
import pygame
import random

pygame.init()
size = width, height = 800, 1000
speed = 1
color = (100, 100, 100)

screen = pygame.display.set_mode(size)
screen_rect = screen.get_rect()

aliens = []
# al = pygame.Rect(0, 0, 30, 30)
# ll = random.randint(0, screen.get_width() - al.width)
# al.left = ll
# aliens.append(al)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            sys.exit()

    for bl in aliens:
        r = random.randint(0, 1)
        bl.top += r

        if bl.top < 0:
            bl.top = 0
        if bl.bottom > height:
            aliens.remove(bl)
            del bl

    if len(aliens) < 5:
        for i in range(len(aliens), 5):
            al = pygame.Rect(0, 0, 30, 30)
            ll = random.randint(0, screen.get_width() - al.width)
            al.left = ll
            aliens.append(al)

    screen.fill(color)
    for al in aliens:
        pygame.draw.rect(screen, (0, 255, 0), al)
    pygame.display.flip()








