n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operação = input("Digite a operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Resto, 6-Potência): ").lower().strip()

if operação in ["1", "soma"]:
    print(f"{n1} + {n2} = {n1 + n2}")
elif operação    in ["2", "subtração", "subtracao"]:
    print(f"{n1} - {n2} = {n1 - n2}")
elif operação in ["3", "multiplicação", "multiplicacao"]:
    print(f"{n1} * {n2} = {n1 * n2}")
elif operação in ["4", "divisão", "divisao"]:
    print(f"{n1} / {n2} = {n1 / n2}")
elif operação in ["5", "resto"]:
    print(f"{n1} mod {n2} = {n1 % n2}")
elif operação in ["6", "potência", "potencia"]:
    print(f"{n1} ^ {n2} = {n1 ** n2}")
else:
    print("Operação não suportada")