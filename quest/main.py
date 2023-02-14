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
# square.fill('Blue')
# screen.blit(square, (W / 2-25, H / 2-25))
# pygame.display.update()

text_fonts = pygame.font.Font("fonts/Roboto-Bold.ttf",40)
text_surface = text_fonts.render("Hello, World",True,'Green')
print('hello world')

while run:
    screen.blit(img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

