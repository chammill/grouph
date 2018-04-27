import pygame
import pygame.event as EVENTS
import sys
import os



pygame.init()
# game assets
game_dir = os.path.dirname(__file__)
# relative path to assets dir
assets_dir = os.path.join(game_dir, "assets")
# relative path to image dir
img_dir = os.path.join(assets_dir, "images")

# initialise pygame settings and create game window
pygame.init()

color = pygame.Color
FPS=60
display_height = 600
display_width = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('S.E.E.D')
global IntroBackground
IntroBackground =  pygame.image.load(os.path.join(img_dir, 'MainMenu.png' )).convert()
gameIntroBackground = pygame.image.load(os.path.join(img_dir, 'MainMenu.png' )).convert()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
mainMenuGreen = (42,57,29)

smallText = pygame.font.Font("freesansbold.ttf",20)
dialogueBox = pygame.draw.rect(gameDisplay,color('white'),(50,400,700,200))
moralResponse1 = 0
moralResponse2 = 0
moralResponse3 = 0
moralResponse4 = 0
gameIntroLoop = True

bg_img = pygame.image.load(os.path.join(img_dir, "main_room.png")).convert()
# add rect for bg - helps locate background
bg_rect = bg_img.get_rect()
# load graphics/images for the game
lobbyLevelTwo = pygame.image.load(os.path.join(img_dir, "main_room2.png")).convert()
bg_rect2 = lobbyLevelTwo.get_rect()

# bookshelf
bookshelf_img = pygame.image.load(os.path.join(img_dir, "bookshelf-green.png")).convert()
# security camera spotlights
security_spot = pygame.image.load(os.path.join(img_dir, "camera_spot.png")).convert()
# scientist
scientist_img = pygame.image.load(os.path.join(img_dir, "scientist.png")).convert()

def quitGame():
    pygame.quit()
    sys.exit()
    quit()


def fade(width,height,color):
    fade = pygame.Surface((width,400))
    fade.fill(color)
    clock.tick(20)
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        redrawGameDisplay()
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(26)


def redrawGameDisplay():
    wallpaper(IntroBackground, 0, 0)
    message_display('S.E.E.D',pygame.font.match_font('agencyfb'),115,color('white'),display_width,display_height,True)


def button(msg,x,y,w,h,ic,ac,action=None,FADE=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if FADE == None:
                action()
            else:
                fade(800,600,mainMenuGreen)
                action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))


    butSurf, butRect = text_objects(msg, smallText, color("black"))
    butRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(butSurf,butRect)
    return False

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


