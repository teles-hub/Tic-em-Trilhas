qtd = int(input("Quantidade de meses: "))
faturamento = []

for i in range(qtd):
    fat = float(input(f"Faturamento do mês {i+1}: "))
    faturamento.append(fat)

crescimento = True
queda = True
constante = True

for i in range(1, qtd):
    if faturamento[i] < faturamento[i - 1]:
        crescimento = False
    if faturamento[i] > faturamento[i - 1]:
        queda = False
    if faturamento[i] != faturamento[i - 1]:
        constante = False

print("\n>> Análise de Faturamento <<")
fat_str = ", ".join(
    str(int(f)) if f.is_integer() else str(f) for f in faturamento
)
print(f"Faturamento informado: {fat_str}")

if constante:
    print("Situação: Constante")
elif crescimento:
    print("Situação: Crescimento")
elif queda:
    print("Situação: Queda")
else:
    print("Situação: Sem padrão")