historico = []

while len(historico) < 1000:
    valor = float(input("Digite a transação (-1 para encerrar, 0 para cancelar): "))
    
    if valor == -1:
        break
    elif valor == 0:
        if len(historico) > 0:
            historico.pop()  # Cancela a última transação válida
    else:
        historico.append(valor)

saldo_final = sum(historico)
val_str = str(int(saldo_final)) if saldo_final.is_integer() else f"{saldo_final:.2f}"
print(f"\nSaldo final: {val_str}")