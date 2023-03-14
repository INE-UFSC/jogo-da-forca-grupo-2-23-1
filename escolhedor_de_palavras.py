import random

palavras = ["framboesa", "patela", "cotovelo", "abacate", "revista", "mercado", "academia", "submarino", "camelo", "sobrinha", "mochila", "mosquito", "caranguejo", "lagarto"]

def escolhe_palavra():
    x = random.choice(palavras)
    return(x)