from model.historico import Historico
from model.transacao import Saque

class Conta:

    def __init__(self, numero, cliente):
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property    
    def saldo(self):
        return self.__saldo
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def historico(self):
        return self.__historico
    
    def sacar(self, valor):
        if valor > 0.0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0.0:
            self.__saldo += valor
            return True
        return False
    
    def transferir(self, valor, contaDestino):
        if self.sacar(valor) and contaDestino.depositar(valor):
            return True
        return False
    
    def __str__(self):
        return f"Agência:\t{self.agencia}\nTitular:\t{self.cliente.nome}\n"   


class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite_especial=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.__limite_especial = limite_especial
        self.__limite_saques = limite_saques
        self.__saldo += self.limite_especial

    @property
    def limite_especial(self):
        return self.__limite_especial
    
    @property
    def limite_saques(self):
        return self.__limite_saques
    
    def sacar(self, valor):
        numero_de_saques = len([transacao for transacao in self.historico.transacoes if isinstance(transacao, Saque)])
        if numero_de_saques >= self.limite_saques or valor > self.saldo:
            return False
        return super().sacar(valor)    
    
    def __str__(self):
        return super().__str__() + f"Conta Corrente: {self.numero}"  


class ContaPoupanca(Conta):
    
    def __init__(self, numero, cliente, taxa_rendimento=0.005):
        super().__init__(numero, cliente)
        self.__taxa_rendimento = taxa_rendimento  # Taxa de rendimento padrão de 0,5%
    
    def aplicar_rendimento(self):
        """
        Aplica o rendimento mensal com base na taxa de rendimento sobre o saldo.
        """
        rendimento = self.saldo * self.__taxa_rendimento
        self.depositar(rendimento)
        return rendimento

    @property
    def taxa_rendimento(self):
        return self.__taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, nova_taxa):
        if nova_taxa > 0:
            self.__taxa_rendimento = nova_taxa

    def __str__(self):
        return super().__str__() + f"Conta Poupança: {self.numero}"
