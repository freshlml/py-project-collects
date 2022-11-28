import sys
import pygame

pygame.init()
size = width, height = 800, 1000
speed = 1
color = (100, 100, 100)

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

ship_image = pygame.image.load("zoom.svg")  # todo, pygame 对svg支持度不行
# ship_image = pygame.image.load("airplane-40453_640.png")
# ship_image = pygame.transform.smoothscale(ship_image, (100, 150))  # todo png 缩小后竟然变模糊
ship_rect = ship_image.get_rect()

ship_rect.centerx = screen_rect.centerx
ship_rect.bottom = screen_rect.bottom

bls = []

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
                bl = pygame.Rect(0, 0, 3, 15)
                bl.top = ship_rect.top
                bl.centerx = ship_rect.centerx
                bls.append(bl)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and vertical_direction & __direction['UP']:
                vertical_direction = __direction['NO']
            if event.key == pygame.K_DOWN and vertical_direction & __direction['DOWN']:
                vertical_direction = __direction['NO']
            if event.key == pygame.K_LEFT and horizontal_direction & __direction['LEFT']:
                horizontal_direction = __direction['NO']
            if event.key == pygame.K_RIGHT and horizontal_direction & __direction['RIGHT']:
                horizontal_direction = __direction['NO']

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
        bl.top -= 1
    for bl in bls:
        if bl.bottom < 0:
            bls.remove(bl)

    screen.fill(color)
    screen.blit(ship_image, ship_rect)
    for bl in bls:
        pygame.draw.rect(screen, 255, bl)
    pygame.display.flip()


