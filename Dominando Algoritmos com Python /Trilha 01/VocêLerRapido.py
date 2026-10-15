nome = input("Digite seu nome: ")
livro = input("Digite o nome do livro: ")
paginas = int(input("Digite o total de páginas: "))
tempo_seg_por_pagina = float(input("Digite o tempo em segundos de leitura por página: "))

tempo_total_segundos = paginas * tempo_seg_por_pagina
tempo_horas = tempo_total_segundos / 3600.0

print(f"\n{nome}, você finalizará a leitura do livro {livro} em aproximadamente {tempo_horas:.2f} horas.")