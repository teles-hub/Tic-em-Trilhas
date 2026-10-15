cor = input("Digite a cor do semáforo: ").lower().strip()

if cor == "vermelho":
    print("Espere")
elif cor == "verde":
    print("Atravesse")
else:
    print("Farol inoperante")