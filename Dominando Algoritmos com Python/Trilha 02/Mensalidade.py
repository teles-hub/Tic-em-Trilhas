sigla = input("Digite a sigla do curso (SI, ADS, CS, EC, ES): ").upper().strip()
isento_str = input("É isento? (sim/não): ").lower().strip()
desconto = float(input("Porcentagem de desconto: "))

isento = True if isento_str in ["sim", "s"] else False

valores = {
    "SI": 900.00,
    "ADS": 750.00,
    "CS": 1150.00,
    "EC": 1300.00,
    "ES": 950.00
}

if sigla not in valores:
    print("Curso não encontrado")
elif isento:
    print("Valor da mensalidade: R$ 0.00")
else:
    valor_base = valores[sigla]
    valor_final = valor_base * (1 - (desconto / 100.0))
    print(f"Valor da mensalidade: R$ {valor_final:.2f}")