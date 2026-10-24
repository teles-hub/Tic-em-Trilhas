def coletar_dados_corrida():
    tamanho_pista_metros = float(input("Digite o tamanho da pista em metros: "))
    quantidade_voltas = int(input("Digite a quantidade de voltas: "))
    tempo_primeira_volta_segundos = float(input("Digite o tempo da primeira volta em segundos: "))
    return tamanho_pista_metros, quantidade_voltas, tempo_primeira_volta_segundos

def processar_desempenho(tamanho_pista_metros, quantidade_voltas, tempo_primeira_volta_segundos):
    distancia_total_kilometros = (tamanho_pista_metros * quantidade_voltas) / 1000
    tempo_total_minutos = (tempo_primeira_volta_segundos * quantidade_voltas) / 60
    return distancia_total_kilometros, tempo_total_minutos

def exibir_analise(distancia_kilometros, tempo_minutos):
    print("\nAnálise Preditiva Concluída")
    print(f"Distância total a ser percorrida: {distancia_kilometros:.2f} km.")
    print(f"Previsão de conclusão: {tempo_minutos:.1f} minutos.")

def programa_principal():
    pista, voltas, tempo_volta = coletar_dados_corrida()
    distancia, tempo = processar_desempenho(pista, voltas, tempo_volta)
    exibir_analise(distancia, tempo)

programa_principal()