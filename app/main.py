import textwrap

from model.transacao import *
from model.cliente import *

def menu():
    menu = """\n
    ===================== MENU =====================
    [ d]\tDepositar
    [ s]\tSacar
    [ t]\tTransferir
    [ e]\tExtrato
    [nc]\tNova Conta
    [nu]\tNovo Cliente
    [ q]\tSair
    ==> """
    opcao = input(textwrap.dedent(menu))
    while opcao not in ["d", "s", "t", "e", "nc", "nu", "q"]:
        opcao = input(textwrap.dedent(menu))
    return opcao

def menu_cliente():
    menu = """\n
    ===================== MENU =====================
    [pf]\tPessoa Física
    [pj]\tPessoa Jurídica
    [ r]\tRetornar ao menu principal
    ==> """
    opcao = input(textwrap.dedent(menu))
    while opcao not in ["pf", "pj", "r"]:
        opcao = input(textwrap.dedent(menu))
    return opcao

def depositar(clientes):
    while True:
        opcao = menu_cliente()
        if opcao == "r":
            break
        else:
            executar_cliente_depositar(opcao, clientes)

def sacar(clientes):
    while True:
        opcao = menu_cliente()
        if opcao == "r":
            break
        else:
            executar_cliente_sacar(opcao, clientes)

def transferir(clientes):
    while True:
        opcao = menu_cliente()
        if opcao == "r":
            break
        else:
            executar_cliente_transferir(opcao, clientes)

def filtrar_cliente(opcao, identificador, clientes):
    if opcao == "pf":
        clientes_pf = [cliente for cliente in clientes if isinstance(cliente, PessoaFisica)]
        for cliente_pf in clientes_pf:
            if cliente_pf.cpf == identificador:
                return cliente_pf
        return None
    else:
        clientes_pj = [cliente for cliente in clientes if isinstance(cliente, PessoaJuridica)]
        for cliente_pj in clientes_pj:
            if cliente_pj.cnpj == identificador:
                return cliente_pj
        return None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui contas")
    return cliente.conta[0]

def ler_identificador(mensagem):
    return input(mensagem)

def ler_valor(mensagem):
    return float(input(mensagem))

def imprimir(mensagem):
    print(mensagem)

def executar_cliente_depositar(opcao, clientes):
    if opcao == "pf":
        identificador = ler_identificador("Informe o CPF do cliente: ")
    else:
        identificador = ler_identificador("Informe o CNPJ do cliente: ")

    cliente  = filtrar_cliente(opcao, identificador, clientes)
    
    if not cliente:
        imprimir("Cliente não encontrado")
        return None
    
    valor = ler_valor("Informe o valor do depósito: ")
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    
    if not conta:
        return None
    cliente.realizar_transacao(conta, transacao)


def executar_cliente_sacar(opcao, clientes):
    if opcao == "pf":
        identificador = ler_identificador("Informe o CPF do cliente: ")
    else:
        identificador = ler_identificador("Informe o CNPJ do cliente: ")

    cliente  = filtrar_cliente(opcao, identificador, clientes)
    
    if not cliente:
        imprimir("Cliente não encontrado.")
        return None
    
    valor = ler_valor("Informe o valor do saque: ")
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    
    if not conta:
        return None
    cliente.realizar_transacao(conta, transacao)

def executar_cliente_transferir(opcao, clientes):
    if opcao == "pf":
        identificador = ler_identificador("Informe o CPF do cliente: ")
    else:
        identificador = ler_identificador("Informe o CNPJ do cliente: ")

    cliente_origem = filtrar_cliente(opcao, identificador, clientes)

    if not cliente_origem:
        imprimir("Cliente não encontrado.")
        return None
    
    conta_origem = recuperar_conta_cliente(cliente_origem)

    if not conta_origem:
        return None

    imprimir("Selecione o tipl de cliente para realizar a transferência")    
    opcao = menu_cliente()

    if opcao == "pf":
        identificador = ler_identificador("Informe o CPF do cliente: ")
    else:
        identificador = ler_identificador("Informe o CNPJ do cliente: ")
    
    cliente_destino = filtrar_cliente(opcao, identificador, clientes)

    if not cliente_destino:
        return None
    
    conta_destino = recuperar_conta_cliente(cliente_destino)
    valor = ler_valor("Informe o valor a ser transferido: ")       
    transacao = Transferencia(valor, conta_origem, conta_destino)
    cliente_origem.realizar_transacao(conta_origem, transacao)

def exibir_extrato(clientes):
    pass

def criar_conta(clientes, contas):
    pass

def criar_cliente(clientes):
    pass

def executar(opcao, clientes, contas):
    if opcao == "d":
        depositar(clientes)
    elif opcao == "s":
        sacar(clientes)
    elif opcao == "t":
        transferir(clientes)
    elif opcao == "e":
        exibir_extrato(clientes)
    elif opcao == "nc":
        criar_conta(clientes, contas)
    elif opcao == "nu":
        criar_cliente(clientes)


def main():
    clientes = []
    contas = []
    while True:
        opcao = menu()        
        if opcao == "q":
            break
        else:
            executar(opcao)

if __name__ == "__main__":
    main()