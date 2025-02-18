import pygame
import math

# window size
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)

# colour + text colour
WHITE = (255, 255, 255)
text_color = WHITE

# arched text
def draw_arched_text(surface, text, center, radius, start_angle, font, text_color):
    angle_step = math.pi / (len(text) * 1.5) # Adjust spacing

    for i, letter in enumerate(text):
        angle = start_angle + i * angle_step
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        text_surface = font.render(letter, True, text_color)
        surface.blit(text_surface, (x, y))