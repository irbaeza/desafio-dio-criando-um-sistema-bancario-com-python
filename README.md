# Sistema Bancário em Python

Este é um projeto desenvolvido como parte de um desafio proposto pela DIO (Digital Innovation One) no Bootcamp de Engenharia de Dados com Python da NTT DATA. O objetivo do desafio é criar um sistema bancário simples utilizando Python, onde é possível realizar operações básicas como depósito, saque e visualização de extrato.

## Funcionalidades

O sistema bancário possui as seguintes funcionalidades:

### 1. Depósito
- Permite ao usuário realizar depósitos em sua conta.
- Apenas valores positivos podem ser depositados.
- Os depósitos são registrados com a data e o valor, e podem ser visualizados no extrato.

### 2. Saque
- Permite ao usuário realizar saques, respeitando as seguintes regras:
  - Até 3 saques diários.
  - Limite de R$ 500,00 por saque.
  - Verificação de saldo suficiente antes de realizar o saque.
- Os saques são registrados com a data e o valor, e podem ser visualizados no extrato.

### 3. Extrato
- Permite ao usuário visualizar todas as operações realizadas (depósitos e saques).
- Exibe o saldo atual da conta.
- Todos os valores são apresentados no formato R$ xxx.xx.

## Regras de Negócio

As principais regras de negócio implementadas no sistema são:

- **Depósito**:
  - Apenas valores positivos podem ser depositados.
  - O depósito é registrado no extrato com a data e o valor.

- **Saque**:
  - Limite de 3 saques diários.
  - Limite máximo de R$ 500,00 por saque.
  - Verificação de saldo antes de realizar o saque.
  - O saque é registrado no extrato com a data e o valor.

- **Extrato**:
  - Listagem de todos os depósitos e saques realizados.
  - Exibição do saldo atual no final do extrato.

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/irbaeza/desafio-dio-criando-um-sistema-bancario-com-python.git
   ```
3. Navegue até o diretório do projeto:
  ```bash
  cd desafio-dio-criando-um-sistema-bancario-com-python
  ```
4. Execute o arquivo desafio.py:
```bash
  python desafio.py
```
## Tecnologias Utilizadas
Python 3.x
Biblioteca datetime para manipulação de datas.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com melhorias ou novas funcionalidades.
