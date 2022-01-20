import pygame.image
import pygame
import math
import os
pygame.init()

WIDTH = 1920
HEIGHT = 1080
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((1920, 1080))
road = [(100, 100), (1820, 100), (1820, 780), (100, 780)]
clock = pygame.time.Clock()
pygame.display.set_caption('Tower Of Defence')
# PATH = os.getcwd()

ROOT = '/Users/mac2/PycharmProjects/pythonProject1/compUsTowerDefence/npcs'


class Warrior:
    def __init__(self, x, y, road):
        self.images_left = [pygame.image.load(ROOT + '/skins/Knight/SL1.png'),
                            pygame.image.load(ROOT + '/skins/Knight/SL2.png'),
                            pygame.image.load(ROOT + '/skins/Knight/SL3.png')]
        self.images_right = [pygame.image.load(ROOT + '/skins/Knight/SR1.png'),
                             pygame.image.load(ROOT + '/skins/Knight/SR2.png'),
                             pygame.image.load(ROOT + '/skins/Knight/SR3.png')]
        self.type = 'running'
        self.road = road
        self.road_stop = 0
        self.hp = 100
        self.speed = 5
        self.place = self.x, self.y = x, y
        self.bounty = 50
        self.image = self.images_right[0]
        self.rect = self.image.get_rect(center=self.place)
        self.step = 0

    def draw(self):
        a.anim()
        screen.blit(self.image, self.rect)
        pygame.display.flip()

    def move(self):
        if self.road:
            dx, dy = 0, 0
            if math.sqrt(abs(self.rect.x - self.road[0][0]) ** 2 + abs(self.rect.y - self.road[0][1]) ** 2) <= self.speed:
                self.road.append(self.road.pop(0))
            H = math.sqrt((self.rect.x - self.road[0][0]) ** 2 + (self.rect.y - self.road[0][1]) ** 2)
            x = self.rect.x - self.road[0][0]
            y = self.rect.y - self.road[0][1]
            if H:
                cos = round(x / H, 2)
                sin = round(y / H, 2)
                if x != 0 and y != 0:
                    dx = -self.speed * cos
                    dy = -self.speed * sin
                if cos == 1:
                    dx = -self.speed
                if cos == -1:
                    dx = self.speed
                if sin == 1:
                    dy = -self.speed
                if sin == -1:
                    dy = self.speed
            self.rect.x += dx
            self.rect.y += dy

    def anim(self):
        if self.step == 3:
            self.step = 0
        if self.rect.x - self.road[0][0] >= 0:
            self.image = self.images_left[self.step]
        else:
            self.image = self.images_right[self.step]
        self.step += 1


a = Warrior(0, 0, road)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    a.draw()
    a.move()
    for i in range(len(road)):
        pygame.draw.rect(screen, pygame.Color('red'), (list(road[i])[0], list(road[i])[1], 5, 5))
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
