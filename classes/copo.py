# Desenvolva sua classe Copo aqui.

from classes import Recipente

class Copo(Recipente):
    
    def __init__(self, tamanho: float):
        super().__init__(tamanho)

    def encher(self, bebida = 'água'):
        if self.limpo == False:
            return 'Não se pode encher um copo sujo'
        else:
            self.sujar()
            self.conteudo += self.tamanho
            self.bebida = bebida

    def beber(self, quantidade: float):
        if quantidade < 0:
            return 'Quantidade deve ser positiva'
        elif quantidade > self.conteudo:
            return 'Não há bebida suficiente no copo'
        else:
            self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True

    def __repr__(self):
        if self.esta_vazio:
            return f'Um copo vazio de {self.tamanho}ml'
        else:
            return f'Um copo de tamanho {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}'

    def __str__(self):
        if self.conteudo == 0:
            return f'Um copo vazio de {self.tamanho}ml'
        else:
            return f'Um copo de tamanho {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}'         