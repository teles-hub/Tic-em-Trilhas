while True:
    print("\nMenu de Opções:")
    print("1. Somar\n2. Subtrair\n3. Multiplicar\n4. Dividir\n0. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Fim.")
        break
    elif opcao in [1, 2, 3, 4]:
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))

        if opcao == 1:
            print(f"Resultado: {n1} + {n2} = {n1 + n2}")
        elif opcao == 2:
            print(f"Resultado: {n1} - {n2} = {n1 - n2}")
        elif opcao == 3:
            print(f"Resultado: {n1} * {n2} = {n1 * n2}")
        elif opcao == 4:
            if n2 == 0:
                print("Divisão por zero não permitida")
            else:
                print(f"Resultado: {n1} / {n2} = {n1 / n2}")
    else:
        print("Opção inválida")