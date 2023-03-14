import pygame

def desenha_cabeca(screen):
    pygame.draw.circle(surface=screen, color='red', center=(207, 144), radius=20, width=5)
    pygame.display.update()

def desenha_corpo(screen):
    pygame.draw.line(surface=screen, color='red', start_pos=(207, 164), end_pos=(207, 214), width=5)
    pygame.display.update()

def desenha_braco_dir(screen):
    pygame.draw.line(surface=screen, color='red', start_pos=(207, 174), end_pos=(227, 194), width=5)
    pygame.display.update()

def desenha_braco_esq(screen):
    pygame.draw.line(surface=screen, color='red', start_pos=(207, 174), end_pos=(187, 194), width=5)
    pygame.display.update()

def desenha_perna_dir(screen):
    pygame.draw.line(surface=screen, color='red', start_pos=(207, 214), end_pos=(227, 234), width=5)
    pygame.display.update()

def desenha_perna_esq(screen):
    pygame.draw.line(surface=screen, color='red', start_pos=(207, 214), end_pos=(187, 234), width=5)
    pygame.display.update()


STATUS_CORPO = [desenha_cabeca, desenha_corpo, desenha_braco_dir, desenha_braco_esq, desenha_perna_dir, desenha_perna_esq]

def init_pygame():
    pygame.init()

    scrn = pygame.display.set_mode((800, 600))
    scrn.fill('white')

    pygame.display.set_caption('image')
    forca = pygame.image.load("./imagens/forca.png").convert()
    scrn.blit(forca, (100, 100))
    pygame.display.flip()

    desenha_cabeca(scrn)
    desenha_corpo(scrn)
    desenha_braco_dir(scrn)
    desenha_braco_esq(scrn)
    desenha_perna_dir(scrn)
    desenha_perna_esq(scrn)

if __name__ == '__main__':
    init_pygame()

    running  = True
    while running:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False
    pygame.quit()
