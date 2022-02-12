import compUsTowerDefence.main as main
import os
import random
import pygame
import sys
# from maps import *


def process_cords(cords):
    for i in range(len(cords)):
        cord = cords[i].replace('(', '').replace(')', '').replace('\n', '').replace(',', '').split()
        cord = int(cord[0]), int(cord[1])
        cords[i] = cord
    return cords


class BattleMap:
    def __init__(self):
        chozen_map = random.choice([file for file in os.listdir(main.find_pack('maps'))])
        self.map_img = pygame.image.load(f"{main.find_pack('maps')}/{chozen_map}/{chozen_map}.png")
        self.map_rect = self.map_img.get_rect(topleft=(0, 0))
        self.waypoints = process_cords(open(f"{main.find_pack('maps')}/{chozen_map}/{chozen_map}.route").readlines())
        self.mounting_points = process_cords(open(main.find_file('example.mp')).readlines())

    def draw(self, screen):
        screen.blit(self.map_img, self.map_rect)

    def check_building_ground(self, x, y):
        for i in self.mounting_points:
            if i[0] <= x <= i[0] + 70 and i[1] <= y <= i[1] + 70:
                return True
        return False


a = BattleMap()
print(a.check_building_ground(780, 480))
