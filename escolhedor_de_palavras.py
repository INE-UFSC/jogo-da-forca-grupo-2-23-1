import random


# Alterei o nome da variavel da palavra escolhida pra palavra escolhida
def escolhe_palavra():
    palavras = ["framboesa", "patela", "cotovelo", "abacate", "revista", "mercado", "academia", "submarino", "camelo",
                "sobrinha", "mochila", "mosquito", "caranguejo", "lagarto"]
    palavra_escolhida = random.choice(palavras)
    return palavra_escolhida

# So pegar o tamanho da palavra que foi escolhida pra quando for fazer os traços poder usar
def tamanho(palavra_escolhida):
    tamanho_da_palavra = len(palavra_escolhida)
    return tamanho_da_palavra


