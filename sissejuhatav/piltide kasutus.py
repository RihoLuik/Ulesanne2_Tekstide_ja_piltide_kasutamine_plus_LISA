import pygame
pygame.init()

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#Lisame pildid
bg = pygame.image.load("images/bg.jpg")
screen.blit(bg,[0,0])

youWin = pygame.image.load("images/youwin.png")
youWin = pygame.transform.scale(youWin, [300, 120])
screen.blit(youWin,[180,100])

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False