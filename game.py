import os
import sys

import pygame

pygame.init()
size = WIDTH, HEIGHT = 850, 550
FPS = 50
screen = pygame.display.set_mode(size)
FIRST_IMAGE = 'first_image'
SECOND_IMAGE = 'second_image'
flag = FIRST_IMAGE
MAPSIZE = 12750


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_screen():
    pass


class Main_bird(pygame.sprite.Sprite):
    image = load_image('mainbird.png', -1)

    def __init__(self):
        super().__init__(bird_sprite)
        self.image = Main_bird.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 80
        self.rect.y = 220

    def update(self):
        if pygame.sprite.collide_mask(self, palms) or pygame.sprite.collide_mask(self, palms_copy):
            print('game over')
        if self.rect.y == 550:
            self.rect.y = -50
        self.rect = self.rect.move(0, 2)


class Palms(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('картаполная.png', -1)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 220
        self.rect.y = 0

    def update(self):
        global flag
        if palms_copy.rect.x == -MAPSIZE + WIDTH and flag == SECOND_IMAGE:
            self.rect.x = WIDTH
            flag = FIRST_IMAGE
        if flag == FIRST_IMAGE:
            if palms_copy.rect.x > -MAPSIZE or self.rect.x < 850:
                palms_copy.rect = palms_copy.rect.move(-1, 0)
            self.rect = self.rect.move(-1, 0)
            if flag == SECOND_IMAGE or palms.rect.x < -MAPSIZE:
                self.rect.x = WIDTH

class Palms_copy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.flag = FIRST_IMAGE
        self.image = load_image('fullmapcopy.png', -1)
        self.rect = self.image.get_rect()
        self.mask_copy = pygame.mask.from_surface(self.image)
        self.rect.y = 0

    def update(self):
        global flag
        if palms.rect.x == -MAPSIZE + WIDTH and flag == FIRST_IMAGE:
            self.rect.x = WIDTH
            flag = SECOND_IMAGE
        if flag == SECOND_IMAGE:
            if palms.rect.x > -MAPSIZE:
                palms.rect = palms.rect.move(-1, 0)
            self.rect = self.rect.move(-1, 0)
        if flag == FIRST_IMAGE or palms_copy.rect.x < -MAPSIZE:
            self.rect.x = WIDTH

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Birdie')
clock = pygame.time.Clock()
start_screen()

bird_sprite = pygame.sprite.GroupSingle()
all_sprites = pygame.sprite.Group()
player = Main_bird()
palms = Palms()
palms_copy = Palms_copy()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.rect = player.rect.move(0, -35)
    screen.fill((142, 250, 245))
    all_sprites.draw(screen)
    bird_sprite.draw(screen)
    bird_sprite.update()
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)
