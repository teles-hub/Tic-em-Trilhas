qtd = int(input("Quantidade de alunos: "))
notas = []

for i in range(qtd):
    nota = float(input(f"Nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / qtd
maior = max(notas)
menor = min(notas)

aprovados = sum(1 for n in notas if n >= 6)
reprovados = sum(1 for n in notas if n < 6)

print("\n>> Resultado da Turma <<")
notas_str = ", ".join(
    str(int(n)) if n.is_integer() else str(n) for n in notas
)
print(f"Notas informadas: {notas_str}")
print(f"Média da turma: {media:.0f}" if media.is_integer() else f"Média da turma: {media:.1f}")
print(f"Maior nota: {int(maior) if maior.is_integer() else maior}")
print(f"Menor nota: {int(menor) if menor.is_integer() else menor}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")

if reprovados == 0:
    print("Situação geral: Todos os alunos foram aprovados")
else:
    print("Situação geral: Nem todos os alunos foram aprovados")