def gerenciar_estoque():
    lista_produtos = []
    lista_quantidades = []
    
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Adicionar produto")
        print("2. Realizar entrada no estoque")
        print("3. Realizar saída no estoque")
        print("4. Listar estoque")
        print("0. Sair")
        opcao_escolhida = int(input("Escolha uma opção: "))
        
        if opcao_escolhida == 0:
            print("Encerrando o programa...")
            break
        elif opcao_escolhida == 1:
            if len(lista_produtos) >= 1000:
                print("Limite atingido")
            else:
                nome_produto = input("Digite o nome do produto: ")
                quantidade_produto = int(input("Digite a quantidade inicial: "))
                lista_produtos.append(nome_produto)
                lista_quantidades.append(quantidade_produto)
                print("Produto adicionado com sucesso!")
        elif opcao_escolhida == 2:
            codigo_produto = int(input("Digite o número do produto: ")) - 1
            quantidade_entrada = int(input("Digite a quantidade de entrada: "))
            if 0 <= codigo_produto < len(lista_produtos):
                lista_quantidades[codigo_produto] += quantidade_entrada
                print("Entrada realizada com sucesso!")
        elif opcao_escolhida == 3:
            codigo_produto = int(input("Digite o número do produto: ")) - 1
            quantidade_saida = int(input("Digite a quantidade de saída: "))
            if 0 <= codigo_produto < len(lista_produtos):
                if quantidade_saida <= lista_quantidades[codigo_produto]:
                    lista_quantidades[codigo_produto] -= quantidade_saida
                    print("Saída realizada com sucesso!")
                else:
                    print("Quantidade indisponível!")
        elif opcao_escolhida == 4:
            if not lista_produtos:
                print("Nenhum produto cadastrado.")
            else:
                print("Estoque atual:")
                for indice in range(len(lista_produtos)):
                    print(f"Produto {indice + 1}: {lista_produtos[indice]} - {lista_quantidades[indice]} unidades")

def programa_principal():
    gerenciar_estoque()

programa_principal()