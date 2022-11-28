import sys
import pygame

pygame.init()
size = width, height = 1200, 800
speed = 50
p = [1, 1]
black = 0
keep_moved = True

screen = pygame.display.set_mode(size)

ball_image = pygame.image.load("intro_ball.gif")
ball_rect = ball_image.get_rect()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                keep_moved = not keep_moved

    if keep_moved:
        # ball_rect.move(20, 20)
        ball_rect.left += p[0]
        ball_rect.top += p[1]
        if ball_rect.left < 0 or ball_rect.right > width:
            p[0] = -p[0]
        if ball_rect.top < 0 or ball_rect.bottom > height:
            p[1] = -p[1]

    screen.fill(black)
    screen.blit(ball_image, ball_rect)
    pygame.display.flip()


