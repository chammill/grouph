# import modules for pygame template
import pygame, random, sys, os
# import event
import pygame.event as EVENTS


# 
# variables for pygame window - space invaders vertical screen style
winWidth = 800
winHeight = 600
FPS = 60
level = 1

# variables for commonly used colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)



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




# initialise pygame settings and create game window
interaction = "empty"

# game assets
game_dir = os.path.dirname(__file__)
# relative path to assets dir
assets_dir = os.path.join(game_dir, "assets")
# relative path to image dir
img_dir = os.path.join(assets_dir, "images")

# initialise pygame settings and create game window
pygame.init()
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Top Down RPG view")
clock = pygame.time.Clock()






# create a default player sprite for the game
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = pygame.transform.scale(char_img, (24, 30))
        # set colorkey to remove white background for char's rect
        self.image.set_colorkey(WHITE)
        #check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = winWidth / 1.5
        self.rect.bottom = winHeight - 20

        self.speed_x = 0
        self.speed_y = 0

    # update per loop iteration
    def update(self):
        self.speed_x = 0
        self.speed_y = 0

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_a]:
            self.speed_x = -4
            #change to facing left image
            self.image = pygame.transform.scale(char_img_l, (24, 30))
            # set colorkey to remove black background for ship's rect
            self.image.set_colorkey(WHITE)
        if key_state[pygame.K_d]:
            self.speed_x = 4
            #change to facing right image
            self.image = pygame.transform.scale(char_img_r, (24, 30))
            # set colorkey to remove black background for ship's rect
            self.image.set_colorkey(WHITE)
        if key_state[pygame.K_w]:
            self.speed_y = -4
            #change to facing up image
            self.image = pygame.transform.scale(char_img_u, (24, 30))
            # set colorkey to remove black background for ship's rect
            self.image.set_colorkey(WHITE)
        if key_state[pygame.K_s]:
            self.speed_y = 4
            #change to facing down image
            self.image = pygame.transform.scale(char_img, (24, 30))
            # set colorkey to remove black background for ship's rect
            self.image.set_colorkey(WHITE)
        self.rect.x += self.speed_x

        if self.rect.right > winWidth:
            self.rect.right = winWidth
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
        if self.rect.bottom > winHeight:
            self.rect.bottom = winHeight
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom





#wall
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
wall = Wall(0, 110, 25, 600)
wall_list.add(wall)

# top left wall 
wall = Wall(0, 110, 370, 60)
wall_list.add(wall)

# top right wall 
wall = Wall(460, 110, 370, 60)
wall_list.add(wall)

# right wall 
wall = Wall(775, 130, 25, 600)
wall_list.add(wall)

# top right desk 
wall = Wall(470, 265, 60, 40)
wall_list.add(wall)

# top left desk 
wall = Wall(290, 265, 60, 40)
wall_list.add(wall)

# bottom right desk 
wall = Wall(470, 375, 60, 50)
wall_list.add(wall)

# bottom left desk 
wall = Wall(290, 375, 60, 50)
wall_list.add(wall)



all_sprite_list.add(wall)





