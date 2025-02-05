import os
import sys
from random import randint, choice

import pygame

pygame.init()
size = WIDTH, HEIGHT = 850, 550
FPS = 50
screen = pygame.display.set_mode(size)
FIRST_IMAGE = 'first_image'
SECOND_IMAGE = 'second_image'
flag = FIRST_IMAGE
MAPSIZE = 12750
points = 0
start_game = 0 # 0 - игра не началась, показать заставку. 1 - игра идёт. 2 - игра закончилась, финальный экран, 3 - игра на паузе


def terminate():
    save_data(str(points))
    pygame.quit()
    sys.exit()

def save_data(text):
    if os.path.isfile("saved_result.txt"):
        with open("saved_result.txt", "r") as f:
            saved = f.readline()
            if int(saved) < int(text):
                with open("saved_result.txt", "w") as f:
                    f.write(str(text))
    else:
        with open("saved_result.txt", "w") as f:
             f.write(str(text))

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
    if not os.path.isfile("saved_result.txt"):
        record = "0"
    else:
        with open("saved_result.txt", "r") as f:
            record = f.readline()
    intro_text = ["FLUPPY BIRDIE", "",
                  "Правила игры",
                  "Нажимайте пробел чтобы избежать столкновения с пальмами",
                  "и собирайте ягодки для большего количества очков.",
                  f"Ваш рекорд: {record}"]
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

def final_screen():
    if not os.path.isfile("saved_result.txt"):
        record = "0"
    else:
        with open("saved_result.txt", "r") as f:
            record = f.readline()
    intro_text = ["Упс! Птенец врезался в пальму!",
                  "Вы проиграли.",
                  f"Ваш результат: {points}",
                  f"Ваш лучший результат: {record}"]
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

def pause_screen():
    if not os.path.isfile("saved_result.txt"):
        record = "0"
    else:
        with open("saved_result.txt", "r") as f:
            record = f.readline()
    intro_text = ["Игра на паузе.",
                  f"Ваш результат: {points}",
                  f"Ваш лучший результат: {record}"]
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

class StartButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(btn_sprite)
        self.image = load_image('start.png', -1)
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 350
        self.rect.y = 300
    def update(self):
        self.rect.x = 350
        self.rect.y = 300

class RestartButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(final_btn_sprite)
        self.image = load_image('restart.png', -1)
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 350
        self.rect.y = 300
    def update(self):
        self.rect.x = 350
        self.rect.y = 300


class QuitButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(final_btn_sprite)
        self.image = load_image('quit.png')
        self.image = pygame.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 350
        self.rect.y = 400
    def update(self):
        self.rect.x = 350
        self.rect.y = 400


class PauseButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('pause.jpg', -1)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 10
        self.rect.y = 40

    def update(self):
        self.rect.x = 10
        self.rect.y = 40

class ContinueButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(contbtn_sprite)
        self.image = load_image('continue.png', -1)
        self.image = pygame.transform.scale(self.image, (150, 60))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 350
        self.rect.y = 220

    def update(self):
        self.rect.x = 350
        self.rect.y = 220


