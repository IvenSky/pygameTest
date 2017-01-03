import  pygame
from  pygame.locals import *
import  math

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("pie page --press 1,2,3,4")
myfont = pygame.font.Font(None,60)

color = 200,80,60
width = 8
x = 300
y = 250
radius = 200
position = x-radius,y-radius,radius*2,radius*2

piecel1 = False
piecel2 = False
piecel3 = False
piecel4 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            print("up")
            if event.key == pygame.K_ESCAPE:
                print("escape")
                sys.exit()
            elif event.key == pygame.K_1:
                piecel1 = True
                print("1")
                print(piecel1)
            elif event.key == pygame.K_2:
                piecel2 =True
                print("2")
            elif event.key == pygame.K_3:
                piecel3 = True
                print("3")
            elif event.key == pygame.K_4:
                print("4")
                piecel4 = True

    screen.fill((0, 0, 200))
    textIamge1 = myfont.render("1",True,color)
    screen.blit(textIamge1,(x+radius/2-20,y-radius/2))
    textIamge2= myfont.render("2", True, color)
    screen.blit(textIamge2, (x - radius / 2 , y - radius / 2))
    textIamge3 = myfont.render("3", True, color)
    screen.blit(textIamge3, (x - radius / 2 , y +radius / 2 - 20))
    textIamge4 = myfont.render("4", True, color)
    screen.blit(textIamge4, (x + radius / 2 - 20, y + radius / 2 - 20))
    if piecel1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y-radius),width)
        pygame.draw.line(screen,color,(x,y),(x+radius,y),width)
    if piecel2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
    if piecel3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x-radius, y ), width)
        pygame.draw.line(screen, color, (x, y), (x , y+radius), width)
    if piecel4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)
    if piecel1 and piecel2 and piecel3 and piecel4:
        color = 0,255,0
    pygame.display.update()