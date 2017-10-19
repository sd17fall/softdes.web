import os
import pygame

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

screen = pygame.display.set_mode((640, 480))

x = width / 2
y = height / 2
dy = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            y = 0
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
    y += dy
    dy += 1
    dy *= 0.99
    if y > 480:
        dy = -dy
    pygame.display.update()

pygame.quit()
