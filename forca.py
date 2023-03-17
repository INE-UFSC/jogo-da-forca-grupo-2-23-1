import pygame
from corretor import *
from imprimir import *
from escolhedor_de_palavras import *
from fimdejogo import *

class ForcaJogo:
    def __init__(self):
        self.palavra_escolhida = escolhe_palavra()
        self.erros = 0
        self.letra_jogada = []
        self.letra_errada = []
        self.check_palavra = [" "] * len(self.palavra_escolhida)

#erros = 0 #Coloquei o "erros" nesse arquivo e no arquivo do corretor, quando for montar tem que tirar um deles
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
    gameover(screen)


escolhe_palavra()
STATUS_CORPO = [desenha_cabeca, desenha_corpo, desenha_braco_dir, desenha_braco_esq, desenha_perna_dir, desenha_perna_esq]

def init_pygame():
    pygame.init()

    scrn = pygame.display.set_mode((800, 600))
    scrn.fill('white')

    pygame.display.set_caption('image')
    forca = pygame.image.load("./imagens/forca.png").convert()
    scrn.blit(forca, (100, 100))
    pygame.display.flip()

    return scrn

def forca_jogar():

    scrn = init_pygame()

    jogo = ForcaJogo()
    tracos_palavra(jogo.palavra_escolhida, scrn)
    parte_atual = iter(STATUS_CORPO)


    running  = True
    while running:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False
            if event.type == pygame.KEYDOWN:
                letra = chr(event.key)

                resultado = corretor_palavra(letra, jogo.palavra_escolhida, jogo.letra_jogada)
                print(letra, jogo.palavra_escolhida, jogo.letra_jogada, resultado)
                jogo.letra_jogada.append(letra)

                if not resultado:
                    jogo.letra_errada.append(letra)
                    jogo.erros += 1
                    parte_desenho = next(parte_atual)
                    parte_desenho(scrn)

                    if letra not in jogo.letra_jogada:
                        letras_erradas(scrn, letra)
                else:
                    imprimir_letras(jogo.palavra_escolhida, letra, jogo.check_palavra, scrn)

                    if not " " in jogo.check_palavra:
                        parabens(scrn)

    pygame.quit()

if __name__ == '__main__':
    forca_jogar()