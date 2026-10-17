posicao = int(input("Digite a posição desejada: "))

if posicao <= 0:
    print("Posição inválida")
elif posicao == 1 or posicao == 2:
    print(f"O valor na posição {posicao} da sequência de Fibonacci é 1")
else:
    a, b = 1, 1
    # Laço para calcular as próximas posições até a desejada
    for _ in range(3, posicao + 1):
        a, b = b, a + b
    print(f"O valor na posição {posicao} da sequência de Fibonacci é {b}")