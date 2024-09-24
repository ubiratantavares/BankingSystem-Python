# BankingSystem-Python

## Desafio de Projeto: Modelando o Sistema Bancário em POO com Python

Com base na imagem e no diagrama de classes que você compartilhou, vou criar o código em Python representando as classes, interfaces e associações conforme o diagrama.

### Classes em Python

1 **Classe `Historico`**

    * Armazena todas as transações realizadas em uma lista, utilizando o método `adicionar_transacao` para adicionar as transações realizadas.

2 **Interface `Transacao` (usando a classe abstrata `ABC` do Python)**

    * Definida como uma interface com um método abstrato `registrar`, que deve ser implementado nas subclasses `Deposito` e `Saque`.

    * A interface `Transacao` tem subclasses concretas (`Deposito` e `Saque`), que implementam o método `registrar`.

3 **Classe `Conta`**

    * Classe que mantém os dados básicos de uma conta bancária, como saldo, número, agência, cliente e histórico de transações. Ela tem métodos para sacar e depositar, bem como um método `nova_conta` que cria uma nova conta.

    * A classe `Conta` tem uma associação com a classe `Historico`, representada pela composição (uma conta tem um histórico).

4 **Classe `Cliente`**

    * Armazena o endereço e a lista de contas associadas a ele. Ele pode realizar transações em uma conta e adicionar novas contas.

    * A classe `Cliente` tem uma associação com `Conta`, representada por uma lista de contas.

5 **Classes específicas `Deposito` e `Saque`**

    * Ambas implementam a interface `Transacao`. Elas registram a transação na conta associada, modificando o saldo e adicionando a transação ao histórico.

6 **Classes filhas `ContaCorrente` e `PessoaFisica`**

    - **`ContaCorrente`**: Herda de `Conta` e adiciona os atributos `limite` e `limite_saques`, específicos para esse tipo de conta.

    - **`PessoaFisica`**: Herda de `Cliente` e adiciona atributos como CPF, nome e data de nascimento.
