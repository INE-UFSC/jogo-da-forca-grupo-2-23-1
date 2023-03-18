# x é a letra do jogador
# y é a palavra

def corretor_palavra(x, y):
    for letra_da_palavra in list(y):
        #if x in letra_jogada:
        #    return False
        if x == letra_da_palavra:
            return True

    return False
