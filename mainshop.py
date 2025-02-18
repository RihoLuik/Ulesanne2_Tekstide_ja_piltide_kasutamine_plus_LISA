import pygame
from utils import screen, screen_size, text_color

# Initialize pygame
pygame.init()

# Load images
bg_shop = pygame.image.load("images/main/bg_shop.jpg") # Background image
seller = pygame.image.load("images/main/seller.png") # Seller character
chat_box = pygame.image.load("images/main/chat.png") # Chat box

# Window name
pygame.display.set_caption("Ülesanne 2 - Shop Scenario - R.Luik")

# Image scaling
bg_shop = pygame.transform.scale(bg_shop, screen_size)
seller = pygame.transform.scale(seller, (225, 300))
chat_box = pygame.transform.scale(chat_box, (300, 225))

font = pygame.font.Font(None, 30)
chat_text = "Tere, mina olen Riho Luik,\nkuidas saan täna abiks olla?" # Use \n but handle manually
chat_lines = chat_text.split("\n") # Split text into a list of lines

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw images
    screen.blit(bg_shop, (0, 0)) # Background covers the entire window
    screen.blit(seller, (75, 125)) # Position seller on the left
    screen.blit(chat_box, (210, 20)) # Place chat box on the right

    # Render and display each line separately
    start_y = 62.5 # Y position for the first line
    line_spacing = 30 # Space between lines

    for i, line in enumerate(chat_lines):
        text_surface = font.render(line, True, text_color)
        screen.blit(text_surface, (225, start_y + i * line_spacing)) # Move each line down

    pygame.display.flip()

pygame.quit()