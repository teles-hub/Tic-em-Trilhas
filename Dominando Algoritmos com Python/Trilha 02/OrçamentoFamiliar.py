ganhos = float(input("Digite o total de ganhos (R$): "))
gastos = float(input("Digite o total de gastos (R$): "))

if ganhos >= gastos:
    print("Você está dentro do orçamento!")
else:
    print("Você está fora do orçamento! Não gaste mais!")