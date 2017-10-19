import os
import pygame

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

screen = pygame.display.set_mode((640, 480))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (320, 240), 50)
    pygame.display.update()

pygame.quit()
