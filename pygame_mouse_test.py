import pygame
import random
pygame.init()
SCREEN = pygame.display.set_mode((600,600))
pygame.display.update()

RUN = True
POS = (0,0)
CLR = (255,0,0)

while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:
                if POS == (0,0):
                    POS = event.pos
                pygame.draw.line(SCREEN, CLR, POS,
                                 event.pos, 2)
                POS = event.pos
            else:
                POS = (0,0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                SCREEN.fill((0,0,0))
            if event.key == pygame.K_SPACE:
                CLR = (random.randrange(10,255), random.randrange(10,255),
                       random.randrange(10,255))
                

        pygame.display.update()
pygame.quit()
