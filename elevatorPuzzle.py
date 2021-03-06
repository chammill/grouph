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

#lever coordinates
leverWidth = 60
leverHeight = 70
leverY = 500

lever1X = 75
lever2X = 200
lever3X = 325
lever4X = 450


#light coordinates
lightX = 675

light1Y = 45
light2Y = 160
light3Y = 275
light4Y = 395


#light truths
global toggle1
toggle1 = False
global toggle2
toggle2 = False
global toggle3
toggle3 = False
global toggle4
toggle4 = False

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

#lever
leverOne = Lever(lever1X,leverY)
leverTwo = Lever(lever2X,leverY)
leverThree = Lever(lever3X,leverY)
leverFour = Lever(lever4X,leverY)
# add sprite to game's sprite group
#game_sprites.add(player)
game_sprites.add(leverOne)
game_sprites.add(leverTwo)
game_sprites.add(leverThree)
game_sprites.add(leverFour)

#light
lightOne = Light(lightX,light1Y)
lightTwo = Light(lightX,light2Y)
lightThree = Light(lightX,light3Y)
lightFour = Light(lightX,light4Y)

game_sprites.add(lightOne)
game_sprites.add(lightTwo)
game_sprites.add(lightThree)
game_sprites.add(lightFour)

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

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(os.path.join(img_dir, image_file)).convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('elevator-circuit-draft.png', [0,0])

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
    # draw
    # 'rendering' to the window
    window.fill(BLACK)
    window.blit(BackGround.image, BackGround.rect)
    game_sprites.draw(window)
    # update the display window...
    pygame.display.update()