import  pygame
from  pygame.locals import *
import  math

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("draw Arc")

while True:
    for event in pygame.event.get():
        if event in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))
    color = 255,0,255
    width = 5
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    position  = 200,150,200,200
    pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
    pygame.display.update()