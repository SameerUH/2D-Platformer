import pygame
import sys
import os
from pygame.locals import *
import random
import time

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()

#Colours:
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#Screen dimensions:
SCREENWIDTH = 1100
SCREENHEIGHT = 800
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)

#Start screen
font = pygame.font.Font('freesansbold.ttf', 32)  #Imports the font and size of the text that will be displayed in the start screen.
text = font.render('Click to start game', True, WHITE, BLACK)  #Renders the font to not make it look blurry/broken and sets the colour of the text and the background of the text.
textRect = text.get_rect()  #Creates a rectangle as the shape of the text.
textRect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)  #Sets the position of the text that will appear on screen.

#Player dimensions:
PLAYER_X = 50  #Player's starting x-coordinate.
PLAYER_Y = 700  #Player's starting y-coordinate.
PLAYER_VEL = 0.5  #Speed of the player as they move.
PLAYERSPRITENAME = 'ninjacharacterpygameprojectwithremovedbackground.png'  #Name of the file of the image that will be used as the player's character.
DEFAULT_IMAGE_SIZE = (125, 100)  #Size of the image that will be displayed on the screen.

class Player(pygame.sprite.Sprite):  #Class to create the player
    def __init__(self, image, x, y):  #Function to intitialise the character using self, image, x and y as parameters.
        pygame.sprite.Sprite.__init__(self)  #Sets the player as a sprite.
        self.image = pygame.image.load(image)  #Sets the image of the player by loading the ninjacharacterwithremovedbackground image.
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)  #Scales the image of the player by using .scale to shrink it to the DEFAULT_IMAGE_SIZE
        self.rect = self.image.get_rect()  #Creates a shape for the player which will allow the player to be displayed on screen.
        self.rect.x = x  #Player's x-coordinate
        self.rect.y = y  #Player's y-coordinate
        self.hitbox = (self.rect.x + 37, self.rect.y + 10, 50, 78)  #Creates a rectangular hitbox for the player for collisions.

    def draw_updatescreen(self):  #Update function to allow the player to be constantly updated within the loop.
        playerrect = SCREEN.blit(self.image, (self.rect.x, self.rect.y))  #Displays and updates the player's image in the game.
        self.hitbox = (self.rect.x + 37, self.rect.y + 10, 50, 78)  #Updates the player's hitbox in the game.
        #pygame.draw.rect(SCREEN, WHITE, self.hitbox,2)  #Commented code: Displays the hitbox to keep track and test the collision with other objects and classes.

    def update(self, x, y):  #Update function to update the player's coordinates.
        player.rect.x = x  #Updates the player's x-coordinate.
        player.rect.y = y  #Updates the player's y-coordinate.
        player.hitbox = (self.rect.x + 37, self.rect.y + 10, 50, 78)  #Updates the player's hitbox.

player = Player(PLAYERSPRITENAME, PLAYER_X, PLAYER_Y)  #Creates the character by using the class and certain parameters.

#Jumping code:
PLAYER_isJump = False  #Jumping code set as False to stop the player from constantly jumping.
PLAYER_jumpCount = 9  #Jumping count for the height of the player's jump.
ENEMY_isJump = False  #Jumping code set as False to stop the enemy from constantly jumping.
ENEMY_jumpCount = 9  #Jumping count for the height of the enemy's jump

#Enemy dimensions:
ENEMY_X = 950	#Enemy's starting x-coordinate.
ENEMY_Y = 700	#Enemy's staring y-coordinate.
ENEMY_VEL = 0.2#Enemy's velocity
ENEMYSPRITENAME = 'enemycharacterpygameprojectwithremovedbackground.png'	#Name of the image that will be used for the enemy sprite.
class Enemy(pygame.sprite.Sprite):	#Class to create the enemy.
    def __init__(self, image, x, y):	#Initialisation function to create the characteristics of the enemy.
        pygame.sprite.Sprite.__init__(self)	#Classes the enemy as a sprite.
        self.image = pygame.image.load(image).convert_alpha()	#Loads the image and assigns it to the enemy.
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)	#Scales the image to the same size as the player's image.
        self.rect = self.image.get_rect()
        self.rect.x = x	#Enemy's x-coordinate.
        self.rect.y = y	#Enemy's y-coordinate.
        self.hitbox = (self.rect.x + 37, self.rect.y + 25, 50, 80)	#Enemy's hitbox

    def draw_updatescreen(self):	#Update function to allow the enemy to be constantly updated within the loop.
        enemyrect = SCREEN.blit(self.image, (self.rect.x, self.rect.y))	#Displays and updates the enemy's image in the game.
        self.hitbox = (self.rect.x + 37, self.rect.y + 25, 50, 80)	#Updates the enemy's hitbox in the game.
        #pygame.draw.rect(SCREEN, WHITE, self.hitbox,2)	#Commented code: Displays the hitbox to keep track and test the collision with other objects and classes.

    def update(self, x, y):	#Update function to update the enemy's coordinates.
        enemy.rect.x = x	#Updates the enemy's x-coordinate.
        enemy.rect.y = y	#Updates the enemy's y-coordinate


