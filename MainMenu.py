import pygame



pygame.init()
color = pygame.Color
IntroBackground = pygame.image.load('gameBackground.png')

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('S.E.E.D')
clock = pygame.time.Clock()
smallText = pygame.font.Font("freesansbold.ttf",20)
titleFont = pygame.font.match_font('')

#agencyfb


def quitGame():
    pygame.quit()
    quit()

def fade(width,height):
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
    clock.tick(15)
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        redrawGameDisplay()
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(20)

def redrawGameDisplay():
    wallpaper(IntroBackground, 0, 0)
    message_display('S.E.E.D',titleFont,115,color('blue'),display_width,display_height,True)


def button(msg,x,y,w,h,ic,ac,action=None,FADE=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if FADE == None:
                action()
            else:
                fade(800,600)
                action()


    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    butSurf, butRect = text_objects(msg, smallText, color("black"))
    butRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(butSurf,butRect)



def wallpaper(background,x,y):
    gameDisplay.blit(background,(x,y))

def text_objects(text,Font,color):
    textSurface = Font.render(text,True,color)
    return textSurface, textSurface.get_rect()



def message_display(text,FONT,size,color,xLocation,yLocation,center=None):
    largeText = pygame.font.Font(FONT,size)
    TextSurf, TextRect = text_objects(text, largeText,color)
    if center != None:
        TextRect.center = ((xLocation/2,yLocation/3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def getText(linesSkip=None,lineSize=None,lineNumber=None):
    with open('Story.txt', 'r') as f:
        f_contents = []
        if linesSkip != None:
            f_contents = f.readlines(linesSkip)
            f_contents = f.read(lineSize)
        elif lineNumber != None:
            f_contents = f.readlines(lineNumber)
        else:
            f_contents = f.read(lineSize)

        msg = [str(elem)for elem in f_contents]

        return " ".join(msg)


def mainMenu():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        gameDisplay.fill(color("blue"))
        wallpaper(IntroBackground,0,0)
        message_display('S.E.E.D', titleFont, 115,color('blue'),display_width,display_height,True)

        button("Start", 350,300,100,50,color("forestgreen"),color("green"),gameIntro,True)
        button("Quit", 350, 400, 100, 50, color("darkred"), color("red"),quitGame)




        pygame.display.update()
        clock.tick(15)

def gameIntro():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()

            gameDisplay.fill(color("white"))
            message = getText(None, 30, None)
            message_display(message, 'freesansbold.ttf', 12, color('black'), 300 , 200)

            pygame.display.update()
            clock.tick(30)




def game_loop():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()

            gameDisplay.fill(color("white"))
            pygame.display.update()
            clock.tick(30)


mainMenu()

