inteiras = int(input("Quantidade de ingressos inteira: "))
meias = int(input("Quantidade de ingressos meia: "))
dia_semana = input("Dia da semana: ").lower().strip()
nacional_str = input("É filme nacional? (sim/não): ").lower().strip()

nacional = True if nacional_str in ["sim", "s"] else False

preco_inteira = 28.50
preco_meia = preco_inteira / 2.0

# Regras de prioridade dos preços únicos
if nacional:
    preco_inteira = 5.00
    preco_meia = 5.00
elif dia_semana == "quarta-feira":
    preco_inteira = 14.50
    preco_meia = 14.50

total = (inteiras * preco_inteira) + (meias * preco_meia)
print(f"Total à pagar: R$ {total:.2f}")