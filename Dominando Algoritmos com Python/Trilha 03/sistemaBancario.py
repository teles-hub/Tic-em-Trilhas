saldo = 0.0

while True:
    print("\nMenu de Opções:")
    print("1. Consultar Saldo\n2. Realizar Depósito\n3. Realizar Saque\n0. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == 2:
        deposito = float(input("Digite o valor do depósito: "))
        if deposito <= 0:
            print("Valor inválido")
        else:
            saldo += deposito
            print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == 3:
        saque = float(input("Digite o valor do saque: "))
        if saque <= 0:
            print("Valor inválido")
        elif saque > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= saque
            print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Opção inválida")