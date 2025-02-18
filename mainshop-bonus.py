import pygame
from utils import screen, screen_size, text_color, WHITE, draw_arched_text
import math

# Initialize pygame
pygame.init()

# Load images
bg_shop = pygame.image.load("images/main/bg_shop.jpg") # Background image
seller = pygame.image.load("images/main/seller.png") # Seller character
chat_box = pygame.image.load("images/main/chat.png") # Chat box
vikk100 = pygame.image.load("images/extra/VIKK_logo.png") # VIKK logo
sword = pygame.image.load("images/extra/Mõõk.png") # the oh so grand sword ✨
cake = pygame.image.load("images/extra/cake.png") # the cake, it ain't a celebration without cake... I think that's what they say? 🤔

# Window name
pygame.display.set_caption("Ülesanne 2 - BONUS Shop Scenario - R.Luik")

# Image scaling
bg_shop = pygame.transform.scale(bg_shop, screen_size)
seller = pygame.transform.scale(seller, (225, 300))
chat_box = pygame.transform.scale(chat_box, (330, 225))
vikk100 = pygame.transform.scale(vikk100, (355, 55))
sword = pygame.transform.scale(sword, (165, 165))
cake = pygame.transform.scale(cake, (155, 120))

# Sword rotation
sword = pygame.transform.rotate(sword, 135) # Rotate 45 degrees

# Text stuff
font = pygame.font.Font(None, 30)
font_arch = pygame.font.Font(None, 35)
chat_text = "Got some RARE things on sale,\nstranger!\nWhat're ya buyin'?" # Use \n but handle manually
chat_lines = chat_text.split("\n") # Split text into a list of lines
# for the text, I'm referencing the lines from the merchant in Capcom's Resident Evil 4 (2005) game
# you can find the video with the lines here: https://youtu.be/axZ-SZJhN60?si=XBg9I7gIAvbZKZfc
# or here on the fandom page: https://residentevil.fandom.com/wiki/Merchant/quotes

# the bread and butter of the code (a.k.a the main stuff that makes it actually show up 😊)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw images
    screen.blit(bg_shop, (0, 0)) # Background covers the entire window
    screen.blit(seller, (75, 125)) # Postion seller in front of the counter
    screen.blit(cake, (325, 175)) # Position cake to be on the counter AND underneath the chat box
    screen.blit(chat_box, (210, 20)) # Position the chat box to be near the sellers mouth, so it would seem like he's talking
    screen.blit(vikk100, (0, 425)) # Position the logo to be in the bottom left corner of the screen
    screen.blit(sword, (475, 90)) # Position the sword to be hung on the right side of the wall


    # Draw arched text above the logo
    draw_arched_text(screen, "TULEVIK", (295, 430), 90, -math.pi / 2, font_arch, WHITE)
    draw_arched_text(screen, "2050", (295, 460), 65, -math.pi / 2, font_arch, WHITE)

    # Render and display each line separately
    start_y = 62.5 # Y position for the first line
    line_spacing = 30 # Space between lines

    for i, line in enumerate(chat_lines):
        text_surface = font.render(line, True, text_color)
        screen.blit(text_surface, (225, start_y + i * line_spacing)) # Move each line down

    pygame.display.flip()

pygame.quit()