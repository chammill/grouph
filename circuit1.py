import pygame, sys
pygame.init()

winWidth = 800
winHeight = 600
FPS = 30

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("game template")

x = 30
y = 40
width = 20
height = 20
vel = 5
block_size = 10

lineX = 30
lineY = 46
lineWidth = 500
lineHeight = 5

RED = (255,0,0)
GREEN = (0, 255,0)

toggle1 = RED
toggle2 = RED
toggle3 = RED
toggle4 = RED

global lever1
lever1 = False
global lever2
lever2 = False
global lever3
lever3 = False
global lever4
lever4 = False

leverWidth = 20
leverHeight = 30
leverY = 500

lever1X = 120
lever2X = 220
lever3X = 320
lever4X = 420

cirRad = 10

def gameExit():
    pygame.quit()
    sys.exit()

def mouseClick():
    coor = pygame.mouse.get_pos()
    global lever1
    global lever2
    global lever3
    global lever4

    global toggle1
    global toggle2
    global toggle3
    global toggle4
    if (lever1X<coor[0]<(lever1X+leverWidth)):
        if (leverY<coor[1]<(leverY+leverHeight)):
            if (lever1 == False):
                lever1 = True
                toggle1 = GREEN
            else:
                lever1 = False
                toggle1 = RED
            if (lever3 == False):
                lever3 = True
                toggle3 = GREEN
            else:
                lever3 = False
                toggle3 = RED
    if (lever2X < coor[0] < (lever2X + leverWidth)):
        if (leverY < coor[1] < (leverY + leverHeight)):
            if (lever1 == False):
                lever1 = True
                toggle1 = GREEN
            else:
                lever1 = False
                toggle1 = RED
            if (lever4 == False):
                lever4 = True
                toggle4 = GREEN
            else:
                lever4 = False
                toggle4 = RED
    if (lever3X < coor[0] < (lever3X + leverWidth)):
        if (leverY < coor[1] < (leverY + leverHeight)):
            if (lever2 == False):
                lever2 = True
                toggle2 = GREEN
            else:
                lever2 = False
                toggle2 = RED
            if (lever3 == False):
                lever3 = True
                toggle3 = GREEN
            else:
                lever3 = False
                toggle3 = RED
    if (lever4X < coor[0] < (lever4X + leverWidth)):
        if (leverY < coor[1] < (leverY + leverHeight)):
            if (lever2 == False):
                lever2 = True
                toggle2 = GREEN
            else:
                lever2 = False
                toggle2 = RED
            if (lever4 == False):
                lever4 = True
                toggle4 = GREEN
            else:
                lever4 = False
                toggle4 = RED


while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit()

    keys = pygame.key.get_pressed()
    mouse1 = pygame.mouse.get_pressed()
    #pygame.mouse.set_visible()

    if (mouse1 == (1,0,0)):
        mouseClick()

    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 255, 255), (lever1X, leverY, leverWidth, leverHeight))
    pygame.draw.rect(window, (255, 255, 255), (lever2X, leverY, leverWidth, leverHeight))
    pygame.draw.rect(window, (255, 255, 255), (lever3X, leverY, leverWidth, leverHeight))
    pygame.draw.rect(window, (255, 255, 255), (lever4X, leverY, leverWidth, leverHeight))

    pygame.draw.rect(window, (255,0,0), (x,y, width,height))
    pygame.draw.rect(window, (255, 0, 0), (x+500, y, width, height))
    pygame.draw.rect(window, (255,0,0), (lineX,lineY,lineWidth,lineHeight))
    pygame.draw.circle(window, toggle1, (x+ 650, y+ 7), cirRad, 0)

    pygame.draw.rect(window, (0, 255, 0), (x, y+100, width, height))
    pygame.draw.rect(window, (0, 255, 0), (x + 500, y+100, width, height))
    pygame.draw.rect(window, (0, 255, 0), (lineX, lineY+100, lineWidth, lineHeight))
    pygame.draw.circle(window, toggle2, (x + 650, y + 107), cirRad, 0)

    pygame.draw.rect(window, (0, 0, 255), (x, y + 200, width, height))
    pygame.draw.rect(window, (0, 0, 255), (x + 500, y + 200, width, height))
    pygame.draw.rect(window, (0, 0, 255), (lineX, lineY+200, lineWidth, lineHeight))
    pygame.draw.circle(window, toggle3, (x + 650, y + 207), cirRad, 0)

    pygame.draw.rect(window, (255,255,0), (x, y + 300, width, height))
    pygame.draw.rect(window, (255,255,0), (x + 500, y + 300, width, height))
    pygame.draw.rect(window, (255, 255, 0), (lineX, lineY+300, lineWidth, lineHeight))
    pygame.draw.circle(window, toggle4, (x + 650, y + 307), cirRad, 0)

    pygame.display.update()

    if (toggle1 == GREEN):
        if (toggle2 == GREEN):
            if (toggle3 == GREEN):
                if (toggle4 == GREEN):
                    myfont = pygame.font.SysFont("Arial", 60)
                    label = myfont.render("You Win!", 1, (255, 255, 0))
                    window.blit(label, (500, 450))
                    pygame.display.update()

pygame.quit()