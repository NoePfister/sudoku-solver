import pygame
import sys

pygame.init()

# Setting up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Window Example')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Filling the screen with a color (optional)
    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()