import pygame, os, random
from Mario import Mario

RUN = True
pygame.init()
WIN = pygame.display.set_mode((640,800))
MARIO = Mario()
CLOCK = pygame.time.Clock()

def handleEvent():
    global RUN
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            RUN = False

def update():
    global CLOCK
    CLOCK.tick(30)
    MARIO.update(CLOCK)
    handleEvent()
    draw()

def draw():
    global WIN
    WIN.fill((200,255,200))
    MARIO.draw(WIN)
    pygame.display.update()

while RUN:
    update()

pygame.quit()
