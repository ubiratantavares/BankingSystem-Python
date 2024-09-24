from datetime import datetime

class Transacao:

    def __init__(self, valor, conta):
        self.__valor = valor
        self.__tipo = self.__class__.__name__
        self.__data = datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        self.__conta = conta

    @property
    def valor(self):
        return self.__valor
    
    @property
    def tipo(self):
        return self.__tipo    
    
    @property
    def data(self):
        return self.__data
    
    @property
    def conta(self):
        return self.__conta
    
    def registrar(self):
        pass

class Deposito(Transacao):

    def __init__(self, valor, conta):
        super().__init__(valor, conta)

    def registrar(self):
        if self.conta.depositar(self.valor):
            self.conta.historico.adicionar_transacao(self)

class Saque(Transacao):

    def __init__(self, valor, conta):
        super().__init__(valor, conta)

    def registrar(self):
        if self.conta.sacar(self.valor):
            self.conta.historico.adicionar_transacao(self)

class Transferencia(Transacao):

    def __init__(self, valor, conta, conta_destino):
        super().__init__(valor, conta)
        self.__conta_destino = conta_destino

    @property
    def conta_destino(self):
        return self.__conta_destino      

    def registrar(self):
        if self.conta.transferir(self.valor, self.conta_destino):
            self.conta.historico.adicionar_transacao(self)
            self.conta_destino.historico.adicionar_transacao(self)
