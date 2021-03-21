import pygame
from numba import njit

## numba jit does not work with pygame, classes, etc.
class Box:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255),(self.x,10,50,50),2)

    def handleinput(self, event):
        pass

    def update(self):
        self.x += 1
        if self.x > 630:
            self.x = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    box = Box(1,1)
    
    running = True

    while (running):
        ## handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                box.handleinput(event)

        ## update game logic
        box.update()

        ## draw
        screen.fill((0,0,0))
        box.draw(screen)
        pygame.display.update()

    pygame.quit()
    
        

main()
