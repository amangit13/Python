import pygame
import random


class Cell:
    def __init__(self, val, r, c):
        
        self.val = 11 if (r,c) in ((0,0),(6,0),(0,6),(6,6)) else val
        self.trs = 0
        self.r = r*52+52
        self.c = c*52+52
        self.off = 0
        self.step = .3
        
    def draw(self, screen):            
        screen.blit(IMG[self.val], (self.c, self.r, 50,50))

        if self.trs:
            screen.blit(TRS, (self.c, self.r + self.off, 50, 50))
            self.off += self.step
            
            if self.off > 5:
                self.step = -.3
            else:
                if self.off <= 0:
                    self.step = .3

    def update(self, event):
        pass

class Board:
    
    def __init__(self):
        self.cell = [[Cell(random.randint(0,10),r,c)
                      for r in range(7)] for c in range(7)]

    def setTRS(self):
        self.cell[random.randint(1,6)][random.randint(1,6)].trs = 1
        
    def update(self):
        pass

    def draw(self, screen):
        for rows in self.cell:
            for col in rows:
                col.draw(screen)

## init
pygame.init()
dic = {0:'NE',1:'NS',2:'NE',3:'SE',4:'SW',5:'NW',
       6:'NWE',7:'SWE',8:'NES',9:'NWS', 10:'NEWS',
       11:'PLY'}

IMG = [pygame.image.load('pygame'+dic[key]+'.png') for key in dic]
TRS = pygame.image.load('pygameTRS.png')

screen = pygame.display.set_mode((600,480))
board = Board()
board.setTRS()
fps = pygame.time.Clock()

## game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    ## update

    ## draw
    board.draw(screen)
    pygame.display.update()
    fps.tick(30)
    

pygame.quit()
