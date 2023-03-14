letra_jogador = input()

#x é a letra do jogador
#y é a palavra
def corretor(x, y):
    for letra_da_palavra in list(y):
        if x==letra_da_palavra:
            return True
            break
        else: 
            return False
