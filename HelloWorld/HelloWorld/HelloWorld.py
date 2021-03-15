import pygame, random, os

win = None
font = None

class Sprite:
    def __init__(self):
        self.x=10
        self.y=10

    def update(self):
        self.x+=1
        self.y+=1
        if (self.x > win.get_width()):
            self.x = random.randint(1,100)
        if (self.y > win.get_height()):
            self.y= random.randint(1,100)

    def draw(self):
        #pygame.draw.circle(win, pygame.Color(255,0,0), (self.x,self.y),2)
        pygame.draw.line(win, pygame.Color(255,0,0,),(self.x, self.y), (self.x+1, self.y),5)


def mainInit():
    global font, win, sonic
    pygame.init()
    font = pygame.font.get_default_font()
    
    print(font)
    win = pygame.display.set_mode((1024,768))

def draw():
    #win.fill((0,0,0,0))
    ball.draw()
    pygame.display.update()

def updateLoop():
 
    running = True
    while running:
        ball.update()
        draw()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
    return 


mainInit()
global ball
ball = Sprite()
updateLoop()
pygame.quit()


