palavra_original = input("Digite a palavra original: ")
palavra_soletrada = ""

print("Digite letra por letra (0 para finalizar):")
while True:
    letra = input()
    if letra == "0":
        break
    palavra_soletrada += letra.lower()

print(f"Palavra original: {palavra_original}")
print(f"Palavra soletrada: {palavra_soletrada}")