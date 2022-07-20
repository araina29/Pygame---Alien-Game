import pygame

#initializing the pygame module
pygame.init()

#creating a screen with values 800 to 600 as the resolution

screen = pygame.display.set_mode((800,600))

#Setting the title
pygame.display.set_caption("Space Invaders")

#Adding an image on the screen 
image = pygame.image.load('image.png')
#X and Y coordinates for player 1 
x_1 = 400 
y_1 = 550
change_player = 0
#showing player one on the screen
def player(x_1,y_1):
    screen.blit(image,(x_1,y_1))


#The game loop and used for closing the window
program_run = True
while program_run:
    change_player = 0.1
    x_1 += change_player
    y_1 -= change_player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_run = False
    #RGB -- Red, Green ,BLue
    screen.fill((0,0,0))
    player(x_1,y_1)
    pygame.display.update()


