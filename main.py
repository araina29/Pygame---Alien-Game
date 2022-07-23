import pygame
import random
import math 

#initializing the pygame module
pygame.init()

#creating a screen with values 800 to 600 as the resolution

screen = pygame.display.set_mode((800,600))
score = 0
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

#Enemy
# Adding multiple enemies
imagee = []
x_2 = []
y_2 = []
changeex = []
changeey = []
num_enemy = 6
#Using the for loop to get more values in the lists
for i in range(num_enemy):
    imagee.append(pygame.image.load('alien.png'))
    x_2.append(random.randint(0,800))
    y_2.append(random.randint(50,150))
    changeex.append(1)
    changeey.append(40)


#showing enemy one on the screen
def enemy(x_1,y_1,i):
    screen.blit(imagee[i],(x_1,y_1))

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

#checking  for the collision between the bullet and the spaceship
def check_collision(x_2,y_2,x_3,y_3):
    #calculating the distance between the bullet and the spaceship
    D = math.sqrt(math.pow(x_2 - x_3,2) + math.pow(y_2 - y_3,2))
    if D < 27:
        return True
    else:
        return False



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
    for i in range(num_enemy):
        x_2[i] += changeex[i] # moving the enemy
        if x_2[i] == 30 :
            changeex[i] = 1
            y_2[i] += changeey[i] #lowering the enemy by 0.3
        elif x_2[i] >= 770:
            changeex[i] = -1
            y_2[i] += changeey[i]
        
        #collision 
        collision = check_collision(x_2[i],y_2[i],x_3,y_3)
        if collision :
            #Getting the bullet back 
            y_3 == 550
            bullet_state = "ready"
            score += 1
            #respawning the enemy
            x_2[i] = random.randint(0,750)
            y_2[i] = random.randint(50,150)
        
        enemy(x_2[i],y_2[i],i)

    #bullet Movement
    #shooting multiple bullets
    if y_3 <= 0 :
        y_3 = 550
        bullet_state = "ready" 
    if bullet_state is "fire":
        fire_bullet(x_3,y_3)
        y_3 -= bulletpy

    
        
    player(x_1,y_1)
    
    pygame.display.update()


