import os
import sys

import pygame
from random import randint

pygame.init()
size = WIDTH, HEIGHT = 850, 550
FPS = 50
screen = pygame.display.set_mode(size)
FIRST_IMAGE = 'first_image'
SECOND_IMAGE = 'second_image'
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
    image = load_image('mainbird.jpg', -1)

    def __init__(self):
        super().__init__(bird_sprite)
        self.image = Main_bird.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 80
        self.rect.y = 220

    def update(self):
        if pygame.sprite.collide_mask(self, palms):
            pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.rect = self.rect.move(0, 1)


class Palms(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.flag = FIRST_IMAGE
        self.image = load_image('картаполная.png', -1)
        self.image_copy = load_image('fullmapcopy.png', -1)
        self.rect = self.image.get_rect()
        self.rect_copy = self.image_copy.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_copy = pygame.mask.from_surface(self.image_copy)
        self.rect.x = -11700
        self.rect.y = 0
        self.rect_copy.x = WIDTH
        self.rect_copy.y = 0


    def update(self):
        if self.rect.x == -11900  and self.flag == FIRST_IMAGE:
            self.rect_copy.x = WIDTH
            self.flag = SECOND_IMAGE

        elif self.rect_copy.x == -11900 and self.flag == SECOND_IMAGE:
            self.rect.x = WIDTH
            self.flag = FIRST_IMAGE

        if self.flag == FIRST_IMAGE:
            if self.rect_copy.x > -MAPSIZE:
                self.rect_copy = self.rect_copy.move(-1, 0)
            self.rect = self.rect.move(-1, 0)
        else:
            if self.rect.x > -MAPSIZE:
                self.rect = self.rect.move(-1, 0)
            self.rect_copy = self.rect_copy.move(-1, 0)
        print(self.rect_copy.x)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Birdie')
clock = pygame.time.Clock()
start_screen()

bird_sprite = pygame.sprite.GroupSingle()
all_sprites = pygame.sprite.Group()
player = Main_bird()
palms = Palms()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    screen.fill((142, 250, 245))
    all_sprites.draw(screen)
    bird_sprite.draw(screen)
    bird_sprite.update()
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)