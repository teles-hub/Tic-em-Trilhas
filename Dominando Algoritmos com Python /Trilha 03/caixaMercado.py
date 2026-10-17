total = 0.0

while True:
    valor = float(input("Digite o valor da compra (0 para encerrar): "))

    if valor == 0:
        break
    elif valor < 0:
        print(f"Valor inválido: {valor}")
    else:
        total += valor

if total > 0:
    parcelas = int(input("Digite a quantidade de parcelas: "))

    if parcelas <= 1:
        print(f"Pagamento à vista: R$ {total:.2f}")
    else:
        valor_parcela = total / parcelas
        print(f"Total da compra: R$ {total:.2f}")
        print(f"Parcelado em {parcelas}x de R$ {valor_parcela:.2f}")