qtd_p = int(input("Quantidade de Açaí P: "))
qtd_m = int(input("Quantidade de Açaí M: "))
qtd_g = int(input("Quantidade de Açaí G: "))
desconto_pct = float(input("Porcentagem do cupom de desconto: "))

subtotal = (qtd_p * 13.50) + (qtd_m * 15.00) + (qtd_g * 17.50)
total = subtotal * (1 - (desconto_pct / 100.0))

print("\nSeu pedido foi registrado.")
print(f"- Açaí P: {qtd_p}")
print(f"- Açaí M: {qtd_m}")
print(f"- Açaí G: {qtd_g}")
print(f"Desconto de {desconto_pct:.0f}% aplicado.")
print(f"Total R$ {total:.2f}")