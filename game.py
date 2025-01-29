import os
import sys

import pygame
from random import randint

pygame.init()
size = WIDTH, HEIGHT = 850, 550
FPS = 50
screen = pygame.display.set_mode(size)


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
        super().__init__(all_sprites)
        self.image = Main_bird.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 80
        self.rect.y = 220

    def update(self):
        self.rect = self.rect.move(0, 2)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Birdie')
clock = pygame.time.Clock()
start_screen()

all_sprites = pygame.sprite.Group()
player = Main_bird()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.rect = player.rect.move(0, -35)
    screen.fill((142, 250, 245))
    all_sprites.draw(screen)
    player.update()
    pygame.display.flip()
    clock.tick(FPS)
