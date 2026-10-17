maior = None
menor = None

while True:
    temp = float(input("Digite a temperatura (0 para sair): "))

    if temp == 0:
        break

    if temp < -50 or temp > 60:
        print("Temperatura inválida")
        continue

    if maior is None or temp > maior:
        maior = temp
    if menor is None or temp < menor:
        menor = temp

if maior is not None and menor is not None:
    print(f"Maior temperatura: {maior:.0f}")
    print(f"Menor temperatura: {menor:.0f}")