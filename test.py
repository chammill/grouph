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
IntroBackground =  pygame.image.load(os.path.join(img_dir, 'MainMenu.png' )).convert()
gameIntroBackground = pygame.image.load(os.path.join(img_dir, 'MainMenu.png' )).convert()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)


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
# player's character
char_img = pygame.image.load(os.path.join(img_dir, "char1.png")).convert()
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


def fade(width,height):
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
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
                fade(800,600)
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


#


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


global lever1
global lever2
global lever3
global lever4
global lever5
global lever6

global lever1X
global lever2X
global lever3X
global lever4X
global lever5X
global lever6X


lever1 = False

lever2 = False

lever3 = False

lever4 = False

lever5 = False

lever6 = False


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
        if key_state[pygame.K_d]:
            self.speed_x = 4
        if key_state[pygame.K_w]:
            self.speed_y = -4
        if key_state[pygame.K_s]:
            self.speed_y = 4
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


# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

# left wall
wall = Wall(0, 0, 25, 600)
wall_list.add(wall)

# top left wall
wall = Wall(0, 0, 370, 60)
wall_list.add(wall)

# top right wall
wall = Wall(460, 0, 370, 60)
wall_list.add(wall)

# right wall
wall = Wall(775, 10, 25, 600)
wall_list.add(wall)

# top right desk
wall = Wall(470, 145, 60, 40)
wall_list.add(wall)

# top left desk
wall = Wall(290, 145, 60, 40)
wall_list.add(wall)

# bottom right desk
wall = Wall(470, 255, 60, 50)
wall_list.add(wall)

# bottom left desk
wall = Wall(290, 255, 60, 50)
wall_list.add(wall)

all_sprite_list.add(wall)


