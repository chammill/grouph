import pygame
import pygame.event as EVENTS



pygame.init()
color = pygame.Color
IntroBackground = pygame.image.load('gameBackground.png')
gameIntroBackground = pygame.image.load('introBack.jpg')
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('S.E.E.D')
clock = pygame.time.Clock()
smallText = pygame.font.Font("freesansbold.ttf",20)
dialogueBox = pygame.draw.rect(gameDisplay,color('white'),(50,400,700,200))
moralResponse1 = 0
moralResponse2 = 0
moralResponse3 = 0
moralResponse4 = 0
def quitGame():
    pygame.quit()
    quit()

def fade(width,height):
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
    clock.tick(20)
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        redrawGameDisplay()
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(29)

def redrawGameDisplay():
    wallpaper(IntroBackground, 0, 0)
    message_display('S.E.E.D','freesansbold.ttf',115,color('blue'),display_width,display_height,True)


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

def continueDialogue():
    pygame.display.update()
    stop = 1
    while stop > 0:
        for event in EVENTS.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop = 0
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()



def moralDialogue(moralEvent=None):
    pygame.display.update()
    stop = 1
    while stop > 0:
        for event in EVENTS.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    #moralEvent(1)
                    print("1")
                elif event.key == pygame.K_2:
                    #moralEvent(2)
                    print('2')
                elif event.key == pygame.K_3:
                    #moralEvent(3)
                    print('3')
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

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


def getText(lineStart,lineEnd):
    f = open("Story.txt", 'r')
    lines = f.readlines()
    f.close()
    story = []

    for lineNumber in range(lineStart, lineEnd):
        story.append(lines[lineNumber])

    return story


def displayDialogue(story):

    basicFont = pygame.font.SysFont(None, 20)

    text = basicFont.render('', True, (255, 0, 255), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx += 55
    textrect.centery += 390

    pygame.draw.rect(gameDisplay, color('white'), (50, 400, 700, 150))

    for line in story:
        # each i has a newline character, so by i[:-1] we will get rid of it
        text = basicFont.render(line[:-1], True, (0, 0, 0), (255, 255, 255))
        # by changing the y coordinate each i from lines will appear just
        # below the previous i
        textrect.centery += 15
        gameDisplay.blit(text, textrect)










def mainMenu():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        gameDisplay.fill(color("blue"))
        wallpaper(IntroBackground,0,0)
        message_display('S.E.E.D', 'freesansbold.ttf', 115,color('blue'),display_width,display_height,True)

        button("Start", 350,300,100,50,color("forestgreen"),color("green"),gameIntro)
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
            gameDisplay.fill(color("green"))
            wallpaper(gameIntroBackground,0,0)


            opening = getText(0,5)
            displayDialogue(opening)
            continueDialogue()

            opening = getText(6,10)
            displayDialogue(opening)
            continueDialogue()

            opening = getText(11, 15)
            displayDialogue(opening)
            continueDialogue()

            dialogue = getText(22, 25)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(26, 27)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(28, 30)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(31, 32)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(33, 34)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(35, 36)
            displayDialogue(dialogue)
            continueDialogue()

            #LobbyLevel
            dialogue = getText(41, 42)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(43, 44)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(45, 48)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(52,53)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(54,55)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(56, 57)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(58, 59)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(60, 63)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(64, 65)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()

            dialogue = getText(66, 67)
            displayDialogue(dialogue)
            continueDialogue()




            moralDialogue()



            clock.tick(30)







mainMenu()

