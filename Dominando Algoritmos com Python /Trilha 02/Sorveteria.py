gramas = float(input("Digite o peso em gramas: "))

if gramas <= 0:
    print("Peso inválido")
else:
    preco_100g = 3.00 if gramas >= 1000 else 3.50
    total = (gramas / 100) * preco_100g
    print(f"O total é R$ {total:.2f}")