tamanho_pista = float(input("Tamanho da pista em metros: "))
voltas = int(input("Quantidade de voltas: "))
tempo_primeira_volta_seg = float(input("Tempo da primeira volta em segundos: "))

distancia_total_km = (tamanho_pista * voltas) / 1000.0
tempo_total_minutos = (tempo_primeira_volta_seg * voltas) / 60.0

print("\nAnálise Preditiva Concluída")
print(f"Distância total a ser percorrida: {distancia_total_km:.2f} km.")
print(f"Previsão de conclusão: {tempo_total_minutos:.1f} minutos.")