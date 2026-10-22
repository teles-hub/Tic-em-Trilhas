qtd = int(input("Quantidade de medicamentos: "))

farmacia_a = []
print("Preços na Farmácia A:")
for i in range(qtd):
    farmacia_a.append(float(input(f"Produto {i+1}: ")))

farmacia_b = []
print("Preços na Farmácia B:")
for i in range(qtd):
    farmacia_b.append(float(input(f"Produto {i+1}: ")))

baratos_a = 0
baratos_b = 0
mesmo_preco = 0

for i in range(qtd):
    if farmacia_a[i] < farmacia_b[i]:
        baratos_a += 1
    elif farmacia_b[i] < farmacia_a[i]:
        baratos_b += 1
    else:
        mesmo_preco += 1

total_a = sum(farmacia_a)
total_b = sum(farmacia_b)

print("\nFARMAZOOM")
str_a = ", ".join(str(int(p)) if p.is_integer() else str(p) for p in farmacia_a)
str_b = ", ".join(str(int(p)) if p.is_integer() else str(p) for p in farmacia_b)
print(f"Farmácia A: {str_a}")
print(f"Farmácia B: {str_b}\n")

print("Produtos mais Baratos")
print(f"Na Farmácia A: {baratos_a}")
print(f"Na Farmácia B: {baratos_b}")
print(f"Mesmo preço: {mesmo_preco}\n")

print("Total")
print(f"Farmácia A: R$ {int(total_a) if total_a.is_integer() else total_a:.2f}")
print(f"Farmácia B: R$ {int(total_b) if total_b.is_integer() else total_b:.2f}\n")

if total_a < total_b:
    print("Melhor opção: Farmácia A")
elif total_b < total_a:
    print("Melhor opção: Farmácia B")
else:
    print("Melhor opção: Empate")