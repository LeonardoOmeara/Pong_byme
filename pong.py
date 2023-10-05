import pygame, sys


#General setup
pygame.init()
clock = pygame.time.Clock()


#Setting up the main window
# screen_width = 1280
# screen_height = 960
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Welcome to Pong!')

#Game objects
#Rectangles -> ball
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

while True:
    #Handling input
    for event in pygame.event.get():
        #this for loop checks the user actions 
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Visuals
    screen.fill(bg_color)  # Limpiar la pantalla con el color de fondo
    pygame.draw.rect(screen, light_grey, player)        
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.rect(screen, light_grey, ball)


    #Updating the window, this allow to see the changes in the screen
    pygame.display.flip()
    #60 fps, how many frames per second you want to 'refresh' the game
    clock.tick(60)




