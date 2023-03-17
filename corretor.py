import pygame
import corretor
import imprimir
import escolhedor_de_palavras
def chute_jogador():
    letra_jogador = input("Fale uma letra: ")
    jogada = letra_jogador.strip().upper()
    return jogada

# x é a letra do jogador
# y é a palavra
def corretor_palavra(x, y, letra_jogada):
    for letra_da_palavra in list(y):
        #if x in letra_jogada:
        #    return False
        if x == letra_da_palavra:
            return True

    return False