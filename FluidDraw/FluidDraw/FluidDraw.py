import pygame

pygame.init()
SCREEN = pygame.display.set_mode((1024,768))
FONT = pygame.font.SysFont("",34)
SMALLFNT = pygame.font.SysFont("", 22)
LAYER = 0
SCALE = 1

class Comp:
    def __init__(self, x,y,name,desc = "", layer=0,w=200,h=100):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name
        self.desc = desc
        self.layer = layer

    def draw(self):
        global SCREEN
        if self.layer == LAYER:
            pygame.draw.rect(SCREEN,(255,255,255),(self.x*SCALE,self.y*SCALE,self.w*SCALE,self.h*SCALE),1)
            fnt = FONT.render(self.name,True,(255,255,255))
            sfnt = SMALLFNT.render(self.desc,True,(255,255,255))
            fnt = pygame.transform.rotozoom(fnt, 0, SCALE)
            sfnt = pygame.transform.rotozoom(sfnt, 0, SCALE)
            SCREEN.blit(fnt,((self.x+3)*SCALE,(self.y+3)*SCALE))
            SCREEN.blit(sfnt,((self.x+3)*SCALE,(self.y+50)*SCALE))

if __name__ == "__main__":
    RUN = True

    comps = [Comp(10,10,"TW Scheduler"), 
         Comp(400,10,"TW Allocator", "allocates machines")
         ]

    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                RUN = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                RUN = False
            elif event.type == pygame.MOUSEWHEEL:
                SCALE += event.y/10
                if SCALE < .5:
                    SCALE = .5
                if SCALE > 4:
                   SCALE = 4
 
        SCREEN.fill((0,0,0))
        for c in comps:
            c.draw()
        pygame.display.update()

    pygame.quit()

