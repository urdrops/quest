import pygame

pygame.init()
W = 512
H = 512
screen = pygame.display.set_mode((512, 512))
img = pygame.image.load('img/street.jpg')
pygame.display.set_icon(img)
pygame.display.set_caption('Glitc-in-the-Head')  # GITH
run = True
square = pygame.Surface((50, 50))
square.fill('Blue')
screen.blit(square, (W / 2-25, H / 2-25))
pygame.display.update()


while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        up = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('da')
                up += 1
                screen.blit(square, (W / 2-25, up))
                pygame.display.update()