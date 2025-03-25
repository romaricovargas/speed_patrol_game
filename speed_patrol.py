
import pygame

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Speed Patrol")

#Main game loop
running = True
while running:
    #Check to see if the user want to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#End the game
pygame.quit()






