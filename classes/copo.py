# Desenvolva sua classe Copo aqui.

from classes import Recipiente

class Copo(Recipiente):
    
    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True):
        super().__init__(tamanho, conteudo=conteudo, limpo=limpo)

    def encher(self, bebida = 'água'):
        if self.limpo:
            self.sujar()
            self.conteudo += self.tamanho
            self.bebida = bebida            
        else:
            return 'Não se pode encher um copo sujo'

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
        if self.esta_vazio():
            return f'Um copo vazio de {float(self.tamanho)}ml'
        else:
            return f'Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}'

    def __str__(self):
        if self.conteudo == 0:
            return f'Um copo vazio de {float(self.tamanho)}ml'
        else:
            return f'Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}'         