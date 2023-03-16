letra_jogador = input()
letra_jogada = []

#x é a letra do jogador
#y é a palavra
def corretor(x, y):
    for letra_da_palavra in list(y):
        if x in letra_jogada:
            return False
        elif x==letra_da_palavra:
            return True
        else: 
            return False
    letra_jogada.append(x)
