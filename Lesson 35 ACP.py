import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My ACP PROJECT")

BLACK = (0, 0, 0)
LILAC = (200, 162, 200)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

rect_width = 100
rect_height = 60
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

font = pygame.font.SysFont("Comic Sans MS", 40)
text = font.render("Hello, I am a rectangle!", True, WHITE)

color_changer = pygame.Rect(50, 400, 80, 40)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.draw.rect(screen, LILAC, rectangle)
    pygame.draw.circle(screen, ORANGE, (100, 100), 40)

    random_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    pygame.draw.rect(screen, random_color, color_changer)

    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
