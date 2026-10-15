cor1 = input("Primeira cor: ").lower().strip()
cor2 = input("Segunda cor: ").lower().strip()

primarias = ["vermelho", "azul", "amarelo"]

if cor1 not in primarias or cor2 not in primarias:
    print("Apenas cores primárias são aceitas.")
elif cor1 == cor2:
    print(f"A combinação resulta em: {cor1.capitalize()}")
elif (cor1 == "vermelho" and cor2 == "azul") or (cor1 == "azul" and cor2 == "vermelho"):
    print("A combinação resulta em: Roxo")
elif (cor1 == "vermelho" and cor2 == "amarelo") or (cor1 == "amarelo" and cor2 == "vermelho"):
    print("A combinação resulta em: Laranja")
else:
    print("A combinação resulta em: Verde")