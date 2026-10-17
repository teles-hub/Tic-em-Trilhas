base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))

if base <= 0 or altura <= 0:
    print("Retângulo inválido")
else:
    for _ in range(altura):
        print("*" * base)