# create a bookshelf
class Bookshelf(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = bookshelf_img
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(GREEN)
        # check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 50
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
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


# define game quit and program exit







# create security spots
class Security(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = security_spot
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(WHITE)
        # check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 2.5
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = x
        self.rect.bottom = y
        # speed along the x-axis
        self.speed_x = 1
        # speed along the y-axis
        self.speed_y = 0
        # check timer for last update to reverse
        self.reverse_update = pygame.time.get_ticks()
        self.time_elapsed_since_last_action = 0

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

security_spot1 = Security(120, 140)
security_spot2 = Security(365, 140)
security_spot3 = Security(120, 240)
security_spot4 = Security(120, 380)
security_spot5 = Security(620, 140)
security_spot6 = Security(465, 380)
security_spot7 = Security(665, 380)



#Next Level Interactions
lobbyLevelPart2 = Bookshelf(450,590)
elevatorDoor = Bookshelf(450,595)
elevatorDoorLeaving = Bookshelf(350,300)
bathroomDoor = Bookshelf(50,300)
bathroomDoorExit = Bookshelf(715,400)
officeEntrance = Bookshelf(425,200)
officeExit = Bookshelf(450,595)
elevatorDoorToBasement = Bookshelf(425,575)
basementDoorOneCorrect = Bookshelf(500,200)
basementDoorOneWrong = Bookshelf(400, 175)
basementDoorTwoCorrect = Bookshelf(700,475)
basementDoorTwoWrong = Bookshelf(200,100)
basementDoorThree = Bookshelf(425,200)


#dialogue prompts
officeDesk = Bookshelf(400,200)

#Panels
elevatorPanel = Bookshelf(450,300)
bathroomPanel = Bookshelf(550,175)

# sprite groups - game, mob, projectiles...
playerColl = pygame.sprite.Group()
game_sprites = pygame.sprite.Group()
mob_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
interactives = pygame.sprite.Group()
wrongDoor = pygame.sprite.Group()
maps = pygame.sprite.Group()
security_spots1 = pygame.sprite.Group()



# create player object spawns
playerList =[]
playerlobbyPart1 = Player(25,280)
playerlobbyPart2 = Player(400,150)
playerelevatorLevel = Player(400,350)
playerWaitingRoomOne = Player(425,575)
playerBathroom = Player(650,400)
playerWaitingRoomTwo = Player(50,300)
playerOffice = Player(400,550)
playerWaitingRoomThree = Player(400,200)
playerBasementOne = Player(400,590)
playerBasementTwo = Player(50,300)
playerBasementThree = Player(50,500)
playerFinal = Player(400,500)


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
    all_sprite_list.add(player)




scientist = Scientist()



security_spots1.add(security_spot1, security_spot2, security_spot3, security_spot4, security_spot5, security_spot6,
                    security_spot7)

# add sprite to game's sprite group
'''game_sprites.add(playerlobbyPart1, scientist)'''
# add sprites for security spots

# new bookshelf group

interactives.add(lobbyLevelPart2)
game_sprites.add(playerlobbyPart1)




# define interAction






def gameExit():
    pygame.quit()
    sys.exit()


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

def mouseClick():
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





def mainMenu():



    while gameIntroLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        gameDisplay.fill(color("blue"))
        wallpaper(IntroBackground,0,0)
        message_display('S.E.E.D', pygame.font.match_font('agencyfb'), 115,color('white'),display_width,display_height,True)

        button("Start", 350,300,100,50,color("forestgreen"),color("green"),gameIntro)
        button("Quit", 350, 400, 100, 50, color("darkred"), color("red"),quitGame)

        frames = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        pygame.display.flip()
        gameDisplay.blit(frames, (50, 50))


        pygame.display.update()
        clock.tick(60)

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
        displayDialogue(opening)
        continueDialogue()

        opening = getText(6, 10)
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

        game = False
        gameIntroLoop = False



            # LobbyLevel
            # dialogue = getText(41, 42)
            # displayDialogue(dialogue)
            # continueDialogue()

            #dialogue = getText(43, 44)
            #displayDialogue(dialogue)
            #continueDialogue()

            #dialogue = getText(45, 48)
            #displayDialogue(dialogue)
            #continueDialogue()
            #
            #dialogue = getText(52,53)
            #displayDialogue(dialogue)
            #continueDialogue()
            #
            #dialogue = getText(54,55)
            #displayDialogue(dialogue)
            #continueDialogue()

            #dialogue = getText(56, 57)
            #displayDialogue(dialogue)
            #continueDialogue()

            #dialogue = getText(58, 59)
            #displayDialogue(dialogue)
            #continueDialogue()

            #dialogue = getText(60, 63)
            #displayDialogue(dialogue)
            #continueDialogue()

            #dialogue = getText(64, 65)
            #displayDialogue(dialogue)
            #continueDialogue()

            #            fade(display_width,display_height)



def lobbyLevel():

    bg_img = pygame.image.load(os.path.join(img_dir, "lobby1New.png")).convert()
    test = False

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
        
        # add check fif cor collision - bookshelf and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerlobbyPart1, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window

        if collisions:

            '''interaction = "bookshelf"'''
            # add rect for bg - helps locate background
            gameDisplay.fill(BLACK)
            # draw background image - specify image file and rect to load image
            bg_img = pygame.image.load(os.path.join(img_dir, "lobby2New.png")).convert()
            game_sprites.remove(playerlobbyPart1)
            game_sprites.add(playerlobbyPart2)
            interactives.add(elevatorDoor)




        else:
            interaction = "none"
            # draw
            gameDisplay.fill(BLACK)

        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerlobbyPart1, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            print('gotcha')


        collisions = pygame.sprite.spritecollide(playerlobbyPart2, interactives, True, pygame.sprite.collide_circle)
        if collisions:
            running = False
            print('gotcha')

        # draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        interactives.update()


        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        frames = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        pygame.display.flip()
        gameDisplay.blit(frames, (50, 50))
        # update the display window...
        pygame.display.update()


def elevatorLevel():

    bg_img = pygame.image.load(os.path.join(img_dir, "elevatorFinal.png")).convert()
    game_sprites.remove(playerlobbyPart2)
    game_sprites.add(playerelevatorLevel)

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
        collisions = pygame.sprite.spritecollide(playerelevatorLevel, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background

            # draw background image - specify image file and rect to load image
            elevatorPuzzle()
            interactives.add(elevatorDoorLeaving)

        else:
            interaction = "none"
            # draw
            gameDisplay.fill(BLACK)

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



def waitingRoomLevelOne():

    bg_img = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()
    game_sprites.add(playerWaitingRoomOne)
    game_sprites.remove(playerelevatorLevel)
    interactives.add(bathroomDoor)

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
        collisions = pygame.sprite.spritecollide(playerWaitingRoomOne, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            running = False

        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(player, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            print('gotcha')

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def bathroomLevel():

    bg_img = pygame.image.load(os.path.join(img_dir, "bathroomFinal.png")).convert()
    game_sprites.add(playerBathroom)
    game_sprites.remove(playerWaitingRoomOne)

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
        collisions = pygame.sprite.spritecollide(playerBathroom, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:

            bathroomPuzzle()
            interactives.add(bathroomDoorExit)
            interactives.remove(bathroomPanel)

        collisions = pygame.sprite.spritecollide(playerBathroom, interactives, True, pygame.sprite.collide_circle)

        if collisions:
            running = False

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()


def waitingRoomLevelTwo():

    bg_img = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()
    game_sprites.remove(playerBathroom)
    game_sprites.add(playerWaitingRoomTwo)
    interactives.add(officeEntrance)
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

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def officeLevel():

    bg_img = pygame.image.load(os.path.join(img_dir, "mainOffice.png")).convert()
    game_sprites.remove(playerWaitingRoomTwo)
    game_sprites.add(playerOffice)
    interactives.empty()
    interactives.add(officeDesk)


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

def waitingRoomLevelThree():

    bg_img = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()
    game_sprites.remove(playerOffice)
    game_sprites.add(playerWaitingRoomThree)
    interactives.empty()
    interactives.add(elevatorDoor)

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
        collisions = pygame.sprite.spritecollide(playerWaitingRoomThree, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            running = False


        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(player, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            print('gotcha')

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def basementLevelOne():

    bg_img = pygame.image.load(os.path.join(img_dir, "basementRoom1.png")).convert()
    game_sprites.remove(playerWaitingRoomThree)
    game_sprites.add(playerBasementOne)
    interactives.empty()
    interactives.add(basementDoorOneCorrect)
    wrongDoor.add(basementDoorOneWrong)

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
        collisions = pygame.sprite.spritecollide(playerBasementOne, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background
            # draw background image - specify image file and rect to load image
            running = False

        else:
            interaction = "none"
            # draw
            gameDisplay.fill(BLACK)

        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(player, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            print('gotcha')

        collisions = pygame.sprite.spritecollide(playerBasementOne, wrongDoor, True, pygame.sprite.collide_circle)
        if collisions:
            print('dead')



        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def basementLevelTwo():

    bg_img = pygame.image.load(os.path.join(img_dir, "basementRoom2.png")).convert()
    game_sprites.remove(playerBasementOne)
    game_sprites.add(playerBasementTwo)
    interactives.empty()
    interactives.add(basementDoorTwoCorrect)
    wrongDoor.add(basementDoorTwoWrong)

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
        collisions = pygame.sprite.spritecollide(playerBasementTwo, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background
            # draw background image - specify image file and rect to load image
            running = False

        else:
            interaction = "none"
            # draw
            gameDisplay.fill(BLACK)

        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(playerBasementTwo, wrongDoor, True, pygame.sprite.collide_circle)
        if collisions:
            print('dead')

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def basementLevelThree():

    bg_img = pygame.image.load(os.path.join(img_dir, "basementRoom3.png")).convert()
    game_sprites.remove(playerBasementTwo)
    game_sprites.add(playerBasementThree)
    interactives.empty()
    interactives.add(officeEntrance)


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
        collisions = pygame.sprite.spritecollide(playerBasementThree, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background
            # draw background image - specify image file and rect to load image
            running = False



        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        '''collisions = pygame.sprite.spritecollide(player, wrongDoor, True, pygame.sprite.collide_circle)
        if collisions:
            print('gotcha')'''

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def FinalBossRoom():

    bg_img = pygame.image.load(os.path.join(img_dir, "serverRoom.png")).convert()
    game_sprites.remove(playerBasementThree)
    game_sprites.add(playerFinal)
    interactives.empty()
    interactives.add(elevatorDoor)

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
        collisions = pygame.sprite.spritecollide(player, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background

            # draw background image - specify image file and rect to load image


        else:
            interaction = "none"
            # draw


        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(player, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            print('gotcha')

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()

def ending():

    bg_img = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()

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
        collisions = pygame.sprite.spritecollide(player, interactives, True, pygame.sprite.collide_circle)
        # check collisions for game window
        if collisions:
            interaction = "bookshelf"
            # add rect for bg - helps locate background
            gameDisplay.fill(BLACK)
            # draw background image - specify image file and rect to load image


        else:
            interaction = "none"
            # draw
            gameDisplay.fill(BLACK)

        # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
        collisions = pygame.sprite.spritecollide(player, security_spots1, True, pygame.sprite.collide_circle)
        if collisions:
            print('gotcha')

        #draw background image - specify image file and rect to load image
        gameDisplay.blit(bg_img, bg_rect)

        # draw all sprites to the game window
        game_sprites.draw(gameDisplay)
        # update the display window...
        pygame.display.update()



    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

mainMenu()
lobbyLevel()

interactives.add(elevatorPanel)


lightOne = Light(lightX,light1Y)
lightTwo = Light(lightX,light2Y)
lightThree = Light(lightX,light3Y)
lightFour = Light(lightX,light4Y)

toggle1 = False
toggle2 = False
toggle3 = False
toggle4 = False

elevatorLevel()


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

light1X =83
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



toggle1 = False
toggle2 = False
toggle3 = False
toggle4 = False
toggle5 = False
toggle6 = False

interactives.add(bathroomPanel)
bathroomLevel()




interactives.add(officeEntrance)
waitingRoomLevelTwo()

officeLevel()
waitingRoomLevelThree()
basementLevelOne()
basementLevelTwo()
basementLevelThree()
FinalBossRoom()
#nding()