meta = input("Descrição da meta: ")
valor_meta = float(input("Valor necessário para atingir a meta (R$): "))
salario = float(input("Salário mensal (R$): "))
despesas = float(input("Total das despesas mensais (R$): "))

saldo_apos_despesas = salario - despesas
reserva_fixa = saldo_apos_despesas * 0.30
disponivel_meta = saldo_apos_despesas - reserva_fixa
prazo_meses = valor_meta / disponivel_meta if disponivel_meta > 0 else 0

print(f"\nMeta: {meta} (R$ {valor_meta:.2f})")
print(f"Salário: R$ {salario:.2f} - Despesas: R$ {despesas:.2f}\n")
print(f"Saldo após despesas: R$ {saldo_apos_despesas:.2f}")
print(f"Reserva fixa (30%): R$ {reserva_fixa:.2f}")
print(f"Valor disponível para a meta: R$ {disponivel_meta:.2f} por mês")
print(f"Prazo estimado para atingir a meta: {prazo_meses:.2f} meses")