enemy = Enemy(ENEMYSPRITENAME, ENEMY_X, ENEMY_Y)	#Creates the character by using 	the class and certain parameters.
#Star - the player gets points by colliding with it
STAR_X = random.randint(0, 1000)	#Stars starting x-coordinates
STAR_Y = random.randint(0, 700)	#Stars starting y-coordinates
STARSPRITENAME = 'starwithremovedbackground.png'	#Name of the image for the star.
DEFAULT_IMAGE_SIZE = (125, 100)	#Size of the star.
class Star(pygame.sprite.Sprite):	#Class to create the star.
    def __init__(self, image, x, y):	#Function to initialise the star using self, image, x and y as parameters.
        pygame.sprite.Sprite.__init__(self)	#Classes star as a sprite.
        self.image = pygame.image.load(image).convert_alpha()	#Loads and stores the star image as the sprite image.
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)	#Scales the image size to be the same size as the other characters.
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)	#Star's x-coordinates.
        self.rect.y = random.randint(0, 700)	#Star's y-coordinates.
        self.hitbox = (self.rect.x + 35, self.rect.y + 40, 70, 70)	#Star's hitbox

    def draw_updatescreen(self):	#Update function to allow the star to be constantly updated within the loop.
        star = SCREEN.blit(self.image, (self.rect.x, self.rect.y))	#Displays and updates the star's image in the game.
        self.hitbox = (self.rect.x + 35, self.rect.y + 30, 50, 50)	#Updates the star's hitbox in the game.
        #pygame.draw.rect(SCREEN, WHITE, self.hitbox,2)	#Commented code: Displays the hitbox to keep track and test the collision with other objects and classes.

    def update(self, x, y):	#Update function to update the star's coordinates
        star.rect.x = random.randint(0, 1000)	#Updates the star's x-coordinate
        star.rect.y = random.randint(0, 700)	#Updates the star's y-coordinate

star = Star(STARSPRITENAME, STAR_X, STAR_Y)	#Creates the star by using 	the class and certain parameters.
#Floor dimensions:
PLATFORM_X = -400	#X-coordinate of the floor.
PLATFORM_Y = 710	#Y-coordinate of the floor.
PLATFORMSPRITENAME = 'flooringpygameprojectwithremovedbackground.png'	#Name of the image of the floor which will be displayed in pygame.
PLATFORMSIZE = (1900, 200)	#Size of the image of the floor.
class Platform(pygame.sprite.Sprite):	#Class to create the floor.	
    def __init__(self, image, x, y):	#Function to initialise the floor using self, image, x and y as parameters.
        pygame.sprite.Sprite.__init__(self)	#Classes the floor as a sprite.
        self.image = pygame.image.load(image).convert_alpha()	#Loads and stores the image of the floor.
        self.image = pygame.transform.scale(self.image, PLATFORMSIZE)	#Scales the image of the floor.
        self.rect = self.image.get_rect()
        self.rect.x = x	#X-coordinate of the floor.
        self.rect.y = y	#Y-coordinate of the floor.
        self.hitbox = (self.rect.x + 55, self.rect.y + 70, 1500, 180)	#Hitbox of the floor.
	
    def draw_updatescreen(self):	#Update function to allow the floor to be constantly updated within the loop.
        platform = SCREEN.blit(self.image, (self.rect.x, self.rect.y))	#Displays and updates the floor's image in the game.
        self.hitbox = (self.rect.x + 55, self.rect.y + 70, 1500, 180)	#Updates the floor's hitbox in the game.
        #pygame.draw.rect(SCREEN, WHITE, self.hitbox,2)	#Commented code: Displays the hitbox to keep track and test the collision with other objects and classes.


    def update(self, x, y):	#Update function to update the floor's coordinates.
        platform.rect.x = x	#Updates the floor's x-coordinate.
        platform.rect.y = y	#Updates the floor's y-coordinate.


