def coletar_compras():
    lista_valores_compras = []
    print("Digite os valores das compras (digite 0 para encerrar):")
    while True:
        valor_digitado = float(input("Valor do item (R$): "))
        if valor_digitado == 0:
            break
        lista_valores_compras.append(valor_digitado)
    quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
    return lista_valores_compras, quantidade_parcelas

def processar_caixa(lista_valores_compras, quantidade_parcelas):
    total_acumulado = 0
    for valor_item in lista_valores_compras:
        if valor_item < 0:
            print(f"Valor inválido: {valor_item:.0f}")
        else:
            total_acumulado += valor_item
    return total_acumulado, quantidade_parcelas

def exibir_resumo_caixa(total_acumulado, quantidade_parcelas):
    print()
    if quantidade_parcelas <= 1:
        print(f"Pagamento à vista: R$ {total_acumulado:.0f}")
    else:
        valor_cada_parcela = total_acumulado / quantidade_parcelas
        print(f"Total da compra: R$ {total_acumulado:.0f}")
        print(f"Parcelado em {quantidade_parcelas}x de R$ {valor_cada_parcela:.2f}")

def programa_principal():
    lista_compras, parcelas = coletar_compras()
    total_compra, parcelas = processar_caixa(lista_compras, parcelas)
    exibir_resumo_caixa(total_compra, parcelas)

programa_principal()