import pygame

pygame.init()
screen = pygame.display.set_mode((512, 512))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