platform = Platform(PLATFORMSPRITENAME, PLATFORM_X, PLATFORM_Y)	#Creates the star by using 	the class and certain parameters.

#Platforms in the air
class Platform_2(pygame.sprite.Sprite):	#Class to create the platforms in the air.
    def __init__(self, image, x, y):	#Function to initialise the platforms in the air using self, image, x and y as parameters.
        pygame.sprite.Sprite.__init__(self)	#Classes the platforms as a sprite.
        self.image = pygame.image.load(image).convert_alpha()	#Loads ands stores the image of the platform.
        self.rect = self.image.get_rect()
        self.rect.x = x	#X-coordinate of the platforms.
        self.rect.y = y	#Y-coordinate of the platforms.
        self.hitbox = (self.rect.x + 55, self.rect.y + 70, 180, 25)	#Hitboxes of the platforms.

    def draw_updatescreen(self):	#Update function to allow the platforms to be constantly updated within the loop.
        platform_2 = SCREEN.blit(self.image, (self.rect.x, self.rect.y))	#Displays and updates the platforms' images in the game.
        self.hitbox = (self.rect.x + 55, self.rect.y + 70, 180, 25)	#Updates the platforms' hitbox in the game.
        #pygame.draw.rect(SCREEN, WHITE, self.hitbox,2)	#Commented code: Displays the hitbox to keep track and test the collision with other objects and classes.


    def update(self, x, y):	#Update functon to update the platforms' coordinates.
        platform_2.rect.x = x	#Updates the platforms' x-coordinate.
        platform_2.rect.y = y	#Updates the platforms' y-coordinate.


PLATFORM2_X = 400	#Platform 2 x-coordinate.
PLATFORM2_Y = 550	#Platform 2 y-coordinate.
platform_2 = Platform_2(PLATFORMSPRITENAME, PLATFORM2_X, PLATFORM2_Y)	#Creation of platform 2 using Platform_2 class and passed parameters.

PLATFORM3_X = 150	#Platform 3 x-coordinate.
PLATFORM3_Y = 365	#Platform 3 y-coordinate.
platform_3 = Platform_2(PLATFORMSPRITENAME, PLATFORM3_X, PLATFORM3_Y)	#Creation of platform 3 using Platform_2 class and passed parameters.

PLATFORM4_X = 400	#Platform 4 x-coordinate.
PLATFORM4_Y = 180	#Platform 4 y-coordinate.
platform_4 = Platform_2(PLATFORMSPRITENAME, PLATFORM4_X, PLATFORM4_Y)	#Creation of platform 4 using Platform_2 class and passed parameters.

PLATFORM5_X = 650	#Platform 5 x-coordinate.
PLATFORM5_Y = 365	#Platform 5 y-coordinate.
platform_5 = Platform_2(PLATFORMSPRITENAME, PLATFORM5_X, PLATFORM5_Y)	#Creation of platform 5 using Platform_2 class and passed parameters.

PLATFORM6_X = -75	#Platform 6 x-coordinate.
PLATFORM6_Y = 550	#Platform 6 y-coordinate.
platform_6 = Platform_2(PLATFORMSPRITENAME, PLATFORM6_X, PLATFORM6_Y)	#Creation of platform 6 using Platform_2 class and passed parameters.

PLATFORM7_X = 875	#Platform 7 x-coordinate.
PLATFORM7_Y = 550	#Platform 7 y-coordinate.
platform_7 = Platform_2(PLATFORMSPRITENAME, PLATFORM7_X, PLATFORM7_Y)	#Creation of platform 7 using Platform_2 class and passed parameters.

PLATFORM8_X = -75	#Platform 8 x-coordinate.
PLATFORM8_Y = 180	#Platform 8 y-coordinate.
platform_8 = Platform_2(PLATFORMSPRITENAME, PLATFORM8_X, PLATFORM8_Y)	#Creation of platform 8 using Platform_2 class and passed parameters.

