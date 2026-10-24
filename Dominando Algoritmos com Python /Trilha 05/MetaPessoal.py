def coletar_dados_meta():
    descricao_meta = input("Digite a descrição da meta: ")
    valor_meta = float(input("Digite o valor necessário para a meta (R$): "))
    salario_mensal = float(input("Digite o seu salário mensal (R$): "))
    despesas_mensais = float(input("Digite o total de despesas mensais (R$): "))
    return descricao_meta, valor_meta, salario_mensal, despesas_mensais

def processar_planejamento(valor_meta, salario_mensal, despesas_mensais):
    saldo_apos_despesas = salario_mensal - despesas_mensais
    reserva_fixa = saldo_apos_despesas * 0.30
    valor_disponivel = saldo_apos_despesas - reserva_fixa
    prazo_meses = valor_meta / valor_disponivel
    return saldo_apos_despesas, reserva_fixa, valor_disponivel, prazo_meses

def exibir_relatorio(descricao_meta, valor_meta, salario_mensal, despesas_mensais, saldo_apos_despesas, reserva_fixa, valor_disponivel, prazo_meses):
    print(f"\nMeta: {descricao_meta} (R$ {valor_meta:.2f})")
    print(f"Salário: R$ {salario_mensal:.2f} - Despesas: R$ {despesas_mensais:.2f}")
    print(f"Saldo após despesas: R$ {saldo_apos_despesas:.2f}")
    print(f"Reserva fixa (30%): R$ {reserva_fixa:.2f}")
    print(f"Valor disponível para a meta: R$ {valor_disponivel:.2f} por mês")
    print(f"Prazo estimado para atingir a meta: {prazo_meses:.2f} meses")

def programa_principal():
    descricao, meta, salario, despesas = coletar_dados_meta()
    saldo, reserva, disponivel, prazo = processar_planejamento(meta, salario, despesas)
    exibir_relatorio(descricao, meta, salario, despesas, saldo, reserva, disponivel, prazo)

programa_principal()