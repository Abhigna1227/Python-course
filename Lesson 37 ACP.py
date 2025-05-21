import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event: Color Change Time!")

colors = [pygame.Color("red"), pygame.Color("green"), pygame.Color("blue"), pygame.Color("yellow")]

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        self.color = random.choice(colors)
        self.image.fill(self.color)

sprite1 = ColorSprite(150, 200, random.choice(colors))
sprite2 = ColorSprite(450, 200, random.choice(colors))

all_sprites = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
