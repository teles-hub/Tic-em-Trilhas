produtos = []
quantidades = []

while True:
    print("\nMenu de Opções")
    print("1. Adicionar produto\n2. Realizar entrada no estoque\n3. Realizar saída no estoque\n4. Listar estoque\n0. Sair")
    opcao = input("Opção: ").strip()

    if opcao == "0":
        print("Encerrando o programa...")
        break
    elif opcao == "1":
        if len(produtos) >= 1000:
            print("Limite máximo de 1000 produtos atingido!")
        else:
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade inicial: "))
            produtos.append(nome)
            quantidades.append(qtd)
            print("Produto adicionado com sucesso!")
    elif opcao == "2":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            num = int(input("Número do produto: ")) - 1
            if 0 <= num < len(produtos):
                qtd = int(input("Quantidade a adicionar: "))
                quantidades[num] += qtd
                print("Entrada realizada com sucesso!")
            else:
                print("Produto inválido.")
    elif opcao == "3":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            num = int(input("Número do produto: ")) - 1
            if 0 <= num < len(produtos):
                qtd = int(input("Quantidade a retirar: "))
                if qtd > quantidades[num]:
                    print("Quantidade indisponível em estoque.")
                else:
                    quantidades[num] -= qtd
                    print("Saída realizada com sucesso!")
            else:
                print("Produto inválido.")
    elif opcao == "4":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\nEstoque atual:")
            for i in range(len(produtos)):
                print(f"Produto {i+1}: {produtos[i]} - {quantidades[i]} unidades")
    else:
        print("Opção inválida.")