qtd_1 = int(input("Quantidade de figurinhas do Jogador 1: "))
j1 = []
for _ in range(qtd_1):
    j1.append(int(input()))

qtd_2 = int(input("Quantidade de figurinhas do Jogador 2: "))
j2 = []
for _ in range(qtd_2):
    j2.append(int(input()))

em_comum = sorted(list(set(j1).intersection(set(j2))))
apenas_j1 = sorted(list(set(j1) - set(j2)))
apenas_j2 = sorted(list(set(j2) - set(j1)))

trocas_possiveis = min(len(apenas_j1), len(apenas_j2))

print(f"\nFigurinhas em comum: {', '.join(map(str, em_comum))}")
print(f"Apenas jogador A: {', '.join(map(str, apenas_j1))}")
print(f"Apenas jogador B: {', '.join(map(str, apenas_j2))}")
print(f"Quantidade de trocas possíveis: {trocas_possiveis}")