projeto = input("Nome do projeto: ")
qtd = int(input("Quantidade de doações: "))
meta = float(input("Valor da meta: "))

doacoes = []
for i in range(qtd):
    valor = float(input(f"Valor da doação {i+1}: "))
    doacoes.append(valor)

total = sum(doacoes)
maior = max(doacoes)

print("\n>> Resumo das Doações <<")
print(f"Projeto: {projeto}")
doacoes_str = ", ".join(
    str(int(d)) if d.is_integer() else str(d) for d in doacoes
)
print(f"Doações recebidas: {doacoes_str}\n")
print(f"Total arrecadado: {int(total) if total.is_integer() else total}")
print(f"Maior doação: {int(maior) if maior.is_integer() else maior}")

if total >= meta:
    print("Situação: Meta atingida")
else:
    print("Situação: Meta não atingida")