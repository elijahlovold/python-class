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
pygame.display.set_caption("Moving Cube")

def check_x_direction() -> bool: 
    """Return true if moving in the x."""
    return direction[X_COORD_I] != 0

def spawn_fruit() -> tuple:
    x = int(random.randint(0, WIDTH)/CUBE_SIZE)*CUBE_SIZE
    y = int(random.randint(0, HEIGHT)/CUBE_SIZE)*CUBE_SIZE

    return (x, y)

direction = [0, CUBE_SIZE]

X_COORD_I = 0
Y_COORD_I = 1
snake_body = [(50, 50), (75, 50), (100, 50), (125, 50), (150, 50)]

fruit_life = 0
fruit = spawn_fruit()

score = 0

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
    if check_x_direction(): 
        if keys[pygame.K_UP]:
            direction[X_COORD_I] = 0
            direction[Y_COORD_I] = -CUBE_SIZE

        if keys[pygame.K_DOWN]:
            direction[X_COORD_I] = 0
            direction[Y_COORD_I] = CUBE_SIZE
    else: 
        if keys[pygame.K_RIGHT]:
            direction[Y_COORD_I] = 0
            direction[X_COORD_I] = CUBE_SIZE
        if keys[pygame.K_LEFT]:
            direction[Y_COORD_I] = 0
            direction[X_COORD_I] = -CUBE_SIZE

    # check if fruit life has expired
    fruit_life += 1
    if fruit_life >= 20: 
        fruit = spawn_fruit()
        fruit_life = 0

    # caculate new head position
    current_x = snake_body[0][X_COORD_I]
    current_y = snake_body[0][Y_COORD_I]

    dx = direction[X_COORD_I]
    dy = direction[Y_COORD_I]

    # make the head segment at the current + whatever direction
    new_segment = (current_x + dx, current_y + dy)
        
    # check collision body
    # note, don't check the last element as it will be moving 
    for i in range(0, len(snake_body)-1): 
        if new_segment == snake_body[i]: 
            print("you die")
            running = False

    # check collision walls
    x = new_segment[X_COORD_I]
    if x >= WIDTH or x < 0: 
        print("you die")
        running = False
    y = new_segment[Y_COORD_I]
    if y >= HEIGHT or y < 0: 
        print("you die")
        running = False

    # add the new head
    snake_body.insert(0, new_segment)

    # check collision fruit
    if new_segment == fruit: 
        score += 1
        print(f"Your score is: {score}")
        fruit = spawn_fruit()
        fruit_life = 0
    else: 
        # if we eat a fruit, don't remove tail
        snake_body.pop()

    # set the background
    screen.fill(WHITE)

    # iterate through body segments and draw
    for segment in snake_body: 
        x = segment[X_COORD_I]
        y = segment[Y_COORD_I]
        pygame.draw.rect(screen, BLUE, (x, y, CUBE_SIZE, CUBE_SIZE))

    # draw the fruit
    x = fruit[X_COORD_I]
    y = fruit[Y_COORD_I]
    pygame.draw.rect(screen, RED, (x, y, CUBE_SIZE, CUBE_SIZE))

    pygame.display.update()

pygame.quit()
