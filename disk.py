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
        self.has_moved = False



    def unselect(self):
        self.is_selected = False



    def update(self):
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
            self.has_moved = True
            Disk.moves += 1









class DiskManager():

    def __init__(self):
        self.disks = []
        self.num_of_disks = 6
        self.game_won = False


        for i in range(1, self.num_of_disks):
            self.disks.append(Disk(self.num_of_disks - i, COLORS[i - 1], i))


    def update(self, rods):
        for disk in self.disks:
            disk.update()

        all_on_same_rod_and_true = (
            len(set(d.rod_index for d in self.disks)) == 1 and
            all(d.has_moved for d in self.disks)
        )

        if all_on_same_rod_and_true:
            self.game_won = True
            print("game won")



    def draw(self, surface):
        if self.game_won:
            font = pygame.font.SysFont(None, 36)  # None = default font, 36 = size
            text_surface = font.render(f"Game Won!  Took {Disk.moves} Moves To Win", True, (255, 255, 255))  # White text
            surface.blit(text_surface, (50, 50))  # Draw at position (50, 50)



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

    def reset(self):
        self.__init__()
        Disk.moves = 0

    def win(self):
        for disk in self.disks:
            disk.rod_index = 0
            disk.has_moved = True
