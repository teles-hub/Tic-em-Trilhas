qtd = int(input("Quantidade de dias: "))
pesos = []

for i in range(qtd):
    pesos.append(float(input(f"Peso do dia {i+1}: ")))

maior_peso = max(pesos)
dia_maior = pesos.index(maior_peso) + 1

menor_peso = min(pesos)
dia_menor = pesos.index(menor_peso) + 1

pesos_str = ", ".join(str(int(p)) if p.is_integer() else str(p) for p in pesos)
print(f"\nPesos informados: {pesos_str}")
print(f"Maior peso: {int(maior_peso) if maior_peso.is_integer() else maior_peso} kg (Dia {dia_maior})")
print(f"Menor peso: {int(menor_peso) if menor_peso.is_integer() else menor_peso} kg (Dia {dia_menor})\n")

print("Gráfico de evolução:")
for i in range(qtd):
    quadrados = int(pesos[i] // 5)
    barra = "#" * quadrados
    val_str = str(int(pesos[i])) if pesos[i].is_integer() else str(pesos[i])
    print(f"Dia {i+1} | {barra} {val_str}")