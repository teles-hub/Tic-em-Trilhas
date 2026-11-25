def executar_sistema_bancario():
    saldo_atual = 0.0
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Consultar Saldo")
        print("2. Realizar Depósito")
        print("3. Realizar Saque")
        print("0. Sair")
        opcao_menu = int(input("Escolha uma opção: "))
        
        if opcao_menu == 0:
            break
        elif opcao_menu == 1:
            print(f"Saldo atual: R$ {saldo_atual:.0f}")
        elif opcao_menu == 2:
            valor_deposito = float(input("Digite o valor para depósito: "))
            if valor_deposito <= 0:
                print("Valor inválido")
            else:
                saldo_atual += valor_deposito
        elif opcao_menu == 3:
            valor_saque = float(input("Digite o valor para saque: "))
            if valor_saque <= 0:
                print("Valor inválido")
            elif valor_saque > saldo_atual:
                print("Saldo insuficiente")
            else:
                saldo_atual -= valor_saque
        else:
            print("Opção inválida")

def programa_principal():
    executar_sistema_bancario()

programa_principal()