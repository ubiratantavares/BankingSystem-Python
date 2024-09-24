# Classe Cliente com endereço e contas
from model.transacao import Transacao
from model.conta import Conta

class Cliente:

    def __init__(self, endereco, nome):
        self.__endereco = endereco
        self.__nome = nome
        self.__contas = []

    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def contas(self):
        return self.__contas    

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self, endereco, nome, cpf, data_nascimento):
        super().__init__(endereco, nome)
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento

class PessoaJuridica(Cliente):

    def __init__(self, endereco, nome, cnpj, data_abertura):
        super().__init__(endereco, nome)
        self.__cnpj = cnpj
        self.__data_abertura = data_abertura

    @property
    def cnpj(self):
        return self.__cnpj
    
    @property
    def data_abertura(self):
        return self.__data_abertura
    
    

