nome = input("Digite seu nome: ")
valor_compra = float(input("Digite o valor da compra (R$): "))
desconto_pct = float(input("Digite a porcentagem de desconto: "))

total_final = valor_compra * (1 - (desconto_pct / 100.0))

print(f"\nOlá {nome}, sua compra de R$ {valor_compra:.2f} foi confirmada!")
print(f"Foi aplicado um desconto de {desconto_pct}%.")
print(f"O total final ficou em R$ {total_final:.2f}")