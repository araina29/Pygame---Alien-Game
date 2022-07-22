import pygame
import random
#initializing the pygame module
pygame.init()

#creating a screen with values 800 to 600 as the resolution

screen = pygame.display.set_mode((800,600))

#Setting the title
pygame.display.set_caption("Space Invaders")

#Adding an image on the screen 
imagep = pygame.image.load('image.png')
#X and Y coordinates for player 1 
x_1 = 400 
y_1 = 550
changep = 0
#showing player one on the screen
def player(x_1,y_1):
    screen.blit(imagep,(x_1,y_1))

imagee = pygame.image.load('alien.png')
x_2 = random.randint(0,800)
y_2 = random.randint(50,150)
changeex = 1
changeey = 40
#showing enemy one on the screen
def enemy(x_1,y_1):
    screen.blit(imagee,(x_1,y_1))

#Background
bg = pygame.image.load("bg.jpg")

#Bullet 
imageb = pygame.image.load('bullet.png')
#X and Y coordinates for bullet are
x_3 = 0
y_3 = 550
bulletpx = 0
bulletpy = 5
bullet_state = "ready" # ready state is bassiclly u cant see the bullet on the screen
# fire -- the bullet is currently moving 
#showing player one on the screen
def player(x_1,y_1):
    screen.blit(imagep,(x_1,y_1))

def fire_bullet(x_3,y_3):
    global bullet_state
    bullet_state = "fire"
    #Adding 16 and 10 respectively to get the bullet above the spaceship 
    screen.blit(imageb,(x_3 + 10 ,y_3 + 10))

#The game loop and used for closing the window
program_run = True
while program_run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_run = False
        
        #Checking for pressing and releasing of keystrokes respectively
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changep = -1 # moving to the left
            if event.key == pygame.K_RIGHT:
                changep = 1  #moving to the right
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    #get the current x cordinate of the spaceship 
                    #and prevents bullets from moving around the screen
                    x_3 = x_1
                    fire_bullet(x_1,y_3)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT : 
                changep = 0 # changing the movement to 0
        

    #RGB -- Red, Green ,BLue
    screen.fill((0,0,0))
    # Background image 
    screen.blit(bg,(0,0))
    # Leading to movement
    x_1 += changep
    if x_1 == 30 :
        x_1 = 30
    elif x_1 >= 770:
        x_1 = 770
    #Enemy movement 
    x_2 += changeex # moving the enemy
    if x_2 == 30 :
        changeex = 1
        y_2 += changeey #lowering the enemy by 0.3
    elif x_2 >= 770:
         changeex = -1
         y_2 += changeey

    #bullet Movement
    #shooting multiple bullets
    if y_3 <= 0 :
        y_3 = 550
        bullet_state = "ready" 
    if bullet_state is "fire":
        fire_bullet(x_3,y_3)
        y_3 -= bulletpy
    
    player(x_1,y_1)
    enemy(x_2,y_2)
    pygame.display.update()


