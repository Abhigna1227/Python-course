import pygame

# Initialize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialise display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

# Load and scale images correctly
background_image = pygame.transform.scale(pygame.image.load('Background image.jpg').convert(),(SCREEN_WIDTH, SCREEN_HEIGHT))
Image_for_code = pygame.transform.scale(
    pygame.image.load('Image for code.png').convert_alpha(), 
    (200, 200))
Image_for_code_rect = Image_for_code.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))
# Create text
text = pygame.font.Font(None, 36).render('Hello World', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
# Game loop function
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(Image_for_code, Image_for_code_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Run the game
if __name__ == '__main__':
    game_loop()
