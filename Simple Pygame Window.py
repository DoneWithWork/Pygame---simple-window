# Importing the Pygame and sys module
import pygame
import sys


# Initialize all imported pygame modules
pygame.init()

# Assigning width and height to variables 
width = 600
height = 700

# Using RGB values to get the colour white
white  = (250,250,250)

# Setting up window 
screen = pygame.display.set_mode((width,height))

# Setting title of window
pygame.display.set_caption("Pygame window")

# Getting the framerate 
clock = pygame.time.Clock()

# Fill screen with the colour white
screen.fill(white)

# Updating the display
pygame.display.flip()

# Setting run as True
run = True

# While run is True, programme will still run
while run:
    for event in pygame.event.get(): # Getting all user inputs
        if event.type == pygame.QUIT: # If the user clicks the X button to exit the window
            run = False # Run is set to False, which ends the while loop
            pygame.quit() # Deactivates Pygame libraries and closes window
            sys.exit() # Stops programme from running

    # Setting framerate to 120 frames per second. 
    clock.tick(120)
    
