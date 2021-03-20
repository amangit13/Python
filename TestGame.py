import time
import pygame


def gameinit():
    pygame.init()
    pygame.font.init()

def update():
    frame = 100
    running = True
    pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                running = False
            else:
                print(event)

        if (frame >= 100):
            pygame.display.update()
            frame = 0
        frame += 1

def main():
    print ("new game tbd")

    gameinit()
    
    myfont = pygame.font.SysFont("Ariel",60)

    surface = pygame.display.set_mode((640,400))

    fontsurf = myfont.render ("Amaira", True, (255,255,255))

    surface.blit(fontsurf, (12,12))

    pygame.draw.rect(surface, (255,0,0), (10,10,100,100), 2)

    update()

    pygame.quit()
    print ("done")

main()
