import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player settings
player = pygame.Rect(375, 275, 50, 50)
player_speed = 5

# Enemy settings
enemies = []
for _ in range(7):
    x = random.randint(0, WIDTH - 50)
    y = random.randint(0, HEIGHT - 50)
    enemies.append(pygame.Rect(x, y, 50, 50))

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw and check enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
        if player.colliderect(enemy):
            score += 1
            # Reposition enemy randomly
            enemy.x = random.randint(0, WIDTH - 50)
            enemy.y = random.randint(0, HEIGHT - 50)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
