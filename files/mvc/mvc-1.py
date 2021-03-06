import os
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"


class Ball:
    def __init__(self, x, y, radius=50, color=RED):
        self.initial_pos = (x, y)
        self.x = x
        self.y = y
        self.dy = 1
        self.color = color
        self.radius = radius

    def step(self):
        self.y += self.dy
        self.dy += 1
        self.dy *= 0.99
        if self.y + self.radius > 480:
            self.dy = -self.dy

    def reset(self):
        self.x, self.y = self.initial_pos

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)),
                           self.radius)

    def contains_pt(self, pt):
        x, y = pt
        if not self.x - self.radius < x < self.x + self.radius:
            return False
        if not self.y - self.radius < y < self.y + self.radius:
            return False
        return True


screen = pygame.display.set_mode((640, 480))

ball1 = Ball(320, 240, radius=80)
ball2 = Ball(550, 140, radius=60, color=(0, 255, 0))
ball3 = Ball(100, 140, radius=40, color=(0, 127, 255))

balls = [ball1, ball2, ball3]

running = True
while running:  # forever -- until user clicks in close box
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if ball.contains_pt(pygame.mouse.get_pos()):
                    ball.reset()
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # erases screen
    for ball in balls:
        ball.step()
        ball.draw()
    pygame.display.update()  # updates real screen from staged screen

pygame.quit()
