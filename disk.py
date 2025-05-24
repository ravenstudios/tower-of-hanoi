from constants import *
import pygame


class Disk():
    moves = 0
    def __init__(self, width, color, y_index):

        self.width = width * BLOCK_SIZE
        self.height = BLOCK_SIZE // 2
        self.color = color
        self.x = GAME_WIDTH // 2  - self.width // 2
        self.y = GAME_HEIGHT - BLOCK_SIZE // 2 * y_index
        self.rod_index = 1
        self.is_selected = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)



    def unselect(self):
        self.is_selected = False



    def update(self, rods, diskManager):
        pass


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.is_selected:
            pygame.draw.rect(surface, WHITE, self.rect, 1)


    def click(self, diskManager, mouse_pos):

        if self.rect.collidepoint(mouse_pos):
            disks_on_current_rod = [disk for disk in diskManager.disks if disk.rod_index == self.rod_index]
            if self != disks_on_current_rod[-1]:
                return
            if self.is_selected:
                self.is_selected = False
            else:
                diskManager.unselect_all()
                self.is_selected = True


    def move(self, rod, diskManager):
        if self.is_selected and rod.index != self.rod_index:
            disks_on_rod = []

            for disk in diskManager.disks:
                if disk.rod_index == rod.index:
                    disks_on_rod.append(disk)

            if disks_on_rod:
                top_disk_length = disks_on_rod[-1].rect.width
                if top_disk_length < self.rect.width:
                    return
                self.rect.y = GAME_HEIGHT - self.rect.height * (len(disks_on_rod) + 1)
            else:
                self.rect.y = GAME_HEIGHT - self.rect.height

            self.rod_index = rod.index
            self.rect.x = rod.x - self.width // 2 + rod.width // 2
            self.is_selected = False
            Disk.moves += 1

            # find if the top disk is smaller than current disk








class DiskManager():

    def __init__(self):
        self.disks = []
        self.num_of_disks = 6
        for i in range(1, self.num_of_disks):
            self.disks.append(Disk(self.num_of_disks - i, COLORS[i - 1], i))


    def update(self, rods):
        for disk in self.disks:
            disk.update(rods, self)


    def draw(self, surface):
        for disk in self.disks:
            disk.draw(surface)


    def unselect_all(self):
        for disk in self.disks:
            disk.unselect()

    def click(self, mouse_pos):
        for disk in self.disks:
            disk.click(self, mouse_pos)

    def move(self, rod):
        for disk in self.disks:
            disk.move(rod, self)
