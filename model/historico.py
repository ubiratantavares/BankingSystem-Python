
class Historico:
    def __init__(self):
        self.__transacoes = []

    @property
    def transacoes(self):
        return self.__transacoes    

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
