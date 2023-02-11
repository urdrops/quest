import random
import time

import pygame

WIDTH = 512
HEIGHT = 512
FPS = 165

def random_color():
    return random.randint(0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Glitch-in-the-Head')
run = True
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
while run:
    random_color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    screen.fill(random_color)
    clock.tick(FPS)
    print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    pygame.display.flip()