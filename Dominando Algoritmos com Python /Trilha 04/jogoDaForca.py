palavra = input("Digite a palavra secreta: ").upper().strip()
print("\n" * 30)  # Limpa o console ocultando a palavra secreta

secreta = list(palavra)
descoberta = ["_"] * len(secreta)
erros = 0

while erros < 7 and "_" in descoberta:
    print(f"Estado: {''.join(descoberta)}")
    print(f"Erros: {erros}")
    chute = input("Digite uma letra: ").upper().strip()

    if chute in secreta:
        for i in range(len(secreta)):
            if secreta[i] == chute:
                descoberta[i] = chute
    else:
        erros += 1

if "_" not in descoberta:
    print(f"\nEstado: {''.join(descoberta)}")
    print(f"Erros: {erros}")
    print("Parabéns! Você descobriu a palavra.")
else:
    print(f"\nEstado: {''.join(descoberta)}")
    print("Erros: 7")
    print(f"Você perdeu! A palavra era: {palavra}")