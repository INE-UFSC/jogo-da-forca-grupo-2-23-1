import pygame


class Corpo:
    PARTES_CORPO = [
        'cabeça', 'corpo', 'braço-esquerdo', 'braço-direito',
        'perna-esquerda', 'perna-direita'
    ]

    def __init__(self, tela_desenho, max_erros=6):
        self.tela = tela_desenho
        self.partes_usadas = iter(self.PARTES_CORPO[:max_erros])

    def adiciona_parte(self):
        parte = next(self.partes_usadas)

        img = pygame.image.load(f'./imagens/{parte}.png').convert().convert_alpha()
        img_rect = img.get_rect(center = (260, 278))

        self.tela.blit(img, img_rect)
        pygame.display.flip()
