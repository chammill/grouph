# import modules for pygame template
import pygame, random, sys, os
# import event
import pygame.event as EVENTS


# 
# variables for pygame window - space invaders vertical screen style
winWidth = 800
winHeight = 600
FPS = 60


# variables for commonly used colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

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
        self.image = pygame.transform.scale(char_img, (49, 37))
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
        if key_state[pygame.K_d]:
            self.speed_x = 4
        if key_state[pygame.K_w]:
            self.speed_y = -4
        if key_state[pygame.K_s]:
            self.speed_y = 4
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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # load ship image & scale to fit game window...
        self.image = bookshelf_img
        # set colorkey to remove black background for ship's rect
        self.image.set_colorkey(GREEN)
        #check images and get rect...
        self.rect = self.image.get_rect()
        # set radius for circle bounding
        self.radius = 50
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = winWidth / 3
        self.rect.bottom = winHeight - 20








# define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

# load graphics/images for the game
bg_img = pygame.image.load(os.path.join(img_dir, "main_room.png")).convert()
# add rect for bg - helps locate background
bg_rect = bg_img.get_rect()
# load graphics/images for the game
bg_img2 = pygame.image.load(os.path.join(img_dir, "main_room2.png")).convert()
# add rect for bg - helps locate background
bg_rect2 = bg_img2.get_rect()
# player's character
char_img = pygame.image.load(os.path.join(img_dir, "char1.png")).convert()
# bookshelf
bookshelf_img = pygame.image.load(os.path.join(img_dir, "bookshelf-green.png")).convert()
#security camera spotlights
security_spot = pygame.image.load(os.path.join(img_dir, "camera_spot.png")).convert()




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










security_spot1 = Security(120, 140)
security_spot2 = Security(365, 140)
security_spot3 = Security(120, 240)
security_spot4 = Security(120, 380)

security_spot5 = Security(620, 140)

security_spot6 = Security(465, 380)
security_spot7 = Security(665, 380)


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

security_spots1.add(security_spot1, security_spot2, security_spot3, security_spot4, security_spot5, security_spot6, security_spot7)

# add sprite to game's sprite group
game_sprites.add(player, bookshelf, security_spots1)
# add sprites for security spots

# new bookshelf group
interactives.add(bookshelf)

# define interAction
def interAction():
    print(interaction)
    if interaction == "bookshelf":
        nextLvl()
        

def nextLvl():
    




    wall_list.empty()
    game_sprites.remove(security_spots1)






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
        # draw
        bg_img = pygame.image.load(os.path.join(img_dir, "main_room2.png")).convert()
        # add rect for bg - helps locate background
        window.fill(BLACK)
        # draw background image - specify image file and rect to load image
        nextLvl()

    else:
        interaction = "none"
        # draw
        window.fill(BLACK)


    # add check for collision - security spots and player sprite (False = hit object is not deleted from game window)
    collisions = pygame.sprite.spritecollide(player, security_spots1, True, pygame.sprite.collide_circle)
    if collisions:
        print('gotcha')

    # draw background image - specify image file and rect to load image    
    window.blit(bg_img, bg_rect)
        







    
    # draw all sprites to the game window
    game_sprites.draw(window)
    # update the display window...
    pygame.display.update()
