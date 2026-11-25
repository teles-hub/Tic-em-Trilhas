pessoas = int(input("Quantas pessoas vão participar do churrasco? "))


carne_kg = (pessoas * 300) / 1000
linguica_kg = (pessoas * 200) / 1000
frango_kg = (pessoas * 150) / 1000


custo_carne = carne_kg * 50.00
custo_linguica = linguica_kg * 28.00
custo_frango = frango_kg * 22.00

custo_total = custo_carne + custo_linguica + custo_frango
por_pessoa = custo_total / pessoas

print("Quantidades:")
print(
    f"Carne: {carne_kg:.1f} kg - Linguiça: {linguica_kg:.1f} kg - Frango:"
    f" {frango_kg:.1f} kg"
)
print("\nCusto total:")
print(
    f"Carne: R$ {custo_carne:.2f} - Linguiça: R$ {custo_linguica:.2f} - Frango:"
    f" R$ {custo_frango:.2f}"
)
print(f"\nCusto total do churrasco: R$ {custo_total:.2f}")
print(f"Cada pessoa deve contribuir com: R$ {por_pessoa:.2f}")