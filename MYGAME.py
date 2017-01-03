import  pygame
from  pygame.locals import  *

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("draw circles")
myfont = pygame.font.Font(None,60)

white = 255,255,255
blue = 0,0,255
# textImage = myfont.render("d",True,white)



#循环事件
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))
    #draw a ccircles
    color = 255,255,0
    position = 300,200
    radius = 100
    width = 10
    pygame.draw.circle(screen,color,position,radius,width)
    pygame.display.update()