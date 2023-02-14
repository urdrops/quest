import pygame
#настройка дисплея и кадра игры
WIDTH = 800
HEIGHT = 500
FPS = 60
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Glith in head')
pygame.display.set_icon(pygame.image.load('C:/Users/NOTEBOOK/Desktop/quest/quest/images/swords.png'))
clock = pygame.time.Clock()

#группировка спрайтов
all_sprites = pygame.sprite.Group()

# список анимации
player_walk = [
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/right/image_part_001.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/right/image_part_002.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/right/image_part_003.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/right/image_part_004.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/right/image_part_005.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/right/image_part_006.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/right/image_part_007.png',
]
player_fight = [
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/fight/image_part_001.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/fight/image_part_002.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/fight/image_part_003.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/fight/image_part_004.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/fight/image_part_005.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/fight/image_part_006.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/fight/image_part_007.png',
]
player_stay = [
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/stay/image_part_001.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/stay/image_part_002.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/stay/image_part_003.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/stay/image_part_004.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/stay/image_part_005.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/stay/image_part_006.png',
    'C:/Users/NOTEBOOK/Desktop/quest/quest/player/stay/image_part_006.png',
]

# какой то ебанный спрайт

#добавляем в группу 


# задний фон спрайт
#class Background(pygame.sprite.Sprite):
#    def __init__(self):
  #      pygame.sprite.Sprite.__init__(self)
    #    self.image = screen.fill(255,255,255)#pygame.image.load('C:/Users/NOTEBOOK/Desktop/quest/quest/images/background_game.jpg')
    #    self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT ))
     #   self.rect = self.image.get_rect()

#добавляем в группу 
#back_ground = Background()
#all_sprites.add(back_ground) 

# Цикл игры и счетчики
running = True
count = 40
count2 = 800
a = 0
animation_count = 0
animations = player_stay[animation_count]

while running:
    # кнопки
    keys = pygame.key.get_pressed()
        # спрайт игрока
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(animations)
            self.image = pygame.transform.scale(self.image, (220/100 * 100, 155/100 * 100))
            self.image = pygame.transform.flip(self.image,a,0)
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 100 * 50, HEIGHT / 100 * 80)
    player = Player()
    all_sprites.add(player) 
    # Облока 
    class Sky(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('C:/Users/NOTEBOOK/Desktop/quest/quest/images/317130244148211.png')
            self.image = pygame.transform.scale(self.image, (220/100 * 100, 155/100 * 100))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 100 * count, HEIGHT / 100 * 10)
    sky = Sky()
    all_sprites.add(sky)
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    #counts
    if animation_count == 6:
        animation_count = 0
    else:
        animation_count += 1
    
    # Ввод процесса (события)
    for event in pygame.event.get():

        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))       
    #screen.blit(back_ground.image, back_ground.rect)  
    screen.blit(player.image, player.rect)
    screen.blit(sky.image, sky.rect)
    pygame.display.update()

    if keys[pygame.K_RIGHT]:
        count -= 2
        count2 -= 2 # для облаков
        if count < 0:
            count = 100
        if count2 < 0:
            count2 = 100
        a = 0
        animations = player_walk[animation_count]
    elif keys[pygame.K_LEFT]:
        count += 2
        count2 += 2 # для облаков 
        if count > 100:
            count = 0
        if count2 > 100:
            count2 = 0
        a = 215
        animations = player_walk[animation_count]
    elif keys[pygame.K_SPACE]:
        animations = player_fight[animation_count]
        
    else: 
        animations = player_stay[animation_count]
    
