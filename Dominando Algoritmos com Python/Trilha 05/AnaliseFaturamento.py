def coletar_faturamentos():
    quantidade_meses = int(input("Digite a quantidade de meses a analisar: "))
    lista_faturamentos = []
    for mes in range(1, quantidade_meses + 1):
        faturamento_mes = float(input(f"Digite o faturamento do mês {mes}: "))
        lista_faturamentos.append(faturamento_mes)
    return lista_faturamentos

def analisar_tendencia(lista_faturamentos):
    tendencia_crescente = True
    tendencia_decrescente = True
    
    for indice in range(len(lista_faturamentos) - 1):
        if lista_faturamentos[indice + 1] < lista_faturamentos[indice]:
            tendencia_crescente = False
        if lista_faturamentos[indice + 1] > lista_faturamentos[indice]:
            tendencia_decrescente = False
            
    if tendencia_crescente and tendencia_decrescente:
        return "Constante"
    elif tendencia_crescente:
        return "Crescimento"
    elif tendencia_decrescente:
        return "Queda"
    else:
        return "Sem padrão"

def exibir_analise_faturamento(lista_faturamentos, situacao_faturamento):
    print("\n>> Análise de Faturamento <<")
    valores_formatados = ", ".join(f"{valor:.0f}" for valor in lista_faturamentos)
    print(f"Faturamento informado: {valores_formatados}")
    print(f"Situação: {situacao_faturamento}")

def programa_principal():
    faturamentos = coletar_faturamentos()
    situacao = analisar_tendencia(faturamentos)
    exibir_analise_faturamento(faturamentos, situacao)

programa_principal()