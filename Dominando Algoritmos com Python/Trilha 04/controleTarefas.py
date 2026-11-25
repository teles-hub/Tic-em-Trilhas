tarefas = []
status = []  # False para pendente, True para concluída

while True:
    print("\nMenu de Opções")
    print("1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar concluída\n4. Exibir pendentes\n0. Sair")
    opcao = input("Opção: ").strip()

    if opcao == "0":
        print("Encerrando o programa...")
        break
    elif opcao == "1":
        descricao = input("Descrição da tarefa: ")
        tarefas.append(descricao)
        status.append(False)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nLista de tarefas:")
            for i in range(len(tarefas)):
                marcador = "[X]" if status[i] else "[]"
                print(f"{i+1}- {marcador} {tarefas[i]}")
    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            num = int(input("Número da tarefa a concluir: ")) - 1
            if 0 <= num < len(tarefas):
                status[num] = True
                print(f"Tarefa {num+1} marcada como concluída.")
            else:
                print("Tarefa inválida.")
    elif opcao == "4":
        pendentes = [i for i in range(len(tarefas)) if not status[i]]
        if not pendentes:
            print("Nenhuma tarefa pendente.")
        else:
            print("\nTarefas pendentes:")
            for i in pendentes:
                print(f"{i+1}- [] {tarefas[i]}")
    else:
        print("Opção inválida.")