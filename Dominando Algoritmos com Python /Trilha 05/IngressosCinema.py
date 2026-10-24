def coletar_dados_cinema():
    quantidade_inteiras = int(input("Digite a quantidade de ingressos Inteira: "))
    quantidade_meias = int(input("Digite a quantidade de ingressos Meia: "))
    dia_semana = input("Digite o dia da semana: ").strip().lower()
    filme_nacional = input("É um filme nacional? (Sim/Não): ").strip().lower()
    return quantidade_inteiras, quantidade_meias, dia_semana, filme_nacional

def processar_ingressos(quantidade_inteiras, quantidade_meias, dia_semana, filme_nacional):
    if "sim" in filme_nacional:
        preco_ingresso = 5.00
        return (quantidade_inteiras + quantidade_meias) * preco_ingresso
    elif "quarta" in dia_semana:
        preco_ingresso = 14.50
        return (quantidade_inteiras + quantidade_meias) * preco_ingresso
    else:
        return (quantidade_inteiras * 28.50) + (quantidade_meias * 14.25)

def exibir_total_cinema(total_pagar):
    print("\nTotal à pagar:")
    print(f"R$ {total_pagar:.2f}")

def programa_principal():
    inteiras, meias, dia, nacional = coletar_dados_cinema()
    total_pagar = processar_ingressos(inteiras, meias, dia, nacional)
    exibir_total_cinema(total_pagar)

programa_principal()