import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's Add Sprites!")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sprite dimensions
sprite_width = 50
sprite_height = 50

# Create two rectangles (sprites)
player = pygame.Rect(100, 100, sprite_width, sprite_height)
enemy = pygame.Rect(300, 300, sprite_width, sprite_height)

# Speed
speed = 1

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Fill background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Draw sprites
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    pygame.display.update()

# Quit Pygame nicely
pygame.quit()