PLATFORM9_X = 875	#Platform 9 x-coordinate.
PLATFORM9_Y = 180	#Platform 9 y-coordinate.
platform_9 = Platform_2(PLATFORMSPRITENAME, PLATFORM9_X, PLATFORM9_Y)	#Creation of platform 9 using Platform_2 class and passed parameters.

#Constants
Gamecount = 0
player_score = 0
lives = 3

while True:
    SCREEN.fill(BLACK)  #Fills the background with black
    SCREEN.blit(text, (textRect))  #Displays the start screen text.
    #Start screen
    pos = pygame.mouse.get_pos()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if events.type == pygame.MOUSEBUTTONDOWN:  #If statement to check if the player has clicked the mousebutton
        Gamecount = Gamecount + 1  #If the statement is True then increments a variable called Gamecount
        textRect.center = (-100, -200)  #Moves the position of the start screen text to make it look like it disappeared but in reality it has just moved off the screen.

    if Gamecount >= 1:  #If statement to check if Gamecount >= 1, if it has then the game starts and the user can play the game.
        player_input = pygame.key.get_pressed()  #Sets the player's input as a variable.
        #Player movements:
        if (player_input[pygame.K_LEFT]) or (player_input[pygame.K_a]):  #If statement to check if the left arrow or the a button has been pressed on the keyboard.
            PLAYER_X -= PLAYER_VEL  #If the statement is True then the player's x-coordinate is decreased by the player's velocity to move left.
        if (player_input[pygame.K_RIGHT]) or (player_input[pygame.K_d]):  #If statement to check if the right arrow or the d button has been pressed on the keyboard.
            PLAYER_X += PLAYER_VEL  #If the statement is True then the player's x-coordinate is increased by the player's velocity to move right.
          
        #Jumping code
        if not (PLAYER_isJump):  #If statement to check if the PLAYER_isJump is False.
            if player_input[pygame.K_UP] or player_input[pygame.K_w]:  	#If statement to check if the up arrow or w button has been pressed.  
                PLAYER_isJump = True	#If it has been pressed then it sets PLAYER_isJump to True.
        else:
            if PLAYER_jumpCount >= -9:	#If statement to check if the PLAYER_jumpCount is greater or equal to -9	
                PLAYER_Y -= (PLAYER_jumpCount * abs(PLAYER_jumpCount)) * 0.5	#If it is then it decrements the player's y-coordinateby small values.
                PLAYER_jumpCount -= 0.5	#Decrements the PLAYER_jumpCount by 0.5.
            else:
                PLAYER_jumpCount = 9	#Sets the PLAYER_jumpCount to 9
                PLAYER_isJump = False	#Sets the PLAYER_isJump to False.

        if PLAYER_Y != (ENEMY_Y) and PLAYER_Y <= (ENEMY_Y - 92.5) or PLAYER_Y <= (ENEMY_Y - 92.5):	#If statement to check if the player's y-coordinate is at a certain distance away from the enemy's y coordinate.
            if not (ENEMY_isJump):	#If statement to check if the ENEMY_isJump is False.
                ENEMY_isJump = True	#If it is false then it is turned to True.
            else:
                if ENEMY_jumpCount >= -9:	#If statement to check if the ENEMY_jumpCount is greater or equal to -9.
                    ENEMY_Y -= (ENEMY_jumpCount * abs(ENEMY_jumpCount)) * 0.5	#If it is then it decrements the enemy's y-coordinate by small values.
                    ENEMY_jumpCount -= 0.5	#Decrements the ENEMY_jumpCount by 0.5.
                else:
                    ENEMY_jumpCount = 9	#Sets the ENEMY_jumpCount to 9.
                    ENEMY_isJump = False	#Sets the ENEMY_isJump to False.

        #Gravity
        PLAYER_Y += 6
        ENEMY_Y += 6

        #Boundary statements:
        if PLAYER_X > 1100 or PLAYER_X < -50:
            PLAYER_X = 80
            PLAYER_Y = 700
            ENEMY_X = 980
            ENEMY_Y = 700
        elif PLAYER_Y > 700 or PLAYER_Y < -50:
            PLAYER_Y = 700
            ENEMY_Y = 700
        if ENEMY_Y > 700 or ENEMY_Y < -50:
            ENEMY_Y = 700
        
        #Enemy pathfinding:
        if ENEMY_X != PLAYER_X and ENEMY_X > PLAYER_X:	#If statement to check if the enemy's x-coordinate doesn't equal and is greater then the player's x-coordinate.
            ENEMY_X -= ENEMY_VEL	#Decrements the enemy's x-coordinate by the enemy's velocity to make it closer to the player's x-coordinate.
        if ENEMY_X != PLAYER_X and ENEMY_X < PLAYER_X:	#If statement to check if the enemy's x-coordinate doesn't equal and is less then the player's x-coordinate.
            ENEMY_X += ENEMY_VEL	#Increments the enemy's x-coordinate by the enemy's velocity to make it closer to the player's x-coordinate.

        #Collision:
        #Player collision with platform
        if player.hitbox[1] < platform.hitbox[1] + platform.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform.hitbox[1]:	#If statement to check if the player's y-coordinate is in between the top and bottom sides of the platform's hitbox.
            if player.hitbox[0] + player.hitbox[2] > platform.hitbox[0] and player.hitbox[0] < platform.hitbox[0] + platform.hitbox[2]:	#If statement to check if the player's x-coordinate is in between the left and right sides of the platform's hitbox.
                PLAYER_Y -= 6	#If the player's coordinates are inside the hitbox then it decrements the player's y-coordinate to counter gravity.

        #Player collision with platforms in the air
        if player.hitbox[1] < platform_2.hitbox[1] + platform_2.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform_2.hitbox[1]:	#If statement to check if the player's y-coordinate is in between the top and bottom sides of the platform's hitbox.
            if player.hitbox[0] + player.hitbox[2] > platform_2.hitbox[0] and player.hitbox[0] < platform_2.hitbox[0] + platform_2.hitbox[2]:	#If statement to check if the player's x-coordinate is in between the left and right sides of the platform's hitbox.
                PLAYER_Y = 536	#If the player's coordinates are inside the hitbox then it sets the player's y-coordinate to be constantly above the platform.
                PLAYER_Y -= 6	#If the player's coordinates are inside the hitbox then it decrements the player's y-coordinate to counter gravity and make it so the player doesn't fall through the platform.

        if player.hitbox[1] < platform_3.hitbox[1] + platform_3.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform_3.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > platform_3.hitbox[0] and player.hitbox[0] < platform_3.hitbox[0] + platform_3.hitbox[2]:
                PLAYER_Y = 351
                PLAYER_Y -= 6

        if player.hitbox[1] < platform_4.hitbox[1] + platform_4.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform_4.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > platform_4.hitbox[0] and player.hitbox[0] < platform_4.hitbox[0] + platform_4.hitbox[2]:
                PLAYER_Y = 166
                PLAYER_Y -= 6

        if player.hitbox[1] < platform_5.hitbox[1] + platform_5.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform_5.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > platform_5.hitbox[0] and player.hitbox[0] < platform_5.hitbox[0] + platform_5.hitbox[2]:
                PLAYER_Y = 351
                PLAYER_Y -= 6

        if player.hitbox[1] < platform_6.hitbox[1] + platform_6.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform_6.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > platform_6.hitbox[0] and player.hitbox[0] < platform_6.hitbox[0] + platform_6.hitbox[2]:
                PLAYER_Y = 536
                PLAYER_Y -= 6

        if player.hitbox[1] < platform_7.hitbox[1] + platform_7.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform_7.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > platform_7.hitbox[0] and player.hitbox[0] < platform_7.hitbox[0] + platform_7.hitbox[2]:
                PLAYER_Y = 536
                PLAYER_Y -= 6

        if player.hitbox[1] < platform_8.hitbox[1] + platform_8.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform_8.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > platform_8.hitbox[0] and player.hitbox[0] < platform_8.hitbox[0] + platform_8.hitbox[2]:
                PLAYER_Y = 166
                PLAYER_Y -= 6

        if player.hitbox[1] < platform_9.hitbox[1] + platform_9.hitbox[3] and player.hitbox[1] + player.hitbox[3] > platform_9.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > platform_9.hitbox[0] and player.hitbox[0] < platform_9.hitbox[0] + platform_9.hitbox[2]:
                PLAYER_Y = 166
                PLAYER_Y -= 6

        #Enemy collision with the platforms
        if enemy.hitbox[1] < platform.hitbox[1] + platform.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > platform.hitbox[1]:	#If statement to check if the enemy's y-coordinate is in between the top and bottom sides of the platform's hitbox.
            if enemy.hitbox[0] + enemy.hitbox[2] > platform.hitbox[0] and enemy.hitbox[0] < platform.hitbox[0] + platform.hitbox[2]:	#If statement to check if the enemy's x-coordinate is in between the left and right sides of the platform's hitbox.
                ENEMY_Y -= 6	#Decrements the enemy's y-coordinate to counter gravity.

        if enemy.hitbox[1] < platform_2.hitbox[1] + platform_2.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > platform_2.hitbox[1]:	#If statement to check if the enemy's y-coordinate is in between the top and bottom sides of the platform's hitbox.
            if enemy.hitbox[0] + enemy.hitbox[2] > platform_2.hitbox[0] and enemy.hitbox[0] < platform_2.hitbox[0] + platform_2.hitbox[2]:	#If statement to check if the enemy's x-coordinate is in between the left and right sides of the platform's hitbox.
                ENEMY_Y = 520	#If the enemy's hitbox is inside the platform's hitbox then it constantly sets the enemy's y-coordinate to be above the platform.
                ENEMY_Y -= 6	#Decrements the enemy's y-coordinate to counter gravity.

        if enemy.hitbox[1] < platform_3.hitbox[1] + platform_3.hitbox[3] and enemy.hitbox[1] + player.hitbox[3] > platform_3.hitbox[1]:
            if enemy.hitbox[0] + enemy.hitbox[2] > platform_3.hitbox[0] and enemy.hitbox[0] < platform_3.hitbox[0] + platform_3.hitbox[2]:
                ENEMY_Y = 335
                ENEMY_Y -= 6

        if enemy.hitbox[1] < platform_4.hitbox[1] + platform_4.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > platform_4.hitbox[1]:
            if enemy.hitbox[0] + enemy.hitbox[2] > platform_4.hitbox[0] and enemy.hitbox[0] < platform_4.hitbox[0] + platform_4.hitbox[2]:
                ENEMY_Y = 150
                ENEMY_Y -= 6

        if enemy.hitbox[1] < platform_5.hitbox[1] + platform_5.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > platform_5.hitbox[1]:
            if enemy.hitbox[0] + enemy.hitbox[2] > platform_5.hitbox[0] and enemy.hitbox[0] < platform_5.hitbox[0] + platform_5.hitbox[2]:
                ENEMY_Y = 335
                ENEMY_Y -= 6

        if enemy.hitbox[1] < platform_6.hitbox[1] + platform_6.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > platform_6.hitbox[1]:
            if enemy.hitbox[0] + enemy.hitbox[2] > platform_6.hitbox[0] and enemy.hitbox[0] < platform_6.hitbox[0] + platform_6.hitbox[2]:
                ENEMY_Y = 520
                ENEMY_Y -= 6

        if enemy.hitbox[1] < platform_7.hitbox[1] + platform_7.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > platform_7.hitbox[1]:
            if enemy.hitbox[0] + enemy.hitbox[2] > platform_7.hitbox[0] and enemy.hitbox[0] < platform_7.hitbox[0] + platform_7.hitbox[2]:
                ENEMY_Y = 520
                ENEMY_Y -= 6

        if enemy.hitbox[1] < platform_8.hitbox[1] + platform_8.hitbox[3] and enemy.hitbox[1] + enemy.hitbox[3] > platform_8.hitbox[1]:
            if enemy.hitbox[0] + enemy.hitbox[2] > platform_8.hitbox[0] and enemy.hitbox[0] < platform_8.hitbox[0] + platform_8.hitbox[2]:
                ENEMY_Y = 150
                ENEMY_Y -= 6

        if enemy.hitbox[1] < platform_9.hitbox[1] + platform_9.hitbox[3] and enemy.hitbox[1] + player.hitbox[3] > platform_9.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > platform_9.hitbox[0] and player.hitbox[0] < platform_9.hitbox[0] + platform_9.hitbox[2]:
                ENEMY_Y = 150
                ENEMY_Y -= 6

        #Player colision with star
        if player.hitbox[1] < star.hitbox[1] + star.hitbox[3] and player.hitbox[1] + star.hitbox[3] > star.hitbox[1]:	#If statement to check if the players hitbox y-coordinate is in between the star's hitbox top and bottom sides.
            if player.hitbox[0] + player.hitbox[2] > star.hitbox[0] and player.hitbox[0] < star.hitbox[0] + star.hitbox[2]:	#If statement to check if the player's hitbox x-coordinate is in between the star's hitbox left and right sides.
                print("You got a point, your score is now", player_score)	#If the statement is true then it prints that they got a point and prints their score.
                star.rect.x = random.randint(50, 950)	#It then changes the star's x-coordinate to a random number.
                star.rect.y = random.randint(50, 700)	#It then chages the star's y-coordinate to a random number.
                player_score += 1	#It then increments the player's score by 1.

        #Enemy collision with star
        if enemy.hitbox[1] < star.hitbox[1] + star.hitbox[3] and enemy.hitbox[1] + star.hitbox[3] > star.hitbox[1]:	#If statement to check if the enemy's hitbox y-coordinate is in between the star's hitbox top and bottom sides.
            if enemy.hitbox[0] + enemy.hitbox[2] > star.hitbox[0] and enemy.hitbox[0] < star.hitbox[0] + star.hitbox[2]:	#If statement to check if the enemy's hitbox x-coordinate is in between the star's hitbox left and right sides.
                star.rect.x = random.randint(50, 950)	#Changes the star's x-coordinate to a random number.
                star.rect.y = random.randint(50, 700)	#Changes the star's y-coordinate to a random number.

        #Player collision with enemy
        if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + enemy.hitbox[3] > enemy.hitbox[1]:	#If statement to check if the player's hitbox y-coordinate are between the enemy's hitbox top and bottom sides.
            if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:	#If statemment to check if the player's hitbox x-coordinate are between the enemy's htibox left and right sides.
                PLAYER_X = 50	#Resets the player's x-coordinate to the starting position.
                PLAYER_Y = 700	#Resets the player's y-coordinate to the starting position.
                ENEMY_X = 950	#Resets the enemy's x-coordinate to the starting position.
                ENEMY_Y = 700	#Resets the enemy's y-coordinate to the starting position.
                lives -= 1	#Decrements the player's lives by 1.

        #Star stuck in platforms:
        if star.hitbox[1] < platform_2.hitbox[1] + platform_2.hitbox[3] and star.hitbox[1] + star.hitbox[3] > platform_2.hitbox[1]:	#If statement to check if the star's hitbox y-coordinates are between the platform's hitbox top and bottom sides.
            if star.hitbox[0] + star.hitbox[2] > platform_2.hitbox[0] and star.hitbox[0] < platform_2.hitbox[0] + platform_2.hitbox[2]: #If statement to check if the star's hitbox x-coordinates are between the platform's left and right sides.
                star.rect.x = random.randint(50, 950)	#Changes the star's x-coordinate to a random number.
                star.rect.y = random.randint(50, 700)	#Changes the star's y-coordinate to a random number.
                star.hitbox = (star.rect.x + 35, star.rect.y + 40, 70, 70)	#Changes the star's hitbox to be with the star's new coordinates.

        if star.hitbox[1] < platform_3.hitbox[1] + platform_3.hitbox[3] and star.hitbox[1] + star.hitbox[3] > platform_3.hitbox[1]:
            if star.hitbox[0] + star.hitbox[2] > platform_3.hitbox[0] and star.hitbox[0] < platform_3.hitbox[0] + platform_3.hitbox[2]:
                star.rect.x = random.randint(50, 950)
                star.rect.y = random.randint(50, 700)
                star.hitbox = (star.rect.x + 35, star.rect.y + 40, 70, 70)

        if star.hitbox[1] < platform_4.hitbox[1] + platform_4.hitbox[3] and star.hitbox[1] + star.hitbox[3] > platform_4.hitbox[1]:
            if star.hitbox[0] + star.hitbox[2] > platform_4.hitbox[0] and star.hitbox[0] < platform_4.hitbox[0] + platform_4.hitbox[2]:
                star.rect.x = random.randint(50, 950)
                star.rect.y = random.randint(50, 700)
                star.hitbox = (star.rect.x + 35, star.rect.y + 40, 70, 70)

        if star.hitbox[1] < platform_5.hitbox[1] + platform_5.hitbox[3] and star.hitbox[1] + star.hitbox[3] > platform_5.hitbox[1]:
            if star.hitbox[0] + star.hitbox[2] > platform_5.hitbox[0] and star.hitbox[0] < platform_5.hitbox[0] + platform_5.hitbox[2]:
                star.rect.x = random.randint(50, 950)
                star.rect.y = random.randint(50, 700)
                star.hitbox = (star.rect.x + 35, star.rect.y + 40, 70, 70)

        if star.hitbox[1] < platform_6.hitbox[1] + platform_6.hitbox[3] and star.hitbox[1] + star.hitbox[3] > platform_6.hitbox[1]:
            if star.hitbox[0] + star.hitbox[2] > platform_6.hitbox[0] and star.hitbox[0] < platform_6.hitbox[0] + platform_6.hitbox[2]:
                star.rect.x = random.randint(50, 950)
                star.rect.y = random.randint(50, 700)
                star.hitbox = (star.rect.x + 35, star.rect.y + 40, 70, 70)

        if star.hitbox[1] < platform_7.hitbox[1] + platform_7.hitbox[3] and star.hitbox[1] + star.hitbox[3] > platform_7.hitbox[1]:
            if star.hitbox[0] + star.hitbox[2] > platform_7.hitbox[0] and star.hitbox[0] < platform_7.hitbox[0] + platform_7.hitbox[2]:
                star.rect.x = random.randint(50, 950)
                star.rect.y = random.randint(50, 700)
                star.hitbox = (star.rect.x + 35, star.rect.y + 40, 70, 70)

        if star.hitbox[1] < platform_8.hitbox[1] + platform_8.hitbox[3] and star.hitbox[1] + star.hitbox[3] > platform_8.hitbox[1]:
            if star.hitbox[0] + star.hitbox[2] > platform_8.hitbox[0] and star.hitbox[0] < platform_8.hitbox[0] + platform_8.hitbox[2]:
                star.rect.x = random.randint(50, 950)
                star.rect.y = random.randint(50, 700)
                star.hitbox = (star.rect.x + 35, star.rect.y + 40, 70, 70)


        #Score display
        score_display = font.render('Score: ' + str(player_score), True, WHITE, BLACK)	#Renders the font of the display and chooses the colour and text that will be displayed on screen.
        scoreRect = score_display.get_rect()	#Turns the shape with the text into a rectangle.
        scoreRect.center = (1000, 50)	#Coordinates of the score text.
        SCREEN.blit(score_display, (scoreRect))	#Displays the score on the screen.

        #Lives display
        lives_display = font.render("Lives: " + str(lives), True, WHITE, BLACK)	#Renders the font of the display and chooses the colour and text that will be displayed on screen.
        livesRect = lives_display.get_rect()	#Turns the shape with the text into a rectangle.
        livesRect.center = (100, 50)	#Coordinates of the lives text.
        SCREEN.blit(lives_display, livesRect)	#Displays the numbers of lives left on screen

        #Game updates:
        if lives > 0:	#If statement to check if the player is still alive.
            player.update(PLAYER_X, PLAYER_Y)	#Updates the player's coordinates using function within class.
            enemy.update(ENEMY_X, ENEMY_Y)	#Updates enemy's coordinates using function within class.
            player.draw_updatescreen()	#Updates the player's image on the screen.
            enemy.draw_updatescreen()	#Updates the enemy's image on the screen.
            platform.draw_updatescreen()	#Updates the floor's image on the screen.
            star.draw_updatescreen()	#Updates the star's image on the screen.
            platform_2.draw_updatescreen()	#Updates the platform's image on the screen.
            platform_3.draw_updatescreen()	
            platform_4.draw_updatescreen()
            platform_5.draw_updatescreen()
            platform_6.draw_updatescreen()
            platform_7.draw_updatescreen()
            platform_8.draw_updatescreen()
            platform_9.draw_updatescreen()
        elif lives <= 0:	#If statement to check if the player is dead.
            lives_display = font.render("You have no more lives, Game over", True, WHITE, BLACK)	#Changes the lives display to say that they player has no more lives left.
            livesRect = lives_display.get_rect()
            livesRect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)	#Changes the position of the lives display to be in the center of the screen.
            SCREEN.fill(BLACK)	#Fills the screen with black to remove the images.
            SCREEN.blit(lives_display, livesRect)	#Displays the lives display telling the player they have no more lives left.
            scoreRect.center = (550, 500)	#Changes the position of the scores display to be underneath the lives display.
            SCREEN.blit(score_display, (scoreRect))	#Displays the score display.
    pygame.display.update()	#Updates the screen.