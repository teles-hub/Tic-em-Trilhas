def coletar_dados():
    quantidade_pequeno = int(input("Digite a quantidade de açaí P: "))
    quantidade_medio = int(input("Digite a quantidade de açaí M: "))
    quantidade_grande = int(input("Digite a quantidade de açaí G: "))
    desconto_percentual = float(input("Digite a porcentagem de desconto: "))
    return quantidade_pequeno, quantidade_medio, quantidade_grande, desconto_percentual

def processar_total(quantidade_pequeno, quantidade_medio, quantidade_grande, desconto_percentual):
    subtotal = (quantidade_pequeno * 13.50) + (quantidade_medio * 15.00) + (quantidade_grande * 17.50)
    total_com_desconto = subtotal * (1 - (desconto_percentual / 100))
    return total_com_desconto

def exibir_resumo(quantidade_pequeno, quantidade_medio, quantidade_grande, desconto_percentual, total_com_desconto):
    print("\nSeu pedido foi registrado.")
    print(f"- Açaí P: {quantidade_pequeno}")
    print(f"- Açaí M: {quantidade_medio}")
    print(f"- Açaí G: {quantidade_grande}")
    print(f"- Desconto de {desconto_percentual:.0f}% aplicado.")
    print(f"Total R$ {total_com_desconto:.2f}")

def programa_principal():
    pequeno, medio, grande, desconto = coletar_dados()
    total = processar_total(pequeno, medio, grande, desconto)
    exibir_resumo(pequeno, medio, grande, desconto, total)

programa_principal()