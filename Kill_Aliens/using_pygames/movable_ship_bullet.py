import sys
import pygame
import random


pygame.init()
size = width, height = 800, 1000
speed = 1
color = (100, 100, 100)
finished = False

__direction = {
    "NO": 0,
    "UP": 1,
    "DOWN": 2,
    "LEFT": 4,
    "RIGHT": 8
}

horizontal_direction = __direction['NO']
vertical_direction = __direction['NO']

screen = pygame.display.set_mode(size)
screen_rect = screen.get_rect()


class Ship(pygame.sprite.Sprite):

    def __init__(self, screen_rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources/airplane.svg")  # todo, pygame 对svg支持度不行
        # ship_image = pygame.image.load("airplane-40453_640.png")
        # ship_image = pygame.transform.smoothscale(ship_image, (100, 150))  # todo png 缩小后竟然变模糊
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.bottom = screen_rect.bottom


ship = Ship(screen_rect)
ship_rect = ship.rect

bls = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, top, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.top = top
        self.rect.centerx = centerx


aliens = pygame.sprite.Group()


class Alien(pygame.sprite.Sprite):

    def __init__(self, screen, ship_rect):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        # self.rect = pygame.Rect(0, 0, 30, 30)
        self.image = pygame.image.load("resources/alien.svg")
        self.rect = self.image.get_rect()
        ll = random.randint(ship_rect.width/2, screen.get_width() - ship_rect.width/2)
        self.rect.left = ll


def restart():
    bls.empty()
    aliens.empty()
    ship_rect.centerx = screen_rect.centerx
    ship_rect.bottom = screen_rect.bottom


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vertical_direction = __direction['UP']
            if event.key == pygame.K_DOWN:
                vertical_direction = __direction['DOWN']
            if event.key == pygame.K_LEFT:
                horizontal_direction = __direction['LEFT']
            if event.key == pygame.K_RIGHT:
                horizontal_direction = __direction['RIGHT']
            if event.key == pygame.K_s:
                bl = Bullet(screen, ship_rect.top, ship_rect.centerx)
                bls.add(bl)
            if event.key == pygame.K_a:
                poi = -6
                for i in range(3):
                    bls.add(Bullet(screen, ship_rect.top, ship_rect.centerx + poi + -poi * i))
            if event.key == pygame.K_SPACE:
                if finished:
                    restart()
                    finished = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and vertical_direction & __direction['UP']:
                vertical_direction = __direction['NO']
            if event.key == pygame.K_DOWN and vertical_direction & __direction['DOWN']:
                vertical_direction = __direction['NO']
            if event.key == pygame.K_LEFT and horizontal_direction & __direction['LEFT']:
                horizontal_direction = __direction['NO']
            if event.key == pygame.K_RIGHT and horizontal_direction & __direction['RIGHT']:
                horizontal_direction = __direction['NO']

    if finished: continue

    if vertical_direction or horizontal_direction:
        if vertical_direction & __direction['UP']:
            ship_rect.top -= speed
        if vertical_direction & __direction['DOWN']:
            ship_rect.top += speed
        if horizontal_direction & __direction['LEFT']:
            ship_rect.left -= speed
        if horizontal_direction & __direction['RIGHT']:
            ship_rect.left += speed

        if ship_rect.left < 0:
            ship_rect.left = 0
        if ship_rect.right > width:
            ship_rect.right = width

        if ship_rect.top < 0:
            ship_rect.top = 0
        if ship_rect.bottom > height:
            ship_rect.bottom = height

    for bl in bls:
        bl.rect.top -= 1
    for bl in bls:
        if bl.rect.bottom <= 0:
            bls.remove(bl)

    for al in aliens:
        r = random.randint(0, 1)
        al.rect.top += r

        if al.rect.top < 0:
            al.tect.top = 0
        if al.rect.bottom > height:
            aliens.remove(al)
            del al
        elif pygame.sprite.collide_mask(ship, al):
            finished = True

    # if pygame.sprite.spritecollideany(ship, aliens):
    #     finished = True
    collisions = pygame.sprite.groupcollide(bls, aliens, True, True)

    if len(aliens) < 5:
        for i in range(len(aliens), 5):
            al = Alien(screen, ship_rect)
            aliens.add(al)

    screen.fill(color)
    screen.blit(ship.image, ship_rect)
    for bl in bls:
        pygame.draw.rect(screen, 255, bl)
    for al in aliens:
        pygame.draw.rect(screen, (0, 255, 0), al)
    pygame.display.flip()

