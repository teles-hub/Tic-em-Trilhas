nota_candidato = float(input("Nota do candidato: "))
nota_corte = float(input("Nota de corte: "))
nota_min_aprovacao = float(input("Nota mínima para aprovação: "))

if nota_candidato < nota_corte:
    print("Situação candidato: Reprovado")
elif nota_candidato >= nota_min_aprovacao:
    print("Situação candidato: Aprovado")
else:
    print("Situação candidato: Lista de Espera")