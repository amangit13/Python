import serial
import time
import pygame

ser = serial.Serial("com4",9600, timeout=0)
#ser.set_buffer_size(rx_size = 4_028,tx_size = 256)
pygame.init()
SCREEN = pygame.display.set_mode((800,500))
FONT = pygame.font.SysFont("",34)
SMALLFNT = pygame.font.SysFont("", 22)
LAYER = 0
SCALE = 1
CONTENT = ""

class Plotter:
    def __init__(self):
        self.x = 1
        self.y=0
        self.scalex = 1


    def draw(self):
        global SCREEN
        global CONTENT
        waiting = ser.in_waiting
        print (waiting)

        if waiting > 0:
            CONTENT = ser.read(waiting)

            pxarray = pygame.PixelArray(SCREEN)

            for cont in CONTENT:
                self.scalex += 1
                self.x += 1
                
                if self.x > 799:
                    self.x=0
                    SCREEN.fill((0,0,0))

                self.y = cont+10
                pxarray[self.x,self.y] = (255,0,0)
            pxarray.close()

        #sfnt = SMALLFNT.render(CONTENT,True,(255,255,255))
        #SCREEN.blit(sfnt,(100,300))

if __name__ == "__main__":
    RUN = True

    comps = Plotter()

    fps = pygame.time.Clock()

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
 
        comps.draw()

        pygame.display.update()
        fps.tick(10)
        
    pygame.quit()
    ser.close()






