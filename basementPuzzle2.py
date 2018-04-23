# import modules for pygame template
import pygame, random, sys, os
# import event
import pygame.event as EVENTS

# variables for pygame window
winWidth = 800
winHeight = 600
FPS = 30

# variables for commonly used colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#lever variables
global lever1
lever1 = False
global lever2
lever2 = False
global lever3
lever3 = False
global lever4
lever4 = False
global lever5
lever5 = False
global lever6
lever6 = False
global lever7
lever7 = False
global lever8
lever8 = False

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

#light truths
global toggle1
toggle1 = False
global toggle2
toggle2 = False
global toggle3
toggle3 = False
global toggle4
toggle4 = False
global toggle5
toggle5 = False
global toggle6
toggle6 = False
global toggle7
toggle7 = False
global toggle8
toggle8 = False

# game assets
game_dir = os.path.dirname(__file__)
# relative path to assets dir
assets_dir = os.path.join(game_dir, "assets")
# relative path to image dir
img_dir = os.path.join(assets_dir, "images")

# initialise pygame settings and create game window
pygame.init()
#window = pygame.display.set_mode((winWidth, winHeight), pygame.FULLSCREEN)
#window = pygame.display.set_mode((winWidth, winHeight), pygame.RESIZABLE)
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("sprites - basic")
clock = pygame.time.Clock()

# create a default player sprite for the game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, "yellow-ball.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #checks images and get rect...
        self.rect.center = (winWidth / 2, winHeight / 2)
        self.y_speed = 4

    def update(self):
        self.rect.x += 3
        self.rect.y += self.y_speed
        if self.rect.bottom > winHeight - 200:
            self.y_speed = -4
        if self.rect.top < 200:
            self.y_speed = 4
        if self.rect.left > winWidth:
            self.rect.right = 0

class Lever(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, "lever-down.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect() #checks images and get rect...
        self.rect.center = (winWidth / 2, winHeight / 2)
        self.rect.x = x
        self.rect.y = y
        #x = 60 wide
        #y = 70 height

    def switchUp(self):
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

class Light(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, "red-light.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()  # checks images and get rect...
        self.rect.center = (winWidth / 2, winHeight / 2)
        self.rect.x = x
        self.rect.y = y
    def checkTValue(self,toggle):
        if (toggle==False):
            x = self.rect.x
            y = self.rect.y
            self.image = pygame.image.load(os.path.join(img_dir, "green-light.png")).convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()  # checks images and get rect...
            self.rect.center = (winWidth / 2, winHeight / 2)
            self.rect.x = x
            self.rect.y = y
        elif (toggle==True):
            x = self.rect.x
            y = self.rect.y
            self.image = pygame.image.load(os.path.join(img_dir, "red-light.png")).convert()
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()  # checks images and get rect...
            self.rect.center = (winWidth / 2, winHeight / 2)
            self.rect.x = x
            self.rect.y = y


# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# game sprite group
game_sprites = pygame.sprite.Group()
# create player object
#player = Player()
leverOne = Lever(lever1X,leverY)
leverTwo = Lever(lever2X,leverY)
leverThree = Lever(lever3X,leverY)
leverFour = Lever(lever4X,leverY)
leverFive = Lever(lever5X,leverY)
leverSix = Lever(lever6X,leverY)
leverSeven = Lever(lever7X,leverY)
leverEight = Lever(lever8X,leverY)
# add sprite to game's sprite group
#game_sprites.add(player)
game_sprites.add(leverOne)
game_sprites.add(leverTwo)
game_sprites.add(leverThree)
game_sprites.add(leverFour)
game_sprites.add(leverFive)
game_sprites.add(leverSix)
game_sprites.add(leverSeven)
game_sprites.add(leverEight)

lightOne = Light(lightX,light1Y)
lightTwo = Light(lightX,light2Y)
lightThree = Light(lightX,light3Y)
lightFour = Light(lightX,light4Y)
lightFive = Light(lightX,light5Y)
lightSix = Light(lightX,light6Y)
lightSeven = Light(lightX,light7Y)
lightEight = Light(lightX,light8Y)

game_sprites.add(lightOne)
game_sprites.add(lightTwo)
game_sprites.add(lightThree)
game_sprites.add(lightFour)
game_sprites.add(lightFive)
game_sprites.add(lightSix)
game_sprites.add(lightSeven)
game_sprites.add(lightEight)


def mouseClick():
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
    if (lever1X < coor[0] < (lever1X+leverWidth) and lever1 == False and leverY < coor[1] < (leverY + leverHeight)):
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
        if (toggle6==True):
            toggle6=False
        else :
            toggle6=True
    elif  (lever1X < coor[0] < (lever1X+leverWidth) and lever1==True and leverY < coor[1] < (leverY + leverHeight)):
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
    if (lever2X < coor[0] < (lever2X+leverWidth) and lever2 == False and leverY < coor[1] < (leverY + leverHeight)):
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
    elif  (lever2X < coor[0] < (lever2X+leverWidth) and lever2==True and leverY < coor[1] < (leverY + leverHeight)):
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
    if (lever3X < coor[0] < (lever3X+leverWidth) and lever3 == False and leverY < coor[1] < (leverY + leverHeight)):
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
    elif  (lever3X < coor[0] < (lever3X+leverWidth) and lever3==True and leverY < coor[1] < (leverY + leverHeight)):
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
    if (lever4X < coor[0] < (lever4X+leverWidth) and lever4 == False and leverY < coor[1] < (leverY + leverHeight)):
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
    elif  (lever4X < coor[0] < (lever4X+leverWidth) and lever4==True and leverY < coor[1] < (leverY + leverHeight)):
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
    if (lever5X < coor[0] < (lever5X+leverWidth) and lever5 == False and leverY < coor[1] < (leverY + leverHeight)):
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
    elif  (lever5X < coor[0] < (lever5X+leverWidth) and lever5==True and leverY < coor[1] < (leverY + leverHeight)):
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
    if (lever6X < coor[0] < (lever6X+leverWidth) and lever6 == False and leverY < coor[1] < (leverY + leverHeight)):
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
    elif  (lever6X < coor[0] < (lever6X+leverWidth) and lever6==True and leverY < coor[1] < (leverY + leverHeight)):
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
    if (lever7X < coor[0] < (lever7X+leverWidth) and lever7 == False and leverY < coor[1] < (leverY + leverHeight)):
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
    elif  (lever7X < coor[0] < (lever7X+leverWidth) and lever7==True and leverY < coor[1] < (leverY + leverHeight)):
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
    if (lever8X < coor[0] < (lever8X+leverWidth) and lever8 == False and leverY < coor[1] < (leverY + leverHeight)):
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
    elif  (lever8X < coor[0] < (lever8X+leverWidth) and lever8==True and leverY < coor[1] < (leverY + leverHeight)):
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

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(os.path.join(img_dir, image_file)).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('elevator-circuit-draft-8.png', [0,0])

mouse1 = pygame.mouse.get_pressed()

# create game loop
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
            mouseClick()


    # 'updating' the game
    # update all game sprites
    game_sprites.update()
    # 'rendering' to the window
    window.fill(BLACK)
    window.blit(BackGround.image, BackGround.rect)
    game_sprites.draw(window)
    # update the display window...
    pygame.display.update()