import  pygame
from  pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("draw Line")

while True:
    for  event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

#draw line
    color = 100,255,200
    screen.fill((0,80,0))
    width = 10

    pygame.draw.line(screen,color,(100,100),(500,400),width)
    pygame.display.update()