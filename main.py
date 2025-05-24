from constants import *
import pygame

import disk
import rods

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

diskManager = disk.DiskManager()
rods = rods.Rods()



def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        fps = clock.get_fps()
        moves = disk.Disk.moves
        pygame.display.set_caption(f"Tower of Hanoi - FPS: {fps:.2f}, Moves:{moves}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                diskManager.click(pos)
                rods.click(pos, diskManager)



        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    rods.draw(surface)
    diskManager.draw(surface)
    pygame.display.flip()



def update():
    diskManager.update(rods.rods)
    rods.update()



if __name__ == "__main__":
    main()
