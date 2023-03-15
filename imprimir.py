import random

palavras = ["framboesa", "patela", "cotovelo", "abacate", "revista", "mercado", "academia", "submarino", "camelo", "sobrinha", "mochila", "mosquito", "caranguejo", "lagarto"]

def escolhe_palavra():
    x = random.choice(palavras)
    return(x)

def tracos_palavra():
    
    palavra = list(escolhe_palavra())
    n = len(palavra)
    black = (0, 0,0)
    if n == 4:
        pos, posf = 100, 200
        for _ in range(4):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, black, start_pos, end_pos, 10)
            pos += 125
            posf += 125
    elif n == 5:
        pos, posf = 100, 200
        for _ in range(5):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, black, start_pos, end_pos, 10)
            pos += 125
            posf += 125
    elif n == 6:
        pos, posf = 25, 125
        for _ in range(6):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, black, start_pos, end_pos, 10)
            pos += 125
            posf += 125
    elif n == 7:
        pos, posf = 50, 125
        for _ in range(7):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, black, start_pos, end_pos, 10)
            pos += 100
            posf += 100
    elif n == 8:
        pos, posf = 15, 90
        for _ in range(8):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, black, start_pos, end_pos, 10)
            pos += 100
            posf += 100
    elif n == 9:
        pos, posf = 50, 105
        for _ in range(9):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, black, start_pos, end_pos, 10)
            pos += 80
            posf += 80
    elif n == 10:
        pos, posf = 8, 73
        for _ in range(10):
            start_pos = (pos, 500)
            end_pos = (posf,500)
            pygame.draw.line(scrn, black, start_pos, end_pos, 10)
            pos += 80
            posf += 80

def imprimir_letras():
    
    palavra = list(escolhe_palavra())
    n = len(palavra)
    font = pygame.font.Font(None, 80)
    black = (0, 0,0)
    if n == 4:
        la, la1 = 130,450
        for i in range(n):
            text = font.render(palavra[i], True, (0,0,0))
            scrn.blit(text, (la, la1))
            la += 127
    if n == 5:
        la, la1 = 130,450
        for i in range(n):
            text = font.render(palavra[i], True, (0,0,0))
            scrn.blit(text, (la, la1))
            la += 127
    if n == 6:
        la, la1 = 55,450
        for i in range(n):
            text = font.render(palavra[i], True, (0,0,0))
            scrn.blit(text, (la, la1))
            la += 125
    if n == 7:
        la, la1 = 65,450
        for i in range(n):
            text = font.render(palavra[i], True, (0,0,0))
            scrn.blit(text, (la, la1))
            la += 101
    if n == 8:
        
    elif n== 10: 
        la, la1 = 20,450
        for i in range(n):
            text = font.render(palavra[i], True, (0,0,0))
            scrn.blit(text, (la, la1))
            la += 80

# black = (0,0,0)
#    pos, posf = 50, 125
#    for _ in range(7):
#        start_pos = (pos, 500)
#        end_pos = (posf,500)
#        pygame.draw.line(scrn, black, start_pos, end_pos, 10)
#        pos += 100
#        posf += 100
#    palavra = list("MASASAS")
#    n = len(palavra)
#    black = (0, 0,0)
#    font = pygame.font.Font(None, 80)
#    la, la1 = 65,450
#    for i in range(n):
#        text = font.render(palavra[i], True, (0,0,0))
#        scrn.blit(text, (la, la1))
#        la += 101

tracos_palavra()