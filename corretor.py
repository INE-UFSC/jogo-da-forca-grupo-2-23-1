def chute_jogador():
    letra_jogador = input("Fale uma letra: ")
    jogada = letra_jogador.strip().upper()
    return jogada
letra_jogada = []
# Coloquei o "erros" nesse arquivo e no arquivo da forca, quando for montar tem que tirar um deles
# x é a letra do jogador
# y é a palavra
def corretor(x, y):
    for letra_da_palavra in list(y):
        if x in letra_jogada:
            return False
        elif x == letra_da_palavra:
            return True
        else:
            erros += 1
            return False
    letra_jogada.append(x)
