import pygame
from forca import forca_jogar

def gameover(scrn):
    font = pygame.font.Font(None, 120)
    scrn.fill('white')
    black = (0,0,0)
    text = font.render("GAME OVER", True, black)
    scrn.blit(text, (800/4, 600/4))
    pygame.display.update()
    running  = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def parabens(scrn):
    font = pygame.font.Font(None, 120)
    scrn.fill('white')
    black = (0,0,0)
    text = font.render("PARABENS", True, black)
    scrn.blit(text, (800/4, 600/4))
    pygame.display.update()
    running  = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False