import pygame

from corpo import Corpo
from corretor import *
from escolhedor_de_palavras import *
from fimdejogo import *
from imprimir import *


class ForcaJogo:
    def __init__(self, tela):
        self.palavra_escolhida = escolhe_palavra()
        self.erros = 0
        self.letra_jogada = set()
        self.check_palavra = [" "] * len(self.palavra_escolhida)
        self.max_erros = 6
        self.corpo = Corpo(tela)

        tracos_palavra(self.palavra_escolhida, tela)

    def joga_letra(self, letra, tela):
        letra_correta = corretor_palavra(letra, self.palavra_escolhida)

        if not letra_correta and letra not in self.letra_jogada:
            self.erros += 1

            if self.erros > self.max_erros:
                gameover(tela)

            self.corpo.adiciona_parte()
            letras_erradas(tela, letra)
        else:
            imprimir_letras(self.palavra_escolhida, letra, self.check_palavra, tela)

            if not " " in self.check_palavra:
                parabens(tela)

        self.letra_jogada.add(letra)

def init_pygame():
    pygame.init()

    scrn = pygame.display.set_mode((800, 600))
    scrn.fill('#0D5C33')

    pygame.display.set_caption('image')
    forca = pygame.image.load("./imagens/forca.png").convert()
    scrn.blit(forca, (100, 100))
    pygame.display.flip()

    return scrn

def main():
    tela = init_pygame()

    jogo = ForcaJogo(tela)

    running  = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                letra = chr(event.key).lower()

                if ord(letra) < ord('a') or ord(letra) > ord('z'):
                    continue

                jogo.joga_letra(letra, tela)

    pygame.quit()

if __name__ == '__main__':
    main()