class Main_bird(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(bird_sprite)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        global points, start_game
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if pygame.sprite.collide_mask(self, palms) or pygame.sprite.collide_mask(self, palms_copy):
            start_game = 2
        if self.rect.y == 550:
            self.rect.y = -50
        self.rect = self.rect.move(0, 2)


class Berry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('berry.png', -1)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = -50

    def update(self):
        global points
        do_collid = pygame.sprite.collide_mask(self, player)
        if do_collid or self.rect.x < -40:
            self.rect.x = WIDTH
            y = choice([randint(50, HEIGHT // 2 - 100), randint(HEIGHT // 2 + 100, HEIGHT - 100)])
            for _ in range(4): # У системы есть 4 попытки выбрать положение, при котором ягодка не касается пальмы.
                               # Если такое положение так и не было найдено - значит ягодка растёт на пальме :)
                if palms.rect.collidepoint(self.rect.x, y) or palms_copy.rect.collidepoint(self.rect.x, y):
                    y = choice([randint(50, HEIGHT // 2 - 100), randint(HEIGHT // 2 + 100, HEIGHT - 100)])
                else:
                    break
            self.rect.y = y
            if do_collid:
                points += 300
        self.rect = self.rect.move(-1, 0)


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
            if palms_copy.rect.x > -MAPSIZE or self.rect.x > 0:
                palms_copy.rect = palms_copy.rect.move(-1, 0)
            self.rect = self.rect.move(-1, 0)
        elif palms.rect.x > -MAPSIZE + WIDTH:
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
        if palms.rect.x == -MAPSIZE + WIDTH  and flag == FIRST_IMAGE:
            self.rect.x = WIDTH
            flag = SECOND_IMAGE
        if flag == SECOND_IMAGE:
            if palms.rect.x > -MAPSIZE or self.rect.x > 0:
                palms.rect = palms.rect.move(-1, 0)
            self.rect = self.rect.move(-1, 0)
        elif palms.rect.x > -MAPSIZE + WIDTH:
            self.rect.x = WIDTH




screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Birdie')
clock = pygame.time.Clock()
start_screen()

final_btn_sprite = pygame.sprite.Group()
btn_sprite = pygame.sprite.GroupSingle()
bird_sprite = pygame.sprite.GroupSingle()
contbtn_sprite = pygame.sprite.GroupSingle()
all_sprites = pygame.sprite.Group()
startbutton = StartButton()
restartbutton = RestartButton()
quitbutton = QuitButton()
pausebutton = PauseButton()
continuebutton = ContinueButton()
player = Main_bird(load_image('sprites.png', -1), 5, 3, 80, 220)
palms = Palms()
palms_copy = Palms_copy()
berry = Berry()

f1 = pygame.font.Font(None, 36)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            terminate()
        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN)
                and start_game == 1):
            player.rect = player.rect.move(0, -35)
        if event.type == pygame.MOUSEBUTTONDOWN and start_game == 0 and startbutton.rect.collidepoint(event.pos)\
                or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start_game == 0):
            start_game = 1
        if event.type == pygame.MOUSEBUTTONDOWN and (start_game == 2 or start_game == 3) and restartbutton.rect.collidepoint(event.pos)\
                or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start_game == 2):
            start_game = 1
            palms.rect.x = 220
            flag = FIRST_IMAGE
            save_data(str(points))
            points = 0
        if ((event.type == pygame.MOUSEBUTTONDOWN and start_game == 1 and pausebutton.rect.collidepoint(event.pos)) or
                (event.type == pygame.KEYDOWN and start_game == 1 and event.key == pygame.K_q)):
            save_data(str(points))
            start_game = 3
        if ((event.type == pygame.MOUSEBUTTONDOWN and start_game == 3 and continuebutton.rect.collidepoint(event.pos))
                or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start_game == 3)):
            start_game = 1
        if event.type == pygame.MOUSEBUTTONDOWN and (start_game == 2 or start_game == 3) and quitbutton.rect.collidepoint(event.pos):
            terminate()

    if start_game == 0:
        start_screen()
        btn_sprite.draw(screen)
        btn_sprite.update()
    elif start_game == 1:
        screen.fill((142, 250, 245))
        all_sprites.draw(screen)
        bird_sprite.draw(screen)
        bird_sprite.update()
        all_sprites.update()
        points += 1
        points_txt = f1.render(str(points), 1, (0, 0, 0))
        screen.blit(points_txt , (10, 10))
    elif start_game == 2:
        final_screen()
        save_data(str(points))
        final_btn_sprite.draw(screen)
        final_btn_sprite.update()
    elif start_game == 3:
        pause_screen()
        contbtn_sprite.draw(screen)
        contbtn_sprite.update()
        final_btn_sprite.draw(screen)
        final_btn_sprite.update()
    pygame.display.flip()
    clock.tick(FPS)