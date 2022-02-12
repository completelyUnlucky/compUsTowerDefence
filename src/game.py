import pygame
import sys
import os
from compUsTowerDefence.src.battleMap import BattleMap
from compUsTowerDefence.npcs.runner import Warrior


class Battlefield:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.battleMap = BattleMap()
        self.towerTypes = []
        self.npcTypes = [Warrior]
        self.towers = []
        self.npc = [Warrior(300, 1080, self.battleMap.waypoints)]
        self.projectiles = []
        self.hp = 20
        self.gold = 0
        self.hpFlow = 0  # amount of npcHp spawned per second. measures difficulty
        self.clock = pygame.time.Clock()

    def getNpcList(self):
        return os.listdir('../npcs/')[1:]

    def utilizeCorpses(self):
        i = 0
        while i < len(self.npc):
            if self.npc[i].hp <= 0:
                self.gold += self.npc[i].bounty
                self.npc.pop(i)
            else:
                i += 1

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.battleMap.draw(self.screen)
        for npc in self.npc:
            npc.draw()
        for tower in self.towers:
            tower.draw(self.screen)

    def buildTower(self, tower, x, y):
        # self.towers.append(tower(x, y))
        # self.gold -= tower.price
        pass

    def mainLoop(self):
        while self.hp > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if self.battleMap.check_building_ground(x, y):
                            self.buildTower(None, x, y)
                            print(self.battleMap.check_building_ground(x, y))
            self.draw()
            self.update()
            self.clock.tick(60)
            pygame.display.flip()

    def update(self):
        for npc in self.npc:
            npc.move()
        self.utilizeCorpses()


tmp = Battlefield()
tmp.mainLoop()
