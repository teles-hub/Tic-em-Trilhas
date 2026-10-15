n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
faltas = int(input("Quantidade de faltas: "))

media = (n1 + n2 + n3) / 3.0

if media < 0 or media > 10 or faltas < 0:
    print("Parâmetros inválidos")
elif faltas > 4:
    print(f"Média: {media:.1f}. Situação: Reprovado por Falta")
elif media == 0:
    print("Desistente")
elif media >= 8.0:
    print(f"Média: {media:.1f}. Situação: Aprovado com sucesso")
elif media >= 6.0:
    print(f"Média: {media:.1f}. Situação: Aprovado")
else:
    print(f"Média: {media:.1f}. Situação: Recuperação")