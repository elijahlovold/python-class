
import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH = 500
HEIGHT = 500
CUBE_SIZE = 25

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Setup window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Load image (make sure 'sprite.png' exists in the same directory)
sprite_image = pygame.image.load('sprites/mine.jpeg')

# Get the rect for positioning and collision detection
sprite_rect = sprite_image.get_rect()

# Initial position of the sprite
sprite_rect.topleft = (WIDTH // 2, HEIGHT // 2)

# Main loop
running = True
while running:
    pygame.time.delay(500)  # Control frame rate

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # change direction with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass

    # set the background
    screen.fill(WHITE)

   # Draw the sprite at its new position
    screen.blit(sprite_image, sprite_rect)

    pygame.display.update()

pygame.quit()
