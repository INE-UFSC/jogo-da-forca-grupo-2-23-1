import pygame

from corretor import *
from escolhedor_de_palavras import *
from fimdejogo import *
from imprimir import *


def letras_erradas(scrn, letra_errada):
    string_letras = '　'*(ord(letra_errada) - ord('a')) \
        + letra_errada + '　'*(ord('z') - ord(letra_errada))

    font = pygame.font.Font(None, 42)
    text = font.render(string_letras, True, (255, 255, 255))
    scrn.blit(text, (50, 50))
    pygame.display.update()


def tracos_palavra(palavra, scrn):
    n = len(palavra)
    cor = (255, 255, 255)
    if n == 4:
        pos, posf = 100, 200
        for _ in range(4):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, cor, start_pos, end_pos, 10)
            pygame.display.update()
            pos += 125
            posf += 125
    elif n == 5:
        pos, posf = 100, 200
        for _ in range(5):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, cor, start_pos, end_pos, 10)
            pygame.display.update()
            pos += 125
            posf += 125
    elif n == 6:
        pos, posf = 25, 125
        for _ in range(6):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, cor, start_pos, end_pos, 10)
            pygame.display.update()
            pos += 125
            posf += 125
    elif n == 7:
        pos, posf = 50, 125
        for _ in range(7):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, cor, start_pos, end_pos, 10)
            pygame.display.update()
            pos += 100
            posf += 100
    elif n == 8:
        pos, posf = 15, 90
        for _ in range(8):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, cor, start_pos, end_pos, 10)
            pygame.display.update()
            pos += 100
            posf += 100
    elif n == 9:
        pos, posf = 50, 105
        for _ in range(9):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, cor, start_pos, end_pos, 10)
            pygame.display.update()
            pos += 80
            posf += 80
    elif n == 10:
        pos, posf = 8, 73
        for _ in range(10):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, cor, start_pos, end_pos, 10)
            pygame.display.update()
            pos += 80
            posf += 80

def imprimir_letras(palavra_escolhida, letra, check_palavra, scrn):
    n = len(palavra_escolhida)

    font = pygame.font.Font(None, 80)
    cor = (255, 255, 255)
    if letra in palavra_escolhida:
        for j in range(n):
            if letra == palavra_escolhida[j]:
                check_palavra[j] = letra
    if n == 4:
        la, la1 = 130,440
        for i in range(n):
            text = font.render(check_palavra[i], True, cor)
            scrn.blit(text, (la, la1))
            la += 127
            pygame.display.update()
    if n == 5:
        la, la1 = 130,440
        for i in range(n):
            text = font.render(check_palavra[i], True, cor)
            scrn.blit(text, (la, la1))
            la += 127
            pygame.display.update()
    if n == 6:
        la, la1 = 55,440
        for i in range(n):
            text = font.render(check_palavra[i], True, cor)
            scrn.blit(text, (la, la1))
            la += 125
            pygame.display.update()
    if n == 7:
        la, la1 = 65,440
        for i in range(n):
            text = font.render(check_palavra[i], True,cor)
            scrn.blit(text, (la, la1))
            la += 101
            pygame.display.update()
    if n == 8:
        la, la1 = 35,440
        for i in range(n):
            text = font.render(check_palavra[i], True, cor)
            scrn.blit(text, (la, la1))
            la += 100
            pygame.display.update()
    
    if n == 9:
        la, la1 = 55,440
        for i in range(n):
            text = font.render(check_palavra[i], True, cor)
            scrn.blit(text, (la, la1))
            la += 81
            pygame.display.update()
    
    elif n== 10: 
        la, la1 = 20,440
        for i in range(n):
            text = font.render(check_palavra[i], True, cor)
            scrn.blit(text, (la, la1))
            la += 80
            pygame.display.update()

    return check_palavra
