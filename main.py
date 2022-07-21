import pygame

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
x_2 = 400 
y_2 = 100
changee = 0
#showing enemy one on the screen
def enemy(x_1,y_1):
    screen.blit(imagee,(x_1,y_1))


#The game loop and used for closing the window
program_run = True
while program_run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_run = False
        
        #Checking for pressing and releasing of keystrokes respectively
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changep = -0.3 # moving to the left
            if event.key == pygame.K_RIGHT:
                changep = 0.3  #moving to the right
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT: 
                changep = 0 # changing the movement to 0

    #RGB -- Red, Green ,BLue
    screen.fill((0,0,0))
    # Leading to movement
    x_1 += changep
    if x_1 == 30 :
        x_1 = 30
    elif x_1 >= 770:
        x_1 = 770

    player(x_1,y_1)
    enemy(x_2,y_2)
    pygame.display.update()


