# Desenvolva sua classe Recipiente aqui.

class Recipente:

    def __init__(self, tamanho: float):
        if tamanho < 0:
            self.tamanho = 0
        else:
            self.tamanho = tamanho
        self.conteudo = 0
        self.limpo = True

    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        else:
            return False

    def lavar(self):
        self.esvaziar()
        self.limpo = True

    def esta_limpo(self):
        if self.limpo == True:
            return True
        else: 
            return False

    def estado(self):
        if self.limpo == True:
            return 'limpo'
        else:
            return 'sujo'

    def sujar(self):
        self.limpo = False

    def __repr__(self):
        return f'Um recipiente {self.estado()} não especificado'

    def __str__(self):
        return f'Um recipiente {self.estado()} não especificado'
