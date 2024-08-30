# Regras projeto - depósito , extrato e saque 

# Depósito:
"""
1. Deve ser possivel depositar APENAS valores positivos; OK
2. Não é necessário pedir identificação (agência e conta bancária); OK
3. Todos os depósitos devem ser armazenado em uma var e exibidos em extrato (histórico mostrando: data, depósito e valor) OK
"""

# Saque
""""
1. 3 saques diários
2. Limite de R$ 500 por saque. OK
3. Caso o user não tenha saldo em conta, o sistema deve exibir: "Saldo insuficiente."
4. Todos os saques devem ser armazenado em uma var e exibidos em extrato (histórico mostrando: data, depósito e valor)
"""

# Extrato
"""
1. Listar todos os depósitos e saques OK
2. No final da lista exibir o saldo atual OK
3. Os valores devem ser exibidos no formato R$ xxx.xx OK
"""

# função data
from datetime import date
data_atual = date.today()
data_formatada = data_atual.strftime("%d/%m/%Y")

# variáveis 
saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# funções

def deposito(valor_despositado):
    global saldo
    global extrato
    global data_formatada

    saldo += valor_despositado
    extrato += f"{data_formatada} - Depósito - Valor: + R${valor_despositado:.2f}.\n"
    print("Depósito feito com sucesso!")

def saque(valor_sacado):
    global saldo
    global extrato
    global data_formatada
    global numero_saques

    saldo -= valor_sacado
    extrato += f"\n {data_formatada} - Saque - Valor: - R${valor_sacado:.2f}.\n"
    print(f"Saque feito com sucesso! Você tem {LIMITE_SAQUES - numero_saques} saques restantes hoje.")

menu = f"""
------------------------------------------

Banco do Barril
{data_formatada}

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> Selecione a opção desejada: """

while True:

    opcao = input(menu)

    if opcao == "d":

        while True:
            valor_deposito = int(input("\n Digite o valor para depósito: R$ "))
            if valor_deposito < 1 :
                print("\n Valor não disponível. Por favor, digite um valor maior que 0.")
            else:
                deposito(valor_deposito)
                break

    elif opcao == "s":

        while True:
                print(numero_saques)
                if numero_saques != LIMITE_SAQUES:

                    valor_saque = int(input("\n Digite o valor para saque: R$ "))

                    if valor_saque < 1:
                        print("\n Valor não disponível. Por favor, digite um valor maior que 0.")
                
                    elif valor_saque > LIMITE:
                        print("\n Valor não disponível para saque. Por favor, digite um valor de até R$ 500.00 para saque.")
    
                    elif valor_saque > saldo:
                        print("\n Saldo insuficiente.")
                        break
                    
                    else:
                        saque(valor_saque)
                        numero_saques += 1
                        break
                else:
                    print(f"Você já atingiu o limite de {LIMITE_SAQUES} saques por dia.")
                    break

    elif opcao == "e":
        mensagem_extrato = f"""
        ------------------------------------------

        Extrato:
        
        \n{extrato}

Saldo atual: R${saldo:.2f}.
    
        Banco do Barril
        {data_formatada}

        ------------------------------------------
        """ 
        print(mensagem_extrato)

    elif opcao == "q":
        print("Saindo. Obrigado por usar o Banco do Barril!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
