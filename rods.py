from constants import *
import pygame


class Rod(object):

    def __init__(self, x, index):

        self.width = BLOCK_SIZE // 2
        self.height = BLOCK_SIZE * 3
        self.color = (139, 69, 19)
        self.x = x
        self.y = GAME_HEIGHT - self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.index = index


    def update(self):
            pass



    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


    def click(self, rods, mouse_pos, diskManager):
        if self.rect.collidepoint(mouse_pos):
            diskManager.move(self)



class Rods(object):
    def __init__(self):
        self.rods = []
        self.gap = BLOCK_SIZE * 3.5
        self.offset = BLOCK_SIZE * 1.5

        self.rods.append(Rod(GAME_WIDTH // 6 - BLOCK_SIZE // 4, 0))
        self.rods.append(Rod(GAME_WIDTH // 2 - BLOCK_SIZE // 4, 1))
        self.rods.append(Rod(GAME_WIDTH - GAME_WIDTH // 6 - BLOCK_SIZE // 4, 2))


    def update(self):
        for rod in self.rods:
            rod.update()


    def draw(self, surface):
        for rod in self.rods:
            rod.draw(surface)


    def unselect_all(self):
        for rod in self.rods:
            rod.unselect()


    def click(self, mouse_pos, diskManager):
        for rod in self.rods:
            rod.click(self, mouse_pos, diskManager)
