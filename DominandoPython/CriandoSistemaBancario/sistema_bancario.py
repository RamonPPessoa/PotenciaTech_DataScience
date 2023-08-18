# Definindo as constantes
MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

SALDO_INICIAL = 0
LIMITE_SAQUE = 500
MAX_SAQUES = 3

# Inicializando as variáveis
saldo = SALDO_INICIAL
extrato = ""
conta_saques = 0

# Loop principal
while True:

    # Lendo a opção do usuário
    opcao = input(MENU)

    # Verificando a opção escolhida
    if opcao == "d":
        # Opção de depósito
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            # Atualizando o saldo e o extrato
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            # Mensagem de erro para valor inválido
            print("Não foi possível realizar o depósito! O valor informado é inválido.")

    elif opcao == "s":
        # Opção de saque
        valor = float(input("Informe o valor do saque: "))

        # Verificando as condições para o saque
        saldo_insuficiente = valor > saldo

        limite_excedido = valor > LIMITE_SAQUE

        saques_excedidos = conta_saques >= MAX_SAQUES

        if saldo_insuficiente:
            # Mensagem de erro para saldo insuficiente
            print("Não foi possível realizar o saque! Você não tem saldo suficiente.")

        elif limite_excedido:
            # Mensagem de erro para limite excedido
            print("Não foi possível realizar o saque! O valor do saque excede o limite.")

        elif saques_excedidos:
            # Mensagem de erro para número máximo de saques excedido
            print("Não foi possível realizar o saque! Número máximo de saques excedido.")

        elif valor > 0:
            # Atualizando o saldo, o extrato e o contador de saques
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            conta_saques += 1

        else:
            # Mensagem de erro para valor inválido
            print("Não foi possível realizar o saque! O valor informado é inválido.")

    elif opcao == "e":
        # Opção de extrato
        print("\n================ EXTRATO ================")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        # Opção de sair
        break

    else:
        # Mensagem de erro para opção inválida
        print("Opção inválida, por favor selecione outra opção.")