def displayDialogue(story,pos=None):

    basicFont = pygame.font.SysFont(None, 20)


    text = basicFont.render('', True, (255, 0, 255), (0,0,0))
    textrect = text.get_rect()
    textrect.centerx += 55
    textrect.centery += 390

    if pos == None:
        pygame.draw.rect(gameDisplay, WHITE, (50, 400, 700, 100))
        text = basicFont.render('', True, (255, 0, 255), (0,0,0))
        textrect = text.get_rect()
        textrect.centerx += 55
        textrect.centery += 390

    else:
        text = basicFont.render('', True, (255, 0, 255), (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx += 55
        textrect.centery += 40

        pygame.draw.rect(gameDisplay, WHITE, (50, 50, 700, 100))



    for line in story:
        # each i has a newline character, so by i[:-1] we will get rid of it
        text = basicFont.render(line[:-1], True, (0, 0, 0), (255, 255, 255))
        # by changing the y coordinate each i from lines will appear just
        # below the previous i
        textrect.centery += 15
        gameDisplay.blit(text, textrect)
    '''gameDisplay.blit(contHint, textrect)'''


# variables for commonly used colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


global toggle1
global toggle2
global toggle3
global toggle4
global toggle5
global toggle6
global toggle7
global toggle8
global toggle9
global toggle10

global lever1
global lever2
global lever3
global lever4
global lever5
global lever6
global lever7
global lever8
global lever9
global lever10

global lever1X
global lever2X
global lever3X
global lever4X
global lever5X
global lever6X
global lever7X
global lever8X
global lever9X
global lever10x


lever1 = False
lever2 = False
lever3 = False
lever4 = False
lever5 = False
lever6 = False
lever7 = False
lever8 = False
lever9 = False
lever10 = False

toggle1 = False
toggle2 = False
toggle3 = False
toggle4 = False
toggle5 = False
toggle6 = False
toggle7 = False
toggle8 = False
toggle9 = False
toggle10 = False

# initialise pygame settings and create game window
#interaction = "empty"


# create a default player sprite for the game
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = pygame.transform.scale(char_img, (24, 30))
        # set colorkey to remove white background for char's rect
        self.image.set_colorkey(WHITE)
        # check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = x
        self.rect.bottom = y

        self.speed_x = 0
        self.speed_y = 0

    # update per loop iteration
    def update(self):
        self.speed_x = 0
        self.speed_y = 0

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_a]:
            self.speed_x = -4
            # change to facing left image
            self.image = pygame.transform.scale(char_img_l, (24, 30))
            # set colorkey to remove black background for ship's rect
            self.image.set_colorkey(WHITE)
        if key_state[pygame.K_d]:
            self.speed_x = 4
            # change to facing right image
            self.image = pygame.transform.scale(char_img_r, (24, 30))
            # set colorkey to remove black background for ship's rect
            self.image.set_colorkey(WHITE)
        if key_state[pygame.K_w]:
            self.speed_y = -4
            # change to facing up image
            self.image = pygame.transform.scale(char_img_u, (24, 30))
            # set colorkey to remove black background for ship's rect
            self.image.set_colorkey(WHITE)
        if key_state[pygame.K_s]:
            self.speed_y = 4
            # change to facing down image
            self.image = pygame.transform.scale(char_img, (24, 30))
            # set colorkey to remove black background for ship's rect
            self.image.set_colorkey(WHITE)
        self.rect.x += self.speed_x

        if self.rect.right > display_width:
            self.rect.right = display_width
        if self.rect.left < 0:
            self.rect.left = 0

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.speed_x > 0:
                self.rect.right = block.rect.left

            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                # Check and see if we hit anything

        self.rect.y += self.speed_y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > display_height:
            self.rect.bottom = display_height

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


# player's character
char_img = pygame.image.load(os.path.join(img_dir, "char1.png")).convert()
# player's character facing right
char_img_r = pygame.image.load(os.path.join(img_dir, "char1r.png")).convert()
# player's character facing left
char_img_l = pygame.image.load(os.path.join(img_dir, "char1l.png")).convert()
# player's character facing up
char_img_u = pygame.image.load(os.path.join(img_dir, "char1u.png")).convert()


# wall
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

# create a bookshelf
class Bookshelf(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = bookshelf_img
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(GREEN)
        # check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.image = pygame.Surface([width, height])
        self.rect.centerx = x
        self.rect.bottom = y

# create a scientist
class Scientist(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = scientist_img
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(WHITE)
        # check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 1
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = display_width - 300
        self.rect.bottom = display_height - 280

# create security spots
class Security(pygame.sprite.Sprite):
    def __init__(self, x, y, flag,xStart=0,Ystart=0):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = security_spot
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(WHITE)
        #check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 2.5
       # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = x
        self.rect.bottom = y
        # speed along the x-axis
        self.speed_x = xStart
        # speed along the y-axis
        self.speed_y = Ystart
        # check timer for last update to reverse
        self.reverse_update = pygame.time.get_ticks()
        self.time_elapsed_since_last_action = 0
        self.flag = flag

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # call reverse update
        time_now = pygame.time.get_ticks()


        # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
        if self.time_elapsed_since_last_action < 50:
            self.time_elapsed_since_last_action += 1
        else:
            self.time_elapsed_since_last_action = 0
            self.reverse()

    def reverse(self):
        if self.flag == 1:
            if self.speed_x > 0:
                self.speed_x = -1
            else:
                self.speed_x = 1

        if self.flag == 2:
            self.speed_x = 0
            if self.speed_y > 0:
                self.speed_y = -1
            else:
                self.speed_y = 1

        if self.flag ==3 :
            if self.speed_y > 0:
                self.speed_y = -1
                if self.speed_x > 0:
                    self.speed_x = -1
                else:
                    self.speed_x = 1
            else:
                self.speed_y = 1
                if self.speed_x > 0:
                    self.speed_x = -1
                else:
                    self.speed_x = 1

class Lever(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, "lever-down.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #checks images and get rect...
        self.rect.center = (display_width / 2, display_height / 2)
        self.rect.x = x
        self.rect.y = y
        #x = 60 wide
        #y = 70 height

    def switchUp(self):
        global lever1
        global lever2
        global lever3
        global lever4
        global lever5
        global lever6
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load(os.path.join(img_dir, "lever-middle.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # checks images and get rect...
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load(os.path.join(img_dir, "lever-up.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # checks images and get rect...
        self.rect.x = x
        self.rect.y = y

    def switchDown(self):
        x = self.rect.x
        y = self.rect.y
        self.image = pygame.image.load(os.path.join(img_dir, "lever-middle.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # checks images and get rect...
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load(os.path.join(img_dir, "lever-down.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # checks images and get rect...
        self.rect.x = x
        self.rect.y = y

#lever coordinates
leverWidth = 60
leverHeight = 70
leverY = 500

lever1X = 75
lever2X = 200
lever3X = 325
lever4X = 450
lever5X = 560
lever6X = 680

lightRowOneY = 90
lightRowTwoY = 205

#Levers
leverOne = Lever(lever1X,leverY)
leverTwo = Lever(lever2X,leverY)
leverThree = Lever(lever3X,leverY)
leverFour = Lever(lever4X,leverY)
leverFive = Lever(lever5X,leverY)
leverSix = Lever(lever6X,leverY)

class Light(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, "red-light.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()  # checks images and get rect...
        self.rect.center = (display_width / 2, display_height / 2)
        self.rect.x = x
        self.rect.y = y
    def checkTValue(self,toggle):
        if (toggle==False):
            x = self.rect.x
            y = self.rect.y
            self.image = pygame.image.load(os.path.join(img_dir, "green-light.png")).convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()  # checks images and get rect...
            self.rect.center = (display_width / 2, display_height / 2)
            self.rect.x = x
            self.rect.y = y
        elif (toggle==True):
            x = self.rect.x
            y = self.rect.y
            self.image = pygame.image.load(os.path.join(img_dir, "red-light.png")).convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()  # checks images and get rect...
            self.rect.center = (display_width / 2, display_height / 2)
            self.rect.x = x
            self.rect.y = y

#light coordinates
lightX = 675

lever1X = 75
lever2X = 190
lever3X = 320
lever4X = 440
lever5X = 560
lever6X = 680
light1Y = 45
light2Y = 160
light3Y = 275
light4Y = 395

#Lights
lightOne = Light(lightX,light1Y)
lightTwo = Light(lightX,light2Y)
lightThree = Light(lightX,light3Y)
lightFour = Light(lightX,light4Y)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(os.path.join(img_dir, image_file)).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


#Next Level Interactions
lobbyLevelPart2 = Wall(400,550,100,100)
elevatorDoor = Wall(400,500,50,20)
elevatorDoorLeaving = Wall(350,275,50,50)
bathroomDoor = Wall(25,300,10,50)
bathroomDoorExit = Wall(640,350,10,50)
officeEntrance = Wall(425,175,50,50)
officeExit = Wall(350,545,50,50)
elevatorDoorToBasement = Wall(410,570,50,50)
basementDoorOneCorrect = Wall(615,170,10,50)
basementDoorOneWrong = Wall(400, 60,50,50)
basementDoorTwoCorrect = Wall(595,430,50,50)
basementDoorTwoWrong = Wall(375,537,50,50)
basementDoorThree = Wall(425,100,50,20)


#dialogue prompts
lobbyDesk = Wall(680,275,50,50)
moralEvent1 = Wall(225,200,300,40)
officeDesk = Wall(370,225,90,50)


#Panels
elevatorPanel = Wall(495,245,50,100)
bathroomPanel = Wall(550,150,50,50)
basementPuzzle1Correct =Wall(180,270,50,30)
basementPuzzle1Wrong = Wall(610,460,30,30)
basementPuzzle2Correct = Wall(185,360,30,30)
basementPuzzle2Wrong = Wall(495,65,50,50)
basementPuzzle3Correct = Wall(585,410,30,30)
basementPuzzle3Wrong = Wall(585,200,30,30)

# sprite groups - game, mob, projectiles...
game_sprites = pygame.sprite.Group()
mob_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
interactives = pygame.sprite.Group()
correctDoor = pygame.sprite.Group()
wrongDoor = pygame.sprite.Group()
security_spots1 = pygame.sprite.Group()
puzzleInteractions = pygame.sprite.Group()
puzzleInteractionsW = pygame.sprite.Group()
wall_list = pygame.sprite.Group()


# create player object spawns
playerList =[]
playerlobbyPart1 = Player(25,280)
playerlobbyPart2 = Player(400,150)
playerelevatorLevel = Player(400,350)
playerWaitingRoomOne = Player(425,550)
playerBathroom = Player(625,400)
playerWaitingRoomTwo = Player(50,350)
playerOffice = Player(400,550)
playerWaitingRoomThree = Player(400,200)
playerBasementOne = Player(415,550)
playerBasementTwo = Player(225,200)
playerBasementThree = Player(190,410)
playerFinal = Player(380,450)


playerList.append(playerlobbyPart1)
playerList.append(playerlobbyPart2)
playerList.append(playerelevatorLevel)
playerList.append(playerWaitingRoomOne)
playerList.append(playerBathroom)
playerList.append(playerWaitingRoomTwo)
playerList.append(playerWaitingRoomThree)
playerList.append(playerOffice)
playerList.append(playerBasementOne)
playerList.append(playerBasementTwo)
playerList.append(playerBasementThree)
playerList.append(playerFinal)

for player in playerList:
    player.walls = wall_list



scientist = Scientist()

# add sprite to game's sprite group
'''game_sprites.add(playerlobbyPart1, scientist)'''
# add sprites for security spots

# new bookshelf group

interactives.add(lobbyLevelPart2)

def gameExit():
    pygame.quit()
    sys.exit()

def puzzleReset():
    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6
    global toggle7
    global toggle8
    global toggle9
    global toggle10

    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6
    global lever7
    global lever8
    global lever9
    global lever10

    global lever1X
    global lever2X
    global lever3X
    global lever4X
    global lever5X
    global lever6X
    global lever7X
    global lever8X
    global lever9X
    global lever10x

    lever1 = False
    lever2 = False
    lever3 = False
    lever4 = False
    lever5 = False
    lever6 = False
    lever7 = False
    lever8 = False
    lever9 = False
    lever10 = False

    toggle1 = False
    toggle2 = False
    toggle3 = False
    toggle4 = False
    toggle5 = False
    toggle6 = False
    toggle7 = False
    toggle8 = False
    toggle9 = False
    toggle10 = False

def createWall(level):

    if (level == 'lobby1'):
        # top wall
        wall = Wall(0, 80, 800, 60)
        wall_list.add(wall)


        # left wall
        wall = Wall(0, 80, 25, 600)
        wall_list.add(wall)



        # right wall
        wall = Wall(775, 80, 25, 600)
        wall_list.add(wall)



        # bottom wall
        wall = Wall(0, 490, 380, 120)
        wall_list.add(wall)



        # top desk
        wall = Wall(150, 180, 80, 30)
        wall_list.add(wall)



        # middle desk
        wall = Wall(680, 280, 30, 80)
        wall_list.add(wall)



        # bottom desk
        wall = Wall(280, 410, 30, 80)
        wall_list.add(wall)


        #Fallen Bookshelf
        wall = Wall(540, 490, 200, 100)
        wall_list.add(wall)



    elif (level == 'lobby2'):

        # top wall
        wall = Wall(0, 20, 800, 60)
        wall_list.add(wall)

        # left wall
        wall = Wall(195, 00, 20, 800)
        wall_list.add(wall)

        # right wall
        wall = Wall(575, 80, 25, 600)
        wall_list.add(wall)


        # bottom wall
        wall = Wall(0, 520, 800, 120)
        wall_list.add(wall)


        #Bookshelves
        wall = Wall(225, 360, 40, 40)
        wall_list.add(wall)


        wall = Wall(520, 210, 65, 40)
        wall_list.add(wall)


        wall = Wall(410, 360, 150, 80)
        wall_list.add(wall)


    elif (level == 'elevator'):

        # top wall
        wall = Wall(250, 200, 400, 60)
        wall_list.add(wall)


        # left block
        wall = Wall(230, 140, 120, 200)
        wall_list.add(wall)


        # left wall
        wall = Wall(255, 120, 20, 400)
        wall_list.add(wall)


        # right block
        wall = Wall(440, 140, 120, 200)
        wall_list.add(wall)


        # right wall
        wall = Wall(520, 120, 20, 400)
        wall_list.add(wall)


        # bottom wall
        wall = Wall(250, 470, 400, 60)
        wall_list.add(wall)


    elif (level == 'waitingRoom'):

        # left wall
        wall = Wall(0, 0, 25, 600)
        wall_list.add(wall)

        # top left wall
        wall = Wall(0,120, 370, 60)
        wall_list.add(wall)


        # top right wall
        wall = Wall(460, 120, 370, 60)
        wall_list.add(wall)


        # right wall
        wall = Wall(775, 10, 25, 600)
        wall_list.add(wall)


        # top right desk
        wall = Wall(470, 270, 60, 40)
        wall_list.add(wall)


        # top left desk
        wall = Wall(290, 270, 60, 40)
        wall_list.add(wall)


        # bottom right desk
        wall = Wall(470, 380, 60, 50)
        wall_list.add(wall)


        # bottom left desk
        wall = Wall(290, 380, 60, 50)
        wall_list.add(wall)


        #Bottom Wall
        wall = Wall(0, 565, 800, 120)
        wall_list.add(wall)

    elif (level == 'bathroom'):

        # top wall
        wall = Wall(0, 0, 800, 200)
        wall_list.add(wall)


        # stalls
        wall = Wall(180, 285, 60, 200)
        wall_list.add(wall)


        # left wall
        wall = Wall(140, 00, 20, 800)
        wall_list.add(wall)


        # right wall
        wall = Wall(650, 80, 25, 600)
        wall_list.add(wall)


        # bottom wall
        wall = Wall(0, 530, 800, 120)
        wall_list.add(wall)


        #Sinks
        wall = Wall(265, 200, 220, 40)
        wall_list.add(wall)

    elif (level == 'office'):

        # left wall
        wall = Wall(105, 170, 30, 350)
        wall_list.add(wall)


        # Right wall
        wall = Wall(665, 170, 30, 350)
        wall_list.add(wall)


        # Top wall
        wall = Wall(105, 170, 600, 50)
        wall_list.add(wall)


        # Bottom wall
        wall = Wall(105, 550, 600, 50)
        wall_list.add(wall)


        #BookShelf
        wall = Wall(570, 220, 80, 40)
        wall_list.add(wall)

    elif (level == 'basement1'):

        # top wall
        wall = Wall(0, 20, 800, 60)
        wall_list.add(wall)

        # left wall
        wall = Wall(175, 00, 20, 800)
        wall_list.add(wall)

        # right wall
        wall = Wall(620, 80, 25, 600)
        wall_list.add(wall)

        # bottom wall
        wall = Wall(0, 550, 800, 120)
        wall_list.add(wall)

        # top clutter
        wall = Wall(320, 80, 80, 80)
        wall_list.add(wall)

        # left clutter
        wall = Wall(180, 190, 135, 80)
        wall_list.add(wall)

        wall = Wall(317, 252, 30, 60)
        wall_list.add(wall)

        wall = Wall(200, 310, 40, 90)
        wall_list.add(wall)

        wall = Wall(295, 390, 115, 80)
        wall_list.add(wall)

        wall = Wall(360, 165, 40, 20)
        wall_list.add(wall)

        wall = Wall(310, 330, 40, 50)
        wall_list.add(wall)

        # left server
        wall = Wall(500, 255, 135, 50)
        wall_list.add(wall)

    elif (level == 'basement2'):

        # top wall
        wall = Wall(0, 20, 800, 60)
        wall_list.add(wall)


        # left wall
        wall = Wall(175, 00, 20, 800)
        wall_list.add(wall)
        game_sprites.add(wall)

        # right wall
        wall = Wall(620, 80, 25, 600)
        wall_list.add(wall)


        # bottom wall
        wall = Wall(0, 550, 800, 120)
        wall_list.add(wall)


        # top clutter
        wall = Wall(455, 80, 25, 60)
        wall_list.add(wall)


        # top right clutter
        wall = Wall(520, 180, 60, 45)
        wall_list.add(wall)


        wall = Wall(580, 125, 20, 60)
        wall_list.add(wall)


        # left clutter
        wall = Wall(200, 280, 60, 45)
        wall_list.add(wall)


        wall = Wall(200, 400, 100, 70)
        wall_list.add(wall)


        wall = Wall(280, 360, 60, 45)
        wall_list.add(wall)




        # bottom right clutter
        wall = Wall(500, 380, 180, 45)
        wall_list.add(wall)
        game_sprites.add(wall)

        wall = Wall(430, 420, 60, 45)
        wall_list.add(wall)
        game_sprites.add(wall)

    elif (level == 'basement3'):

        # top right clutter
        wall = Wall(520, 140, 120, 45)
        wall_list.add(wall)


        # desk
        wall = Wall(200, 140, 40, 45)
        wall_list.add(wall)


        # server
        wall = Wall(200, 240, 110, 45)
        wall_list.add(wall)


        # left clutter
        wall = Wall(200, 460, 100, 25)
        wall_list.add(wall)


        wall = Wall(140, 40, 40, 540)
        wall_list.add(wall)


        wall = Wall(630, 60, 20, 500)
        wall_list.add(wall)


        wall = Wall(430, 340, 130, 60)
        wall_list.add(wall)


        wall = Wall(580, 475, 20, 60)
        wall_list.add(wall)


        wall = Wall(460, 325, 110, 25)
        wall_list.add(wall)


        wall = Wall(200, 460, 100, 25)
        wall_list.add(wall)


    elif (level == 'FinalRoom'):

        # top wall
        wall = Wall(0, 20, 800, 160)
        wall_list.add(wall)
        game_sprites.add(wall)

        # left wall
        wall = Wall(175, 00, 20, 800)
        wall_list.add(wall)
        game_sprites.add(wall)


        # right wall
        wall = Wall(620, 80, 25, 600)
        wall_list.add(wall)
        game_sprites.add(wall)

        # bottom wall
        wall = Wall(0, 475, 800, 120)
        wall_list.add(wall)
        game_sprites.add(wall)

        # right server
        wall = Wall(510, 255, 135, 50)
        wall_list.add(wall)
        game_sprites.add(wall)

        # left server
        wall = Wall(160, 330, 135, 40)
        wall_list.add(wall)
        game_sprites.add(wall)

        # top clutter
        wall = Wall(315, 230, 25, 30)
        wall_list.add(wall)
        game_sprites.add(wall)

        # bottom clutter
        wall = Wall(515, 405, 25, 25)
        wall_list.add(wall)
        game_sprites.add(wall)

def mouseClickElevator():
    coor = pygame.mouse.get_pos()
    global lever1
    global lever2
    global lever3
    global lever4
    global toggle1
    global toggle2
    global toggle3
    global toggle4
    if (lever1X < coor[0] < (lever1X+leverWidth) and lever1 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverOne.switchUp()
        lever1 = True
        lightFour.checkTValue(toggle4)
        lightThree.checkTValue(toggle3)
        if (toggle4==True):
            toggle4=False
        else :
            toggle4=True
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
    elif  (lever1X < coor[0] < (lever1X+leverWidth) and lever1==True and leverY < coor[1] < (leverY + leverHeight)):
        leverOne.switchDown()
        lever1 = False
        lightFour.checkTValue(toggle4)
        lightThree.checkTValue(toggle3)
        if (toggle4==True):
            toggle4=False
        else :
            toggle4=True
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
    if (lever2X < coor[0] < (lever2X+leverWidth) and lever2 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverTwo.switchUp()
        lever2 = True
        lightOne.checkTValue(toggle1)
        lightTwo.checkTValue(toggle2)
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        if (toggle1==True):
            toggle1=False
        else :
            toggle1=True
        if (toggle2==True):
            toggle2=False
        else :
            toggle2=True
    elif  (lever2X < coor[0] < (lever2X+leverWidth) and lever2==True and leverY < coor[1] < (leverY + leverHeight)):
        leverTwo.switchDown()
        lever2 = False
        lightOne.checkTValue(toggle1)
        lightTwo.checkTValue(toggle2)
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        if (toggle1==True):
            toggle1=False
        else :
            toggle1=True
        if (toggle2==True):
            toggle2=False
        else :
            toggle2=True
    if (lever3X < coor[0] < (lever3X+leverWidth) and lever3 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverThree.switchUp()
        lever3 = True
        lightThree.checkTValue(toggle3)
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
    elif  (lever3X < coor[0] < (lever3X+leverWidth) and lever3==True and leverY < coor[1] < (leverY + leverHeight)):
        leverThree.switchDown()
        lever3 = False
        lightThree.checkTValue(toggle3)
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
    if (lever4X < coor[0] < (lever4X+leverWidth) and lever4 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverFour.switchUp()
        lever4 = True
        lightThree.checkTValue(toggle3)
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
    elif  (lever4X < coor[0] < (lever4X+leverWidth) and lever4==True and leverY < coor[1] < (leverY + leverHeight)):
        leverFour.switchDown()
        lever4 = False
        lightThree.checkTValue(toggle3)
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True


## Puzzle Level 1
def elevatorPuzzle():
    mouse1 = pygame.mouse.get_pressed()
    BackGround = Background('elevator-circuit-draft.png', [0, 0])
    game_sprites.empty()

    game_sprites.add(leverOne)
    game_sprites.add(leverTwo)
    game_sprites.add(leverThree)
    game_sprites.add(leverFour)

    game_sprites.add(lightOne)
    game_sprites.add(lightTwo)
    game_sprites.add(lightThree)
    game_sprites.add(lightFour)

    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)
        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:

                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    gameExit()

            # check click on window exit button
            if event.type == pygame.QUIT:
                gameExit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClickElevator()

            # 'updating' the game
            # update all game sprites
        game_sprites.update()
        # draw
        # 'rendering' to the window
        gameDisplay.fill(BLACK)
        gameDisplay.blit(BackGround.image, BackGround.rect)
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

        if (toggle1 == True):
            if (toggle2 == True):
                if (toggle3 == True):
                    if (toggle4 == True):
                        pygame.display.update()
                        running = False
    game_sprites.empty()
    game_sprites.add(playerelevatorLevel)

def bathroomPuzzle():
    BackGround = Background('pipe-draft-full.png', [0, 0])
    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6

    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6

    game_sprites.empty()

    game_sprites.add(leverOne)
    game_sprites.add(leverTwo)
    game_sprites.add(leverThree)
    game_sprites.add(leverFour)
    game_sprites.add(leverFive)
    game_sprites.add(leverSix)



    game_sprites.add(lightOne)
    game_sprites.add(lightTwo)
    game_sprites.add(lightThree)
    game_sprites.add(lightFour)
    game_sprites.add(lightFive)
    game_sprites.add(lightSix)

    # check loop is running at set speed
    clock.tick(FPS)
    # 'processing' inputs (events)

    running = True
    while running:
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:

                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    gameExit()

            # check click on window exit button
            if event.type == pygame.QUIT:
                gameExit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClickBathroom()

        # 'updating' the game
        # update all game sprites
        game_sprites.update()
        # draw
        # 'rendering' to the window
        gameDisplay.fill(BLACK)
        gameDisplay.blit(BackGround.image, BackGround.rect)
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

        if (toggle1 == True):
            if (toggle2 == True):
                if (toggle3 == True):
                    if (toggle4 == True):
                        if (toggle5 == True):
                            if (toggle6 == True):
                                running = False
                                game_sprites.empty()
                                game_sprites.add(playerBathroom)

def mouseClickBathroom():
    coor = pygame.mouse.get_pos()
    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6
    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6
    if (lever1X < coor[0] < (lever1X+leverWidth) and lever1 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverOne.switchUp()
        lever1 = True
        lightOne.checkTValue(toggle1)
        lightThree.checkTValue(toggle3)
        if (toggle1==True):
            toggle1=False
        else :
            toggle1=True
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
    elif  (lever1X < coor[0] < (lever1X+leverWidth) and lever1==True and leverY < coor[1] < (leverY + leverHeight)):
        leverOne.switchDown()
        lever1 = False
        lightOne.checkTValue(toggle1)
        lightThree.checkTValue(toggle3)
        if (toggle1==True):
            toggle1=False
        else :
            toggle1=True
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
    if (lever2X < coor[0] < (lever2X+leverWidth) and lever2 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverTwo.switchUp()
        lever2 = True
        lightOne.checkTValue(toggle1)
        lightTwo.checkTValue(toggle2)
        if (toggle1==True):
            toggle1=False
        else :
            toggle1=True
        if (toggle2==True):
            toggle2=False
        else :
            toggle2=True
    elif  (lever2X < coor[0] < (lever2X+leverWidth) and lever2==True and leverY < coor[1] < (leverY + leverHeight)):
        leverTwo.switchDown()
        lever2 = False
        lightOne.checkTValue(toggle1)
        lightTwo.checkTValue(toggle2)
        if (toggle1==True):
            toggle1=False
        else :
            toggle1=True
        if (toggle2==True):
            toggle2=False
        else :
            toggle2=True
    if (lever3X < coor[0] < (lever3X+leverWidth) and lever3 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverThree.switchUp()
        lever3 = True
        lightThree.checkTValue(toggle3)
        lightSix.checkTValue(toggle6)
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True
    elif  (lever3X < coor[0] < (lever3X+leverWidth) and lever3==True and leverY < coor[1] < (leverY + leverHeight)):
        leverThree.switchDown()
        lever3 = False
        lightThree.checkTValue(toggle3)
        lightSix.checkTValue(toggle6)
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True
    if (lever4X < coor[0] < (lever4X+leverWidth) and lever4 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverFour.switchUp()
        lever4 = True
        lightThree.checkTValue(toggle3)
        lightFive.checkTValue(toggle5)
        lightSix.checkTValue(toggle6)
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
        if (toggle5==True):
            toggle5=False
        else :
            toggle5=True
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True
    elif  (lever4X < coor[0] < (lever4X+leverWidth) and lever4==True and leverY < coor[1] < (leverY + leverHeight)):
        leverFour.switchDown()
        lever4 = False
        lightThree.checkTValue(toggle3)
        lightFive.checkTValue(toggle5)
        lightSix.checkTValue(toggle6)
        if (toggle3==True):
            toggle3=False
        else :
            toggle3=True
        if (toggle5==True):
            toggle5=False
        else :
            toggle5=True
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True
    if (lever5X < coor[0] < (lever5X+leverWidth) and lever5 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverFive.switchUp()
        lever5 = True
        lightFour.checkTValue(toggle4)
        lightSix.checkTValue(toggle6)
        if (toggle4==True):
            toggle4=False
        else :
            toggle4=True
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True
    elif  (lever5X < coor[0] < (lever5X+leverWidth) and lever5==True and leverY < coor[1] < (leverY + leverHeight)):
        leverFive.switchDown()
        lever5 = False
        lightFour.checkTValue(toggle4)
        lightSix.checkTValue(toggle6)
        if (toggle4==True):
            toggle4=False
        else :
            toggle4=True
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True
    if (lever6X < coor[0] < (lever6X+leverWidth) and lever6 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverSix.switchUp()
        lever6 = True
        lightFive.checkTValue(toggle5)
        lightSix.checkTValue(toggle6)
        if (toggle5==True):
            toggle5=False
        else :
            toggle5=True
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True
    elif  (lever6X < coor[0] < (lever6X+leverWidth) and lever6==True and leverY < coor[1] < (leverY + leverHeight)):
        leverSix.switchDown()
        lever6 = False
        lightFive.checkTValue(toggle5)
        lightSix.checkTValue(toggle6)
        if (toggle5==True):
            toggle5=False
        else :
            toggle5=True
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True

def basementPuzzleOne():
    BackGround = Background('elevator-circuit-draft-6.png', [0, 0])

    # check loop is running at set speed
    clock.tick(FPS)
    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6

    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6

    game_sprites.empty()

    game_sprites.add(leverOne)
    game_sprites.add(leverTwo)
    game_sprites.add(leverThree)
    game_sprites.add(leverFour)
    game_sprites.add(leverFive)
    game_sprites.add(leverSix)

    game_sprites.add(lightOne)
    game_sprites.add(lightTwo)
    game_sprites.add(lightThree)
    game_sprites.add(lightFour)
    game_sprites.add(lightFive)
    game_sprites.add(lightSix)

    running = True
    while running:
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:

                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    gameExit()

            # check click on window exit button
            if event.type == pygame.QUIT:
                gameExit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClickBasementOne()

        # 'updating' the game
        # update all game sprites
        game_sprites.update()
        # 'rendering' to the window
        gameDisplay.fill(BLACK)
        gameDisplay.blit(BackGround.image, BackGround.rect)
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()
        if (toggle1 == True):
            if (toggle2 == True):
                if (toggle3 == True):
                    if (toggle4 == True):
                        if (toggle5 == True):
                            if (toggle6 == True):
                                running = False
                                game_sprites.empty()
                                game_sprites.add(playerBasementOne)

def mouseClickBasementOne():
    coor = pygame.mouse.get_pos()
    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6
    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6
    if (lever1X < coor[0] < (lever1X + leverWidth) and lever1 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverOne.switchUp()
        lever1 = True
        lightThree.checkTValue(toggle3)
        lightFour.checkTValue(toggle4)
        lightSix.checkTValue(toggle6)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    elif (lever1X < coor[0] < (lever1X + leverWidth) and lever1 == True and leverY < coor[1] < (leverY + leverHeight)):
        leverOne.switchDown()
        lever1 = False
        lightThree.checkTValue(toggle3)
        lightFour.checkTValue(toggle4)
        lightSix.checkTValue(toggle6)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    if (lever2X < coor[0] < (lever2X + leverWidth) and lever2 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverTwo.switchUp()
        lever2 = True
        lightOne.checkTValue(toggle1)
        lightFive.checkTValue(toggle5)
        lightSix.checkTValue(toggle6)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    elif (lever2X < coor[0] < (lever2X + leverWidth) and lever2 == True and leverY < coor[1] < (leverY + leverHeight)):
        leverTwo.switchDown()
        lever2 = False
        lightOne.checkTValue(toggle1)
        lightFive.checkTValue(toggle5)
        lightSix.checkTValue(toggle6)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    if (lever3X < coor[0] < (lever3X + leverWidth) and lever3 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverThree.switchUp()
        lever3 = True
        lightOne.checkTValue(toggle1)
        lightFour.checkTValue(toggle4)
        lightSix.checkTValue(toggle6)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    elif (lever3X < coor[0] < (lever3X + leverWidth) and lever3 == True and leverY < coor[1] < (leverY + leverHeight)):
        leverThree.switchDown()
        lever3 = False
        lightOne.checkTValue(toggle1)
        lightFour.checkTValue(toggle4)
        lightSix.checkTValue(toggle6)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    if (lever4X < coor[0] < (lever4X + leverWidth) and lever4 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverFour.switchUp()
        lever4 = True
        lightTwo.checkTValue(toggle2)
        lightFour.checkTValue(toggle4)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
    elif (lever4X < coor[0] < (lever4X + leverWidth) and lever4 == True and leverY < coor[1] < (leverY + leverHeight)):
        leverFour.switchDown()
        lever4 = False
        lightTwo.checkTValue(toggle2)
        lightFour.checkTValue(toggle4)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
    if (lever5X < coor[0] < (lever5X + leverWidth) and lever5 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverFive.switchUp()
        lever5 = True
        lightThree.checkTValue(toggle3)
        lightFour.checkTValue(toggle4)
        lightFive.checkTValue(toggle5)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
    elif (lever5X < coor[0] < (lever5X + leverWidth) and lever5 == True and leverY < coor[1] < (leverY + leverHeight)):
        leverFive.switchDown()
        lever5 = False
        lightThree.checkTValue(toggle3)
        lightFour.checkTValue(toggle4)
        lightFive.checkTValue(toggle5)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
    if (lever6X < coor[0] < (lever6X + leverWidth) and lever6 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverSix.switchUp()
        lever6 = True
        lightTwo.checkTValue(toggle2)
        lightThree.checkTValue(toggle3)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
    elif (lever6X < coor[0] < (lever6X + leverWidth) and lever6 == True and leverY < coor[1] < (leverY + leverHeight)):
        leverSix.switchDown()
        lever6 = False
        lightTwo.checkTValue(toggle2)
        lightThree.checkTValue(toggle3)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True

def basementPuzzleTwo():
    BackGround = Background('elevator-circuit-draft-8.png', [0, 0])

    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6
    global lever7
    global lever8

    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6
    global toggle7
    global toggle8

    game_sprites.empty()

    game_sprites.add(leverOne)
    game_sprites.add(leverTwo)
    game_sprites.add(leverThree)
    game_sprites.add(leverFour)
    game_sprites.add(leverFive)
    game_sprites.add(leverSix)
    game_sprites.add(leverSeven)
    game_sprites.add(leverEight)

    game_sprites.add(lightOne)
    game_sprites.add(lightTwo)
    game_sprites.add(lightThree)
    game_sprites.add(lightFour)
    game_sprites.add(lightFive)
    game_sprites.add(lightSix)
    game_sprites.add(lightSeven)
    game_sprites.add(lightEight)

    running = True
    while running:
        # check loop is running at set speed
        clock.tick(FPS)
        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:

                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    gameExit()

            # check click on window exit button
            if event.type == pygame.QUIT:
                gameExit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClickBasementPuzzleTwo()

        # 'updating' the game
        # update all game sprites
        game_sprites.update()
        # 'rendering' to the window
        gameDisplay.fill(BLACK)
        gameDisplay.blit(BackGround.image, BackGround.rect)
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()
        if (toggle1 == True):
            if (toggle2 == True):
                if (toggle3 == True):
                    if (toggle4 == True):
                        if (toggle5 == True):
                            if (toggle6 == True):
                                if (toggle7 == True):
                                    if (toggle8 == True):
                                        running = False
                                        game_sprites.empty()
                                        game_sprites.add(playerBasementTwo)

def basementPuzzleThree():
    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6
    global lever7
    global lever8

    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6
    global toggle7
    global toggle8

    game_sprites.add(leverOne)
    game_sprites.add(leverTwo)
    game_sprites.add(leverThree)
    game_sprites.add(leverFour)
    game_sprites.add(leverFive)
    game_sprites.add(leverSix)
    game_sprites.add(leverSeven)
    game_sprites.add(leverEight)
    game_sprites.add(leverNine)
    game_sprites.add(leverTen)

    game_sprites.add(lightOne)
    game_sprites.add(lightTwo)
    game_sprites.add(lightThree)
    game_sprites.add(lightFour)
    game_sprites.add(lightFive)
    game_sprites.add(lightSix)
    game_sprites.add(lightSeven)
    game_sprites.add(lightEight)

    BackGround = Background('elevator-circuit-draft-8.png', [0, 0])

    while True:
        # check loop is running at set speed
        clock.tick(FPS)
        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:

                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    gameExit()

            # check click on window exit button
            if event.type == pygame.QUIT:
                gameExit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClickBasementPuzzleThree

        # 'updating' the game
        # update all game sprites
        game_sprites.update()
        # 'rendering' to the window
        gameDisplay.fill(BLACK)
        gameDisplay.blit(BackGround.image, BackGround.rect)
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()
        if (toggle1 == True):
            if (toggle2 == True):
                if (toggle3 == True):
                    if (toggle4 == True):
                        if (toggle5 == True):
                            if (toggle6 == True):
                                if (toggle7 == True):
                                    if (toggle8 == True):
                                        if(toggle9 == True):
                                            if(toggle10 == True):
                                                running = False
                                                game_sprites.empty()
                                                game_sprites.add(playerBasementThree)



def mouseClickBasementPuzzleTwo():
    coor = pygame.mouse.get_pos()
    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6
    global lever7
    global lever8

    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6
    global toggle7
    global toggle8



    if (lever1X < coor[0] < (lever1X + leverWidth) and lever1 == False and leverY < coor[1] < (
                leverY + leverHeight)):
        leverOne.switchUp()
        lever1 = True
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    elif (lever1X < coor[0] < (lever1X + leverWidth) and lever1 == True and leverY < coor[1] < (
                leverY + leverHeight)):
        leverOne.switchDown()
        lever1 = False
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    if (lever2X < coor[0] < (lever2X + leverWidth) and lever2 == False and leverY < coor[1] < (
                leverY + leverHeight)):
        leverTwo.switchUp()
        lever2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True
    elif (lever2X < coor[0] < (lever2X + leverWidth) and lever2 == True and leverY < coor[1] < (
                leverY + leverHeight)):
        leverTwo.switchDown()
        lever2 = False
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True
    if (lever3X < coor[0] < (lever3X + leverWidth) and lever3 == False and leverY < coor[1] < (
                leverY + leverHeight)):
        leverThree.switchUp()
        lever3 = True
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    elif (lever3X < coor[0] < (lever3X + leverWidth) and lever3 == True and leverY < coor[1] < (
                leverY + leverHeight)):
        leverThree.switchDown()
        lever3 = False
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    if (lever4X < coor[0] < (lever4X + leverWidth) and lever4 == False and leverY < coor[1] < (
                leverY + leverHeight)):
        leverFour.switchUp()
        lever4 = True
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
    elif (lever4X < coor[0] < (lever4X + leverWidth) and lever4 == True and leverY < coor[1] < (
                leverY + leverHeight)):
        leverFour.switchDown()
        lever4 = False
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
    if (lever5X < coor[0] < (lever5X + leverWidth) and lever5 == False and leverY < coor[1] < (
                leverY + leverHeight)):
        leverFive.switchUp()
        lever5 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    elif (lever5X < coor[0] < (lever5X + leverWidth) and lever5 == True and leverY < coor[1] < (
                leverY + leverHeight)):
        leverFive.switchDown()
        lever5 = False
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    if (lever6X < coor[0] < (lever6X + leverWidth) and lever6 == False and leverY < coor[1] < (
                leverY + leverHeight)):
        leverSix.switchUp()
        lever6 = True
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True
    elif (lever6X < coor[0] < (lever6X + leverWidth) and lever6 == True and leverY < coor[1] < (
                leverY + leverHeight)):
        leverSix.switchDown()
        lever6 = False
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True
    if (lever7X < coor[0] < (lever7X + leverWidth) and lever7 == False and leverY < coor[1] < (
                leverY + leverHeight)):
        leverSeven.switchUp()
        lever7 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    elif (lever7X < coor[0] < (lever7X + leverWidth) and lever7 == True and leverY < coor[1] < (
                leverY + leverHeight)):
        leverSeven.switchDown()
        lever7 = False
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    if (lever8X < coor[0] < (lever8X + leverWidth) and lever8 == False and leverY < coor[1] < (
                leverY + leverHeight)):
        leverEight.switchUp()
        lever8 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True
    elif (lever8X < coor[0] < (lever8X + leverWidth) and lever8 == True and leverY < coor[1] < (
                leverY + leverHeight)):
        leverEight.switchDown()
        lever8 = False
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True


def mouseClickBasementPuzzleThree():

    coor = pygame.mouse.get_pos()

    global lever1
    global lever2
    global lever3
    global lever4
    global lever5
    global lever6
    global lever7
    global lever8
    global lever9
    global lever10

    global toggle1
    global toggle2
    global toggle3
    global toggle4
    global toggle5
    global toggle6
    global toggle7
    global toggle8

    if (lever1X < coor[0] < (lever1X+leverWidth) and lever1 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverOne.switchUp()
        lever1 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
    elif  (lever1X < coor[0] < (lever1X+leverWidth) and lever1==True and leverY < coor[1] < (leverY + leverHeight)):
        leverOne.switchDown()
        lever1 = False
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
    if (lever2X < coor[0] < (lever2X+leverWidth) and lever2 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverTwo.switchUp()
        lever2 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    elif  (lever2X < coor[0] < (lever2X+leverWidth) and lever2==True and leverY < coor[1] < (leverY + leverHeight)):
        leverTwo.switchDown()
        lever2 = False
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    if (lever3X < coor[0] < (lever3X+leverWidth) and lever3 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverThree.switchUp()
        lever3 = True
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
    elif  (lever3X < coor[0] < (lever3X+leverWidth) and lever3==True and leverY < coor[1] < (leverY + leverHeight)):
        leverThree.switchDown()
        lever3 = False
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
    if (lever4X < coor[0] < (lever4X+leverWidth) and lever4 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverFour.switchUp()
        lever4 = True
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
    elif  (lever4X < coor[0] < (lever4X+leverWidth) and lever4==True and leverY < coor[1] < (leverY + leverHeight)):
        leverFour.switchDown()
        lever4 = False
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
    if (lever5X < coor[0] < (lever5X+leverWidth) and lever5 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverFive.switchUp()
        lever5 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True
    elif  (lever5X < coor[0] < (lever5X+leverWidth) and lever5==True and leverY < coor[1] < (leverY + leverHeight)):
        leverFive.switchDown()
        lever5 = False
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True
    if (lever6X < coor[0] < (lever6X+leverWidth) and lever6 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverSix.switchUp()
        lever6 = True
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    elif  (lever6X < coor[0] < (lever6X+leverWidth) and lever6==True and leverY < coor[1] < (leverY + leverHeight)):
        leverSix.switchDown()
        lever6 = False
        lightOne.checkTValue(toggle1)
        if (toggle1 == True):
            toggle1 = False
        else:
            toggle1 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    if (lever7X < coor[0] < (lever7X+leverWidth) and lever7 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverSeven.switchUp()
        lever7 = True
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    elif  (lever7X < coor[0] < (lever7X+leverWidth) and lever7==True and leverY < coor[1] < (leverY + leverHeight)):
        leverSeven.switchDown()
        lever7 = False
        lightFour.checkTValue(toggle4)
        if (toggle4 == True):
            toggle4 = False
        else:
            toggle4 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    if (lever8X < coor[0] < (lever8X+leverWidth) and lever8 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverEight.switchUp()
        lever8 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    elif  (lever8X < coor[0] < (lever8X+leverWidth) and lever8==True and leverY < coor[1] < (leverY + leverHeight)):
        leverEight.switchDown()
        lever8 = False
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightSeven.checkTValue(toggle7)
        if (toggle7 == True):
            toggle7 = False
        else:
            toggle7 = True
    if (lever9X < coor[0] < (lever9X+leverWidth) and lever9 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverNine.switchUp()
        lever9 = True
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    elif  (lever9X < coor[0] < (lever9X+leverWidth) and lever9 ==True and leverY < coor[1] < (leverY + leverHeight)):
        leverNine.switchDown()
        lever9 = False
        lightTwo.checkTValue(toggle2)
        if (toggle2 == True):
            toggle2 = False
        else:
            toggle2 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightSix.checkTValue(toggle6)
        if (toggle6 == True):
            toggle6 = False
        else:
            toggle6 = True
    if (lever10X < coor[0] < (lever10X+leverWidth) and lever10 == False and leverY < coor[1] < (leverY + leverHeight)):
        leverTen.switchUp()
        lever10 = True
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True
    elif  (lever10X < coor[0] < (lever10X+leverWidth) and lever10==True and leverY < coor[1] < (leverY + leverHeight)):
        leverTen.switchDown()
        lever10 = False
        lightThree.checkTValue(toggle3)
        if (toggle3 == True):
            toggle3 = False
        else:
            toggle3 = True
        lightFive.checkTValue(toggle5)
        if (toggle5 == True):
            toggle5 = False
        else:
            toggle5 = True
        lightEight.checkTValue(toggle8)
        if (toggle8 == True):
            toggle8 = False
        else:
            toggle8 = True


#Dialogue Cutscences
def lobbyScenePartOne():

    dialogue = getText(41, 42)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(43, 44)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(45, 48)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(49, 50)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(52, 53)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(54, 55)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(56, 57)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(58, 59)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(60, 63)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(64, 65)
    displayDialogue(dialogue, 'top')
    continueDialogue()

def lobbyScenePartTwo():

    dialogue = getText(66, 67)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(68, 69)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(70, 71)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(72, 73)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(74,75)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(76, 77)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(78, 79)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(80, 81)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(82, 83)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(84, 85)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(86, 88)
    displayDialogue(dialogue, 'top')
    continueDialogue()

def elevatorScenePartOne():

    dialogue = getText(117, 118)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(119, 121)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(122, 123)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(124, 125)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(126, 127)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(128, 129)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(130, 131)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(132, 133)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(134, 135)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(136, 137)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(138, 139)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(140, 141)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(142, 144)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(145, 146)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(147, 148)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(149, 151)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(152, 153)
    displayDialogue(dialogue, 'top')
    continueDialogue()

def elevatorSceneTwo():

    dialogue = getText(156, 157)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(158, 159)
    displayDialogue(dialogue, 'top')
    continueDialogue()

def waitingRoomOneScene():

    dialogue = getText(162, 163)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(164, 165)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(166, 167)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(168, 170)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(171, 174)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(174,175)

    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(147, 148)

    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(147, 148)
    displayDialogue(dialogue, 'top')
    continueDialogue()

def bathroomScene():
    dialogue = getText(181, 182)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(182, 184)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(185, 186)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(187, 190)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(191, 196)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(197, 198)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(199, 200)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(201, 202)
    displayDialogue(dialogue, 'top')
    continueDialogue()

    dialogue = getText(203, 205)
    displayDialogue(dialogue, 'top')
    continueDialogue()



    #moral 2

    dialogue = getText(221, 223)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(221, 223)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(224, 226)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(219, 220)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(227, 229)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(230, 231)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(232, 233)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(234, 235)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(236, 237)
    displayDialogue(dialogue)
    continueDialogue()

def bathroomScenceTwo():
    dialogue = getText(240, 241)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(242, 243)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(244, 245)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(246, 247)
    displayDialogue(dialogue)
    continueDialogue()

def waitingRoomSceneTwo():
    dialogue = getText(250, 251)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(253, 254)
    displayDialogue(dialogue)
    continueDialogue()
    #moral 3 and 4
    dialogue = getText(147, 148)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(147, 148)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(147, 148)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(147, 148)
    displayDialogue(dialogue)
    continueDialogue()

def officeScene():
    dialogue = getText(289, 290)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(291, 292)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(293, 294)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(295, 296)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(297, 300)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(301, 302)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(303, 306)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(307, 308)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(309, 311)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(312, 313)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(314, 315)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(316, 317)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(318, 320)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(321, 323)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(324, 325)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(326, 328)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(329, 330)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(331, 332)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(333, 334)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(335, 336)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(337, 338)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(339, 340)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(341, 342)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(343, 344)
    displayDialogue(dialogue)
    continueDialogue()

def basementOneScene():
    dialogue = getText(349, 350)
    displayDialogue(dialogue,'top')
    continueDialogue()

def basementTwoScene():
    dialogue = getText(351, 352)
    displayDialogue(dialogue)
    continueDialogue()

def basementThreeScene():
    dialogue = getText(353, 354)
    displayDialogue(dialogue, 'top')
    continueDialogue()



def FinalScene():
    dialogue = getText(357, 358)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(359, 360)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(361, 362)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(363, 364)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(365,368)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(369, 370)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(371, 373)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(374, 377)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(378, 379)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(380,382)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(383, 384)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(385,388)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(389, 390)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(391, 392)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(393, 394)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(395, 396)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(397, 398)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(399, 400)
    displayDialogue(dialogue)
    continueDialogue()

    dialogue = getText(401, 402)
    displayDialogue(dialogue)
    continueDialogue()



#Beginning Of Game
def mainMenu():

    while gameIntroLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        gameDisplay.fill(color("blue"))
        wallpaper(IntroBackground,0,0)
        message_display('S.E.E.D', pygame.font.match_font('agencyfb'), 115,color('white'),display_width,display_height,True)

        button("Start", 350,300,100,50,color("forestgreen"),color("green"),gameIntro,True)
        button("Quit", 350, 400, 100, 50, color("darkred"), color("red"),quitGame)

        frames = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        pygame.display.flip()
        gameDisplay.blit(frames, (50, 50))


        pygame.display.update()
        clock.tick(30)

def gameIntro():
    global gameIntroLoop
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()

        gameDisplay.fill(color("green"))
        wallpaper(gameIntroBackground,0,0)
        frames = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        pygame.display.flip()
        gameDisplay.blit(frames, (50, 50))

        opening = getText(0, 5)
        displayDialogue(opening,'top')
        continueDialogue()

        opening = getText(6, 10)
        displayDialogue(opening, 'top')
        continueDialogue()

        opening = getText(11, 15)
        displayDialogue(opening, 'top')
        continueDialogue()

        dialogue = getText(22, 25)
        displayDialogue(dialogue, 'top')
        continueDialogue()

        dialogue = getText(26, 27)
        displayDialogue(dialogue, 'top')
        continueDialogue()

        dialogue = getText(28, 30)
        displayDialogue(dialogue, 'top')
        continueDialogue()

        dialogue = getText(31, 32)
        displayDialogue(dialogue, 'top')
        continueDialogue()

        dialogue = getText(33, 34)
        displayDialogue(dialogue, 'top')
        continueDialogue()

        dialogue = getText(35, 36)
        displayDialogue(dialogue, 'top')
        continueDialogue()

        game = False
        gameIntroLoop = False

def lobbyLevel():

    bg_img = pygame.image.load(os.path.join(img_dir, "lobby1New.png")).convert()
    #Runs First Dialogue Cutscene 1
    cutscene = True
    #Creates Wall for Lobby Level Part 1
    createWall('lobby1')
    running = True
    game_sprites.add((playerlobbyPart1))
    security_spot1 = Security(90, 190, 1, 1)
    security_spot2 = Security(80, 400, 2, 1,1)
    security_spot3 = Security(320, 230, 2, -1)
    security_spot4 = Security(230, 400, 2, 0,-1)

    security_spot5 = Security(420, 400, 3, 1)

    security_spot6 = Security(415, 500, 1, 1)
    security_spot7 = Security(685, 380, 2, 1)
    security_spot8 = Security(610, 310, 2,-1)
    security_spot9 = Security(450, 210, 1,1)




    security_spots1.add(security_spot1, security_spot2, security_spot3,
                        security_spot4, security_spot5, security_spot6,
                        security_spot7,security_spot8,security_spot9)

    game_sprites.add(playerlobbyPart1,security_spots1)

    puzzleInteractions.add(lobbyDesk)

    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)
        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()
            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        collisions = pygame.sprite.spritecollide(playerlobbyPart1, puzzleInteractions , True, pygame.sprite.collide_circle)
        # check collisions for game window

        if collisions:
            lobbyScenePartTwo()

        # add check fif cor collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerlobbyPart1, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window

        if collisions:
            bg_img = pygame.image.load(os.path.join(img_dir, "lobby2New.png")).convert()
            game_sprites.empty()
            security_spots1.empty()

            security_spot1 = Security(400, 400   , 3, -1)
            security_spot2 = Security(390, 380, 3, 1,-1)
            security_spot3 = Security(285, 360, 1, 1)
            security_spots1.add(security_spot1, security_spot2, security_spot3)
            game_sprites.add(playerlobbyPart2,security_spots1)
            interactives.add(elevatorDoor)


            wall_list.empty()
            createWall('lobby2')



        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerlobbyPart1, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 70, color('red'),
                            display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()

        collisions = pygame.sprite.spritecollide(playerlobbyPart2, interactives, True, pygame.sprite.collide_circle)
        if collisions:
            running = False

        collisions = pygame.sprite.spritecollide(playerlobbyPart2, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 70, color('red'),
                            display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()

        # draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        frames = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        pygame.display.flip()
        gameDisplay.blit(frames, (50, 50))
        # update the display window...
        pygame.display.update()
        if cutscene ==True:
            cutscene = False
            lobbyScenePartOne()

def elevatorLevel():

    bg_img = pygame.image.load(os.path.join(img_dir, "elevatorFinal.png")).convert()
    security_spots1.empty()

    game_sprites.empty()
    game_sprites.add(playerelevatorLevel)
    wall_list.empty()
    createWall('elevator')
    interactives.add(elevatorPanel)
    game_sprites.draw(gameDisplay)
    cutscene = True
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()


            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerelevatorLevel, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            elevatorPuzzle()
            interactives.add(elevatorDoorLeaving)
            gameDisplay.fill(BLACK)
            elevatorSceneTwo()


        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerelevatorLevel, interactives, True, pygame.sprite.collide_circle)
        if collisions:
            running = False

        # draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

        if cutscene ==True:
            cutscene = False
            elevatorScenePartOne()

def waitingRoomLevelOne():

    bg_img = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()
    game_sprites.empty()
    security_spots1.empty()

    interactives.empty()
    interactives.add(bathroomDoor)

    security_spot1 = Security(545, 455, 2, 0)
    security_spot2 = Security(750, 400, 3, -1)
    security_spot3 = Security(700, 230, 3, -1)
    security_spot4 = Security(370, 280, 2, 0, -1)
    security_spot5 = Security(380, 365, 1, 1)
    security_spot6 = Security(260, 335, 2, 0)
    security_spot7 = Security(60, 450, 3, 1)
    security_spot8 = Security(165, 265, 3, -1,-1)
    security_spot9 = Security(521, 240, 1, 1)
    security_spot10 = Security(60, 300, 1, 1)


    security_spots1.add(security_spot1, security_spot2, security_spot3,
                        security_spot4, security_spot5, security_spot6,
                        security_spot7, security_spot8, security_spot9
                        ,security_spot10)

    game_sprites.add(playerWaitingRoomOne,security_spots1)
    wall_list.empty()
    createWall('waitingRoom')
    game_sprites.draw(gameDisplay)

    cutscene = True
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()



            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        # update all game sprites
        game_sprites.update()

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerWaitingRoomOne, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            running = False

        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerWaitingRoomOne, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 70, color('red'),
                            display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()


        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)
        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()
        if cutscene ==True:
            cutscene = False
            waitingRoomOneScene()

def bathroomLevel():

    bg_img = pygame.image.load(os.path.join(img_dir, "bathroomFinal.png")).convert()

    game_sprites.empty()
    game_sprites.add(playerBathroom)
    game_sprites.draw(gameDisplay)
    wall_list.empty()
    createWall('bathroom')
    cutscene = True
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)
        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerBathroom, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            bathroomPuzzle()
            interactives.add(bathroomDoorExit)
            interactives.remove(bathroomPanel)
            bathroomScenceTwo()

        collisions = pygame.sprite.spritecollide(playerBathroom, interactives, True, pygame.sprite.collide_circle)

        if collisions:
            running = False

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()
        if cutscene ==True:
            cutscene = False
            bathroomScene()

def waitingRoomLevelTwo():

    bg_img = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()
    game_sprites.empty()
    security_spots1.empty()


    security_spot1 = Security(545, 455, 2, 0)
    security_spot2 = Security(750, 400, 3, -1)
    security_spot3 = Security(700, 230, 3, -1)
    security_spot4 = Security(370, 280, 2, 0, -1)
    security_spot5 = Security(380, 365, 1, 1)
    security_spot6 = Security(260, 335, 2, 0)
    security_spot7 = Security(60, 450, 3, 1)
    security_spot8 = Security(165, 265, 3, -1, -1)
    security_spot9 = Security(521, 240, 1, 1)
    security_spot10 = Security(60, 300, 1, 1)

    security_spots1.add(security_spot1, security_spot2, security_spot3,
                        security_spot4, security_spot5, security_spot6,
                        security_spot7, security_spot8, security_spot9
                        , security_spot10)

    game_sprites.add(playerWaitingRoomTwo,security_spots1)
    interactives.add(officeEntrance)
    game_sprites.draw(gameDisplay)
    waitingRoomSceneTwo()

    wall_list.empty()
    createWall('waitingRoom')
    cutscene = True
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()


            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerWaitingRoomTwo, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            running = False

        collisions = pygame.sprite.spritecollide(playerWaitingRoomTwo, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 70, color('red'),
                            display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()
        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

        if cutscene ==True:
            cutscene = False
            waitingRoomSceneTwo()

def officeLevel():

    bg_img = pygame.image.load(os.path.join(img_dir, "mainOffice.png")).convert()
    game_sprites.empty()

    game_sprites.add(playerOffice)
    interactives.empty()
    interactives.add(officeDesk)
    game_sprites.draw(gameDisplay)
    wall_list.empty()
    createWall('office')
    cutscene = True
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerOffice, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background

            print('get out')
            # draw background image - specify image file and rect to load image
            interactives.add(officeExit)


        collisions = pygame.sprite.spritecollide(playerOffice, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:

            running = False

        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)


        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)


        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

        if cutscene ==True:
            cutscene = False
            officeScene()

def waitingRoomLevelThree():

    bg_img = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()
    game_sprites.empty()
    security_spots1.empty()

    security_spot1 = Security(545, 455, 2, 0)
    security_spot2 = Security(750, 400, 3, -1)
    security_spot3 = Security(700, 230, 3, -1)
    security_spot4 = Security(370, 280, 2, 0, -1)
    security_spot5 = Security(380, 365, 1, 1)
    security_spot6 = Security(260, 335, 2, 0)
    security_spot7 = Security(60, 450, 3, 1)
    security_spot8 = Security(165, 265, 3, -1, -1)
    security_spot9 = Security(521, 240, 1, 1)
    security_spot10 = Security(60, 300, 1, 1)

    security_spots1.add(security_spot1, security_spot2, security_spot3,
                        security_spot4, security_spot5, security_spot6,
                        security_spot7, security_spot8, security_spot9
                        , security_spot10)

    game_sprites.add(playerWaitingRoomThree,security_spots1)

    interactives.empty()
    interactives.add(elevatorDoorToBasement)

    wall_list.empty()
    createWall('waitingRoom')

    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerWaitingRoomThree, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            running = False


        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerWaitingRoomThree, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 70, color('red'),
                            display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def basementLevelOne():

    bg_img = pygame.image.load(os.path.join(img_dir, "basementRoom1fix.png")).convert()
    game_sprites.empty()
    security_spots1.empty()

    security_spot1 = Security(220, 440, 1, 1)
    security_spot2 = Security(430, 380, 3, 1)
    security_spot3 = Security(500, 380, 1, 1)
    security_spot4 = Security(500, 510, 3, 1, 1)
    security_spot5 = Security(310, 230, 3, 1)
    security_spot6 = Security(400, 170, 1, 1)
    security_spot7 = Security(445, 180, 2, 1)


    security_spots1.add(security_spot1, security_spot2, security_spot3,
                        security_spot4, security_spot5, security_spot6,
                        security_spot7)

    game_sprites.add(playerBasementOne,security_spots1)
    game_sprites.draw(gameDisplay)
    basementOneScene()

    interactives.empty()
    puzzleInteractions.add(basementPuzzle1Correct)
    puzzleInteractionsW.add(basementPuzzle1Wrong)



    wall_list.empty()
    createWall('basement1')
    cutscene = True
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        collisions = pygame.sprite.spritecollide(playerBasementOne, puzzleInteractions, True,pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            basementPuzzleOne()
            game_sprites.empty()
            game_sprites.add(playerBasementOne, security_spots1)

            correctDoor.add(basementDoorOneCorrect)

        collisions = pygame.sprite.spritecollide(playerBasementOne, puzzleInteractionsW, True,pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            basementPuzzleOne()

            game_sprites.empty()
            game_sprites.add(playerBasementOne, security_spots1)

            wrongDoor.add(basementDoorOneWrong)

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerBasementOne, correctDoor, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background
            # draw background image - specify image file and rect to load image
            running = False


        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)


        collisions = pygame.sprite.spritecollide(playerBasementOne, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 70, color('red'),
                            display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()

        collisions = pygame.sprite.spritecollide(playerBasementOne, wrongDoor, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 70, color('red'),
                            display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

        if cutscene == True:
            cutscene = False
            basementTwoScene()

def basementLevelTwo():

    bg_img = pygame.image.load(os.path.join(img_dir, "basementRoom2.png")).convert()
    game_sprites.empty()
    security_spots1.empty()
    wrongDoor.empty()
    correctDoor.empty()

    security_spot1 = Security(315, 330, 3, -1,-1)
    security_spot2 = Security(470, 500, 2, 1)
    security_spot3 = Security(460, 220, 3, -1,-1)
    security_spot4 = Security(385, 300, 1, -1)
    security_spot5 = Security(325, 505, 1, 1)
    security_spot6 = Security(530, 340, 1, 1)
    security_spot7 = Security(515, 240, 2, 1)

    security_spots1.add(security_spot1, security_spot2, security_spot3,
                        security_spot4, security_spot5, security_spot6,
                        security_spot7)


    game_sprites.add(playerBasementTwo,security_spots1)
    game_sprites.draw(gameDisplay)


    interactives.empty()
    puzzleInteractions.add(basementDoorTwoCorrect)
    puzzleInteractionsW.add(basementDoorTwoWrong)




    wall_list.empty()
    createWall('basement2')
    cutscene = True
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())


            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        collisions = pygame.sprite.spritecollide(playerBasementTwo, puzzleInteractions, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            basementPuzzleTwo()
            correctDoor.add(basementDoorTwoCorrect)
            game_sprites.empty()
            game_sprites.add(playerBasementOne, security_spots1)



        collisions = pygame.sprite.spritecollide(playerBasementTwo, puzzleInteractionsW, True,
                                                 pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            basementPuzzleTwo()

            game_sprites.empty()
            game_sprites.add(playerBasementTwo, security_spots1)


            wrongDoor.add(basementDoorTwoWrong)

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerBasementTwo, correctDoor, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background
            # draw background image - specify image file and rect to load image
            running = False


        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerBasementTwo, wrongDoor, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 70, color('red'), display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()



        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

        if cutscene ==True:
            cutscene = False
            basementTwoScene()

def basementLevelThree():

    bg_img = pygame.image.load(os.path.join(img_dir, "basementRoom3.png")).convert()
    game_sprites.empty()
    security_spots1.empty()

    interactives.empty()
    correctDoor.empty()
    wrongDoor.empty()
    puzzleInteractionsW.empty()
    puzzleInteractions.empty()

    security_spot1 = Security(355, 400, 1, -1)
    security_spot2 = Security(470, 490, 2, 1)
    security_spot3 = Security(460, 160, 3, -1, -1)
    security_spot4 = Security(380, 300, 1, -1)
    security_spot5 = Security(325, 515, 1, 1)
    security_spot6 = Security(490, 315, 3, -1,-1)
    security_spot7 = Security(300, 120, 2, -1,1)

    security_spots1.add(security_spot1, security_spot2, security_spot3,
                        security_spot4, security_spot5, security_spot6,
                        security_spot7)

    puzzleInteractions.add(basementPuzzle3Correct)
    game_sprites.add(playerBasementThree,security_spots1)
    game_sprites.draw(gameDisplay)

    wall_list.empty()
    createWall('basement3')


    cutscence = True
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()


            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        # 'updating' the game
        # update all game sprites
        game_sprites.update()
        collisions = pygame.sprite.spritecollide(playerBasementThree, puzzleInteractions, True,
                                                 pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            basementPuzzleThree()

            game_sprites.empty()
            game_sprites.add(playerBasementThree, security_spots1)

            correctDoor.add(basementDoorThree)

        if cutscence == True:
            cutscence
            basementThreeScene()

        # check collisions for game window


        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerBasementThree, correctDoor, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:

            running = False

        collisions = pygame.sprite.spritecollide(playerBasementThree, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, press Escape to Quit', pygame.font.match_font('agencyfb'), 115, color('red'),
                            display_width,
                            display_height, True)

            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()

        collisions = pygame.sprite.spritecollide(playerBasementThree, wrongDoor, True, pygame.sprite.collide_circle)
        if collisions:
            gameDisplay.fill(BLACK)
            message_display('Game Over, Press Escape to Quit', pygame.font.match_font('agencyfb'), 115, color('red'),
                            display_width,
                            display_height, True)
            while running:
                # check loop is running at set speed
                clock.tick(FPS)

                # 'processing' inputs (events)
                for event in EVENTS.get():
                    # check keyboard events - keydown
                    if event.type == pygame.KEYDOWN:
                        # check for ESCAPE key
                        if event.key == pygame.K_ESCAPE:
                            quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pygame.mouse.get_pos())

                    # check click on window exit button
                    if event.type == pygame.QUIT:
                        quitGame()


        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()
        if cutscence == True:
            cutscence
            basementThreeScene()

def FinalBossRoom():

    bg_img = pygame.image.load(os.path.join(img_dir, "serverRoom.png")).convert()
    game_sprites.remove(playerBasementThree)
    game_sprites.add(playerFinal)
    interactives.empty()


    wall_list.empty()
    createWall('FinalRoom')

    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()


            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(player, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"





        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)


        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def ending():
    global IntroBackground
    IntroBackground = pygame.image.load(os.path.join(img_dir, 'peacefulEnd.png')).convert()

    game_sprites.empty()
    running = True
    # create game loop
    while running:
        # check loop is running at set speed
        clock.tick(FPS)

        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    quit()


            # check click on window exit button
            if event.type == pygame.QUIT:
                quitGame()
        # 'updating' the game
        # update all game sprites
        game_sprites.update()

        # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)


        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        wallpaper(IntroBackground,0,0)


        dialogue = getText(470, 473)
        displayDialogue(dialogue,'top')
        continueDialogue()

        running = False
        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()



    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)



while True:

    mainMenu()
    lobbyLevel()
    
    #lever coordinates
    leverWidth = 60
    leverHeight = 70
    leverY = 500
    
    lever1X = 75
    lever2X = 200
    lever3X = 325
    lever4X = 450
    
    lightX = 675
    
    light1Y = 45
    light2Y = 160
    light3Y = 275
    light4Y = 395
    
    
    lightRowOneY = 90
    lightRowTwoY = 205
    
    #Levers
    leverOne = Lever(lever1X,leverY)
    leverTwo = Lever(lever2X,leverY)
    leverThree = Lever(lever3X,leverY)
    leverFour = Lever(lever4X,leverY)
    
    lightOne = Light(lightX,light1Y)
    lightTwo = Light(lightX,light2Y)
    lightThree = Light(lightX,light3Y)
    lightFour = Light(lightX,light4Y)
    
    
    
    
    elevatorLevel()
    puzzleReset()
    
    waitingRoomLevelOne()
    
    leverWidth = 60
    leverHeight = 70
    leverY = 500
    
    
    lever1X = 75
    lever2X = 190
    lever3X = 320
    lever4X = 440
    lever5X = 560
    lever6X = 680
    
    lightRowOneY = 90
    lightRowTwoY = 205
    
    light1X = 83
    light2X = 160
    light3X = 237
    
    leverOne = Lever(lever1X, leverY)
    leverTwo = Lever(lever2X, leverY)
    leverThree = Lever(lever3X, leverY)
    leverFour = Lever(lever4X, leverY)
    leverFive = Lever(lever5X, leverY)
    leverSix = Lever(lever6X, leverY)
    
    lightOne = Light(light1X, lightRowOneY)
    lightTwo = Light(light2X, lightRowOneY)
    lightThree = Light(light3X, lightRowOneY)
    lightFour = Light(light1X, lightRowTwoY)
    lightFive = Light(light2X, lightRowTwoY)
    lightSix = Light(light3X, lightRowTwoY)
    
    
    interactives.add(bathroomPanel)
    bathroomLevel()
    puzzleReset()
    
    
    
    interactives.add(officeEntrance)
    waitingRoomLevelTwo()
    officeLevel()
    waitingRoomLevelThree()
    
    #lever coordinates for basementPuzzle
    leverWidth = 60
    leverHeight = 70
    leverY = 500
    
    lever1X = 75
    lever2X = 175
    lever3X = 275
    lever4X = 375
    lever5X = 475
    lever6X = 575
    
    #light coordinates
    lightX = 675
    
    light1Y = 15
    light2Y = 90
    light3Y = 170
    light4Y = 245
    light5Y = 320
    light6Y = 400
    
    
    leverOne = Lever(lever1X, leverY)
    leverTwo = Lever(lever2X, leverY)
    leverThree = Lever(lever3X, leverY)
    leverFour = Lever(lever4X, leverY)
    leverFive = Lever(lever5X, leverY)
    leverSix = Lever(lever6X, leverY)
    
    lightOne = Light(lightX,light1Y)
    lightTwo = Light(lightX,light2Y)
    lightThree = Light(lightX,light3Y)
    lightFour = Light(lightX,light4Y)
    lightFive = Light(lightX,light5Y)
    lightSix = Light(lightX,light6Y)
    
    
    
    puzzleReset()
    basementLevelOne()
    
    #lever coordinates
    leverWidth = 60
    leverHeight = 70
    leverY = 500
    
    lever1X = 25
    lever2X = 125
    lever3X = 225
    lever4X = 325
    lever5X = 425
    lever6X = 525
    lever7X = 625
    lever8X = 725
    
    #light coordinates
    lightX = 675
    
    light1Y = 10
    light2Y = 70
    light3Y = 130
    light4Y = 190
    light5Y = 250
    light6Y = 310
    light7Y = 370
    light8Y = 430
    
    leverOne = Lever(lever1X,leverY)
    leverTwo = Lever(lever2X,leverY)
    leverThree = Lever(lever3X,leverY)
    leverFour = Lever(lever4X,leverY)
    leverFive = Lever(lever5X,leverY)
    leverSix = Lever(lever6X,leverY)
    leverSeven = Lever(lever7X,leverY)
    leverEight = Lever(lever8X,leverY)
    
    lightOne = Light(lightX,light1Y)
    lightTwo = Light(lightX,light2Y)
    lightThree = Light(lightX,light3Y)
    lightFour = Light(lightX,light4Y)
    lightFive = Light(lightX,light5Y)
    lightSix = Light(lightX,light6Y)
    lightSeven = Light(lightX,light7Y)
    lightEight = Light(lightX,light8Y)
    

    basementLevelTwo()
    puzzleReset()
    
    
    
    leverWidth = 60
    leverHeight = 70
    leverY = 500
    
    lever1X = 25
    lever2X = 100
    lever3X = 175
    lever4X = 250
    lever5X = 325
    lever6X = 400
    lever7X = 475
    lever8X = 550
    lever9X = 625
    lever10X = 700
    
    leverOne = Lever(lever1X,leverY)
    leverTwo = Lever(lever2X,leverY)
    leverThree = Lever(lever3X,leverY)
    leverFour = Lever(lever4X,leverY)
    leverFive = Lever(lever5X,leverY)
    leverSix = Lever(lever6X,leverY)
    leverSeven = Lever(lever7X,leverY)
    leverEight = Lever(lever8X,leverY)
    leverNine = Lever(lever9X, leverY)
    leverTen = Lever(lever10X, leverY)
    
    #light coordinates
    lightX = 675
    
    light1Y = 10
    light2Y = 70
    light3Y = 130
    light4Y = 190
    light5Y = 250
    light6Y = 310
    light7Y = 370
    light8Y = 430
    
    lightOne = Light(lightX,light1Y)
    lightTwo = Light(lightX,light2Y)
    lightThree = Light(lightX,light3Y)
    lightFour = Light(lightX,light4Y)
    lightFive = Light(lightX,light5Y)
    lightSix = Light(lightX,light6Y)
    lightSeven = Light(lightX,light7Y)
    lightEight = Light(lightX,light8Y)
    
    
    basementLevelThree()
    FinalBossRoom()
    ending()