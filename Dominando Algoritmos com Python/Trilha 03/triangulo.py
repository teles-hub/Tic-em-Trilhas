altura = int(input("Digite a altura: "))

if altura <= 0:
    print("Triângulo inválido")
else:
    for i in range(1, altura + 1):
        print("*" * i)