# create a bookshelf
class Bookshelf(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = pygame.transform.scale(bookshelf_img, (24, 30))
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(GREEN)
        #check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 2
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = winWidth / 3
        self.rect.bottom = winHeight - 20



# create a scientist
class Scientist(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = scientist_img
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(WHITE)
        #check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 1
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = winWidth - 300
        self.rect.bottom = winHeight - 280





# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# load graphics/images for the game
bg_img = pygame.image.load(os.path.join(img_dir, "elevatorFinal.png")).convert()
# add rect for bg - helps locate background
bg_rect = bg_img.get_rect()

# load graphics/images for the game
bg_img2 = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()
# add rect for bg - helps locate background
bg_rect2 = bg_img2.get_rect()

# load graphics/images for the game
bg_lvl3 = pygame.image.load(os.path.join(img_dir, "officeLevelNew.png")).convert()
# add rect for bg - helps locate background
bg_rect3 = bg_img2.get_rect()


# player's character
char_img = pygame.image.load(os.path.join(img_dir, "char1.png")).convert()
# player's character facing right
char_img_r = pygame.image.load(os.path.join(img_dir, "char1r.png")).convert()
# player's character facing left
char_img_l = pygame.image.load(os.path.join(img_dir, "char1l.png")).convert()
# player's character facing up
char_img_u = pygame.image.load(os.path.join(img_dir, "char1u.png")).convert()

# bookshelf
bookshelf_img = pygame.image.load(os.path.join(img_dir, "bookshelf-green.png")).convert()
#security camera spotlights
security_spot = pygame.image.load(os.path.join(img_dir, "camera_spot.png")).convert()
#scientist
scientist_img = pygame.image.load(os.path.join(img_dir, "scientist.png")).convert()



# create security spots
class Security(pygame.sprite.Sprite):
    def __init__(self, x, y):
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










security_spot1 = Security(120, 260)
security_spot2 = Security(365, 260)
security_spot3 = Security(120, 360)
security_spot4 = Security(120, 500)

security_spot5 = Security(620, 260)

security_spot6 = Security(465, 500)
security_spot7 = Security(665, 500)


# sprite groups - game, mob, projectiles...
game_sprites = pygame.sprite.Group()
mob_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
interactives = pygame.sprite.Group()
maps = pygame.sprite.Group()
security_spots1 = pygame.sprite.Group()
# create player object
player = Player()
player.walls = wall_list
all_sprite_list.add(player)



bookshelf = Bookshelf()
scientist = Scientist()

security_spots1.add(security_spot1, security_spot2, security_spot3, security_spot4, security_spot5, security_spot6, security_spot7)

# add sprite to game's sprite group
game_sprites.add(player, bookshelf, security_spots1, scientist)
# add sprites for security spots

# new bookshelf group
interactives.add(bookshelf)

# define interAction
def interAction():
    print(interaction)
    if interaction == "bookshelf":
        nextLvl()
        
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

## Puzzle Level 1
def nextLvl():
    

    ## Remove the collision walls
    wall_list.empty()
    game_sprites.remove(security_spots1)



    pygame.mixer.init()

    ## Reset the collision walls for the next level

    # left wall 
    wall = Wall(0, 110, 25, 600)
    wall_list.add(wall)

    # top left wall 
    wall = Wall(0, 110, 370, 60)
    wall_list.add(wall)

    # top right wall 
    wall = Wall(460, 110, 370, 60)
    wall_list.add(wall)

    # right wall 
    wall = Wall(775, 130, 25, 600)
    wall_list.add(wall)

    # top right desk 
    wall = Wall(470, 265, 60, 40)
    wall_list.add(wall)

    # top left desk 
    wall = Wall(290, 265, 60, 40)
    wall_list.add(wall)

    # bottom right desk 
    wall = Wall(470, 375, 60, 50)
    wall_list.add(wall)

    # bottom left desk 
    wall = Wall(290, 375, 60, 50)
    wall_list.add(wall)



    all_sprite_list.add(wall)


    
    miniGame1 = True
    while miniGame1 == True:
        pygame.mixer.init()
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


                        ## add to another level function
                        miniGame1 = False
                        running = True
                        game_sprites.add(security_spots1)
                        # draw background image - specify image file and rect to load image    

                        


                    




    
caught = False
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
            elif event.key == pygame.K_SPACE:
                # fire laser beam...
                interAction()

        # check click on window exit button
        if event.type == pygame.QUIT:
            gameExit()
    # 'updating' the game
    # update all game sprites
    game_sprites.update()



       
    # add check for collision - bookshelf and player sprite (False = hit object is not deleted from game window)
    collisions = pygame.sprite.spritecollide(player, interactives, True, pygame.sprite.collide_circle)
    # check collisions for game window
    if collisions:
        interaction = "bookshelf"
        # add rect for bg - helps locate background
        window.fill(BLACK)
        # draw background image - specify image file and rect to load image
        level += 1
        nextLvl()

    else:
        interaction = "none"
        # draw
        window.fill(BLACK)


    # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
    collisions = pygame.sprite.spritecollide(player, security_spots1, True, pygame.sprite.collide_circle)
    if collisions:
        running = False
        caught = True




    # draw background image - specify image file and rect to load image    
    if level == 1:
        window.blit(bg_img, bg_rect)
    elif level == 2 :
        window.blit(bg_img2, bg_rect2)



    while caught == True:
        myfont = pygame.font.SysFont("Arial", 20)
        label = myfont.render("Caught on camera! Press space to continue. Esc to exit", 1, (255, 255, 0))
        window.blit(label, (100, 50))
        pygame.display.flip()

        
        # 'processing' inputs (events)
        for event in EVENTS.get():
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                # check for ESCAPE key
                if event.key == pygame.K_ESCAPE:
                    gameExit()
                elif event.key == pygame.K_SPACE:
                    print('hi')
                    # fire laser beam...
                    caught = False
                    running = True



    
    # draw all sprites to the game window
    game_sprites.draw(window)
    # update the display window...
    pygame.display.update()



##





                

