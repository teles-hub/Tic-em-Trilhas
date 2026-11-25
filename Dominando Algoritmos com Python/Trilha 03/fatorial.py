numero = int(input("Digite um número: "))

if numero <= 0:
    print("Parâmetro inválido.")
else:
    fatorial = 1
    # Multiplica de 1 até o número informado
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")