import pygame, os

class Mario(object):
    def __init__(self):
        self.SPR = pygame.image.load("mario.png")
        self.cellidx = 0

    def update(self, clock):
            self.cellidx += 1
            if self.cellidx == 11:
                self.cellidx = 0

    def draw(self, win):
        win.blit(self.SPR, (100,100), (0, self.cellidx * 57, 40, 53))